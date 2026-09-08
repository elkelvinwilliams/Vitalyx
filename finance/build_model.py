#!/usr/bin/env python3
"""
VYTALIX — 36-month financial model builder (Jan 2027 – Dec 2029).

Builds /finance/Vytalix_Financial_Model_3yr.xlsx with openpyxl (3.1.5).

Design rules
------------
* Every number is a SCENARIO built from stated assumptions (FACTS_BASE.md A8). Nothing is an actual.
* GBP, UK-domiciled. No VAT, no corporation tax (loss-making throughout; R&D tax relief not modelled — upside TO VALIDATE).
* The workbook is formula-driven: the Assumptions sheet holds Conservative / Base / High-growth columns and a
  scenario selector cell (Assumptions!C4). Column F ("Active") = INDEX(C:E, selector) and every timeline formula
  points at column F. Year-dependent inputs use CHOOSE(year index, Y1, Y2, Y3).
* The same logic is computed in pure Python (function `compute`) so that (a) a "Static summary" and "Sensitivity"
  sheet carry visible values without recalculation, and (b) the workbook can be recalculated with LibreOffice
  and checked against Python (function `verify`).
* Hire start month 99 = "not hired within the 36-month model".

Usage:  python3 finance/build_model.py            (build + openpyxl re-open check)
        python3 finance/build_model.py --verify   (also recalculates with LibreOffice and compares to Python)
"""
import datetime as dt
import os
import shutil
import subprocess
import sys
import tempfile

from openpyxl import Workbook, load_workbook
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "Vytalix_Financial_Model_3yr.xlsx")

MONTHS = 36
START = dt.date(2027, 1, 1)
YEARS = [2027, 2028, 2029]
COL0 = 3  # column C = month 1
SCEN_NAMES = ["Conservative", "Base", "High-growth"]
SCEN_KEYS = ["cons", "base", "high"]


def mcol(m):
    return get_column_letter(COL0 + m - 1)


FIRST, LAST = mcol(1), mcol(MONTHS)  # C .. AL
YCOL = {2027: "AN", 2028: "AO", 2029: "AP"}
TCOL = "AQ"


def q(sheet, cell):
    return f"'{sheet}'!{cell}"


# ----------------------------------------------------------------------------------------------------------------
# 1. ASSUMPTIONS  (key, label, (cons, base, high), unit, tag, note)
# ----------------------------------------------------------------------------------------------------------------
HIRES = [
    ("product_lead", "Product lead / CTO"),
    ("dev1", "Developer 1"),
    ("dev2", "Developer 2"),
    ("dev3", "Developer 3"),
    ("bd_lead", "BD / sales lead"),
    ("prog_mgr", "Programme manager (Nigeria)"),
    ("clinical_lead", "Clinical lead (midwife/obstetrician)"),
    ("content_lead", "E-learning content lead"),
    ("consultant", "Senior consultant (billable)"),
]

ASSUMPTIONS = [
    ("H", "General"),
    ("opening_cash", "Opening cash (founder capital, month 1)", (10000, 20000, 30000), "GBP", "ASSUMPTION",
     "Founder's own contribution; TO VALIDATE with founder."),
    ("collection_lag", "Collection lag — services & MaternaLink invoices", (1, 1, 1), "months", "ASSUMPTION",
     "E-learning collected same month (prepaid)."),
    ("avail_days", "Founder available working days per month", (17.33, 17.33, 17.33), "days", "ASSUMPTION",
     "208 days/year ÷ 12 (4 days/week on Vytalix, per 01_BUSINESS_MODEL)."),
    ("ramp_months", "Sales ramp-up (months to full run-rate)", (4, 3, 2), "months", "ASSUMPTION",
     "Ramp factor = MIN(1,(month-1)/ramp). Month 1 = 0 revenue (incorporation, outreach)."),
    ("H", "Advisory (founder-led days and retainers)"),
    ("day_rate", "Founder day rate", (1200, 1500, 1800), "GBP/day", "ESTIMATE",
     "Range £1,200–£1,800 per 01_BUSINESS_MODEL §4.1."),
    ("utilisation", "Founder billable utilisation (all client work)", (0.30, 0.42, 0.55), "%", "ESTIMATE",
     "Share of available days billed (advisory days + retainers + consulting delivery)."),
    ("ret_start", "Retainers — first retainer month", (3, 2, 2), "month", "ASSUMPTION", ""),
    ("ret_y1", "Retainers active — Y1 (average)", (0.5, 1, 2), "count", "ESTIMATE", "Fractional = part-year."),
    ("ret_y2", "Retainers active — Y2 (average)", (1, 2, 3), "count", "ESTIMATE", ""),
    ("ret_y3", "Retainers active — Y3 (average)", (1, 2, 3), "count", "ESTIMATE", ""),
    ("ret_fee", "Retainer fee per month", (3500, 4000, 5000), "GBP/month", "ESTIMATE",
     "£2,500–£6,000 per 01_BUSINESS_MODEL #2."),
    ("ret_days", "Founder days consumed per retainer per month", (2.5, 2.5, 2.5), "days", "ASSUMPTION", ""),
    ("adv_cost_day", "Direct cost per founder billable day (travel, tools)", (50, 50, 50), "GBP/day", "ESTIMATE", ""),
    ("cons_days", "Senior consultant billable days per month (once hired)", (0, 10, 10), "days", "ASSUMPTION",
     "Hire start month in Headcount block; 0 if never hired."),
    ("cons_rate", "Senior consultant billed day rate", (900, 900, 1000), "GBP/day", "ESTIMATE",
     "Associate-level rate £700–£1,000 per 01_BUSINESS_MODEL."),
    ("H", "Consulting (packaged projects)"),
    ("proj_y1", "Projects won — Y1", (2, 5, 8), "count", "ESTIMATE", "Spread evenly across the year after ramp."),
    ("proj_y2", "Projects won — Y2", (4, 8, 14), "count", "ESTIMATE", ""),
    ("proj_y3", "Projects won — Y3", (5, 10, 18), "count", "ESTIMATE", ""),
    ("proj_value", "Average project value", (15000, 20000, 30000), "GBP", "ESTIMATE",
     "Range £15k–£60k; catalogue prices £9.5k–£28k in 01_BUSINESS_MODEL §5."),
    ("fdays_proj", "Founder days per project", (8, 7, 5), "days", "ASSUMPTION",
     "Lower in High-growth because associates deliver more (see delivery cost %)."),
    ("proj_cost_pct", "Consulting delivery cost (associates, expenses) % of value", (0.30, 0.35, 0.45), "%",
     "ESTIMATE", "Cost of sales. Rises with associate share."),
    ("H", "E-learning"),
    ("el_launch", "E-learning launch month", (12, 9, 7), "month", "ASSUMPTION",
     "Two founder-authored courses first (01_BUSINESS_MODEL §6)."),
    ("el_init", "New learners per month at launch", (8, 15, 30), "learners", "ESTIMATE", ""),
    ("el_growth", "Monthly growth in new learners", (0.03, 0.05, 0.07), "%", "ESTIMATE", "Compound, from launch."),
    ("el_arpu", "Average revenue per learner (ARPU)", (150, 200, 300), "GBP", "ESTIMATE",
     "Range £150–£400; course prices £49–£299 UK, regional pricing lower."),
    ("corp_y1", "Corporate licences active — Y1", (0, 0, 1), "count", "ESTIMATE", ""),
    ("corp_y2", "Corporate licences active — Y2", (1, 3, 6), "count", "ESTIMATE", ""),
    ("corp_y3", "Corporate licences active — Y3", (2, 6, 12), "count", "ESTIMATE", ""),
    ("corp_value", "Corporate licence value per year", (2500, 5000, 9000), "GBP/year", "ESTIMATE",
     "£2,500 (10 seats) – £25,000 (250 seats) ladder."),
    ("el_cos_pct", "E-learning platform + payment fees % of revenue", (0.15, 0.15, 0.15), "%", "ESTIMATE", ""),
    ("el_content", "E-learning content build (one-off, launch month)", (8000, 12000, 20000), "GBP", "ESTIMATE",
     "£8k–£15k per course; two courses at launch (High builds more)."),
    ("H", "MaternaLink (in development) — pilots then licences"),
    ("ml_pilot_start", "First paid pilot month", (18, 13, 10), "month", "TO VALIDATE",
     "Gated by IP ownership, safety case, DPIA, a partner site (01_BUSINESS_MODEL §7)."),
    ("ml_pil_y1", "Active paid pilots — Y1", (0, 0, 1), "count", "ESTIMATE", ""),
    ("ml_pil_y2", "Active paid pilots — Y2", (1, 1, 2), "count", "ESTIMATE", ""),
    ("ml_pil_y3", "Active paid pilots — Y3", (1, 2, 4), "count", "ESTIMATE", ""),
    ("ml_pilot_value", "Pilot value per pilot per year", (40000, 75000, 150000), "GBP/year", "ESTIMATE",
     "Range £40k–£150k. Recognised evenly over the months the pilot is active."),
    ("ml_pilot_cost_pct", "Pilot delivery cost % of pilot value", (0.50, 0.45, 0.40), "%", "ESTIMATE",
     "Implementation, training, support; first pilots are near loss-leaders."),
    ("ml_golive", "Per-woman licence go-live month", (27, 19, 15), "month", "TO VALIDATE",
     "Conservative: small and from month 18+ (here 27)."),
    ("ml_delay", "Go-live delay (sensitivity input, months)", (0, 0, 0), "months", "INPUT",
     "Add months here to test regulatory/partner slippage."),
    ("uk_init", "UK women enrolled at go-live", (200, 500, 1500), "women", "ESTIMATE", ""),
    ("uk_add", "UK women added per month after go-live", (50, 100, 300), "women/month", "ESTIMATE", ""),
    ("uk_price", "UK licence per woman per year", (8, 20, 40), "GBP", "ESTIMATE",
     "Range £8–£40. Equivalent to £40k–£120k per trust site licence at 3,000–5,000 births."),
    ("uk_cost", "UK hosting/support cost per woman per year", (4, 4, 4), "GBP", "ESTIMATE", ""),
    ("af_init", "Africa women enrolled at go-live", (1000, 5000, 15000), "women", "ESTIMATE",
     "Donor- or state-funded programme cohorts (LGA-level pilots, not full state)."),
    ("af_add", "Africa women added per month after go-live", (250, 1000, 3000), "women/month", "ESTIMATE", ""),
    ("af_price", "Africa licence per woman per year", (3, 6, 12), "GBP", "ESTIMATE",
     "Range £3–£12 at scale. The Ekiti proposal's £300/woman/year is UNVALIDATED and far above comparables (FACTS_BASE A5); NOT used."),
    ("af_cost", "Africa hosting/SMS/support cost per woman per year", (2, 2.5, 3), "GBP", "ESTIMATE",
     "SMS pass-through excluded (billed at cost)."),
    ("H", "Payroll rates (UK 2026/27)"),
    ("ni_rate", "Employer NI rate (Class 1 secondary)", (0.15, 0.15, 0.15), "%", "KNOWN",
     "15% for 2026/27. Source: https://www.moorepay.co.uk/payroll-hr-rates/tax-and-national-insurance-changes/ ; TO VALIDATE against gov.uk rates page before use."),
    ("ni_threshold", "Employer NI secondary threshold (annual)", (5000, 5000, 5000), "GBP", "KNOWN",
     "£5,000 for 2026/27 (same source)."),
    ("emp_allowance", "Employment Allowance (annual; applied once headcount ≥ 2)", (10500, 10500, 10500), "GBP",
     "KNOWN", "£10,500; a company whose only employee paid above the threshold is a sole director cannot claim — hence applied only from 2+ employees. TO VALIDATE eligibility."),
    ("pen_rate", "Employer auto-enrolment pension minimum", (0.03, 0.03, 0.03), "%", "KNOWN",
     "3% of qualifying earnings. Source: https://www.moorepay.co.uk/payroll-hr-rates/automatic-enrolment/"),
    ("pen_lower", "Qualifying earnings lower limit (annual)", (6240, 6240, 6240), "GBP", "KNOWN", "2026/27 band £6,240–£50,270 (same source)."),
    ("pen_upper", "Qualifying earnings upper limit (annual)", (50270, 50270, 50270), "GBP", "KNOWN", ""),
    ("H", "Founder and hires (start month; 99 = not hired within model)"),
    ("founder_start", "Founder salary — start month", (4, 2, 1), "month", "ASSUMPTION",
     "Conservative: founder draws nothing until first invoices are paid."),
    ("founder_salary", "Founder salary (annual)", (36000, 48000, 60000), "GBP/year", "ASSUMPTION",
     "Below market; opportunity cost £120k (01_BUSINESS_MODEL §3)."),
]
HIRE_INPUTS = {
    "product_lead": ((13, 7, 4), (60000, 65000, 70000)),
    "dev1": ((19, 10, 6), (50000, 55000, 60000)),
    "dev2": ((99, 22, 12), (50000, 55000, 60000)),
    "dev3": ((99, 99, 24), (55000, 55000, 60000)),
    "bd_lead": ((99, 16, 10), (45000, 50000, 55000)),
    "prog_mgr": ((99, 20, 14), (25000, 30000, 30000)),
    "clinical_lead": ((99, 25, 16), (70000, 70000, 75000)),
    "content_lead": ((99, 99, 18), (40000, 40000, 45000)),
    "consultant": ((99, 19, 10), (55000, 55000, 60000)),
}
for k, lab in HIRES:
    st, sal = HIRE_INPUTS[k]
    note = ""
    if k == "prog_mgr":
        note = "Nigeria-based role modelled with UK on-costs as a conservative simplification; local employment/contractor route TO VALIDATE."
    if k == "consultant":
        note = "Adds billable capacity (see Advisory block)."
    ASSUMPTIONS.append((f"{k}_start", f"{lab} — start month", st, "month", "ASSUMPTION", note))
    ASSUMPTIONS.append((f"{k}_salary", f"{lab} — annual salary", sal, "GBP/year", "ESTIMATE", ""))

