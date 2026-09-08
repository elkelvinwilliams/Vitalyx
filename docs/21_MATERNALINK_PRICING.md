# 21 — MATERNALINK PRICING: PER PRODUCT AND ANNUAL SERVICE

**Owner:** CFO with Chief Product Officer · **Status:** PROPOSED v1.0 (8 September 2026) · **Every figure is an ESTIMATE until validated with three buyers per segment** · Supersedes the £300/woman/year figure in the March 2026 Ekiti proposal, which is retired. Governing files: `/FACTS_BASE.md`, `/docs/01_BUSINESS_MODEL.md`, `/docs/08_FINANCIAL_MODEL.md`.

## Executive view
1. MaternaLink is priced as **a platform licence plus optional modules, plus an annual service plan**, with hardware (the Maternity Watch) priced separately as a per-device lease or purchase. This separates software value from device cost and lets buyers start without hardware.
2. Two price books: **UK** (NHS trusts and ICBs, private maternity, employers) and **Africa / programme** (state ministries, NGOs, insurers), because willingness to pay and cost-to-serve differ by an order of magnitude.
3. Indicative annual software price per woman enrolled: **UK £18–£36; Africa programme £4–£10** at scale, with a pilot minimum so no contract is below cost. The old £300/woman/year figure is 8–30× these levels and is not defensible against comparable programmes.
4. Annual service is priced at **18–22% of licence value** (Standard) rising to 30–35% (Premium, 24/7 clinical-safety on-call and named account management), in line with enterprise health-software norms (ESTIMATE).
5. Gross margin target: software 75–85%; services 45–55%; hardware 20–30% (hardware is a channel, not a profit centre).

---

## 1. Product catalogue (what is sold)

| Code | Product | What the buyer gets | Unit | Regulatory posture |
|---|---|---|---|---|
| ML-CORE | **MaternaLink Core platform** | Patient registry (mother + newborn), offline-first capture of symptoms and vitals, timeline, clinician notes, escalation queue, supervisor dashboards, EN/FR interface, exports, audit log | Per site licence + per enrolled woman | Non-diagnostic care-coordination software; intended-use statement controls scope |
| ML-TRIAGE | **Maternity Triage module** | Structured triage intake for maternity assessment units, prioritisation rules configured by the site's clinical governance, contact and outcome logging, waiting-time analytics | Per site | Rules configured and owned by the provider; Vytalix supplies the rule editor, not the rules. Classification TO VALIDATE with MHRA guidance before any rule ships pre-configured |
| ML-ENGAGE | **Woman & partner engagement module** | Daily questionnaire, symptom log (including itching of hands and feet, vomiting, headache, visual disturbance, reduced movements), education content signed off by clinicians, partner quizzes and prompts, appointment reminders via SMS/WhatsApp | Per enrolled woman | Non-diagnostic; symptom logs route to a human. No automated diagnosis |
| ML-GLUCOSE | **Diabetes-in-pregnancy tracking** | Self-reported blood-glucose entries with target ranges set by the clinician, trend view, threshold notifications to the care team | Per enrolled woman with the condition | Threshold notifications configured by the clinician; classification TO VALIDATE (likely needs a device pathway if the software interprets readings) |
| ML-VOICE | **Voice diaries** | Recorded diaries and voice notes attached to the timeline; transcription and translation as a roadmap option | Per enrolled woman | Non-diagnostic storage and playback only. "Voice tracing of baby movements" is a **research track**, not a sold feature, until validated |
| ML-WATCH | **Maternity Watch (device)** | A wearable issued at the 16-week appointment and returned at postnatal discharge; captures pulse, activity and prompts the daily check-in; syncs to the platform | Per device (lease or purchase) plus per-device service | A wearable that measures physiological parameters for clinical use is very likely a **medical device**; Vytalix should procure a UKCA/CE-marked device from an existing manufacturer and integrate it, rather than manufacture (see §6) |
| ML-INTEGRATE | **Integration pack** | Interfaces to the provider's maternity record (e.g., BadgerNet, K2, Euroking), DHIS2 alignment for programmes, HL7/FHIR endpoints, single sign-on | Per interface, one-off plus annual | Standard software integration |
| ML-ANALYTICS | **Programme analytics** | Population dashboards, defaulter tracing, facility performance, exportable indicators | Per programme | Non-clinical analytics |
| ML-TRAIN | **Training and e-learning** | Role-based training for midwives, community health workers, operators; refresher modules; certification of completion (not accredited) | Per cohort or per learner | E-Learning pillar |

Replacement versus integration: where a hospital has no digital maternity record, MaternaLink Core can act as the working record for the programme (replace); where one exists, MaternaLink integrates and never becomes the legal record (integrate). Price the integration pack accordingly.

