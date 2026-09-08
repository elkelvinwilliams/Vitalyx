# 16 — VYTALIX ORGANISATION AND STANDARD OPERATING PROCEDURES

**Owner:** Founder (acting COO) · **Status:** PROPOSED · **Version:** 1.1 (8 September 2026; supersedes 1.0 — adds the four-way status columns, the David Agunede role matrix, per-SOP RACI, the 24-month cost roll-up, and aligns pricing floors and investor-CRM counts with `/assets/PRICING_STRUCTURE.md` and `/investors/INVESTOR_DASHBOARD.md`) · **Governed by:** `/FACTS_BASE.md` (language rules apply to every SOP output) · **Related:** `/docs/02_GROUP_STRUCTURE.md` (governance, advisory board, RACI), `/docs/13_SALES_ENGINE.md`, `/docs/14_MARKETING_AND_CONTENT_ENGINE.md`, `/docs/15_LEGAL_AND_REGULATORY.md`, `/docs/17_FOUNDER_OPERATING_SYSTEM.md`, `/docs/18_90_DAY_EXECUTION_PLAN.md`, `/operations/KPI_DASHBOARD.csv`, `/operations/PIPELINE_TRACKERS.csv`

## Executive view
1. Vytalix today is one person, no legal entity, no staff and one informal collaborator whose role is undefined (VERIFIED, FACTS_BASE §1). The organisation is therefore designed as a **founder-led company with a bought-in bench**: twelve functions, nine founder-led for at least the first six months, three outsourced from Day 1 (legal/compliance, finance, clinical governance), and **no salaried hire before a signed engagement, a grant award or a closed round pays for it**.
2. Every role in the 24-month plan is tied to a **trigger** (revenue threshold, funded milestone or decision gate), never to a calendar date. Year-1 bench cost is £28k–£64k (ESTIMATE); year-2 cost rises to £310k–£530k (ESTIMATE) only if the MaternaLink (in development) MVP is funded — otherwise Vytalix stays a two-person services firm (§3.2).
3. Eleven SOPs cover the loop that turns founder time into cash, capital and product — business development, investor acquisition, fundraising, product development, customer acquisition, customer onboarding, healthcare partnerships, due diligence, compliance, finance, reporting — each in one fixed format: **Trigger → Owner → Process (numbered) → Documents → Approval → KPI → Output**, so a virtual assistant, contractor or first hire can run it without the founder in the room.
4. The SOPs hard-wire the three non-negotiables from the master audit: no MaternaLink claim beyond "in development" (a FACTS_BASE claims check is a numbered step in every external-facing SOP); no investor outreach before the five pre-conditions in `/investors/OUTREACH_ENGINE.md` are logged as met (earliest Wed 14 Oct 2026, Day 31); no processing of patient data without a DPIA and Clinical Safety Officer sign-off.
5. Until incorporation, "Approval" in every SOP resolves to the founder alone, minuted in `/operations/DECISION_LOG.md` (TO CREATE Day 1). From the first board meeting (target Tue 13 Oct 2026, Day 30) the reserved matters in `/docs/02_GROUP_STRUCTURE.md` §4.1 pass to the board. KPIs named in the SOPs are the same definitions as `/operations/KPI_DASHBOARD.csv` and `/docs/17_FOUNDER_OPERATING_SYSTEM.md` §4.

---

## 1. Design principles

| # | Principle | What it means in practice | Enforced by |
|---|---|---|---|
| 1 | Revenue funds people | No salaried hire until (a) trailing 3-month services revenue ≥ £10k/month, or (b) a round or grant that names the role has closed. | Hiring-trigger check in the monthly ritual (founder OS §2.3) |
| 2 | Buy expertise, hire execution | Clinical safety, legal, accounting, regulatory, design and fractional CTO are bought by the day; the first hires are people who ship (engineer, delivery associate, VA). | §2 status columns; §3 plan |
| 3 | One accountable owner per function | Every function has exactly one accountable person at all times — even when that is the founder for nine functions at once. | §2.1 single-owner map |
| 4 | Contractor IP always assigned | Every contractor, associate, adviser and developer signs the IP clause (`/docs/15_LEGAL_AND_REGULATORY.md` §9.1) before work starts. No exceptions, including David Agunede. | SOP 08 step 8; SOP 04 step 1 |
| 5 | Nigeria delivered locally | In-country roles (country lead, CHEW trainers, engineers) are contracted in Nigeria through a local partner or employer-of-record, not relocated from the UK (employment route TO VALIDATE). | §3 triggers; SOP 07 |
| 6 | Founder time is the scarcest asset | ≥ 70% of working time on Vytalix; within that, revenue 40% / investors 20% / product 20% / partnerships-credibility 20% for the first 90 days. Kemek Enterprise Ltd is a declared conflict capped at ≤ 30%. | Founder OS §1 and weekly time audit |
| 7 | Every process ends in a number | Each SOP has a KPI that appears in the Friday review; an SOP with no reported KPI for two consecutive weeks is treated as not running. | SOP 11 |

---

## 2. Organisation structure — twelve functions

Status columns: **Required now** = must exist before revenue or a decision gate · **Outsource** = bought fractional/contract · **Hire later** = salaried, trigger-gated · **Founder-led** = founder is the accountable owner and the doer today. Costs are ESTIMATE, GBP, exclusive of VAT, September 2026 rates.