OPEX_CATS = [
    ("contractors", "Contractors (dev, design, fractional clinical safety officer)", ((1500, 2500, 3000), (4000, 6000, 6000), (8000, 10000, 8000))),
    ("technology", "Technology (cloud, hosting, messaging, tooling)", ((300, 800, 1500), (600, 1500, 3000), (1500, 4000, 8000))),
    ("marketing", "Marketing (content, events, paid tests)", ((300, 600, 1000), (750, 2000, 3000), (2000, 5000, 8000))),
    ("legal", "Legal (ongoing contracts, IP, employment)", ((300, 400, 500), (500, 800, 1000), (1000, 1500, 2000))),
    ("compliance", "Compliance & regulatory (ICO, Cyber Essentials, DTAC/DSPT, clinical safety)", ((150, 400, 800), (300, 1000, 1500), (600, 2000, 3000))),
    ("insurance", "Insurance (PI, PL, D&O, cyber)", ((120, 150, 200), (150, 250, 400), (200, 400, 700))),
    ("software", "Software subscriptions", ((120, 200, 300), (200, 400, 700), (300, 800, 1500))),
    ("travel", "Travel (UK and Nigeria)", ((200, 400, 600), (400, 1000, 1500), (800, 2500, 4000))),
    ("operations", "Operations (co-working, recruitment, misc.)", ((100, 300, 600), (250, 800, 1500), (500, 2000, 4000))),
    ("accountancy", "Accountancy, payroll, company secretarial", ((150, 200, 250), (200, 300, 400), (250, 400, 600))),
]
ASSUMPTIONS.append(("H", "Other operating costs (GBP per month, by year)"))
for k, lab, vals in OPEX_CATS:
    for i, y in enumerate(["Y1", "Y2", "Y3"]):
        ASSUMPTIONS.append((f"{k}_y{i+1}", f"{lab} — {y}", vals[i], "GBP/month", "ESTIMATE", ""))
ASSUMPTIONS += [
    ("legal_setup", "Legal & IP set-up (one-off, month 1)", (6000, 10000, 15000), "GBP", "ESTIMATE",
     "Incorporation, shareholders' agreement, MaternaLink IP assignment/licence, SEIS/EIS advance assurance, trade mark filing."),
    ("H", "Funding injections (amount, month; 99 = not in model)"),
    ("preseed_amt", "Pre-seed equity amount", (250000, 400000, 500000), "GBP", "PROPOSED", "SEIS/EIS angels. SEIS company cap £250k lifetime (TO VALIDATE, see 09_FUNDING_STRATEGY)."),
    ("preseed_m", "Pre-seed month", (6, 4, 3), "month", "PROPOSED", ""),
    ("seed_amt", "Seed equity amount", (0, 2000000, 3000000), "GBP", "PROPOSED", "Only raised if milestones in 09_FUNDING_STRATEGY are TRUE."),
    ("seed_m", "Seed month", (99, 20, 14), "month", "PROPOSED", ""),
    ("seriesa_amt", "Series A equity amount", (0, 0, 6000000), "GBP", "PROPOSED", "High-growth only, month 32."),
    ("seriesa_m", "Series A month", (99, 99, 32), "month", "PROPOSED", ""),
    ("grant1_amt", "Grant 1 (e.g., Innovate UK Smart / SBRI Healthcare)", (0, 75000, 150000), "GBP", "TO VALIDATE",
     "Competitive; success rates low. Recognised as other income when received (simplification)."),
    ("grant1_m", "Grant 1 month", (99, 14, 9), "month", "TO VALIDATE", ""),
    ("grant2_amt", "Grant 2 (e.g., NIHR i4i Connect / foundation)", (0, 0, 250000), "GBP", "TO VALIDATE", ""),
    ("grant2_m", "Grant 2 month", (99, 99, 21), "month", "TO VALIDATE", ""),
]


def scenario_values(idx):
    """Dict key -> value for scenario index 0/1/2."""
    return {a[0]: a[2][idx] for a in ASSUMPTIONS if a[0] != "H"}