---

## 2. Cost-to-serve (why the prices are what they are)

| Cost line | UK per woman per year | Africa programme per woman per year | Notes |
|---|---|---|---|
| Hosting, storage, backups | £0.60–£1.20 | £0.30–£0.60 | UK region; Nigeria residency adds 20–40% |
| Messaging (SMS/WhatsApp) | £1.50–£3.00 | £0.80–£2.00 | ~40 messages per pregnancy; Nigeria SMS via aggregator |
| Support and clinical-safety overhead (allocated) | £3.00–£5.00 | £0.60–£1.20 | Includes hazard-log maintenance, incident handling |
| Onboarding and training (amortised) | £2.00–£4.00 | £0.50–£1.00 | Higher touch in UK trusts |
| Payment/collection, compliance | £0.40 | £0.20 | |
| **Total cost-to-serve** | **£7.50–£13.60** | **£2.40–£5.00** | Floor prices below |
| **Floor price (no contract below)** | **£14** | **£4** | Pilot minimums in §3 protect the floor |

Watch hardware (if used): device £60–£140 unit cost for a suitable wearable from an established manufacturer (ESTIMATE), 24–30 month life, 10–15% loss/damage, refurbishment £8–£15 per cycle. Cost per pregnancy served ≈ £35–£70. Priced at lease £4–£7 per woman per month or purchase with service plan.

---

## 3. Price book A — United Kingdom (ESTIMATE)

### Per product
| Product | Pricing model | Indicative price | Notes |
|---|---|---|---|
| ML-CORE | Site licence + per enrolled woman per year | Site licence £12,000–£30,000/year (by births: <3,000 / 3,000–6,000 / >6,000) **plus** £18–£36 per woman per year | A 5,000-birth trust at £22/woman ≈ £110k + £20k licence = £130k/year |
| ML-TRIAGE | Per site per year | £15,000–£35,000 | Includes rule editor, two configuration workshops |
| ML-ENGAGE | Per enrolled woman per year | £8–£14 | Bundled discount 20% with Core |
| ML-GLUCOSE | Per enrolled woman with condition per year | £20–£30 | Typically 5–10% of the cohort |
| ML-VOICE | Per enrolled woman per year | £3–£5 | Storage included up to 60 minutes per pregnancy |
| ML-WATCH | Lease per device per month; or purchase | £4–£7 per month per device (24-month term) or £120–£220 purchase + £30/year service | Includes replacement pool 10% |
| ML-INTEGRATE | One-off per interface + annual | £15,000–£40,000 setup; £4,000–£8,000/year | Maternity record vendors may charge their own fees (TO VALIDATE) |
| ML-ANALYTICS | Per site per year | £6,000–£12,000 | Included in Enterprise bundle |
| ML-TRAIN | Per cohort (up to 25) | £2,500–£4,500 | E-learning licence £40–£90 per learner per year |
| Implementation | One-off | £25,000–£75,000 per site | Clinical-safety case, DPIA support, configuration, go-live |
| Pilot (12 weeks, one site, up to 300 women) | Fixed | £40,000–£90,000 | Includes evaluation report; converts to annual on success |

### Annual service plans (UK)
| Plan | Price (% of annual licence) | Includes |
|---|---|---|
| Standard | 18–22% (minimum £8,000) | Business-hours support, quarterly releases, security patching, hazard-log maintenance, uptime target 99.5% (design target, not a guarantee until measured) |
| Enhanced | 25–28% | Standard plus extended hours 07:00–22:00, named account manager, two configuration changes per quarter, quarterly service review, DSPT evidence pack |
| Premium | 30–35% | Enhanced plus 24/7 severity-1 response, clinical-safety officer on-call, annual clinical-safety case refresh, dedicated environment option, uptime target 99.9% |

### Enterprise bundles
| Bundle | Contents | Indicative annual (5,000-birth trust) |
|---|---|---|
| Coordinate | Core + Engage + Standard service | £150k–£190k |
| Coordinate + Triage | Above + Triage + Analytics + Enhanced service | £210k–£270k |
| Full programme | Above + Glucose + Voice + Watch lease for 20% of cohort + Premium service | £330k–£420k |

---

## 4. Price book B — Africa and programme funders (ESTIMATE)