| # | Function | Target roles (24-month state) | Required now | Outsource | Hire later | Founder-led | Indicative cost (ESTIMATE) | Hiring / engagement trigger |
|---|---|---|---|---|---|---|---|---|
| 1 | **Board** | Founder (sole director); one independent NED; investor director/observer at pre-seed | Yes — sole director from incorporation; NED by Month 3 | NED (fee or unpaid) | Investor director only if a round lead requires | Yes (chair until NED) | NED £0–£6k/yr; D&O insurance £400–£1,000/yr once investors join | NED search instructed at incorporation (Fri 25 Sept 2026); appointment or two final candidates by Fri 11 Dec 2026 (Day 89) |
| 2 | **Executive Leadership** | CEO (founder); fractional COO / Chief of Staff; CFO at Series A | Yes (CEO) | Fractional COO | CFO (Series A only) | Yes | Founder draw £0 until trailing-month revenue ≥ £7.5k, then £3k/month minimum (business model §3); fractional COO £700–£1,000/day, 2 days/month | Fractional COO when services revenue ≥ £10k/month for 3 months **or** seed closed |
| 3 | **Advisory Board** | Six profiles: obstetrics; senior/digital midwife; NHS digital/commissioning; Nigerian health-system leader; regulatory/CSO; health-tech operator; optional lived-experience adviser (`/docs/02_GROUP_STRUCTURE.md` §4.2) | Yes — none appointed (KNOWN); 2 signed by Day 60, 4 by Day 90 | Advisers (options or fee) | — | Yes (recruits and runs) | 0.25–0.5% options each vesting 24 months, or £500–£1,000/meeting; £4k–£8k/yr cash if fee-based | Approaches from Fri 9 Oct 2026; letters only after written consent to be named; never described as "partners" |
| 4 | **Technology** | Fractional CTO; engineering lead + 2 engineers (UK lead + Nigeria pair); managed DevOps | Fractional CTO for the prototype audit (Day 15–30) | Fractional CTO £600–£900/day, 2–4 days/month | Engineers on funded MVP | Founder owns; CTO executes | Pre-funding £1.2k–£3.6k/month; MVP team £140k–£320k over 16 weeks (`/product/MATERNALINK_MVP_SPEC.md`) | Engineers only when MVP funded (grant or round with ≥ £150k allocated), IP deed executed, CSO engaged |
| 5 | **Product** | Founder as acting CPO; fractional product lead; Head of Product at seed | No (gates before build) | Fractional product lead 1 day/week | Head of Product £75k–£95k | Yes | Fractional lead £2k–£3.5k/month from a design-partner LOI | Fractional lead on the first UK design-partner or Nigeria NGO-cohort LOI; Head of Product on seed close and v1.x live at ≥ 1 site |
| 6 | **Healthcare / Clinical Governance** | Clinical Safety Officer (DCB0129/0160); clinical adviser (advisory #1/#2); clinical lead at first evaluation site; Clinical Advisory Group | Yes — CSO identified by Wed 28 Oct (Day 45), engaged by Thu 12 Nov (Day 60) | CSO £500–£900/day, 1–2 days/month pre-build, 3–4 days/month in build | Clinical lead 0.2 FTE at evaluation site | Founder owns; CSO executes | £0.5k–£1.8k/month pre-build; clinical lead £15k–£25k/yr | CSO before any build work or hazard log; clinical lead when a UK service-evaluation site is agreed (Q2 2027 target, roadmap) |
| 7 | **Commercial** (Advisory, Consulting, E-Learning sales) | Founder as seller and lead deliverer; associate consultants per SOW; BD/delivery manager later | Yes — highest-priority founder function | Associates £700–£1,000/day list (contractor cost £450–£550) only against signed SOWs | BD/delivery manager £55k–£70k + commission | Yes | Associates funded from engagement margin | BD hire when services revenue ≥ £15k/month for 3 months **or** MaternaLink pilot pipeline ≥ 5 qualified organisations; E-Learning sales founder-led until 2 courses live |
| 8 | **Marketing** | Founder as author; freelance designer/editor; part-time marketing executive | No (founder content cadence is required) | Designer £1k–£2k per report; editor £300–£600/article | Part-time marketer 0.5 FTE £18k–£25k/yr | Yes | Tooling £0–£150/month | Part-time marketer when inbound conversations ≥ 15/month for 2 months **and** revenue ≥ £10k/month |
| 9 | **Operations** | Founder; virtual assistant; Operations / Chief-of-Staff hire | No | VA £15–£25/hr, 10 hrs/week (£650–£1,100/month) | Ops hire at Month 12+ if ≥ 6 people | Yes | VA from first services revenue | VA when founder admin (CRM logging, scheduling, invoicing, research) > 8 hrs/week for 2 consecutive weeks (decision Fri 16 Oct 2026) |
| 10 | **Finance** | Outsourced accountant; Xero; fractional FD; R&D tax adviser | Yes — accountant at incorporation | Accountant £80–£200/month; Xero £15–£30/month; fractional FD £800–£1,200/day | Finance manager only post-seed | Founder owns; accountant executes | Year 1 £1.2k–£2.8k | Accountant by Fri 25 Sept 2026; fractional FD on term sheet or cash > £250k; R&D adviser at first MVP spend |
| 11 | **Legal / Compliance** | Fixed-fee start-up solicitor; trademark attorney; fractional DPO; regulatory consultant; Compliance lead later | Yes — solicitor and attorney by Fri 18 Sept 2026 | Solicitor £4k–£9k (90 days); attorney £800–£2,000; DPO £0–£500/month Phase A; regulatory opinion £1.5k–£4k | Compliance/QA lead £60k–£80k or £900/day | Founder owns; professionals execute | Year-1 legal/compliance £9k–£18k (legal doc §Executive view) | DPO before MaternaLink processes any real data; Compliance lead only if G8 concludes "device" or ISO 27001/13485 begins |
| 12 | **Partnerships** | Founder; Nigeria country lead (contract); partnerships manager | No | Nigeria country lead £1.5k–£3k/month (local rates TO VALIDATE) | Partnerships manager £45k–£60k at Month 18+ | Yes | Country lead funded from pilot budget | Country lead when a Nigeria pilot is funded (NGO/donor cohort or state MoU with budget); manager when ≥ 3 live partnerships |

### 2.1 Single-owner map (Day 1, Mon 14 September 2026)

| Function | Accountable owner Day 1 | Executes today | First delegate (when triggered) | Adviser / backup |
|---|---|---|---|---|
| Board; Executive Leadership | Founder | Founder | Independent NED (challenge, not execution) | Solicitor |
| Advisory Board | Founder | Founder (recruits) | — | Advisory #6 (operator) for introductions |
| Technology | Founder | Fractional CTO (audit) | Engineering lead at MVP | Advisory #6 |
| Product | Founder | Founder | Fractional product lead | CSO; Advisory #1/#2 |
| Healthcare / Clinical Governance | Founder | CSO (from Day 60) | Clinical lead at evaluation site | Advisory #1, #2, #5 |
| Commercial | Founder | Founder | Associates (delivery); BD manager | Advisory #3 (NHS buying) |
| Marketing | Founder | Founder; freelance designer per asset | Part-time marketer | — |
| Operations | Founder | Founder | VA (from Month 2 if triggered) | — |
| Finance | Founder | Accountant | Fractional FD | — |
| Legal / Compliance | Founder | Solicitor; attorney; DPO (later) | Compliance lead | Advisory #5 |
| Partnerships | Founder | Founder | Nigeria country lead | Advisory #3, #4 |

### 2.2 David Agunede — role options (decision required by Sun 20 Sept 2026, Day 7; see `/docs/02_GROUP_STRUCTURE.md` §3 and `/docs/15_LEGAL_AND_REGULATORY.md` §8.3)

| If the IP outcome is… | Organisational role (PROPOSED) | Reports to | Compensation basis (PROPOSED) | Governance constraints |
|---|---|---|---|---|
| Option 1 — assignment for equity (default) | Head of Product Africa / Country Lead Nigeria (part-time); attends advisory board | Founder | Vested equity 5–12% (PROPOSED range) with good/bad-leaver; contract fee only when a Nigeria pilot is funded | Not a director until vesting cliff passed; signs IP deed, confidentiality and conflicts declaration |
| Option 2 — exclusive licence with option to acquire | External licensor and named Nigeria adviser | Founder (contractual) | Equity 2–5% and/or capped royalty; consultancy day rate for defined work | No authority to represent Vytalix; licence reviewed by solicitor |
| Option 3 — no agreement by Thu 12 Nov 2026 (Day 60) | No role; clean-room rebuild of v1; no use of his materials or the "Maternal Link" name | — | — | Standstill letter governs conduct until Day 60 |

Language rule: until an agreement is signed, David Agunede is described externally as "a collaborator on the MaternaLink concept", never as co-founder, CTO or Vytalix officer.

### 2.3 Decision rights by function (summary of `/docs/02_GROUP_STRUCTURE.md` §4.3)

| Decision | Founder | Board (from Day 30) | Advisory board | Professional adviser |
|---|---|---|---|---|
| Proposals ≤ £25k; contractor spend ≤ £10k; spend ≤ £2,500 per item | Decides | Informed | — | — |
| Contracts > £50k; borrowing > £25k; issue of shares; salaries > £60k; any government proposal | Recommends | Decides (reserved matter) | Consulted | Solicitor reviews |
| External clinical or regulatory claim | Recommends | Decides | Clinical adviser signs off | Solicitor on financial-promotion wording |
| Intended-use statement change; any line-crossing feature | Recommends | Decides | CSO advises in writing | Regulatory consultant |
| DPIA; safety case; hazard log | Owns | Informed | — | DPO signs DPIA; CSO signs safety case |
| Hires within budget and triggers | Decides | Informed | — | Accountant (payroll) |

---

## 3. Twenty-four-month hiring plan (Sept 2026 – Sept 2028; trigger-gated; all costs ESTIMATE)

### 3.1 Plan by quarter

| Quarter | Role | Type | Trigger (must be true before engagement) | Cost (ESTIMATE) | Funded by | Owner |
|---|---|---|---|---|---|---|
| Q4 2026 (Sep–Dec) | Solicitor; trademark attorney; accountant | Outsourced | Incorporation decision (Mon 14 Sept 2026) | £6k–£12k one-off; £80–£200/month | Founder capital (TO CONFIRM) | Founder |
| Q4 2026 | Fractional CTO (audit scope) | Outsourced | Standstill letter signed; prototype access granted | £1k–£2.5k for audit | Founder capital | Founder |
| Q4 2026 | Virtual assistant (10 hrs/week) | Contract | Admin > 8 hrs/week for 2 consecutive weeks | £650–£1,100/month | First services revenue | Founder |
| Q4 2026 | Clinical Safety Officer (fractional) | Outsourced | Intended-use statement adopted (Day 3); build planned | £0.5k–£1.8k/month | Founder capital / first revenue | Founder |
| Q4 2026 | 2–4 advisory-board members | Advisory | Entity exists (options need a company); written consent to be named | £0 cash (options) or £2k–£4k/yr | Option pool | Founder |
| Q4 2026 | Independent NED | Board | Incorporation; candidate via advisory network | £0–£6k/yr | Founder capital | Founder |
| Q1 2027 (Jan–Mar) | Associate consultant(s), 2–4 days/month | Contract per SOW | ≥ 2 signed engagements needing capacity beyond 10 founder days/month | £450–£550/day cost | Engagement margin | Founder |
| Q1 2027 | Fractional DPO | Outsourced | MaternaLink DPIA started; CRM/newsletter volumes growing | £0–£500/month | Revenue | Founder |
| Q1 2027 | Fractional product lead (1 day/week) | Contract | Design-partner LOI (UK) or NGO-cohort LOI (Nigeria) signed | £2k–£3.5k/month | Revenue / grant | Founder |
| Q1–Q2 2027 | Engineering lead + 2 engineers (UK lead + Nigeria pair) | Contract → employed | MVP funded (grant award or round with ≥ £150k allocated); IP deed executed; CSO engaged | £140k–£320k over 16 weeks | Grant / pre-seed | Founder + fractional CTO |
| Q2 2027 | Fractional FD (1–2 days/month) | Outsourced | Term sheet received or cash > £250k | £0.8k–£2.4k/month | Round | Founder |
| Q2 2027 | Freelance designer/editor (reports, site refresh) | Freelance | Report interviews complete | £1k–£2k per report | Revenue | Founder |
| Q2 2027 | Clinical lead (0.2 FTE) at first evaluation site | Contract / secondment | UK service-evaluation site agreed | £15k–£25k/yr | Grant / round | Founder + CSO |
| Q3 2027 | Nigeria country lead | Contract (local) | Nigeria pilot funded (NGO/donor cohort or state MoU with budget) | £1.5k–£3k/month | Pilot budget | Founder |
| Q3 2027 | Part-time marketing executive (0.5 FTE) | Employed | Inbound ≥ 15/month for 2 months and revenue ≥ £10k/month | £18k–£25k/yr | Revenue | Founder |
| Q3 2027 | BD / delivery manager | Employed | Services ≥ £15k/month for 3 months or pilot pipeline ≥ 5 qualified | £55k–£70k + commission | Revenue | Founder |
| Q4 2027 | Fractional COO / Chief of Staff | Contract | Services ≥ £10k/month for 3 months or seed closed | £1.4k–£2k/month | Revenue / seed | Founder |
| Q4 2027 | Head of Product | Employed | Seed closed; v1.x live at ≥ 1 site | £75k–£95k | Seed | Founder + board |
| Q1 2028 | Regulatory / QA lead | Employed or fractional | G8 device decision = "device", or ISO 13485 decision for v3 | £60k–£80k or £900/day | Seed | Founder + CSO |
| Q1–Q2 2028 | Second engineering pair; support/implementation associate | Employed | ≥ 2 paying sites or a scaled Nigeria pilot (≥ 5k women) | £110k–£160k/yr combined | Seed / pilot revenue | Head of Product |
| Q2–Q3 2028 | Partnerships manager; E-Learning content producer | Employed | ≥ 3 live partnerships; ≥ 2 courses live with ≥ 400 sales | £45k–£60k each | Revenue / seed | Founder |

### 3.2 Cost and headcount roll-up (ESTIMATE)

| Period | Employees | Contracted bench | Bench + people cost | Condition |
|---|---|---|---|---|
| Months 1–6 (Sep 2026 – Feb 2027) | 1 (founder, £0 draw until trailing revenue ≥ £7.5k/month) | 5–7 (solicitor, attorney, accountant, CTO, CSO, VA, advisers) | £14k–£32k | Founder capital + first engagements |
| Months 7–12 (Mar – Aug 2027) | 1–4 (founder; engineers only if MVP funded) | 6–8 | £14k–£32k without MVP; +£140k–£320k with MVP | Grant or pre-seed decides |
| **Year 1 total** | **1–4** | **6–8** | **£28k–£64k (services path); £170k–£380k (funded MVP path)** | |
| Months 13–24 (Sep 2027 – Aug 2028) | 2 (services path) or 8–12 (seed path) | 6–8 | £45k–£90k (services path); £310k–£530k (seed path) | Seed close and pilots landing |

Rule: if neither the seed nor a funded pilot lands, the company stays at ≤ 2 employees and remains a services firm (business model §Executive view, point 5). No role above is hired "in anticipation".

---

## 4. Standard operating procedures

Format for all eleven: **Trigger → Owner → Process (numbered) → Documents → Approval → KPI → Output.** Templates referenced live in `/operations/` (TO CREATE where marked) or in the named documents. Every SOP that produces external material includes a FACTS_BASE claims check as a numbered step. KPI names match `/operations/KPI_DASHBOARD.csv` (Section / KPI / Formula / Unit / Period / Target / Actual / Status_label / Source_system / Owner).

### SOP 01 — Business development (Advisory / Consulting)

**Trigger:** Monday 08:00 weekly plan (founder OS §2.2); any inbound enquiry (respond within 24 hours); from Mon 28 Sept 2026 (Week 3) the weekly quota applies without exception.
**Owner:** Founder (acting Head of Sales). VA (when engaged) does lead research and CRM logging; associates never sell.
**Process:**
1. Pull the ICP list (`/docs/13_SALES_ENGINE.md` §1, segments S1–S2 first; 150 contacts with source URLs by Fri 18 Sept) and confirm the weekly quota: **40 new contacts, 20 conversations, 5 discovery calls, 2 proposals**.
2. Research each contact: role, organisation, funding stage, stated problem; public business email/LinkedIn only; record the source URL in HubSpot Free CRM (stages per sales doc §3.1).
3. Score the lead (sales doc §4): A ≥ 70 = call within 48 h; B = weekly nurture; C = monthly content only.
4. Send the first touch (templates E1/L1, sales doc §12–13) with one personalised reason; log it the same day; daily minimum 8 new contacts and 5 follow-ups.
5. Follow up at +4, +10 and +21 days; three touches without reply = "Closed-lost: no decision" with a coded reason, never deleted; re-contact diarised at 90 days.
6. On a reply, offer three 30-minute slots within 5 working days; send the discovery agenda 24 h before.
7. Run the discovery call to the 30-minute script (sales doc §5); capture Problem / Budget / Authority / Timeline / Success criteria in the CRM within 30 minutes of the call.
8. Within 48 h decide: proposal, second call, refer out, or close-lost with reason code.
9. Draft the proposal from the package menu (`/docs/01_BUSINESS_MODEL.md` §4.1: A1, A2, C1–C8, T1; prices per `/assets/PRICING_STRUCTURE.md`; template `/assets/PROPOSAL_TEMPLATE.md`): fixed price, scope, start date, 14-day validity; packages gated "proof required to sell" (C3, C5, C8) are not quoted until the capability exists.
10. FACTS_BASE claims check: no client names without consent, no MaternaLink capability claims, "MaternaLink (in development)" only.
11. Send; move the deal to "Proposal sent" (50%); diarise +3 (call) and +7 (email) follow-ups — hand-off to SOP 05.
12. Friday 15:00 pipeline clean: every open deal has a next action dated within 7 days; weighted pipeline written to `/operations/PIPELINE_TRACKERS.csv` (Revenue tracker rows).
**Documents:** ICP list; HubSpot CRM; outreach templates E1–E3, L1–L2; discovery script and 20 questions (sales doc §5); proposal template; `/assets/SERVICE_CATALOGUE.md`; `/assets/PRICING_STRUCTURE.md`; loss-reason codes; `/operations/SOW_TEMPLATE.md` (TO CREATE; solicitor review before first use).
**Approval:** Founder for proposals ≤ £25k; board (once formed) for any contract > £50k or any proposal to a public body (reserved matter); solicitor for non-standard terms.
**KPI:** Leads 40/week; Conversations 20/week; Meetings (discovery calls held) 5/week (Month 1 target 10, Month 2 15, Month 3 15); Proposals sent 2/week (Month 1 3, Month 2 4, Month 3 5); reply rate ≥ 8% email, ≥ 15% LinkedIn; lead → conversation ≥ 50%; conversation → meeting ≥ 33%; meeting → proposal ≥ 30%; first signed engagement by Tue 13 Oct 2026 (Day 30), three by Sat 12 Dec (Day 90).
**Output:** Weekly pipeline snapshot (Revenue tracker); proposals sent; discovery notes in CRM; deals at "Proposal sent" handed to SOP 05.

### SOP 02 — Investor acquisition (identification to first meeting)

**Trigger:** All five pre-conditions in `/investors/OUTREACH_ENGINE.md` logged as met in the decision log: (1) incorporated; (2) MaternaLink IP heads of terms signed (deed executed or licence documented by Day 30); (3) 2025 clinical-AI claims retired from all materials; (4) one-pager and data-room v1 ready; (5) SEIS/EIS advance assurance submitted ("applied for", never "approved"). Earliest start: **Wed 14 Oct 2026 (Day 31)**. Before that date the SOP runs in preparation mode only (steps 2–4).
**Owner:** Founder. VA maintains CRM hygiene and re-verification. Solicitor signs off financial-promotion wording (engine §9).
**Process:**
1. Pre-condition check written into `/operations/DECISION_LOG.md`; if any item is open, stop — no outreach, no "soft" messages, no LinkedIn pitching.
2. Work from the investor assets in `/investors/`: master CRM `VYTALIX_INVESTOR_CRM.csv` / `.xlsx` (319 records per `INVESTOR_DASHBOARD.md`, 7 A-tier, 87 B-tier — VERIFIED at CRM build; note the 90-day plan's "253" predates the angel-network and strategic top-ups); ranked list `TOP_25_INVESTORS.md`; `CALL_LISTS.md` (List 1 = Top 25, List 2 = Next 50, List 3 = Next 75, List 4 = remainder); per-investor scripts `OUTREACH_TOP25.md`; stage rules `CRM_PIPELINE.md` (18 stages; every record enters at Researched; "Outreach Ready" requires the pre-conditions). Grant and contract funders sit in `NON_DILUTIVE_FUNDING_ROUTES.md` and are worked under SOP 03, not here.
3. Re-verify every record before contact (team page, mandate, ticket, phone route, "Last Verified" date): List 1 by Fri 16 Oct; Lists 2–3 in the week before each is worked. Phone numbers only from public sources with URL and date; never personal mobiles; "PHONE NOT PUBLICLY AVAILABLE" stays as is — use the stated route.
4. Prepare the one personalised reason per investor (named portfolio company, thesis or public statement) from `OUTREACH_TOP25.md`; edit for voice; replace [Founder], [company number], [link].
5. Sequence: List 1 in Weeks 6–7 (to Fri 30 Oct, Day 47); List 2 in Weeks 8–9 (to Thu 12 Nov, Day 60); List 3 in Weeks 10–12 (to Fri 4 Dec, Day 82); referrals from earlier lists worked first; List 4 thereafter or on referral.
6. Contact: phone-first where a verified public number exists (engine §2 opening, 25 seconds); otherwise email (engine §3, under 150 words) or LinkedIn (engine §4). Cadence: call → same-day email → +4 → +10 → +21 → quarterly update. No follow-up #2 without a new proof point (create one first).
7. Log every touch the same day in `CRM Status`; regenerate the CRM, Top 25, call lists and dashboard every Friday with `python3 investors/build_crm.py`; edits go into `investors/raw/*.csv`, never into the generated files.
8. On a reply, offer three 30-minute slots within 7 days; send the one-pager 24 h before; run the meeting to the 30-minute structure (engine §6); ask "what would stop you?" and commit to a written answer within 48 h (engine §8 objection table).
9. Close every meeting with a dated next step and one referral ask; investors at "Meeting Completed" who request the data room are handed to SOP 03.
10. Weekly: count Identified → Contacted → Calls → Meetings → Discussions; write the Investment rows of `/operations/KPI_DASHBOARD.csv` and the Investor tracker rows of `/operations/PIPELINE_TRACKERS.csv`.
**Documents:** `/investors/VYTALIX_INVESTOR_CRM.csv` and `.xlsx`; `TOP_25_INVESTORS.md`; `CALL_LISTS.md`; `OUTREACH_TOP25.md`; `OUTREACH_ENGINE.md`; `CRM_PIPELINE.md`; `INVESTOR_DASHBOARD.md`; `build_crm.py` and `raw/`; one-pager (`/assets/INVESTOR_ONE_PAGER.md`); deck v1 (`/assets/INVESTOR_PITCH_DECK.md`, stage-honest); data-room index; FCA financial-promotion checklist (engine §9).
**Approval:** Founder confirms pre-conditions in writing; solicitor signs off deck disclaimers and promotion wording before the first send; board (once formed) approves round parameters before any term is discussed.
**KPI:** Contacted (records with ≥ 1 logged outbound touch): Month 2 50, Month 3 75, cumulative 125 by Day 90; Calls (attempts on verified public numbers) 40 / 60 / 100 cumulative; Meetings ("Meeting Completed") 4 / 6 / 10 cumulative; contacted → meeting ≥ 8%; weekly volume in Weeks 6–12: 15 calls, 25 emails, 20 LinkedIn touches, 3 meetings; ≥ 1 referral per meeting; CRM regenerated 100% of Fridays.
**Output:** Investor tracker rows; meeting notes in `CRM Status`; investors requesting the data room handed to SOP 03; monthly investor update list (everyone at "Responded" or later).

### SOP 03 — Fundraising (from investor interest to money received; includes non-dilutive)

**Trigger:** An investor requests the data room or a second meeting; **or** a grant/contract call opens that fits (`/investors/NON_DILUTIVE_FUNDING_ROUTES.md`: Innovate UK Smart, SBRI Healthcare, NIHR i4i, Grand Challenges Canada, others — eligibility TO VALIDATE per call); **or** the board decides to open a round.
**Owner:** Founder; accountant (SEIS/EIS, tax); solicitor (instruments, promotion wording); fractional FD once a term sheet exists.
**Process:**
1. Define the round on one page: amount (pre-seed £150k–£300k, ESTIMATE per `/docs/02_GROUP_STRUCTURE.md` §2; rounds table in `/docs/08_FINANCIAL_MODEL.md` §4.2), instrument (SEIS/EIS-compatible advance subscription agreement or priced round — solicitor to advise), use of funds, 12-month milestones, cap-table impact including any IP-settlement equity.
2. Assemble data-room v1 (index `/operations/DATA_ROOM_INDEX.md`, TO CREATE): one-pager; deck; financial model summary from `/finance/Vytalix_Financial_Model_3yr.xlsx` (scenarios labelled, not forecasts); IP agreement summary; cap table; advisory board (named only with consent); pilot plan; risk register; policies adopted; SEIS/EIS advance-assurance letter or "applied for"; Q&A log.
3. Grant branch: check eligibility (UK-registered company, NHS or clinical partner where required, match funding); score bid/no-bid with `/docs/20_DECISION_FRAMEWORK.md`; allocate 10–15 founder days per bid; first decision Fri 23 Oct 2026; target ≥ 1 bid by Day 90 if a call is open, ≥ 4 per year; separate cost centre opened on award (SOP 10 step 9).
4. Send the data room via a tracked link; log the date; answer every diligence question within 48 h; keep the Q&A log current.
5. Second meeting: present the 90-day milestone plan and the audit-score trend; ask for their diligence list, decision process and timeline.
6. Introduce advisers and, where relevant, a design-partner contact — only with their written consent.
7. Term discussion: solicitor reviews every document; secure a lead first, then fill; never accept an anti-dilution floor for the IP settlement (structure doc §3); board approves terms.
8. Close: signed documents; funds received and reconciled in Xero; Companies House filings (SH01, PSC changes); SEIS1/EIS1 compliance statements via the accountant; cap table updated.
9. Post-close: monthly one-page investor update; board/observer rights implemented; D&O insurance bound (legal doc §11).
**Documents:** Round one-pager; data room; Q&A log; term sheet; subscription documents; SEIS/EIS advance-assurance application and compliance statements; grant application templates; cap-table model; `/docs/09_FUNDING_STRATEGY.md`.
**Approval:** Board approves round terms and issue of shares (reserved matter); solicitor signs off all instruments and financial-promotion compliance; accountant signs off SEIS/EIS.
**KPI:** Discussions (active, at "Due Diligence" or "Investment Discussion"): Month 2 1, Month 3 2; data rooms sent → second meetings ≥ 40%; diligence answers within 48 h 100%; first meeting → term sheet ≤ 90 days (ESTIMATE); Grant bids submitted ≥ 1 by Day 90 (if a call is open); Committed (£, signed not received) and Received (£) reported monthly — base case £0 by Day 90.
**Output:** Signed instruments; cash in bank; filings; updated cap table; monthly investor update; grant submissions.

### SOP 04 — Product development (MaternaLink (in development))

**Trigger:** Gate G0 (IP/ownership documented) passed **and** a minuted build decision (MVP build / build-lite / wait, due Tue 8 Dec 2026, Day 86); or any request to change scope, intended use or a feature.
**Owner:** Founder as acting CPO until a fractional product lead is engaged; fractional CTO for technical decisions; CSO for clinical safety.
**Process:**
1. Confirm the gates before any sprint: G0 IP deed executed; prototype audit passed or "rebuild" chosen (`/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §25); CSO engaged and hazard log open; DPIA v0.1 started; intended-use statement adopted (§21.1); every contributor has signed the IP clause.
2. Work only from `/product/MATERNALINK_PRD.md` (118 requirements, MoSCoW) and `/product/MATERNALINK_MVP_SPEC.md`; no requirement added or re-prioritised without a PRD change record.
3. Two-week sprints: planning Monday; 15-minute daily stand-up (async acceptable); review and retrospective on the second Friday; founder attends the review only.
4. **Line-crossing check** on every feature: does it interpret, score, alert on, triage or predict from clinical information? If yes, it is out of v1 and logged for the G8 qualification decision (strategy §21.2).
5. Every user-facing content item passes clinical sign-off (advisory #1/#2 or CSO) before release; sign-off ID logged.
6. Hazard log (DCB0129) updated at each sprint review; new hazards assessed by the CSO within 5 working days.
7. Security in the definition of done (MVP spec): audit logging, encryption, secrets management, dependency scanning; **no real patient data in any non-production environment**; the Vercel prototype processes no real data until the audit passes.
8. Discovery loop: ≥ 20 women and ≥ 10 professionals per market interviewed before MVP freeze (strategy §3.2); UK discovery interviews 15 by Day 60 feed personas and report 1.
9. Release: staging → penetration test (before go-live and after major change) → safety-case sign-off → production; plain-English release notes.
10. Monthly: Features (Must delivered ÷ Must total), Users, Activation, Retention and Milestones reported to the Product rows of the KPI dashboard and the Product tracker.
**Documents:** PRD; MVP spec; `/product/MATERNALINK_ROADMAP.md`; intended-use statement; hazard log and clinical safety case; DPIA; sprint board; release notes; PRD change records; prototype audit report.
**Approval:** Intended-use or scope changes — board (reserved matter) with CSO written advice; feature release — CSO safety-case sign-off + founder; content — clinical adviser sign-off.
**KPI:** Milestones closed per month (Month 1: IP heads of terms, claims retired, intended-use adopted; Month 2: prototype audit, CSO engaged, PRD v0.2 signed off; Month 3: DPIA v0.1, safety-case skeleton, MVP decision minuted) = 3/3/3; Features delivered 0 until funded (no build before funding); sprint commitment delivered ≥ 80% once building; open critical hazards at release = 0; critical/high vulnerabilities open > 14 days = 0; Discovery interviews 4 / 10 / 16 cumulative by month.
**Output:** Gate evidence (deed, audit report, CSO letter, DPIA); shippable increments once funded; updated hazard log and safety case; DTAC readiness pack; monthly Product KPI rows.

### SOP 05 — Customer acquisition (proposal to signature)

**Trigger:** A proposal has been sent (SOP 01 step 11), or a pilot-scoping conversation reaches "budget and authority confirmed".
**Owner:** Founder.
**Process:**
1. Follow up at +3 days (call) and +7 days (email carrying one new proof point: adviser confirmed, article published, template shared, report finding).
2. Handle objections with the sales doc §15 table; price objections are answered with scope options, never with a price below the floor.
3. Negotiate within guardrails (`/assets/PRICING_STRUCTURE.md`, which supersedes the older figures in sales doc §16): founder day floor £1,200 (list £1,500); associate list £700–£1,000; discount ≤ 10% founder discretion, ≤ 15% for multi-package bundles, always with a scope or concession trade; fixed-fee sprints ± 10%; payment 50% on signature under £20k, 30/40/30 above; 14-day terms; retainers monthly in advance; government (Nigeria) work only after a ≥ 30% mobilisation payment.
4. Confirm the contracting entity: pre-incorporation = founder personal contract with PI insurance and a novation clause (legal doc §1); post-incorporation = company MSA + SOW.
5. Issue MSA + SOW by e-signature with the data-handling statement (no patient data in advisory work; SOP 09 if any personal data must flow).
6. On signature: raise the deposit invoice the same day (SOP 10); move the deal to Closed-won; record source channel, days-to-close and package code.
7. Send the welcome note with kick-off date and onboarding checklist (SOP 06) within 24 h.
8. If lost: code the reason; diarise a 90-day re-contact; ask for a referral.
**Documents:** Proposal; MSA; SOW; e-signature tool; pricing guardrails; invoice template; loss-reason codes; objection table.
**Approval:** Founder ≤ £25k; board > £50k; solicitor for any non-standard clause (liability cap, IP, exclusivity, equity-for-services).
**KPI:** Customers (signed SOWs): Month 1 1, Month 2 1, Month 3 1 (cumulative 3); proposal → customer ≥ 25%; median days proposal → signature ≤ 21; first-invoice-on-signature 100%; discounts below floor 0; Contracted revenue Month 1 £3k–£6k, Month 2 £6k–£10k, Month 3 £8k–£14k, cumulative £15k–£30k (ESTIMATE, not a forecast).
**Output:** Signed MSA/SOW; deposit invoice; CRM record Closed-won; Revenue tracker updated; hand-off to SOP 06.

### SOP 06 — Customer onboarding (signature to first value)

**Trigger:** Signed SOW received.
**Owner:** Founder (delivery lead); VA for logistics; associate if assigned (IP clause signed first).
**Process:**
1. Within 24 h: create the private engagement folder (`/clients/<code>/`) with SOW, contacts, success criteria and the deliverable schedule.
2. Within 3 working days: 45-minute kick-off — confirm scope, deliverables, dates, counterpart, decision-maker, weekly 30-minute check-in, and "done" in the client's words.
3. Send the kick-off note within 24 h (scope confirmation, timeline, risks, next actions) — the baseline for change control.
4. Set up working tools: shared folder, meeting series, NDA if not in the MSA; confirm in writing that no personal or patient data will be shared (or trigger SOP 09 before anything moves).
5. Deliver the first tangible output within 10 working days (interview summary, framework, draft outline) — first value fast.
6. Weekly check-in: progress, blockers, decisions needed; logged in the engagement file.
7. Mid-point review for engagements ≥ 3 weeks: scope-drift check; change request if needed (> 10% of value = re-quoted SOW).
8. Final deliverable → review meeting → sign-off note → final invoice → 10-minute feedback call (NPS; testimonial request with written consent before any use).
9. Close: archive; add reusable assets (playbooks, templates) to the internal library; case study only with client consent and FACTS_BASE-compliant wording.
**Documents:** Engagement folder template; kick-off agenda and note; weekly check-in log; change-request form; sign-off note; `/operations/CLIENT_FEEDBACK_FORM.md` (TO CREATE).
**Approval:** Founder signs off deliverables; client counterpart signs the sign-off note; change requests > 10% of value re-quoted.
**KPI:** Kick-off within 3 working days 100%; first value within 10 working days 100%; on-time delivery 100%; NPS ≥ 8/10; reusable asset per engagement ≥ 1; referral or testimonial from ≥ 50% of engagements; first testimonial with consent by Fri 11 Dec 2026.
**Output:** Delivered engagement; final invoice paid; feedback score; reusable assets; referral or testimonial.

### SOP 07 — Healthcare partnerships (NHS, private providers, NGOs, ministries, incumbents)

**Trigger:** Quarterly partnership planning (first: week of Mon 21 Sept 2026); any inbound approach from a healthcare organisation; any decision in `/docs/20_DECISION_FRAMEWORK.md` that requires a partner; the Ekiti go/no-go inputs (status call by Fri 9 Oct; mDoc conversation by Fri 6 Nov; two-state scorecard by Fri 6 Nov).
**Owner:** Founder; advisory #3 (NHS) and #4 (Nigeria) as advisers; Nigeria country lead when engaged.
**Process:**
1. Maintain the partnership long-list in the Partnership tracker (`/operations/PIPELINE_TRACKERS.csv`): type (design partner, clinical-academic, NGO implementer, incumbent complementarity, ministry, insurer/telecom), value to Vytalix, value to them, gate dependencies.
2. Qualify against the partnership model (`/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §10 and `/docs/12_PARTNERSHIP_STRATEGY.md`): what they must have (active maternity improvement programme, digital midwife role, existing cohort, donor funding) and what Vytalix offers (non-diagnostic v1, evidence generation, no cost to the partner in the first stage).
3. Approach with a one-page partnership brief; never state or imply an existing relationship with any government, NHS body or the incumbent (mDoc) in any material.
4. Ekiti and Nigeria: (a) status call on the March 2026 proposal — facts only, no new offer; (b) one exploratory complementarity conversation with mDoc; (c) scorecard for two alternative states (market doc §2.1); G-D decision at the board on Thu 12 Nov 2026 (Day 60). The £4.5m / £300-per-woman proposal is not restated under any option.
5. Ladder every partnership: conversation → written brief → LOI/MoU → pilot or evaluation agreement → contract. An MoU is never described as a "partnership" in investor material (FACTS_BASE §4).
6. Every LOI/MoU reviewed by the solicitor; anti-bribery clause and conflict-of-interest declaration in every government-facing document (UK Bribery Act applies extraterritorially); no facilitation payments.
7. Any partnership involving patient data triggers SOP 09 (DPIA, data-sharing agreement, CSO review) before any data moves.
8. Monthly: update the tracker; report every government proposal to the board (reserved matter).
**Documents:** Partnership long-list; one-page brief template (`/assets/PARTNERSHIP_DECK.md` as source); LOI/MoU templates (solicitor); state scorecard; anti-bribery policy; conflicts register; gifts and hospitality register.
**Approval:** Founder for conversations and briefs; board for any MoU, government proposal or pricing to a public body; solicitor for every signed document.
**KPI:** Qualified partnership conversations/month ≥ 4 UK, ≥ 2 Nigeria from Month 2; Design-partner conversations at "brief sent" or later: Month 1 1, Month 2 3, Month 3 5; ≥ 1 LOI in drafting by Day 90; Ekiti status logged as KNOWN by Fri 9 Oct; mDoc conversation held by Fri 6 Nov; first conversation → LOI ≤ 90 days (ESTIMATE).
**Output:** Updated Partnership tracker; briefs sent; LOIs/MoUs; documented G-D recommendation for Day 60.

### SOP 08 — Due diligence (on partners, contractors, advisers, investors and the prototype)

**Trigger:** Before signing any agreement with a third party (contractor, associate, adviser, partner, investor, vendor), and before accepting any inbound code or data — the Vercel prototype (`https://maternal-health-psi.vercel.app/`) is the first case, due Tue 13 Oct 2026 (Day 30).
**Owner:** Founder; solicitor for legal checks; fractional CTO for code; accountant for financial checks where relevant.
**Process:**
1. Identity and existence: Companies House (UK) / CAC (Nigeria) / equivalent; directors; sanctions and PEP screening for government-facing and Nigeria dealings (screening tool TO VALIDATE).
2. Reputation: public-record search (litigation, regulatory action, press); two references for contractors and associates.
3. Conflicts: check the conflicts register (Kemek Enterprise Ltd declared); investor conflicts (competing portfolio companies) noted, not disqualifying.
4. Capability: portfolio or case evidence for contractors; for investors, fund status and ticket confirmed from a public source (CRM "Qualified" rule).
5. Code/prototype: authorship and repository ownership; dependency licences; secrets scan; data held and region; credentials; security posture — pass conditions in product strategy §25. Until passed, the prototype is a demo asset and processes no real data.
6. Data: what personal data (if any) would flow; controller/processor roles; sub-processors; region; DPA needed.
7. Financial: counterparties paying Vytalix > £10k — credit check (tool TO VALIDATE); Vytalix payments > £5k — milestone-based terms.
8. IP: the IP-assignment clause is signed before any work starts; for the prototype, confirm who wrote the code and on what terms before any reuse.
9. Record a one-page DD memo: pass / pass with conditions / fail; conditions become contract clauses.
**Documents:** `/operations/DUE_DILIGENCE_CHECKLIST.md` (TO CREATE); DD memo template; prototype audit checklist (strategy §25); conflicts register; sanctions screening record; IP audit questionnaire (sent to David Agunede Wed 16 Sept 2026).
**Approval:** Founder for contractors ≤ £10k and advisers; board for partners, investors and anything > £10k; solicitor where legal warranties are relied on.
**KPI:** 100% of agreements have a DD memo before signature; prototype audit complete by Tue 13 Oct 2026 with a pass / conditions / fail verdict; DD turnaround ≤ 5 working days for standard cases; 0 contributors without a signed IP clause.
**Output:** DD memos; contract conditions; conflicts register update; prototype audit report (reuse vs rebuild recommendation for G-B).

### SOP 09 — Compliance (data protection, clinical safety, claims, corporate, security)

**Trigger:** The compliance calendar (`/docs/15_LEGAL_AND_REGULATORY.md` §14); any new processing activity; any new external material; any incident; any partnership or engagement that touches personal or patient data.
**Owner:** Founder (acting Risk & Compliance lead); fractional DPO; CSO; solicitor.
**Process:**
1. Corporate: confirmation statement, accounts, statutory registers, board minutes per the calendar; conflicts register reviewed quarterly.
2. Data protection: ICO registration (Tier 1, £52) by Fri 2 Oct 2026; legitimate-interests assessment for outreach; privacy notice live before any web form; RoPA by Day 30; DPIA before any patient-data processing (v0.1 by Fri 4 Dec 2026); breach procedure with 72-hour ICO notification readiness; NDPA/NDPC analysis before any Nigeria deployment.
3. Clinical safety: intended-use statement enforced feature-by-feature; hazard log and safety case owned by the CSO; any line-crossing feature logged for G8; regulatory qualification opinion commissioned by Day 45.
4. Claims sign-off: every external artefact (post, deck, proposal, web page, grant bid, investor update) passes the checklist — "MaternaLink (in development)"; no NHS-approved / clinically validated / CE-UKCA / MHRA / government-partner / mortality-reduction claims; every statistic cited to its source; log the check.
5. Security: password manager, MFA and device encryption on every account from Day 1; Cyber Essentials self-assessment started by Day 60, certified by Day 90 (target); security policy P0 items adopted at the first board meeting.
6. Insurance: PI and PL bound before the first paid engagement (Fri 2 Oct 2026); cyber before personal data at scale; D&O on first external investment; annual renewal.
7. Anti-bribery and government dealings: policy adopted at the first board meeting; gifts and hospitality register; every Nigeria payment through a contracted, invoiced route.
8. Incidents: log → contain → assess (DPO/CSO) → notify (ICO/NDPC/client) within statutory windows → root cause → policy update.
9. Quarterly 30-minute compliance review against the risk register (legal doc §13); statuses and owners updated; report to the board.
**Documents:** Compliance calendar; policy set (legal doc §9.2); ICO registration; RoPA; LIA; DPIA template; hazard log; `/operations/CLAIMS_CHECKLIST.md` (TO CREATE); incident log; gifts register; risk register; insurance schedules.
**Approval:** Board adopts policies and approves any clinical/regulatory claim (reserved matter); DPO signs DPIAs; CSO signs safety cases; solicitor signs contracts and financial-promotion wording.
**KPI:** Compliance-calendar items on time 100%; external artefacts with a logged claims check 100%; open P0 compliance items at Day 30 = 0; reportable incidents = 0; Cyber Essentials certified by Fri 11 Dec 2026; ICO reference number by Fri 2 Oct 2026.
**Output:** Registrations and certificates; signed policies; claims-check log; DPIA; quarterly compliance report to the board.

### SOP 10 — Finance (invoicing, cash, spend, bookkeeping, tax)

**Trigger:** Any signed SOW (invoice); Friday 16:15 cash check; monthly close on the 5th working day; any spend > £250; any grant award.
**Owner:** Founder; accountant (close, tax, filings); VA (invoice chasing, receipts); fractional FD when engaged.
**Process:**
1. Invoice on signature (deposit) and on milestones exactly as the SOW states; 14-day terms; Xero invoice with GoCardless/Stripe link; pre-incorporation invoices on the founder's personal contract are novated on incorporation.
2. Chase: day 7 automated reminder; day 15 call; day 30 formal letter; no new work on an account > 30 days overdue without a founder decision.
3. Weekly (Friday 16:15): reconcile the bank in Xero; update cash, receivables, payables and the 13-week cash-flow (`/operations/CASHFLOW_13WEEK.xlsx`, TO CREATE; v0 by Fri 18 Sept); compute runway.
4. Spend: > £250 needs a one-line justification against the budget (`/finance/Vytalix_Financial_Model_3yr.xlsx`; 90-day budget in the execution plan §8, £10.5k–£25.75k ESTIMATE); > £2,500 needs a written quote comparison; borrowing > £25k or a contract > £50k is a board reserved matter.
5. Founder draw: £0 until Month 3; then £3,000/month minimum only when trailing-month revenue ≥ £7,500 (break-even rule, business model §3); otherwise deferred and logged to the founder loan account (accountant to structure).
6. Separate ventures: no Kemek Enterprise Ltd transactions through Vytalix accounts; any shared cost apportioned by written policy and minuted as a related-party matter.
7. Monthly close by the 5th working day: P&L, balance sheet, cash, burn, runway, EBITDA; variance to model; Finance rows of the KPI dashboard updated with ACTUAL labels.
8. Tax and filings: Corporation Tax registration; VAT monitored against the threshold (£90k, TO VALIDATE); PAYE only when salaried; R&D relief assessed at first MVP spend; SEIS/EIS compliance statements after any investment.
9. Grants: separate cost centre; timesheets for match-funding evidence; claims submitted per funder schedule.
**Documents:** Xero; invoice template; 13-week cash-flow; budget vs actual; founder loan account record; expense policy (£250 / £2,500 / £25k thresholds); grant timesheets.
**Approval:** Founder ≤ £2,500; board above, or for borrowing > £25k; accountant signs off filings.
**KPI:** Invoice within 24 h of trigger 100%; Debtor days ≤ 30; monthly close by working day 5 100%; Runway ≥ 6 months by Month 3 (target) or cash-positive; spend variance to budget ≤ 10%; zero missed statutory filings; Revenue (invoiced) Month 1 £0–£3k, Month 2 £4k–£8k, Month 3 £7k–£12k (ESTIMATE).
**Output:** Invoices and receipts; weekly cash position; monthly management accounts; Finance KPI rows; filings.

### SOP 11 — Reporting (weekly, monthly, quarterly; board and investors)

**Trigger:** Friday 15:30 (weekly review); 5th working day (monthly); quarter-end + 10 days (quarterly); every board meeting (Tue 13 Oct, Tue 10 Nov, Tue 8 Dec 2026); investor update date (first Thu 5 Nov 2026).
**Owner:** Founder; VA compiles data; accountant supplies Finance rows.
**Process:**
1. Weekly: complete the review template in `/docs/17_FOUNDER_OPERATING_SYSTEM.md` §5 (revenue, investor interest, product, partnerships, attention); update `/operations/KPI_DASHBOARD.csv` and `/operations/PIPELINE_TRACKERS.csv`; 45 minutes maximum; file as `/operations/reports/YYYY-Www.md`.
2. Monthly: one-page management report — all five KPI sections with formulas and variance to Month 1–3 targets; top 3 wins, top 3 misses, decisions needed; re-score the 22 audit areas in `/docs/00_MASTER_AUDIT.md` §2 (first re-score Wed 14 Oct 2026; target ≥ 20 / ≥ 27 / ≥ 32 at the three closes, ≥ 35 by mid-December).
3. Quarterly: strategy review against the execution-plan gates; decision-framework re-score of live ideas; hiring-plan triggers checked (§3); risk register refreshed; next-quarter plan with owners and dates (first: week of Mon 14 Dec 2026).
4. Board pack: agenda, previous minutes, management report, cash and runway, reserved-matter decisions, compliance report, risk register — circulated 3 working days before.
5. Investor update: one page monthly to everyone at "Responded" or later — metrics, progress, asks, what changed; stage-honest language per FACTS_BASE.
6. Every number in every report carries its label (ACTUAL / TARGET / ESTIMATE); no actual is claimed before it occurs; every value is traceable to the source system named in the CSV.
7. Archive all reports in `/operations/reports/YYYY-MM/` (TO CREATE).
**Documents:** Weekly review template; KPI dashboard CSV; pipeline trackers CSV; monthly report template; `/operations/BOARD_PACK_TEMPLATE.md` (TO CREATE); investor update template; audit re-score sheet.
**Approval:** Founder issues weekly and monthly reports; board approves minutes and pack; investor updates pass the claims check (SOP 09 step 4).
**KPI:** Weekly review completed by Friday 17:00 100% (13/13 in the 90 days); monthly report by working day 5 100%; board pack 3 days ahead 100%; investor update sent monthly 100%; audit re-score monthly, ≥ 35 by Sat 12 Dec 2026.
**Output:** Weekly review; monthly management report; quarterly strategy review; board pack and minutes; investor update; updated audit score.

---

## 5. SOP coverage map and RACI

### 5.1 Hand-offs

| From | To | Hand-off artefact |
|---|---|---|
| SOP 01 Business development | SOP 05 Customer acquisition | Proposal sent |
| SOP 05 Customer acquisition | SOP 06 Onboarding; SOP 10 Finance | Signed SOW; deposit invoice |
| SOP 06 Onboarding | SOP 11 Reporting; SOP 01 (referrals) | Feedback score; testimonial; referral |
| SOP 02 Investor acquisition | SOP 03 Fundraising | Investor at "Meeting Completed" requesting the data room |
| SOP 03 Fundraising | SOP 10 Finance; SOP 04 Product | Funds received; MVP budget released |
| SOP 07 Partnerships | SOP 04 Product; SOP 09 Compliance | LOI; DPIA trigger |
| SOP 08 Due diligence | SOP 03, 04, 07 | DD memo and conditions |
| SOP 09 Compliance | All external-facing SOPs | Claims check; policy constraints |
| SOP 10 Finance | SOP 11 Reporting | Monthly close rows |
| SOP 11 Reporting | SOP 01–10 | Decisions and re-prioritisation |

### 5.2 RACI (R = does, A = accountable, C = consulted, I = informed)

| SOP | Founder | VA | Solicitor / attorney | Accountant | Fractional CTO | CSO / clinical adviser | Board | Advisory board |
|---|---|---|---|---|---|---|---|---|
| 01 Business development | R/A | R (research, logging) | C (templates) | — | — | — | I | C |
| 02 Investor acquisition | R/A | R (hygiene) | C (promotion wording) | C (SEIS/EIS) | — | — | I | C (intros) |
| 03 Fundraising | R/A | I | R (instruments) | R (SEIS/EIS) | — | — | A (terms) | C |
| 04 Product development | R/A | — | C (IP) | — | R (technical) | R (safety) | A (intended use) | C |
| 05 Customer acquisition | R/A | I | C (non-standard clauses) | I | — | — | A (> £50k) | — |
| 06 Customer onboarding | R/A | R (logistics) | — | I | — | — | — | — |
| 07 Healthcare partnerships | R/A | I | R (MoUs) | — | — | C | A (government) | C |
| 08 Due diligence | R/A | R (searches) | R (legal checks) | C | R (code) | — | A (> £10k) | — |
| 09 Compliance | R/A | R (registers) | R (contracts) | C | C (security) | R (safety case) | A (policies, claims) | C |
| 10 Finance | R/A | R (chasing) | — | R (close, tax) | — | — | A (reserved matters) | — |
| 11 Reporting | R/A | R (compile) | — | R (finance rows) | — | — | A (minutes) | I |

---

## Priorities / Risks / Next actions

**Priorities**
1. Stand up the outsourced bench that unblocks everything: solicitor, trademark attorney and accountant instructed by Fri 18 Sept 2026; fractional CTO engaged for the prototype audit by Mon 28 Sept; CSO identified by Wed 28 Oct (Day 45), engaged by Thu 12 Nov (Day 60).
2. Run SOP 01 at full weekly quota from Mon 28 Sept (Week 3); first signed engagement by Tue 13 Oct (Day 30); three by Sat 12 Dec (Day 90).
3. Do not start SOP 02 until the five pre-conditions are logged as met; target start Wed 14 Oct (Day 31); the CRM count to quote is 319, not 253.
4. Two advisory-board members signed (obstetrics/midwifery and regulatory/CSO profiles) by Thu 12 Nov; four by Fri 11 Dec.
5. Settle David Agunede's role (§2.2) by Sun 20 Sept (heads of terms) and Tue 13 Oct (deed) — the org chart cannot be published externally until this is done.

**Risks**
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Founder runs nine functions and none well | High | High | Weekly time audit (founder OS §1); VA trigger measured weekly; SOP quotas are minimums, not aspirations |
| Hiring ahead of revenue | Medium | High | Every hire in §3 is trigger-gated; salaries > £60k are a board reserved matter; monthly hiring-trigger check |
| David Agunede role ambiguity persists past Day 7 | Medium | High | Standstill letter Week 1; three role options pre-defined (§2.2); Day 60 hard stop with clean-room rebuild |
| Contractor IP leaks (developers engaged by others) | Medium | High | IP clause before any work (SOP 08 step 8); prototype audit before reuse |
| Pricing-floor confusion between documents (sales doc §16 vs pricing structure) | Medium | Medium | SOP 05 step 3 names `/assets/PRICING_STRUCTURE.md` as authoritative; sales doc §16 to be aligned at next revision |
| SOPs written but not used | Medium | Medium | Each SOP has a KPI in the Friday review; an SOP with no KPI for two weeks is escalated to the Monday plan (principle 7) |

**Next actions**
| Action | Owner | Deadline |
|---|---|---|
| Create `/operations/DECISION_LOG.md`, `CLAIMS_CHECKLIST.md`, `DUE_DILIGENCE_CHECKLIST.md`, `SOW_TEMPLATE.md`, `DATA_ROOM_INDEX.md` skeletons | Founder | Wed 16 Sept 2026 |
| Instruct solicitor (IP deed, founder IP assignment, MSA/SOW/NDA review, name opinion) and trademark attorney | Founder | Fri 18 Sept 2026 |
| Send David Agunede the IP audit questionnaire and standstill letter; heads of terms | Founder + solicitor | Wed 16 / Fri 18 / Sun 20 Sept 2026 |
| Appoint accountant; Xero live on incorporation | Founder | Fri 25 Sept 2026 |
| Engage fractional CTO for the prototype audit | Founder | Mon 28 Sept 2026 |
| First board meeting: adopt policies, SOPs and hiring-plan triggers; minute G-C and the pre-condition status | Founder + NED (if appointed) | Tue 13 Oct 2026 |
| VA decision (admin > 8 hrs/week test) | Founder | Fri 16 Oct 2026 |
| Shortlist 3 CSO candidates; engage one | Founder | Wed 28 Oct / Thu 12 Nov 2026 |
| Align sales doc §16 day-rate figures to the pricing structure | Founder | Fri 9 Oct 2026 |