# ----------------------------------------------------------------------------------------------------------------
# 2. PYTHON COMPUTATION (mirrors the workbook formulas exactly)
# ----------------------------------------------------------------------------------------------------------------
def compute(v):
    """v: dict of assumption values. Returns dict of monthly lists (index 0 = month 1) and summary metrics."""
    R = {}
    ms = list(range(1, MONTHS + 1))
    year = [START.year + (m - 1) // 12 for m in ms]
    yi = [y - 2026 for y in year]
    ramp = [min(1.0, max(0.0, (m - 1) / v["ramp_months"])) for m in ms]

    def by_year(prefix, i):
        return v[f"{prefix}_y{yi[i]}"]

    # Revenue
    bill = [v["avail_days"] * v["utilisation"] * ramp[i] for i in range(MONTHS)]
    ret = [(by_year("ret", i) if ms[i] >= v["ret_start"] else 0) for i in range(MONTHS)]
    ret_days = [r * v["ret_days"] for r in ret]
    proj = [by_year("proj", i) / 12 * ramp[i] for i in range(MONTHS)]
    proj_days = [p * v["fdays_proj"] for p in proj]
    adv_days = [max(0.0, bill[i] - ret_days[i] - proj_days[i]) for i in range(MONTHS)]
    cap_used = [((ret_days[i] + proj_days[i]) / bill[i]) if bill[i] > 0 else 0 for i in range(MONTHS)]
    adv_rev = [d * v["day_rate"] for d in adv_days]
    ret_rev = [r * v["ret_fee"] for r in ret]
    hire_flag = {k: [1 if ms[i] >= v[f"{k}_start"] else 0 for i in range(MONTHS)] for k, _ in HIRES}
    cons_days = [hire_flag["consultant"][i] * v["cons_days"] for i in range(MONTHS)]
    cons_rev = [d * v["cons_rate"] for d in cons_days]
    advisory = [adv_rev[i] + ret_rev[i] + cons_rev[i] for i in range(MONTHS)]
    consulting = [p * v["proj_value"] for p in proj]
    el_flag = [1 if ms[i] >= v["el_launch"] else 0 for i in range(MONTHS)]
    learners = [el_flag[i] * v["el_init"] * (1 + v["el_growth"]) ** (ms[i] - v["el_launch"]) if el_flag[i] else 0 for i in range(MONTHS)]
    course_rev = [l * v["el_arpu"] for l in learners]
    corp = [el_flag[i] * by_year("corp", i) for i in range(MONTHS)]
    corp_rev = [c * v["corp_value"] / 12 for c in corp]
    elearning = [course_rev[i] + corp_rev[i] for i in range(MONTHS)]
    pil_flag = [1 if ms[i] >= v["ml_pilot_start"] else 0 for i in range(MONTHS)]
    pilots = [pil_flag[i] * by_year("ml_pil", i) for i in range(MONTHS)]
    pilot_rev = [p * v["ml_pilot_value"] / 12 for p in pilots]
    golive = v["ml_golive"] + v["ml_delay"]
    live = [1 if ms[i] >= golive else 0 for i in range(MONTHS)]
    uk_w = [live[i] * (v["uk_init"] + v["uk_add"] * (ms[i] - golive)) for i in range(MONTHS)]
    uk_rev = [w * v["uk_price"] / 12 for w in uk_w]
    af_w = [live[i] * (v["af_init"] + v["af_add"] * (ms[i] - golive)) for i in range(MONTHS)]
    af_rev = [w * v["af_price"] / 12 for w in af_w]
    maternalink = [pilot_rev[i] + uk_rev[i] + af_rev[i] for i in range(MONTHS)]
    revenue = [advisory[i] + consulting[i] + elearning[i] + maternalink[i] for i in range(MONTHS)]

    # Cost of sales
    cos_adv = [(adv_days[i] + ret_days[i]) * v["adv_cost_day"] for i in range(MONTHS)]
    cos_cons = [c * v["proj_cost_pct"] for c in consulting]
    cos_el = [e * v["el_cos_pct"] for e in elearning]
    cos_pil = [p * v["ml_pilot_cost_pct"] for p in pilot_rev]
    cos_lic = [(uk_w[i] * v["uk_cost"] + af_w[i] * v["af_cost"]) / 12 for i in range(MONTHS)]
    cos = [cos_adv[i] + cos_cons[i] + cos_el[i] + cos_pil[i] + cos_lic[i] for i in range(MONTHS)]
    gp = [revenue[i] - cos[i] for i in range(MONTHS)]

    # Headcount and payroll
    founder_flag = [1 if ms[i] >= v["founder_start"] else 0 for i in range(MONTHS)]
    people = [("founder", founder_flag, v["founder_salary"])] + [(k, hire_flag[k], v[f"{k}_salary"]) for k, _ in HIRES]
    headcount = [founder_flag[i] + sum(hire_flag[k][i] for k, _ in HIRES) for i in range(MONTHS)]

    def ni_annual(sal):
        return max(0.0, sal - v["ni_threshold"]) * v["ni_rate"]

    def pen_annual(sal):
        return min(max(sal - v["pen_lower"], 0.0), v["pen_upper"] - v["pen_lower"]) * v["pen_rate"]

    sal_tot = [sum(f[i] * s / 12 for _, f, s in people) for i in range(MONTHS)]
    founder_sal = [founder_flag[i] * v["founder_salary"] / 12 for i in range(MONTHS)]
    emp_sal = [sal_tot[i] - founder_sal[i] for i in range(MONTHS)]
    ni_tot = [sum(f[i] * ni_annual(s) / 12 for _, f, s in people) for i in range(MONTHS)]
    pen_tot = [sum(f[i] * pen_annual(s) / 12 for _, f, s in people) for i in range(MONTHS)]
    ea = [-min(ni_tot[i], v["emp_allowance"] / 12 if headcount[i] >= 2 else 0) for i in range(MONTHS)]
    employment = [sal_tot[i] + ni_tot[i] + pen_tot[i] + ea[i] for i in range(MONTHS)]

    opex_cat = {k: [by_year(k, i) for i in range(MONTHS)] for k, _, _ in OPEX_CATS}
    legal_setup = [v["legal_setup"] if ms[i] == 1 else 0 for i in range(MONTHS)]
    el_content = [v["el_content"] if ms[i] == v["el_launch"] else 0 for i in range(MONTHS)]
    opex = [employment[i] + sum(opex_cat[k][i] for k in opex_cat) + legal_setup[i] + el_content[i] for i in range(MONTHS)]
    ebitda = [gp[i] - opex[i] for i in range(MONTHS)]
    grants = [(v["grant1_amt"] if ms[i] == v["grant1_m"] else 0) + (v["grant2_amt"] if ms[i] == v["grant2_m"] else 0) for i in range(MONTHS)]
    net = [ebitda[i] + grants[i] for i in range(MONTHS)]
    cum_net = []
    for i in range(MONTHS):
        cum_net.append(net[i] + (cum_net[i - 1] if i else 0))

    # Cash flow
    lag = int(v["collection_lag"])
    services = [advisory[i] + consulting[i] for i in range(MONTHS)]
    rec_serv = [(services[i - lag] if i - lag >= 0 else 0) for i in range(MONTHS)]
    rec_el = elearning[:]
    rec_ml = [(maternalink[i - lag] if i - lag >= 0 else 0) for i in range(MONTHS)]
    receipts = [rec_serv[i] + rec_el[i] + rec_ml[i] for i in range(MONTHS)]
    netop = [receipts[i] - cos[i] - opex[i] for i in range(MONTHS)]
    equity = {
        "preseed": [v["preseed_amt"] if ms[i] == v["preseed_m"] else 0 for i in range(MONTHS)],
        "seed": [v["seed_amt"] if ms[i] == v["seed_m"] else 0 for i in range(MONTHS)],
        "seriesa": [v["seriesa_amt"] if ms[i] == v["seriesa_m"] else 0 for i in range(MONTHS)],
    }
    funding = [grants[i] + equity["preseed"][i] + equity["seed"][i] + equity["seriesa"][i] for i in range(MONTHS)]
    opening, closing, cum_pre, min_cash = [], [], [], []
    for i in range(MONTHS):
        o = v["opening_cash"] if i == 0 else closing[i - 1]
        opening.append(o)
        closing.append(o + netop[i] + funding[i])
        cum_pre.append((v["opening_cash"] if i == 0 else cum_pre[i - 1]) + netop[i])
        min_cash.append(min(closing[i], min_cash[i - 1]) if i else closing[i])
    burn = [-n for n in netop]
    avg_burn3 = sum(burn[-3:]) / 3
    runway = (closing[-1] / avg_burn3) if avg_burn3 > 0 else None

    def first(flags):
        for i, f in enumerate(flags):
            if f:
                return i + 1
        return None

    R.update(dict(month=ms, year=year, yi=yi, ramp=ramp, bill=bill, ret=ret, ret_days=ret_days, proj=proj,
                  proj_days=proj_days, adv_days=adv_days, cap_used=cap_used, adv_rev=adv_rev, ret_rev=ret_rev,
                  cons_days=cons_days, cons_rev=cons_rev, advisory=advisory, consulting=consulting, el_flag=el_flag,
                  learners=learners, course_rev=course_rev, corp=corp, corp_rev=corp_rev, elearning=elearning,
                  pil_flag=pil_flag, pilots=pilots, pilot_rev=pilot_rev, live=live, uk_w=uk_w, uk_rev=uk_rev,
                  af_w=af_w, af_rev=af_rev, maternalink=maternalink, revenue=revenue, cos_adv=cos_adv,
                  cos_cons=cos_cons, cos_el=cos_el, cos_pil=cos_pil, cos_lic=cos_lic, cos=cos, gp=gp,
                  headcount=headcount, founder_sal=founder_sal, emp_sal=emp_sal, ni_tot=ni_tot, pen_tot=pen_tot,
                  ea=ea, employment=employment, legal_setup=legal_setup, el_content=el_content, opex=opex,
                  ebitda=ebitda, grants=grants, net=net, cum_net=cum_net, receipts=receipts, netop=netop,
                  funding=funding, opening=opening, closing=closing, cum_pre=cum_pre, min_cash=min_cash,
                  hire_flag=hire_flag, founder_flag=founder_flag, opex_cat=opex_cat, equity=equity, golive=golive))
    R["annual"] = {}
    for key in ["advisory", "consulting", "elearning", "maternalink", "revenue", "cos", "gp", "employment", "opex", "ebitda", "grants", "net", "receipts", "netop"]:
        R["annual"][key] = {y: sum(R[key][i] for i in range(MONTHS) if year[i] == y) for y in YEARS}
    R["annual"]["closing"] = {y: closing[YEARS.index(y) * 12 + 11] for y in YEARS}
    R["annual"]["headcount"] = {y: headcount[YEARS.index(y) * 12 + 11] for y in YEARS}
    R["metrics"] = dict(
        peak_need=max(0.0, -min(cum_pre)),
        peak_need_month=cum_pre.index(min(cum_pre)) + 1,
        be_month=first([e > 0 for e in ebitda]),
        be_cum_month=first([c > 0 for c in cum_net]),
        min_cash=min(closing),
        min_cash_month=closing.index(min(closing)) + 1,
        closing_36=closing[-1],
        equity_total=sum(sum(x) for x in equity.values()),
        grants_total=sum(grants),
        runway=runway,
        rev_3yr=sum(revenue), ebitda_3yr=sum(ebitda), ml_3yr=sum(maternalink),
    )
    return R


# ----------------------------------------------------------------------------------------------------------------
# 3. WORKBOOK
# ----------------------------------------------------------------------------------------------------------------
F_TITLE = Font(bold=True, size=14)
F_H = Font(bold=True, size=11)
F_B = Font(bold=True)
F_IN = Font(color="0000CC")  # inputs: blue
F_NOTE = Font(italic=True, color="666666", size=9)
FILL_H = PatternFill("solid", fgColor="DDEBF7")
FILL_IN = PatternFill("solid", fgColor="FFF2CC")
FILL_T = PatternFill("solid", fgColor="E2EFDA")
FILL_SEL = PatternFill("solid", fgColor="FCE4D6")
THIN = Side(style="thin", color="BBBBBB")
BOX = Border(top=THIN, bottom=THIN, left=THIN, right=THIN)
GBP = '#,##0;[Red]-#,##0'
GBP2 = '#,##0.00;[Red]-#,##0.00'
PCT = '0.0%'
NUM1 = '0.0'


class Model:
    def __init__(self):
        self.wb = Workbook()
        self.A = {}  # assumption key -> row
        self.rows = {}  # (sheet, key) -> row

    def aref(self, key):
        return f"Assumptions!$F${self.A[key]}"

    # --- Assumptions -------------------------------------------------------------------------------------------
    def build_assumptions(self):
        ws = self.wb.active
        ws.title = "Assumptions"
        ws["A1"] = "VYTALIX — Assumptions (all values are scenario inputs; none are actuals)"
        ws["A1"].font = F_TITLE
        ws["A2"] = "Labels: KNOWN (cited) · ESTIMATE · ASSUMPTION · PROPOSED · TO VALIDATE. Blue cells are inputs. Column F = active scenario via INDEX."
        ws["A2"].font = F_NOTE
        ws["A4"] = "SCENARIO SELECTOR (1 = Conservative, 2 = Base, 3 = High-growth)"
        ws["A4"].font = F_H
        ws["C4"] = 2
        ws["C4"].font = Font(bold=True, color="0000CC", size=12)
        ws["C4"].fill = FILL_SEL
        ws["C4"].border = BOX
        ws["D4"] = '=INDEX({"Conservative","Base","High-growth"},1,$C$4)'
        ws["D4"].font = F_B
        ws["A5"] = "Change C4 and the whole workbook (Revenue → Cash flow → Dashboard) re-points. Sensitivity and Static summary are Python-computed values and do not change."
        ws["A5"].font = F_NOTE
        hdr = ["Key", "Assumption", "Conservative", "Base", "High-growth", "ACTIVE", "Unit", "Label", "Note / source"]
        r = 7
        for c, h in enumerate(hdr, 1):
            cell = ws.cell(row=r, column=c, value=h)
            cell.font = F_B
            cell.fill = FILL_H
            cell.border = BOX
        r += 1
        for a in ASSUMPTIONS:
            if a[0] == "H":
                ws.cell(row=r, column=1, value=a[1]).font = F_H
                for c in range(1, 10):
                    ws.cell(row=r, column=c).fill = FILL_H
                r += 1
                continue
            key, label, vals, unit, tag, note = a
            self.A[key] = r
            ws.cell(row=r, column=1, value=key).font = F_NOTE
            ws.cell(row=r, column=2, value=label)
            for i, val in enumerate(vals):
                cell = ws.cell(row=r, column=3 + i, value=val)
                cell.font = F_IN
                cell.fill = FILL_IN
                cell.border = BOX
                cell.number_format = PCT if unit == "%" else (GBP2 if unit in ("GBP", "GBP/day") and val < 100 else (GBP if "GBP" in unit else "0.##"))
            fcell = ws.cell(row=r, column=6, value=f"=INDEX($C{r}:$E{r},1,$C$4)")
            fcell.font = F_B
            fcell.fill = FILL_T
            fcell.border = BOX
            fcell.number_format = ws.cell(row=r, column=3).number_format
            ws.cell(row=r, column=7, value=unit)
            ws.cell(row=r, column=8, value=tag)
            ws.cell(row=r, column=9, value=note).font = F_NOTE
            r += 1
        # derived payroll block
        r += 1
        ws.cell(row=r, column=1, value="Derived payroll on-costs per person (annual) — formulas, not inputs").font = F_H
        r += 1
        for c, h in enumerate(["Key", "Person", "Annual salary (active)", "Employer NI (annual)", "Employer pension (annual)", "Total cost (annual)"], 1):
            ws.cell(row=r, column=c, value=h).font = F_B
        r += 1
        self.payroll_rows = {}
        for k, lab in [("founder", "Founder")] + HIRES:
            sal = self.aref(f"{k}_salary")
            ws.cell(row=r, column=1, value=k).font = F_NOTE
            ws.cell(row=r, column=2, value=lab)
            ws.cell(row=r, column=3, value=f"={sal}").number_format = GBP
            ws.cell(row=r, column=4, value=f"=MAX(0,{sal}-{self.aref('ni_threshold')})*{self.aref('ni_rate')}").number_format = GBP
            ws.cell(row=r, column=5, value=f"=MIN(MAX({sal}-{self.aref('pen_lower')},0),{self.aref('pen_upper')}-{self.aref('pen_lower')})*{self.aref('pen_rate')}").number_format = GBP
            ws.cell(row=r, column=6, value=f"=C{r}+D{r}+E{r}").number_format = GBP
            self.payroll_rows[k] = r
            r += 1
        ws.column_dimensions["A"].width = 16
        ws.column_dimensions["B"].width = 62
        for col in "CDEF":
            ws.column_dimensions[col].width = 14
        ws.column_dimensions["G"].width = 12
        ws.column_dimensions["H"].width = 13
        ws.column_dimensions["I"].width = 90
        ws.freeze_panes = "C8"

    # --- timeline helpers ----------------------------------------------------------------------------------------
    def new_timeline(self, name, title):
        ws = self.wb.create_sheet(name)
        ws["A1"] = title
        ws["A1"].font = F_TITLE
        ws["A2"] = '="Scenario: "&Assumptions!$D$4&"  —  all figures GBP, scenario values, not actuals"'
        ws["A2"].font = F_NOTE
        ws.cell(row=3, column=1, value="Month #").font = F_B
        ws.cell(row=4, column=1, value="Month").font = F_B
        ws.cell(row=5, column=1, value="Year").font = F_B
        ws.cell(row=6, column=1, value="Year index").font = F_B
        for m in range(1, MONTHS + 1):
            c = COL0 + m - 1
            d = dt.date(START.year + (m - 1) // 12, (m - 1) % 12 + 1, 1)
            ws.cell(row=3, column=c, value=m).font = F_B
            dc = ws.cell(row=4, column=c, value=d)
            dc.number_format = "mmm-yy"
            dc.font = F_B
            ws.cell(row=5, column=c, value=d.year).font = F_B
            ws.cell(row=6, column=c, value=f"={mcol(m)}5-2026")
            ws.column_dimensions[mcol(m)].width = 11
        for y, col in YCOL.items():
            ws[f"{col}5"] = y
            ws[f"{col}5"].font = F_B
            ws[f"{col}4"] = f"FY{y}"
            ws[f"{col}4"].font = F_B
            ws.column_dimensions[col].width = 13
        ws[f"{TCOL}4"] = "3-year total"
        ws[f"{TCOL}4"].font = F_B
        ws.column_dimensions[TCOL].width = 13
        ws.column_dimensions["A"].width = 52
        ws.column_dimensions["B"].width = 14
        ws.freeze_panes = "C7"
        for c in range(1, COL0 + MONTHS + 5):
            ws.cell(row=3, column=c).fill = FILL_H
            ws.cell(row=4, column=c).fill = FILL_H
            ws.cell(row=5, column=c).fill = FILL_H
        return ws

    def row(self, ws, r, key, label, fn, fmt=GBP, annual="sum", bold=False, unit=""):
        """fn(m) -> formula string for month m (without leading '=' optional)."""
        self.rows[(ws.title, key)] = r
        ws.cell(row=r, column=1, value=label).font = F_B if bold else Font()
        ws.cell(row=r, column=2, value=unit).font = F_NOTE
        for m in range(1, MONTHS + 1):
            f = fn(m)
            if isinstance(f, str) and not f.startswith("="):
                f = "=" + f
            cell = ws.cell(row=r, column=COL0 + m - 1, value=f)
            cell.number_format = fmt
            if bold:
                cell.font = F_B
                cell.fill = FILL_T
        rng = f"{FIRST}{r}:{LAST}{r}"
        if annual == "sum":
            for y, col in YCOL.items():
                ws[f"{col}{r}"] = f"=SUMIF(${FIRST}$5:${LAST}$5,{col}$5,{rng})"
            ws[f"{TCOL}{r}"] = f"=SUM({rng})"
        elif annual == "end":
            for k, (y, col) in enumerate(YCOL.items()):
                ws[f"{col}{r}"] = f"=INDEX({rng},1,{12 * (k + 1)})"
            ws[f"{TCOL}{r}"] = f"=INDEX({rng},1,{MONTHS})"
        elif annual == "avg":
            for y, col in YCOL.items():
                ws[f"{col}{r}"] = f"=AVERAGEIF(${FIRST}$5:${LAST}$5,{col}$5,{rng})"
            ws[f"{TCOL}{r}"] = f"=AVERAGE({rng})"
        if annual:
            for col in list(YCOL.values()) + [TCOL]:
                ws[f"{col}{r}"].number_format = fmt
                if bold:
                    ws[f"{col}{r}"].font = F_B
                    ws[f"{col}{r}"].fill = FILL_T
        return r

    def header(self, ws, r, text):
        ws.cell(row=r, column=1, value=text).font = F_H
        for c in range(1, COL0 + MONTHS + 5):
            ws.cell(row=r, column=c).fill = FILL_H
        return r

    def ref(self, sheet, key, m):
        return q(sheet, f"{mcol(m)}{self.rows[(sheet, key)]}")

    def ratio_annual(self, ws, r, num_key, den_key):
        for col in list(YCOL.values()) + [TCOL]:
            n = f"{col}{self.rows[(ws.title, num_key)]}"
            d = f"{col}{self.rows[(ws.title, den_key)]}"
            ws[f"{col}{r}"] = f"=IF({d}<>0,{n}/{d},0)"
            ws[f"{col}{r}"].number_format = PCT

    # --- Revenue -----------------------------------------------------------------------------------------------
    def build_revenue(self):
        ws = self.new_timeline("Revenue build", "Revenue build — Advisory, Consulting, E-learning, MaternaLink (in development)")
        A = self.aref
        S = ws.title
        r = 7
        self.row(ws, r, "ramp", "Sales ramp factor", lambda m: f"MIN(1,MAX(0,({mcol(m)}3-1)/{A('ramp_months')}))", NUM1 if False else '0.00', "avg"); r += 1
        r = self.header(ws, r, "ADVISORY") + 1
        self.row(ws, r, "avail", "Founder available days", lambda m: f"{A('avail_days')}", NUM1, "sum", unit="days"); r += 1
        self.row(ws, r, "util", "Founder billable utilisation", lambda m: f"{A('utilisation')}", PCT, "avg"); r += 1
        self.row(ws, r, "bill", "Founder billable days (utilisation × ramp)", lambda m: f"{self.ref(S,'avail',m)}*{self.ref(S,'util',m)}*{self.ref(S,'ramp',m)}", NUM1, "sum", unit="days"); r += 1
        self.row(ws, r, "ret", "Retainers active", lambda m: f"IF({mcol(m)}3>={A('ret_start')},CHOOSE({mcol(m)}6,{A('ret_y1')},{A('ret_y2')},{A('ret_y3')}),0)", '0.0', "avg", unit="count"); r += 1
        self.row(ws, r, "ret_days", "Founder days consumed by retainers", lambda m: f"{self.ref(S,'ret',m)}*{A('ret_days')}", NUM1, "sum", unit="days"); r += 1
        self.row(ws, r, "proj", "Consulting projects (per month, smoothed)", lambda m: f"CHOOSE({mcol(m)}6,{A('proj_y1')},{A('proj_y2')},{A('proj_y3')})/12*{self.ref(S,'ramp',m)}", '0.00', "sum", unit="count"); r += 1
        self.row(ws, r, "proj_days", "Founder days consumed by consulting delivery", lambda m: f"{self.ref(S,'proj',m)}*{A('fdays_proj')}", NUM1, "sum", unit="days"); r += 1
        self.row(ws, r, "adv_days", "Advisory day-rate days sold (residual capacity)", lambda m: f"MAX(0,{self.ref(S,'bill',m)}-{self.ref(S,'ret_days',m)}-{self.ref(S,'proj_days',m)})", NUM1, "sum", unit="days"); r += 1
        self.row(ws, r, "cap_used", "Founder capacity used by retainers + projects (>100% = associate-dependent)", lambda m: f"IF({self.ref(S,'bill',m)}>0,({self.ref(S,'ret_days',m)}+{self.ref(S,'proj_days',m)})/{self.ref(S,'bill',m)},0)", PCT, "avg"); r += 1
        self.row(ws, r, "day_rate", "Founder day rate", lambda m: f"{A('day_rate')}", GBP, "avg", unit="GBP/day"); r += 1
        self.row(ws, r, "adv_rev", "Advisory day-rate revenue", lambda m: f"{self.ref(S,'adv_days',m)}*{self.ref(S,'day_rate',m)}"); r += 1
        self.row(ws, r, "ret_rev", "Retainer revenue", lambda m: f"{self.ref(S,'ret',m)}*{A('ret_fee')}"); r += 1
        self.row(ws, r, "cons_days", "Senior consultant billable days", lambda m: f"{q('Headcount', mcol(m) + str(self.rows[('Headcount','flag_consultant')]))}*{A('cons_days')}", NUM1, "sum", unit="days"); r += 1
        self.row(ws, r, "cons_rev", "Senior consultant revenue", lambda m: f"{self.ref(S,'cons_days',m)}*{A('cons_rate')}"); r += 1
        self.row(ws, r, "advisory", "ADVISORY REVENUE", lambda m: f"{self.ref(S,'adv_rev',m)}+{self.ref(S,'ret_rev',m)}+{self.ref(S,'cons_rev',m)}", bold=True); r += 2
        r = self.header(ws, r, "CONSULTING") + 1
        self.row(ws, r, "proj_value", "Average project value", lambda m: f"{A('proj_value')}", GBP, "avg", unit="GBP"); r += 1
        self.row(ws, r, "consulting", "CONSULTING REVENUE (projects × value)", lambda m: f"{self.ref(S,'proj',m)}*{self.ref(S,'proj_value',m)}", bold=True); r += 2
        r = self.header(ws, r, "E-LEARNING") + 1
        self.row(ws, r, "el_flag", "Launched (1/0)", lambda m: f"IF({mcol(m)}3>={A('el_launch')},1,0)", '0', "end"); r += 1
        self.row(ws, r, "learners", "New learners per month", lambda m: f"IF({self.ref(S,'el_flag',m)}=1,{A('el_init')}*(1+{A('el_growth')})^({mcol(m)}3-{A('el_launch')}),0)", NUM1, "sum", unit="learners"); r += 1
        self.row(ws, r, "arpu", "ARPU", lambda m: f"{A('el_arpu')}", GBP, "avg", unit="GBP"); r += 1
        self.row(ws, r, "course_rev", "Course revenue (learners × ARPU)", lambda m: f"{self.ref(S,'learners',m)}*{self.ref(S,'arpu',m)}"); r += 1
        self.row(ws, r, "corp", "Corporate licences active", lambda m: f"{self.ref(S,'el_flag',m)}*CHOOSE({mcol(m)}6,{A('corp_y1')},{A('corp_y2')},{A('corp_y3')})", '0', "avg", unit="count"); r += 1
        self.row(ws, r, "corp_rev", "Corporate licence revenue", lambda m: f"{self.ref(S,'corp',m)}*{A('corp_value')}/12"); r += 1
        self.row(ws, r, "elearning", "E-LEARNING REVENUE", lambda m: f"{self.ref(S,'course_rev',m)}+{self.ref(S,'corp_rev',m)}", bold=True); r += 2
        r = self.header(ws, r, "MATERNALINK (IN DEVELOPMENT)") + 1
        self.row(ws, r, "pil_flag", "Paid pilots started (1/0)", lambda m: f"IF({mcol(m)}3>={A('ml_pilot_start')},1,0)", '0', "end"); r += 1
        self.row(ws, r, "pilots", "Active paid pilots", lambda m: f"{self.ref(S,'pil_flag',m)}*CHOOSE({mcol(m)}6,{A('ml_pil_y1')},{A('ml_pil_y2')},{A('ml_pil_y3')})", '0', "avg", unit="count"); r += 1
        self.row(ws, r, "pilot_rev", "Pilot revenue (pilots × value ÷ 12)", lambda m: f"{self.ref(S,'pilots',m)}*{A('ml_pilot_value')}/12"); r += 1
        self.row(ws, r, "golive", "Licence go-live month (base + delay)", lambda m: f"{A('ml_golive')}+{A('ml_delay')}", '0', "end", unit="month"); r += 1
        self.row(ws, r, "live", "Licences live (1/0)", lambda m: f"IF({mcol(m)}3>={self.ref(S,'golive',m)},1,0)", '0', "end"); r += 1
        self.row(ws, r, "uk_w", "UK women enrolled", lambda m: f"{self.ref(S,'live',m)}*({A('uk_init')}+{A('uk_add')}*({mcol(m)}3-{self.ref(S,'golive',m)}))", '#,##0', "end", unit="women"); r += 1
        self.row(ws, r, "uk_rev", "UK licence revenue (women × £/yr ÷ 12)", lambda m: f"{self.ref(S,'uk_w',m)}*{A('uk_price')}/12"); r += 1
        self.row(ws, r, "af_w", "Africa women enrolled", lambda m: f"{self.ref(S,'live',m)}*({A('af_init')}+{A('af_add')}*({mcol(m)}3-{self.ref(S,'golive',m)}))", '#,##0', "end", unit="women"); r += 1
        self.row(ws, r, "af_rev", "Africa licence revenue (women × £/yr ÷ 12)", lambda m: f"{self.ref(S,'af_w',m)}*{A('af_price')}/12"); r += 1
        self.row(ws, r, "maternalink", "MATERNALINK REVENUE", lambda m: f"{self.ref(S,'pilot_rev',m)}+{self.ref(S,'uk_rev',m)}+{self.ref(S,'af_rev',m)}", bold=True); r += 2
        self.row(ws, r, "revenue", "TOTAL REVENUE", lambda m: f"{self.ref(S,'advisory',m)}+{self.ref(S,'consulting',m)}+{self.ref(S,'elearning',m)}+{self.ref(S,'maternalink',m)}", bold=True); r += 1
        ws.cell(row=r + 1, column=1, value="Note: the £300/woman/year in the Ekiti proposal is UNVALIDATED (FACTS_BASE A5) and is not used anywhere in this model.").font = F_NOTE

    # --- Headcount ---------------------------------------------------------------------------------------------
    def build_headcount(self):
        ws = self.new_timeline("Headcount", "Headcount and payroll (employer NI 15% above £5,000; pension 3% of qualifying earnings)")
        A = self.aref
        S = ws.title
        r = 7
        r = self.header(ws, r, "HEADCOUNT FLAGS (1 = employed in month)") + 1
        people = [("founder", "Founder")] + HIRES
        for k, lab in people:
            self.row(ws, r, f"flag_{k}", lab, lambda m, k=k: f"IF({mcol(m)}3>={A(k + '_start')},1,0)", '0', "end"); r += 1
        first_flag, last_flag = self.rows[(S, "flag_founder")], r - 1
        self.row(ws, r, "headcount", "TOTAL HEADCOUNT", lambda m: f"SUM({mcol(m)}{first_flag}:{mcol(m)}{last_flag})", '0', "end", bold=True); r += 2
        r = self.header(ws, r, "GROSS SALARIES (monthly)") + 1
        for k, lab in people:
            self.row(ws, r, f"sal_{k}", lab, lambda m, k=k: f"{self.ref(S,'flag_'+k,m)}*Assumptions!$C${self.payroll_rows[k]}/12"); r += 1
        self.row(ws, r, "sal_tot", "Total gross salaries", lambda m: f"SUM({mcol(m)}{self.rows[(S,'sal_founder')]}:{mcol(m)}{r-1})", bold=True); r += 2
        r = self.header(ws, r, "EMPLOYER NATIONAL INSURANCE (monthly)") + 1
        for k, lab in people:
            self.row(ws, r, f"ni_{k}", lab, lambda m, k=k: f"{self.ref(S,'flag_'+k,m)}*Assumptions!$D${self.payroll_rows[k]}/12"); r += 1
        self.row(ws, r, "ni_tot", "Total employer NI (before Employment Allowance)", lambda m: f"SUM({mcol(m)}{self.rows[(S,'ni_founder')]}:{mcol(m)}{r-1})", bold=True); r += 2
        r = self.header(ws, r, "EMPLOYER PENSION (monthly)") + 1
        for k, lab in people:
            self.row(ws, r, f"pen_{k}", lab, lambda m, k=k: f"{self.ref(S,'flag_'+k,m)}*Assumptions!$E${self.payroll_rows[k]}/12"); r += 1
        self.row(ws, r, "pen_tot", "Total employer pension", lambda m: f"SUM({mcol(m)}{self.rows[(S,'pen_founder')]}:{mcol(m)}{r-1})", bold=True); r += 2
        self.row(ws, r, "ea", "Employment Allowance credit (once headcount ≥ 2)", lambda m: f"-MIN({self.ref(S,'ni_tot',m)},IF({self.ref(S,'headcount',m)}>=2,{A('emp_allowance')}/12,0))"); r += 1
        self.row(ws, r, "employment", "TOTAL EMPLOYMENT COST", lambda m: f"{self.ref(S,'sal_tot',m)}+{self.ref(S,'ni_tot',m)}+{self.ref(S,'pen_tot',m)}+{self.ref(S,'ea',m)}", bold=True); r += 1

    # --- Cost of sales -----------------------------------------------------------------------------------------
    def build_cos(self):
        ws = self.new_timeline("Cost of sales", "Cost of sales and gross margin")
        A = self.aref
        S, RV = ws.title, "Revenue build"
        r = 7
        self.row(ws, r, "cos_adv", "Advisory direct costs (travel/tools per billable day)", lambda m: f"({self.ref(RV,'adv_days',m)}+{self.ref(RV,'ret_days',m)})*{A('adv_cost_day')}"); r += 1
        self.row(ws, r, "cos_cons", "Consulting delivery (associates, expenses)", lambda m: f"{self.ref(RV,'consulting',m)}*{A('proj_cost_pct')}"); r += 1
        self.row(ws, r, "cos_el", "E-learning platform and payment fees", lambda m: f"{self.ref(RV,'elearning',m)}*{A('el_cos_pct')}"); r += 1
        self.row(ws, r, "cos_pil", "MaternaLink pilot delivery", lambda m: f"{self.ref(RV,'pilot_rev',m)}*{A('ml_pilot_cost_pct')}"); r += 1
        self.row(ws, r, "cos_lic", "MaternaLink licence hosting/support", lambda m: f"({self.ref(RV,'uk_w',m)}*{A('uk_cost')}+{self.ref(RV,'af_w',m)}*{A('af_cost')})/12"); r += 1
        self.row(ws, r, "cos", "TOTAL COST OF SALES", lambda m: f"SUM({mcol(m)}{self.rows[(S,'cos_adv')]}:{mcol(m)}{r-1})", bold=True); r += 2
        self.row(ws, r, "revenue", "Total revenue", lambda m: f"{self.ref(RV,'revenue',m)}"); r += 1
        self.row(ws, r, "gp", "GROSS PROFIT", lambda m: f"{self.ref(S,'revenue',m)}-{self.ref(S,'cos',m)}", bold=True); r += 1
        self.row(ws, r, "gm", "Gross margin %", lambda m: f"IF({self.ref(S,'revenue',m)}>0,{self.ref(S,'gp',m)}/{self.ref(S,'revenue',m)},0)", PCT, None); r += 1
        self.ratio_annual(ws, r - 1, "gp", "revenue")

    # --- Opex --------------------------------------------------------------------------------------------------
    def build_opex(self):
        ws = self.new_timeline("Opex", "Operating expenses")
        A = self.aref
        S, HC = ws.title, "Headcount"
        r = 7
        r = self.header(ws, r, "PEOPLE") + 1
        self.row(ws, r, "founder_sal", "Founder salary", lambda m: f"{self.ref(HC,'sal_founder',m)}"); r += 1
        self.row(ws, r, "emp_sal", "Employee salaries (hires)", lambda m: f"{self.ref(HC,'sal_tot',m)}-{self.ref(HC,'sal_founder',m)}"); r += 1
        self.row(ws, r, "ni", "Employer NI (15% above secondary threshold)", lambda m: f"{self.ref(HC,'ni_tot',m)}"); r += 1
        self.row(ws, r, "pen", "Employer pension (3% qualifying earnings)", lambda m: f"{self.ref(HC,'pen_tot',m)}"); r += 1
        self.row(ws, r, "ea", "Employment Allowance credit", lambda m: f"{self.ref(HC,'ea',m)}"); r += 1
        self.row(ws, r, "employment", "Total employment cost", lambda m: f"SUM({mcol(m)}{self.rows[(S,'founder_sal')]}:{mcol(m)}{r-1})", bold=True); r += 2
        r = self.header(ws, r, "OTHER OPERATING COSTS") + 1
        first_other = r
        for k, lab, _ in OPEX_CATS:
            self.row(ws, r, k, lab, lambda m, k=k: f"CHOOSE({mcol(m)}6,{A(k+'_y1')},{A(k+'_y2')},{A(k+'_y3')})"); r += 1
        self.row(ws, r, "legal_setup", "Legal & IP set-up (one-off)", lambda m: f"IF({mcol(m)}3=1,{A('legal_setup')},0)"); r += 1
        self.row(ws, r, "el_content", "E-learning content build (one-off at launch)", lambda m: f"IF({mcol(m)}3={A('el_launch')},{A('el_content')},0)"); r += 1
        self.row(ws, r, "other", "Total other operating costs", lambda m: f"SUM({mcol(m)}{first_other}:{mcol(m)}{r-1})", bold=True); r += 2
        self.row(ws, r, "opex", "TOTAL OPERATING EXPENSES", lambda m: f"{self.ref(S,'employment',m)}+{self.ref(S,'other',m)}", bold=True); r += 1

    # --- P&L ---------------------------------------------------------------------------------------------------
    def build_pl(self):
        ws = self.new_timeline("P&L", "Profit and loss — monthly (columns C:AL) and annual (columns AN:AQ)")
        S, RV, CS, OX = ws.title, "Revenue build", "Cost of sales", "Opex"
        r = 7
        r = self.header(ws, r, "REVENUE") + 1
        self.row(ws, r, "advisory", "Advisory", lambda m: f"{self.ref(RV,'advisory',m)}"); r += 1
        self.row(ws, r, "consulting", "Consulting", lambda m: f"{self.ref(RV,'consulting',m)}"); r += 1
        self.row(ws, r, "elearning", "E-learning", lambda m: f"{self.ref(RV,'elearning',m)}"); r += 1
        self.row(ws, r, "maternalink", "MaternaLink (in development)", lambda m: f"{self.ref(RV,'maternalink',m)}"); r += 1
        self.row(ws, r, "revenue", "TOTAL REVENUE", lambda m: f"SUM({mcol(m)}{self.rows[(S,'advisory')]}:{mcol(m)}{r-1})", bold=True); r += 1
        self.row(ws, r, "cos", "Cost of sales", lambda m: f"-{self.ref(CS,'cos',m)}"); r += 1
        self.row(ws, r, "gp", "GROSS PROFIT", lambda m: f"{self.ref(S,'revenue',m)}+{self.ref(S,'cos',m)}", bold=True); r += 1
        self.row(ws, r, "gm", "Gross margin %", lambda m: f"IF({self.ref(S,'revenue',m)}>0,{self.ref(S,'gp',m)}/{self.ref(S,'revenue',m)},0)", PCT, None); r += 1
        self.ratio_annual(ws, r - 1, "gp", "revenue")
        r = self.header(ws, r, "OPERATING EXPENSES") + 1
        self.row(ws, r, "employment", "Employment (founder + hires, incl. NI and pension)", lambda m: f"-{self.ref(OX,'employment',m)}"); r += 1
        for k, lab, _ in OPEX_CATS:
            self.row(ws, r, k, lab.split(" (")[0], lambda m, k=k: f"-{self.ref(OX,k,m)}"); r += 1
        self.row(ws, r, "legal_setup", "Legal & IP set-up (one-off)", lambda m: f"-{self.ref(OX,'legal_setup',m)}"); r += 1
        self.row(ws, r, "el_content", "E-learning content build", lambda m: f"-{self.ref(OX,'el_content',m)}"); r += 1
        self.row(ws, r, "opex", "TOTAL OPERATING EXPENSES", lambda m: f"SUM({mcol(m)}{self.rows[(S,'employment')]}:{mcol(m)}{r-1})", bold=True); r += 2
        self.row(ws, r, "ebitda", "EBITDA / OPERATING RESULT (before grants)", lambda m: f"{self.ref(S,'gp',m)}+{self.ref(S,'opex',m)}", bold=True); r += 1
        self.row(ws, r, "ebitda_flag", "EBITDA positive (1/0)", lambda m: f"IF({self.ref(S,'ebitda',m)}>0,1,0)", '0', None); r += 1
        self.row(ws, r, "grants", "Grant income (other income; TO VALIDATE)", lambda m: f"{self.ref('Cash flow','grants',m)}"); r += 1
        self.row(ws, r, "net", "NET RESULT BEFORE TAX", lambda m: f"{self.ref(S,'ebitda',m)}+{self.ref(S,'grants',m)}", bold=True); r += 1
        self.row(ws, r, "cum_net", "Cumulative net result", lambda m: f"{self.ref(S,'net',m)}" if m == 1 else f"{self.ref(S,'cum_net',m-1)}+{self.ref(S,'net',m)}", GBP, "end"); r += 1
        self.row(ws, r, "cum_flag", "Cumulative result positive (1/0)", lambda m: f"IF({self.ref(S,'cum_net',m)}>0,1,0)", '0', None); r += 1
        ws.cell(row=r + 1, column=1, value="No depreciation, interest, corporation tax or VAT modelled (loss-making; R&D tax relief is an unmodelled upside, TO VALIDATE).").font = F_NOTE

    # --- Cash flow ---------------------------------------------------------------------------------------------
    def build_cashflow(self):
        ws = self.new_timeline("Cash flow", "Cash flow — receipts with collection lag, funding injections, closing cash, runway")
        A = self.aref
        S, RV, CS, OX = ws.title, "Revenue build", "Cost of sales", "Opex"
        r = 7
        self.row(ws, r, "opening", "Opening cash", lambda m: f"{A('opening_cash')}" if m == 1 else f"{self.ref(S,'closing',m-1)}", GBP, None); r += 1
        r = self.header(ws, r, "OPERATING CASH FLOW") + 1

        def lagged(key):
            row = self.rows[(RV, key)]
            rng = q(RV, f"${FIRST}${row}:${LAST}${row}")
            return lambda m: f"IF({mcol(m)}3-{A('collection_lag')}<1,0,INDEX({rng},1,{mcol(m)}3-{A('collection_lag')}))"

        adv_l, con_l, ml_l = lagged("advisory"), lagged("consulting"), lagged("maternalink")
        self.row(ws, r, "rec_serv", "Receipts — advisory & consulting (lagged)", lambda m: f"{adv_l(m)}+{con_l(m)}"); r += 1
        self.row(ws, r, "rec_el", "Receipts — e-learning (prepaid)", lambda m: f"{self.ref(RV,'elearning',m)}"); r += 1
        self.row(ws, r, "rec_ml", "Receipts — MaternaLink (lagged)", ml_l); r += 1
        self.row(ws, r, "receipts", "Total receipts", lambda m: f"SUM({mcol(m)}{self.rows[(S,'rec_serv')]}:{mcol(m)}{r-1})", bold=True); r += 1
        self.row(ws, r, "pay_cos", "Payments — cost of sales", lambda m: f"-{self.ref(CS,'cos',m)}"); r += 1
        self.row(ws, r, "pay_opex", "Payments — operating expenses", lambda m: f"-{self.ref(OX,'opex',m)}"); r += 1
        self.row(ws, r, "netop", "NET OPERATING CASH FLOW", lambda m: f"{self.ref(S,'receipts',m)}+{self.ref(S,'pay_cos',m)}+{self.ref(S,'pay_opex',m)}", bold=True); r += 2
        r = self.header(ws, r, "FUNDING INJECTIONS (by round / month)") + 1
        self.row(ws, r, "grants", "Grant receipts (non-dilutive; TO VALIDATE)", lambda m: f"IF({mcol(m)}3={A('grant1_m')},{A('grant1_amt')},0)+IF({mcol(m)}3={A('grant2_m')},{A('grant2_amt')},0)"); r += 1
        self.row(ws, r, "preseed", "Pre-seed equity (SEIS/EIS angels)", lambda m: f"IF({mcol(m)}3={A('preseed_m')},{A('preseed_amt')},0)"); r += 1
        self.row(ws, r, "seed", "Seed equity", lambda m: f"IF({mcol(m)}3={A('seed_m')},{A('seed_amt')},0)"); r += 1
        self.row(ws, r, "seriesa", "Series A equity", lambda m: f"IF({mcol(m)}3={A('seriesa_m')},{A('seriesa_amt')},0)"); r += 1
        self.row(ws, r, "funding", "Total funding received", lambda m: f"SUM({mcol(m)}{self.rows[(S,'grants')]}:{mcol(m)}{r-1})", bold=True); r += 2
        self.row(ws, r, "netcf", "NET CASH FLOW", lambda m: f"{self.ref(S,'netop',m)}+{self.ref(S,'funding',m)}", bold=True); r += 1
        self.row(ws, r, "closing", "CLOSING CASH", lambda m: f"{self.ref(S,'opening',m)}+{self.ref(S,'netcf',m)}", GBP, "end", bold=True); r += 1
        self.row(ws, r, "min_cash", "Minimum closing cash to date", lambda m: f"{self.ref(S,'closing',m)}" if m == 1 else f"MIN({self.ref(S,'min_cash',m-1)},{self.ref(S,'closing',m)})", GBP, "end"); r += 1
        self.row(ws, r, "cum_pre", "Cumulative cash BEFORE external funding (opening cash + operating cash flow)", lambda m: f"{A('opening_cash')}+{self.ref(S,'netop',m)}" if m == 1 else f"{self.ref(S,'cum_pre',m-1)}+{self.ref(S,'netop',m)}", GBP, "end"); r += 1
        self.row(ws, r, "burn", "Monthly burn (negative of operating cash flow)", lambda m: f"-{self.ref(S,'netop',m)}", GBP, "avg"); r += 1
        self.row(ws, r, "runway", "Runway (months of closing cash at trailing 3-month burn)",
                 lambda m: f'IF(AVERAGE({mcol(max(1,m-2))}{r-1}:{mcol(m)}{r-1})>0,{self.ref(S,"closing",m)}/AVERAGE({mcol(max(1,m-2))}{r-1}:{mcol(m)}{r-1}),"cash-generative")', NUM1, "end"); r += 1

    # --- Funding requirement -----------------------------------------------------------------------------------
    def build_funding(self):
        ws = self.wb.create_sheet("Funding requirement")
        ws["A1"] = "Funding requirement — peak cash need, break-even, runway (active scenario)"
        ws["A1"].font = F_TITLE
        ws["A2"] = '="Scenario: "&Assumptions!$D$4'
        ws["A2"].font = F_NOTE
        CF, PL, HC = "Cash flow", "P&L", "Headcount"
        A = self.aref

        def rng(sheet, key):
            row = self.rows[(sheet, key)]
            return q(sheet, f"${FIRST}${row}:${LAST}${row}")

        def month_date(expr):
            return f'=IF(ISNUMBER({expr}),TEXT(DATE(2027,{expr},1),"mmm yyyy"),"—")'

        items = [
            ("Peak cash need before external funding (max cumulative deficit incl. opening cash)", f"=MAX(0,-MIN({rng(CF,'cum_pre')}))", GBP),
            ("Month of peak cash need", f"=MATCH(MIN({rng(CF,'cum_pre')}),{rng(CF,'cum_pre')},0)", '0'),
            ("Date of peak cash need", month_date("B5"), None),
            ("First month with positive EBITDA (monthly operating break-even)", f'=IFERROR(MATCH(1,{rng(PL,"ebitda_flag")},0),"Not reached in 36 months")', '0'),
            ("Date of monthly break-even", month_date("B7"), None),
            ("First month with positive cumulative net result", f'=IFERROR(MATCH(1,{rng(PL,"cum_flag")},0),"Not reached in 36 months")', '0'),
            ("Minimum closing cash AFTER funding", f"=MIN({rng(CF,'closing')})", GBP),
            ("Month of minimum closing cash", f"=MATCH(MIN({rng(CF,'closing')}),{rng(CF,'closing')},0)", '0'),
            ("Funded-through check", '=IF(B10>=0,"Funding covers all 36 months","SHORTFALL — cash goes negative; raise earlier/more or cut cost")', None),
            ("Closing cash at month 36 (Dec 2029)", f"=INDEX({rng(CF,'closing')},1,{MONTHS})", GBP),
            ("Runway at month 36 (months)", f"=INDEX({rng(CF,'runway')},1,{MONTHS})", NUM1),
            ("Total equity raised in model (36 months)", f"=SUM({rng(CF,'preseed')})+SUM({rng(CF,'seed')})+SUM({rng(CF,'seriesa')})", GBP),
            ("Total grant income in model (36 months)", f"=SUM({rng(CF,'grants')})", GBP),
            ("3-year revenue", f"=SUM({rng(PL,'revenue')})", GBP),
            ("3-year EBITDA", f"=SUM({rng(PL,'ebitda')})", GBP),
            ("Headcount at month 36", f"=INDEX({rng(HC,'headcount')},1,{MONTHS})", '0'),
        ]
        r = 4
        for label, f, fmt in items:
            ws.cell(row=r, column=1, value=label)
            c = ws.cell(row=r, column=2, value=f)
            if fmt:
                c.number_format = fmt
            c.font = F_B
            r += 1
        r += 1
        ws.cell(row=r, column=1, value="Funding rounds in the active scenario (PROPOSED; every round is conditional on the milestones in 09_FUNDING_STRATEGY.md)").font = F_H
        r += 1
        for c, h in enumerate(["Round", "Month", "Date", "Amount (GBP)", "Cumulative cash before this round (model)"], 1):
            ws.cell(row=r, column=c, value=h).font = F_B
        r += 1
        for lab, k in [("Pre-seed (SEIS/EIS)", "preseed"), ("Seed", "seed"), ("Series A", "seriesa"), ("Grant 1", "grant1"), ("Grant 2", "grant2")]:
            ws.cell(row=r, column=1, value=lab)
            ws.cell(row=r, column=2, value=f"={A(k+'_m')}")
            ws.cell(row=r, column=3, value=f'=IF({A(k+"_m")}<=36,TEXT(DATE(2027,{A(k+"_m")},1),"mmm yyyy"),"not in model")')
            ws.cell(row=r, column=4, value=f"={A(k+'_amt')}").number_format = GBP
            ws.cell(row=r, column=5, value=f'=IF({A(k+"_m")}<=36,INDEX({rng(CF,"cum_pre")},1,{A(k+"_m")}),"—")').number_format = GBP
            r += 1
        r += 1
        ws.cell(row=r, column=1, value="Reading this sheet").font = F_H
        notes = [
            "Peak cash need is the external money required to keep cash ≥ 0 with no equity or grants — the number to raise (plus a buffer of 20–30%).",
            "Break-even = first month EBITDA > 0 (before grant income). Cumulative break-even is when losses to date are recovered.",
            "If the funded-through check shows SHORTFALL, the scenario's rounds are too small or too late for its cost base.",
            "Grants are recognised when received; they are competitive and none is secured (TO VALIDATE).",
        ]
        for n in notes:
            r += 1
            ws.cell(row=r, column=1, value="• " + n).font = F_NOTE
        ws.column_dimensions["A"].width = 78
        for col in "BCDE":
            ws.column_dimensions[col].width = 20

    # --- Dashboard ---------------------------------------------------------------------------------------------
    def build_dashboard(self):
        ws = self.wb.create_sheet("Dashboard")
        ws["A1"] = "Dashboard — active scenario"
        ws["A1"].font = F_TITLE
        ws["A2"] = '="Scenario: "&Assumptions!$D$4&"   (change Assumptions!C4). Scenario values, not actuals."'
        ws["A2"].font = F_NOTE
        PL, CF, HC, CS = "P&L", "Cash flow", "Headcount", "Cost of sales"
        ws.append([])
        hdr = ["Metric", "FY2027", "FY2028", "FY2029", "3-year"]
        for c, h in enumerate(hdr, 1):
            cell = ws.cell(row=4, column=c, value=h)
            cell.font = F_B
            cell.fill = FILL_H
        lines = [
            ("Advisory revenue", PL, "advisory", GBP),
            ("Consulting revenue", PL, "consulting", GBP),
            ("E-learning revenue", PL, "elearning", GBP),
            ("MaternaLink revenue (in development)", PL, "maternalink", GBP),
            ("TOTAL REVENUE", PL, "revenue", GBP),
            ("Gross profit", PL, "gp", GBP),
            ("Gross margin %", PL, "gm", PCT),
            ("Total operating expenses", PL, "opex", GBP),
            ("EBITDA (before grants)", PL, "ebitda", GBP),
            ("Grant income", PL, "grants", GBP),
            ("Net result", PL, "net", GBP),
            ("Net operating cash flow", CF, "netop", GBP),
            ("Funding received (equity + grants)", CF, "funding", GBP),
            ("Closing cash (year end)", CF, "closing", GBP),
            ("Headcount (year end)", HC, "headcount", '0'),
        ]
        r = 5
        for label, sheet, key, fmt in lines:
            ws.cell(row=r, column=1, value=label).font = F_B if label.isupper() else Font()
            row = self.rows[(sheet, key)]
            for i, col in enumerate(list(YCOL.values()) + [TCOL]):
                c = ws.cell(row=r, column=2 + i, value=f"={q(sheet, col + str(row))}")
                c.number_format = fmt
            r += 1
        r += 1
        ws.cell(row=r, column=1, value="Funding metrics").font = F_H
        r += 1
        for label, cell, fmt in [("Peak cash need before external funding", "B4", GBP), ("Month of peak cash need", "B5", '0'),
                                 ("First month with positive EBITDA", "B7", '0'), ("Minimum closing cash after funding", "B10", GBP),
                                 ("Funded-through check", "B12", None), ("Runway at month 36 (months)", "B14", NUM1)]:
            ws.cell(row=r, column=1, value=label)
            c = ws.cell(row=r, column=2, value=f"={q('Funding requirement', cell)}")
            if fmt:
                c.number_format = fmt
            c.font = F_B
            r += 1
        # charts
        rev_row = self.rows[(PL, "revenue")]
        ebitda_row = self.rows[(PL, "ebitda")]
        closing_row = self.rows[(CF, "closing")]
        plws, cfws = self.wb[PL], self.wb[CF]
        ch = LineChart()
        ch.title = "Monthly revenue and EBITDA (active scenario)"
        ch.y_axis.title = "GBP"
        ch.height, ch.width = 8, 24
        for row in (rev_row, ebitda_row):
            ch.add_data(Reference(plws, min_col=1, max_col=COL0 + MONTHS - 1, min_row=row), titles_from_data=True, from_rows=True)
        ch.set_categories(Reference(plws, min_col=COL0, max_col=COL0 + MONTHS - 1, min_row=4))
        ws.add_chart(ch, "G4")
        ch2 = LineChart()
        ch2.title = "Closing cash (active scenario)"
        ch2.y_axis.title = "GBP"
        ch2.height, ch2.width = 8, 24
        ch2.add_data(Reference(cfws, min_col=1, max_col=COL0 + MONTHS - 1, min_row=closing_row), titles_from_data=True, from_rows=True)
        ch2.set_categories(Reference(cfws, min_col=COL0, max_col=COL0 + MONTHS - 1, min_row=4))
        ws.add_chart(ch2, "G22")
        ch3 = BarChart()
        ch3.type = "col"
        ch3.grouping = "stacked"
        ch3.overlap = 100
        ch3.title = "Annual revenue by pillar (active scenario)"
        ch3.height, ch3.width = 8, 14
        data = Reference(ws, min_col=1, max_col=4, min_row=5, max_row=8)
        ch3.add_data(data, titles_from_data=True, from_rows=True)
        ch3.set_categories(Reference(ws, min_col=2, max_col=4, min_row=4))
        ws.add_chart(ch3, "A30")
        ws.column_dimensions["A"].width = 44
        for col in "BCDE":
            ws.column_dimensions[col].width = 15

    # --- Static summary & sensitivity (Python values) --------------------------------------------------------------
    def build_static(self, results):
        ws = self.wb.create_sheet("Static summary")
        ws["A1"] = "Static summary — Python-computed values for all three scenarios (visible without recalculation)"
        ws["A1"].font = F_TITLE
        ws["A2"] = "Same logic as the formula sheets (build_model.py, function compute). If a recalculated workbook differs from this sheet, the formulas have been edited."
        ws["A2"].font = F_NOTE
        r = 4
        for si, name in enumerate(SCEN_NAMES):
            R = results[si]
            ws.cell(row=r, column=1, value=f"{name} scenario — annual P&L and cash").font = F_H
            for c in range(1, 7):
                ws.cell(row=r, column=c).fill = FILL_H
            r += 1
            for c, h in enumerate(["Line", "FY2027", "FY2028", "FY2029", "3-year"], 1):
                ws.cell(row=r, column=c, value=h).font = F_B
            r += 1
            for label, key, fmt in [("Advisory", "advisory", GBP), ("Consulting", "consulting", GBP), ("E-learning", "elearning", GBP),
                                    ("MaternaLink (in development)", "maternalink", GBP), ("TOTAL REVENUE", "revenue", GBP),
                                    ("Cost of sales", "cos", GBP), ("Gross profit", "gp", GBP), ("Employment cost", "employment", GBP),
                                    ("Total operating expenses", "opex", GBP), ("EBITDA (before grants)", "ebitda", GBP),
                                    ("Grant income", "grants", GBP), ("Net result", "net", GBP), ("Net operating cash flow", "netop", GBP),
                                    ("Closing cash (year end)", "closing", GBP), ("Headcount (year end)", "headcount", '0')]:
                ws.cell(row=r, column=1, value=label).font = F_B if label.isupper() else Font()
                vals = [R["annual"][key][y] for y in YEARS]
                if key in ("closing", "headcount"):
                    tot = vals[-1]
                else:
                    tot = sum(vals)
                for i, val in enumerate(vals + [tot]):
                    ws.cell(row=r, column=2 + i, value=round(val, 2)).number_format = fmt
                r += 1
            ws.cell(row=r, column=1, value="Gross margin %")
            for i, y in enumerate(YEARS):
                rev = R["annual"]["revenue"][y]
                ws.cell(row=r, column=2 + i, value=(R["annual"]["gp"][y] / rev if rev else 0)).number_format = PCT
            ws.cell(row=r, column=5, value=(sum(R["gp"]) / sum(R["revenue"]) if sum(R["revenue"]) else 0)).number_format = PCT
            r += 1
            M = R["metrics"]
            for label, val, fmt in [("Peak cash need before external funding", M["peak_need"], GBP),
                                    ("Month of peak cash need", M["peak_need_month"], '0'),
                                    ("First month with positive EBITDA", M["be_month"] or "Not reached in 36 months", '0'),
                                    ("First month cumulative result positive", M["be_cum_month"] or "Not reached in 36 months", '0'),
                                    ("Minimum closing cash after funding", M["min_cash"], GBP),
                                    ("Month of minimum closing cash", M["min_cash_month"], '0'),
                                    ("Closing cash month 36", M["closing_36"], GBP),
                                    ("Equity raised in model", M["equity_total"], GBP),
                                    ("Grants in model", M["grants_total"], GBP),
                                    ("Runway at month 36 (months)", M["runway"] if M["runway"] is not None else "cash-generative", NUM1)]:
                ws.cell(row=r, column=1, value=label)
                c = ws.cell(row=r, column=2, value=round(val, 2) if isinstance(val, float) else val)
                c.number_format = fmt
                c.font = F_B
                r += 1
            r += 1
        ws.column_dimensions["A"].width = 48
        for col in "BCDE":
            ws.column_dimensions[col].width = 15

    def build_sensitivity(self, sens):
        ws = self.wb.create_sheet("Sensitivity")
        ws["A1"] = "Sensitivity — Python-computed (static). Re-run build_model.py after changing assumptions."
        ws["A1"].font = F_TITLE
        ws["A2"] = "Each table flexes one or two inputs around the named scenario with everything else unchanged."
        ws["A2"].font = F_NOTE
        r = 4
        for title, header, rows in sens:
            ws.cell(row=r, column=1, value=title).font = F_H
            for c in range(1, len(header) + 1):
                ws.cell(row=r, column=c).fill = FILL_H
            r += 1
            for c, h in enumerate(header, 1):
                ws.cell(row=r, column=c, value=h).font = F_B
            r += 1
            for row in rows:
                for c, val in enumerate(row, 1):
                    cell = ws.cell(row=r, column=c, value=val)
                    if isinstance(val, float):
                        cell.number_format = GBP if abs(val) >= 100 else '0.00'
                r += 1
            r += 1
        ws.column_dimensions["A"].width = 46
        for col in "BCDEFGH":
            ws.column_dimensions[col].width = 18

    def build_readme(self):
        ws = self.wb.create_sheet("README", 0)
        ws["A1"] = "VYTALIX — 36-month financial model (Jan 2027 – Dec 2029)"
        ws["A1"].font = F_TITLE
        lines = [
            "Status: SCENARIO MODEL v1, built 7 September 2026 by finance/build_model.py. GBP. UK-domiciled entity (to be incorporated — TO VALIDATE).",
            "No figure in this workbook is an actual. Vytalix has no revenue, customers, contracts, grants or product in production (FACTS_BASE.md). Every number is a scenario built from the stated assumptions.",
            "",
            "HOW TO USE",
            "1. Assumptions!C4 selects the scenario (1 Conservative, 2 Base, 3 High-growth). Column F ('ACTIVE') = INDEX(C:E, selector) and every formula sheet reads column F.",
            "2. Blue/yellow cells in Assumptions are inputs. Year-dependent inputs (Y1/Y2/Y3) are read with CHOOSE(year index, Y1, Y2, Y3).",
            "3. Timeline sheets run left to right: Revenue build → Cost of sales → Headcount → Opex → P&L → Cash flow → Funding requirement → Dashboard. Months are in columns C:AL; annual totals in AN:AQ.",
            "4. Sensitivity and Static summary are values computed in Python with identical logic; they do not react to C4. Re-run the script after editing assumptions.",
            "5. Assumptions!ml_delay adds months to the MaternaLink licence go-live for slippage tests.",
            "",
            "SHEETS",
            "Assumptions — three scenario columns, selector, derived payroll on-costs. | Revenue build — advisory days × rate × utilisation, retainers, consulting projects × value, e-learning learners × ARPU + corporate licences, MaternaLink pilots × value then per-woman licences from go-live.",
            "Cost of sales — direct costs and gross margin. | Opex — founder salary, hires by start month, contractors, technology, marketing, legal, compliance, insurance, software, travel, operations, accountancy; employer NI 15% above £5,000 and pension 3% of qualifying earnings (2026/27 — see notes in Assumptions).",
            "Headcount — flags, salaries, NI, pension, Employment Allowance. | P&L — monthly and annual. | Cash flow — collection lag, funding by round/month, closing cash, minimum cash, runway.",
            "Funding requirement — peak cash need, break-even month, funded-through check, rounds table. | Dashboard — KPIs and charts. | Sensitivity — day rate, utilisation, MaternaLink go-live delay. | Static summary — all three scenarios.",
            "",
            "CONVENTIONS AND LIMITS",
            "Hire start month 99 = not hired within the model. Costs are paid in the month incurred; services and MaternaLink invoices are collected with a one-month lag; e-learning is prepaid.",
            "No VAT, corporation tax, depreciation, interest or R&D tax relief. Grants are recognised as other income when received and are entirely TO VALIDATE (competitive, none applied for).",
            "The Ekiti proposal's £300 per woman per year is UNVALIDATED (FACTS_BASE A5) and is not used; Africa licences are modelled at £3–£12 per woman per year and UK at £8–£40.",
            "Labels: KNOWN (rate cited to a public source, still TO VALIDATE against gov.uk before use) · ESTIMATE · ASSUMPTION · PROPOSED · TO VALIDATE.",
            "",
            "SOURCES CITED (retrieved 7 Sept 2026 via web search; verify on gov.uk before external use)",
            "Employer NI 15%, secondary threshold £5,000, Employment Allowance £10,500 (2026/27): https://www.moorepay.co.uk/payroll-hr-rates/tax-and-national-insurance-changes/ ; https://employerscalculator.co.uk/guides/employer-ni-rates-2026-27",
            "Auto-enrolment 3% employer minimum on qualifying earnings £6,240–£50,270 (2026/27): https://www.moorepay.co.uk/payroll-hr-rates/automatic-enrolment/",
            "SEIS: £250k company lifetime cap, £200k investor cap, gross assets < £350k, < 3 years trading, < 25 employees: https://thecarry.co.uk/essentials/seis-and-eis-limits-and-thresholds-for-2026 ; https://www.gov.uk/government/statistics/enterprise-investment-scheme-and-seed-enterprise-investment-scheme-may-2026/enterprise-investment-scheme-and-seed-enterprise-investment-scheme-2026",
            "EIS from 6 April 2026: £10m per 12 months (£20m knowledge-intensive), £24m lifetime (£40m KIC), gross assets £30m/£35m, investor £1m (£2m KIC): https://www.farrer.co.uk/news-and-insights/using-eis-and-seis-to-attract-investment-the-benefits-and-some-traps-to-avoid/ ; https://ct.me/content-hub/articles/eis-changes-from-april-2026-higher-investment-limits-for-innovative-companies/",
        ]
        for i, t in enumerate(lines, 3):
            c = ws.cell(row=i, column=1, value=t)
            if t.isupper() and t:
                c.font = F_H
        ws.column_dimensions["A"].width = 160
        for i in range(3, 3 + len(lines)):
            ws.cell(row=i, column=1).alignment = Alignment(wrap_text=True, vertical="top")

    def build(self, results, sens):
        self.build_assumptions()
        # Headcount must exist before Revenue (consultant flag reference) — create sheets in display order but fill rows first.
        self.build_headcount()
        self.build_revenue()
        self.build_cos()
        self.build_opex()
        self.build_pl()
        self.build_cashflow()
        self.build_funding()
        self.build_dashboard()
        self.build_sensitivity(sens)
        self.build_static(results)
        self.build_readme()
        # display order
        order = ["README", "Assumptions", "Revenue build", "Cost of sales", "Opex", "Headcount", "P&L", "Cash flow",
                 "Funding requirement", "Dashboard", "Sensitivity", "Static summary"]
        self.wb._sheets = [self.wb[n] for n in order]
        self.wb.active = 0
        return self.wb


# ----------------------------------------------------------------------------------------------------------------
# 4. SENSITIVITY (Python)
# ----------------------------------------------------------------------------------------------------------------
def sensitivities():
    base = scenario_values(1)
    high = scenario_values(2)
    cons = scenario_values(0)
    out = []

    def metrics(v):
        R = compute(v)
        M = R["metrics"]
        return R, M

    # 1. day rate × utilisation (Base): 3-year revenue
    rates, utils = [1200, 1500, 1800], [0.30, 0.42, 0.55]
    rows = []
    for rt in rates:
        row = [f"Day rate £{rt:,}"]
        for u in utils:
            v = dict(base, day_rate=rt, utilisation=u)
            R, M = metrics(v)
            row.append(round(M["rev_3yr"], 0))
        rows.append(row)
    out.append(("Table 1 — Base scenario: 3-year TOTAL REVENUE (GBP) by founder day rate × utilisation",
                ["", "Utilisation 30%", "Utilisation 42%", "Utilisation 55%"], rows))
    rows = []
    for rt in rates:
        row = [f"Day rate £{rt:,}"]
        for u in utils:
            v = dict(base, day_rate=rt, utilisation=u)
            R, M = metrics(v)
            row.append(round(M["peak_need"], 0))
        rows.append(row)
    out.append(("Table 2 — Base scenario: PEAK CASH NEED before external funding (GBP) by day rate × utilisation",
                ["", "Utilisation 30%", "Utilisation 42%", "Utilisation 55%"], rows))
    rows = []
    for rt in rates:
        row = [f"Day rate £{rt:,}"]
        for u in utils:
            v = dict(base, day_rate=rt, utilisation=u)
            R, M = metrics(v)
            row.append(round(M["ebitda_3yr"], 0))
        rows.append(row)
    out.append(("Table 3 — Base scenario: 3-year EBITDA (GBP) by day rate × utilisation",
                ["", "Utilisation 30%", "Utilisation 42%", "Utilisation 55%"], rows))
    # 2. MaternaLink go-live delay
    for name, v0 in [("Base", base), ("High-growth", high), ("Conservative", cons)]:
        rows = []
        for d in [0, 3, 6, 12]:
            v = dict(v0, ml_delay=d)
            R, M = metrics(v)
            rows.append([f"Go-live delay {d} months (go-live month {v0['ml_golive'] + d})", round(M["ml_3yr"], 0), round(M["rev_3yr"], 0),
                         round(M["ebitda_3yr"], 0), round(M["peak_need"], 0), M["be_month"] or "Not reached", round(M["closing_36"], 0)])
        out.append((f"Table — {name} scenario: MaternaLink licence go-live delay",
                    ["Delay", "MaternaLink 3-yr revenue", "Total 3-yr revenue", "3-yr EBITDA", "Peak cash need", "First EBITDA-positive month", "Closing cash M36"], rows))
    # 3. single-input tornado (Base)
    R0, M0 = metrics(base)
    rows = []
    flex = [("Founder day rate", "day_rate", 1200, 1800), ("Founder utilisation", "utilisation", 0.30, 0.55),
            ("Average consulting project value", "proj_value", 15000, 30000), ("E-learning ARPU", "el_arpu", 150, 300),
            ("MaternaLink pilot value per year", "ml_pilot_value", 40000, 150000), ("Africa licence £/woman/yr", "af_price", 3, 12),
            ("UK licence £/woman/yr", "uk_price", 8, 40), ("Africa women added per month", "af_add", 250, 3000),
            ("Retainers Y2/Y3", ("ret_y2", "ret_y3"), 1, 3)]
    for lab, key, lo, hi in flex:
        res = []
        for val in (lo, hi):
            v = dict(base)
            if isinstance(key, tuple):
                for kk in key:
                    v[kk] = val
            else:
                v[key] = val
            R, M = metrics(v)
            res.append((M["rev_3yr"], M["ebitda_3yr"], M["peak_need"]))
        rows.append([lab, lo, hi, round(res[0][0] - M0["rev_3yr"], 0), round(res[1][0] - M0["rev_3yr"], 0),
                     round(res[0][1] - M0["ebitda_3yr"], 0), round(res[1][1] - M0["ebitda_3yr"], 0),
                     round(res[0][2] - M0["peak_need"], 0), round(res[1][2] - M0["peak_need"], 0)])
    out.append((f"Table — Base scenario one-at-a-time flex (Base 3-yr revenue £{M0['rev_3yr']:,.0f}; 3-yr EBITDA £{M0['ebitda_3yr']:,.0f}; peak need £{M0['peak_need']:,.0f})",
                ["Input", "Low", "High", "Δ Revenue (low)", "Δ Revenue (high)", "Δ EBITDA (low)", "Δ EBITDA (high)", "Δ Peak need (low)", "Δ Peak need (high)"], rows))
    return out


# ----------------------------------------------------------------------------------------------------------------
# 5. CHECKS
# ----------------------------------------------------------------------------------------------------------------
def check_workbook(path):
    """Re-open with openpyxl and scan every formula for references to sheets/cells that exist."""
    import re
    wb = load_workbook(path)
    names = set(wb.sheetnames)
    n_formulas, problems = 0, []
    ref_re = re.compile(r"(?:'([^']+)'|([A-Za-z0-9_&]+))!\$?([A-Z]{1,3})\$?(\d+)")
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith("="):
                    n_formulas += 1
                    f = c.value
                    if "#REF!" in f:
                        problems.append(f"{ws.title}!{c.coordinate}: #REF! in formula")
                    for m in ref_re.finditer(f):
                        sh = m.group(1) or m.group(2)
                        if sh not in names:
                            problems.append(f"{ws.title}!{c.coordinate}: unknown sheet {sh}")
                            continue
                        tgt = wb[sh][f"{m.group(3)}{m.group(4)}"]
                        if tgt.value is None and sh != ws.title:
                            problems.append(f"{ws.title}!{c.coordinate}: points at empty cell {sh}!{m.group(3)}{m.group(4)}")
    return n_formulas, problems


def verify_with_libreoffice(path, results):
    """Set the selector to each scenario, recalc with LibreOffice, compare key rows to Python."""
    tmp = tempfile.mkdtemp()
    report = []
    keyrows = [("Revenue build", "revenue", "revenue"), ("Cost of sales", "cos", "cos"), ("Opex", "opex", "opex"),
               ("P&L", "ebitda", "ebitda"), ("Cash flow", "closing", "closing"), ("Headcount", "headcount", "headcount"),
               ("Cash flow", "cum_pre", "cum_pre")]
    model = Model()  # rebuild to know row numbers
    model.build(results, [])
    for si in range(3):
        wb = load_workbook(path)
        wb["Assumptions"]["C4"] = si + 1
        p = os.path.join(tmp, f"s{si}.xlsx")
        wb.save(p)
        outdir = os.path.join(tmp, f"out{si}")
        os.makedirs(outdir, exist_ok=True)
        subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", outdir, p],
                       check=True, capture_output=True, timeout=180)
        wbv = load_workbook(os.path.join(outdir, f"s{si}.xlsx"), data_only=True)
        maxdiff = 0.0
        for sheet, key, pk in keyrows:
            r = model.rows[(sheet, key)]
            for m in range(1, MONTHS + 1):
                xv = wbv[sheet][f"{mcol(m)}{r}"].value
                pv = results[si][pk][m - 1]
                if xv is None:
                    xv = 0
                d = abs(float(xv) - float(pv))
                if d > maxdiff:
                    maxdiff = d
                if d > 0.5:
                    report.append(f"  MISMATCH {SCEN_NAMES[si]} {sheet}!{mcol(m)}{r} ({key}): excel={xv} python={pv}")
        fr = wbv["Funding requirement"]
        report.append(f"  {SCEN_NAMES[si]}: max |excel-python| on key rows = {maxdiff:.4f}; "
                      f"Funding sheet: peak need={fr['B4'].value:,.0f} (py {results[si]['metrics']['peak_need']:,.0f}), "
                      f"break-even={fr['B7'].value} (py {results[si]['metrics']['be_month']}), "
                      f"min cash={fr['B10'].value:,.0f} (py {results[si]['metrics']['min_cash']:,.0f}), "
                      f"check='{fr['B12'].value}'")
        errs = 0
        for ws in wbv.worksheets:
            for row in ws.iter_rows():
                for c in row:
                    if isinstance(c.value, str) and c.value.startswith("#"):
                        errs += 1
        report.append(f"  {SCEN_NAMES[si]}: cells evaluating to an Excel error after recalc = {errs}")
    shutil.rmtree(tmp, ignore_errors=True)
    return report


def main():
    results = [compute(scenario_values(i)) for i in range(3)]
    sens = sensitivities()
    model = Model()
    wb = model.build(results, sens)
    wb.save(OUT)
    print(f"Wrote {OUT}")
    for si, name in enumerate(SCEN_NAMES):
        R, M = results[si], results[si]["metrics"]
        print(f"\n{name}: revenue by year " + ", ".join(f"{y}: £{R['annual']['revenue'][y]:,.0f}" for y in YEARS)
              + f" | EBITDA " + ", ".join(f"{y}: £{R['annual']['ebitda'][y]:,.0f}" for y in YEARS))
        print(f"  peak need £{M['peak_need']:,.0f} (m{M['peak_need_month']}), break-even m{M['be_month']}, "
              f"min cash £{M['min_cash']:,.0f} (m{M['min_cash_month']}), closing m36 £{M['closing_36']:,.0f}, "
              f"equity £{M['equity_total']:,.0f}, grants £{M['grants_total']:,.0f}, headcount " +
              ", ".join(str(R['annual']['headcount'][y]) for y in YEARS))
    n, problems = check_workbook(OUT)
    print(f"\nopenpyxl re-open check: {len(wb.sheetnames)} sheets, {n} formulas scanned, {len(problems)} reference problems")
    for p in problems[:20]:
        print("  ", p)
    if "--verify" in sys.argv:
        print("\nLibreOffice recalculation check:")
        for line in verify_with_libreoffice(OUT, results):
            print(line)


if __name__ == "__main__":
    main()