| Product | Pricing model | Indicative price | Notes |
|---|---|---|---|
| ML-CORE | Per enrolled woman per year, tiered by volume | £10 (up to 5,000) · £7 (5,001–25,000) · £5 (25,001–100,000) · £4 (100,000+) | Includes programme dashboard; site licence waived for public programmes |
| ML-ENGAGE (SMS/WhatsApp) | Per enrolled woman per year | £3–£5 | Message costs passed through at cost above 40 messages |
| ML-TRIAGE | Per facility per year | £1,500–£4,000 | Facility-level rules owned by the programme's clinical lead |
| ML-GLUCOSE | Per enrolled woman with condition | £6–£10 | |
| ML-VOICE | Per enrolled woman | £1–£2 | Local-language transcription roadmap |
| ML-WATCH | Per device | Lease £2–£4/month or purchase £90–£160 + £15/year service | Only where a programme funds hardware; not in base offers |
| ML-INTEGRATE (DHIS2 / HMIS) | One-off + annual | £8,000–£25,000 + £3,000/year | |
| ML-TRAIN | Per cohort of 30 | £1,200–£2,500 | Train-the-trainer model |
| Implementation | One-off per state or programme | £40,000–£120,000 | Includes data-protection registration support, local hosting decision, baseline evaluation design |
| Annual service | 20% Standard · 28% Enhanced · 35% Premium of software value | Minimum £12,000 | In-country support partner required above 25,000 women (partner margin included) |

### Worked example: a 15,000-woman state programme (year 1)
| Line | Amount |
|---|---|
| Core 15,000 × £7 | £105,000 |
| Engage 15,000 × £4 | £60,000 |
| Triage 20 facilities × £2,500 | £50,000 |
| Implementation (one-off) | £80,000 |
| Training 10 cohorts | £18,000 |
| Enhanced service (28% of £215k software) | £60,200 |
| **Year-1 total** | **£373,200 (≈ £25 per woman)** |
| **Year-2 run-rate** | **≈ £275,000 (≈ £18 per woman)** |
Compared with £4.5m for the same cohort in the retired proposal. Gross margin at these prices ≈ 62% year 1, 74% year 2 (ESTIMATE).

### Worked example: a 5,000-birth UK trust, Coordinate + Triage bundle
| Line | Amount |
|---|---|
| Core licence £20,000 + 5,000 × £22 | £130,000 |
| Engage 5,000 × £10 | £50,000 |
| Triage | £25,000 |
| Analytics | £8,000 |
| Enhanced service (26% of £213k) | £55,400 |
| Implementation (one-off, year 1) | £45,000 |
| **Year-1 total** | **£313,400** · year-2 run-rate £268,400 |

---

## 5. Commercial rules
- Pilot first, always: a fixed-price pilot with an evaluation report, converting to an annual contract with pilot fees credited 50% against year one.
- Minimum contract value: £40,000 (UK), £25,000 (programme), to protect the floor and service quality.
- Multi-year: 5% discount for 3-year terms; annual uplift capped at CPI + 2%.
- Volume discounts only via the published tiers; no ad hoc discounting below floor.
- Payment: UK annual in advance (public sector on receipt of PO); programmes 40% on signature, 40% on go-live, 20% at 6 months, or donor schedule.
- Hardware: never bundle device cost into the per-woman software price; show it as its own line so software margin is visible to investors and price comparisons to competitors are fair.

## 6. The Maternity Watch: build, buy or partner
| Option | Pros | Cons | Verdict |
|---|---|---|---|
| Manufacture a Vytalix device | Brand, margin | Medical-device manufacturer obligations (UKCA, QMS ISO 13485, post-market surveillance), £1m+ and 24+ months | **KILL for now** |
| Integrate an existing UKCA/CE-marked wearable (e.g., a clinically certified wristband) under a supply agreement | Fast, compliant, priced as a pass-through | Lower margin; dependency | **BUILD (partner)** once v1 software is live |
| Consumer wearable (non-medical) for prompts and activity only | Cheap | Cannot be used for clinical vitals; expectation mismatch | **TEST** for engagement-only use (reminders, daily check-in) |

## 7. Validation plan (before any price is quoted externally)
1. Three UK maternity digital leads: reaction to £18–£36 per woman and to bundles (Day 31–60 discovery interviews).
2. Two Nigerian programme leads and one NGO: reaction to £4–£10 per woman and the £25-per-woman year-1 all-in.
3. One insurer/HMO: appetite for per-member pricing.
4. Cost-to-serve check after the prototype audit (hosting, messaging actuals).
5. Regulatory opinion on Triage, Glucose and Watch modules before they are priced in any proposal.

## Priorities / Risks / Next actions
**Priorities:** Core + Engage pricing validated first; Triage and Glucose only after the regulatory opinion; Watch as a partner device.
**Risks:** buyers anchor on free donor-funded programmes (mitigation: pilot-to-contract with evidence; complementarity positioning); under-pricing service (mitigation: minimums); device classification creep.
**Next actions:** put this price book into `/assets/PRICING_STRUCTURE.md` as the MaternaLink section; add price fields to the proposal template; test the two worked examples in the Day 31–60 interviews.
