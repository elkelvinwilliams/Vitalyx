# 24 — MATERNA-LINK INTERROGATED, REINVENTED AND PLANNED

**Date:** 8 September 2026 · **Input:** the 13-slide "MATERNA-LINK: Multimodal AI for Predicting and Preventing Maternal Complications" deck (Oct–Nov 2025) · **Standard:** brutal honesty; every claim labelled KNOWN / ESTIMATE / TO VALIDATE / PROPOSED; no invented traction. Companion files: `investors/partners/PARTNER_TARGET_LIST.csv` (74 organisations), `investors/partners/PARTNER_CRM_TEMPLATE.csv`, `investors/partners/PARTNER_WAR_ROOM.xlsx`.

---

# PART 1 — DEEP PRODUCT AUDIT

## 1.1 What is genuinely innovative
- **The framing of the problem** (deterioration recognised late; communication failures; inequity for Black and Asian women) is exactly where UK maternity policy attention sits (MBRRACE-UK, Ockenden, Kirkup, the national Maternity Early Warning Score). Good instinct.
- **The idea of fusing patient-generated signals from between appointments with clinical data** is the right insight: pregnancy is roughly 280 days and a woman spends perhaps 10–15 hours of it in front of a clinician. The unobserved 99% is the opportunity.
- **Equity by design** (bias monitoring as a first-class component) is ahead of most maternity software, which does not measure who it fails.
- **Voice as a channel for women who will not type** is a genuinely under-used interface in maternity, especially for low literacy and low-bandwidth settings.

## 1.2 What is NOT innovative
- A composite "instability score" from vitals is a **maternity early-warning score**. MEOWS has existed since the 2007 CEMACH report, and NHS England published a **national Maternity Early Warning Score (MEWS)** with RCOG/RCM in 2023–24. Digital MEOWS already ships inside BadgerNet and K2. A new score competing with the national one is a liability, not an innovation.
- "XGBoost plus BERT plus attention fusion" is a standard 2021 Kaggle architecture. Architecture is not a moat; data, validation and workflow are.
- A clinician dashboard with alerts and "suggested actions" is what every vendor shows.
- "Predicting pre-eclampsia" has validated, guideline-backed tools already: Fetal Medicine Foundation first-trimester combined screening; PlGF-based testing (sFlt-1/PlGF ratio) recommended in NICE NG133; fullPIERS for adverse outcomes in confirmed pre-eclampsia. A new model must beat or complement these, not ignore them.

## 1.3 What already exists (KNOWN, verify current status before citing)
| Space | Who | Relevance |
|---|---|---|
| Digital maternity records with early-warning scoring | Clevermed BadgerNet, K2 Medical Systems (Athena/Guardian), Magentus Euroking, Epic Stork | Own the clinical record and MEOWS in most UK units |
| Remote blood-pressure monitoring in pregnancy | Babyscripts (US, at scale with health systems), NHS virtual-ward suppliers (Doccla, Luscii, Current Health), trust-run home BP projects (e.g., Oxford BUMP trials) | The "home monitoring" half of the concept exists; evidence is mixed (see 1.5) |
| Fetal/maternal wearables | Nuvo INVU (FDA-cleared), Bloomlife, Biobeat | Hardware is regulated and capital-intensive |
| Smartphone urinalysis | Healthy.io (CE-marked dipstick reading by phone camera) | The urine-protein input can be bought, not built |
| Voice biomarkers | Kintsugi, Ellipsis Health, Sonde (depression/anxiety) | Some evidence for mental-health screening; none for physiological obstetric deterioration |
| Pre-eclampsia prediction and diagnosis | FMF algorithm; Roche Elecsys sFlt-1/PlGF; Quidel Triage PlGF; fullPIERS | Guideline-recommended; a partner set, not a competitor set |
| Low-resource maternal programmes | mDoc (Nigeria), MomConnect (South Africa), Jacaranda PROMPTS (Kenya), Totohealth | Messaging-first continuity at scale |
| Maternal mental health | Wysa-style tools, perinatal mental-health services, Peanut (community) | Postpartum mental health is the leading cause of late maternal deaths in the UK (MBRRACE) |

## 1.4 Technically difficult
- Fusing irregular, sparse, multi-rate time series (a BP reading every few days, a voice diary when she feels like it, labs monthly) is a hard modelling problem; naive fusion produces confident nonsense.
- Voice features are confounded by device, language, accent, background noise, pregnancy itself (rhinitis, fatigue) and cultural expression; robust extraction across UK and Nigerian populations is research-grade work.
- Rare outcomes: eclampsia, sepsis with organ dysfunction and major haemorrhage are individually rare per pregnancy; a "small pilot cohort" cannot train or validate them. Tens of thousands of pregnancies are needed for calibrated prediction of each.
- Offline-first synchronisation of clinical records with conflict resolution and audit is engineering that most start-ups underestimate.

## 1.5 Scientifically unproven
- **Voice or "emotional biomarkers" predicting pre-eclampsia, sepsis, haemorrhage or thromboembolism:** no published evidence. Stress is associated with adverse outcomes at population level; that is not a prediction signal for an individual acute event.
- **One score for four heterogeneous conditions:** pre-eclampsia is a placental disorder of the second half of pregnancy; haemorrhage is mostly intrapartum/postpartum and acute; sepsis can occur anywhere; VTE risk is assessed with the RCOG scoring tool and managed with prophylaxis. A single "instability" score conflates different physiology, timing and actions. Clinicians will reject it.
- **Home BP monitoring alone improving outcomes:** the Oxford BUMP trials (JAMA 2022) found self-monitoring did **not** significantly speed detection of hypertension or improve BP control versus usual care. The lesson is not "home BP fails" but "the value is in what happens after the reading": escalation, continuity and adherence. Design accordingly.
- **Ethnicity as a model input:** using race as a predictive feature risks encoding bias and is being removed from clinical calculators (eGFR, the VBAC calculator). Ethnicity belongs in **fairness monitoring and outcome auditing**, not as a risk feature, unless a specific, justified, reviewed use exists.

## 1.6 Claims that require evidence
"Early detection of complications", "reduced hospital admissions", "reduced maternal mortality", "mitigation of ethnic disparities", "real-time AI analysis", "actionable score", "completely novel". Each needs a defined outcome, a comparator, a study and, for most, a regulatory pathway.

## 1.7 Claims to remove from investor and partner materials now
- "Predicts pre-eclampsia, sepsis, haemorrhage, thromboembolism" (unvalidated; device-level claim).
- "Reduced hospital admissions and maternal mortality" (no evidence).
- "Completely novel" (it is not; see 1.2 and 1.3).
- "Expand to multiple NHS trusts" as a near-term plan (no trust, no pilot, no DTAC).
- "Black women are 3x more likely to die": use the current MBRRACE-UK figure with the report year (the most recent report I am aware of gives roughly 2.8 times for Black women and 1.7 for Asian women; verify before use).
- "AI analyses data in real time" (nothing is built).

## 1.8 What a clinician would immediately challenge
"Which national guideline does your score map to?" "What does a midwife do with an MIS of 0.62 at 02:00?" "How does this interact with MEWS, which I am mandated to use?" "Who is liable when your alert is wrong, or silent?" "Where is the clinical safety officer and hazard log?" "Why is ethnicity a feature?" "Show me the false-alert rate; alert fatigue kills."

## 1.9 What an NHS innovation team would challenge
DTAC status; DCB0129 clinical safety case; DSPT; interoperability with BadgerNet/K2; NICE Evidence Standards Framework tier and evidence; who the budget-holder is (trust vs ICB vs maternity transformation funding); implementation burden on midwives; equality and health-inequalities impact assessment; whether this duplicates the national MEWS; procurement route (G-Cloud, framework).

## 1.10 What a regulator would challenge
A software product whose intended purpose is to predict or flag risk of specific conditions to inform clinical decisions is a **medical device** in the UK and EU. Under EU MDR Rule 11 it would likely be Class IIa or higher; the UK regime is moving the same way (TO VALIDATE with MHRA guidance current at the time). The MHRA would ask for intended purpose, classification rationale, clinical evaluation, performance data across subgroups, post-market surveillance, and a quality management system (ISO 13485). None exists. Deploying the score clinically without this is unlawful, not merely risky.

## 1.11 What an investor would challenge
No data access, no clinical partner, no entity, no IP agreement, no evidence, a device pathway with 24–36 months and £1–3m before revenue, a crowded remote-monitoring space (Babyscripts), a UK market that is small in pounds, and a team without a clinician or ML lead. Also: why would trusts pay when MEWS is free and BadgerNet already has it?

## 1.12 What a data and privacy expert would challenge
Special-category health data plus ethnicity plus voice (biometric-adjacent) processed for automated risk assessment: lawful basis and Article 9 condition; DPIA mandatory; automated decision-making safeguards (UK GDPR Article 22); data minimisation (why collect socioeconomic index?); voice retention and re-identification risk; cross-border transfer UK–Nigeria; use of patient data for model training (research use requires ethics approval and often section 251 support or explicit consent); vendor sub-processors (cloud AI APIs).

## 1.13 Scores for the CURRENT concept (1–10)
| Dimension | Score | Why |
|---|---|---|
| Clinical value | 4 | Right problem; wrong instrument. A composite AI score duplicates MEWS and cannot be validated at pilot scale. The between-appointment continuity idea has real value that the deck does not articulate. |
| Patient value | 5 | Voice and continuity could matter to women; the deck is clinician-centred and offers women nothing they control. |
| Technical feasibility | 3 | Multimodal fusion on sparse, small data with rare outcomes is not feasible as described. Components are feasible individually. |
| AI defensibility | 2 | Off-the-shelf architecture, no proprietary data, no validation. |
| Data defensibility | 2 | No data. Potential is high if a consented longitudinal cohort is built; none exists. |
| Regulatory feasibility | 2 | As specified, a Class II medical device with no QMS, no evidence and no pathway. Re-scoped, feasibility rises to 6–7. |
| NHS adoption potential | 3 | Duplicates the national MEWS; no DTAC; unclear buyer. Re-scoped as a virtual-ward and continuity service: 6. |
| Commercial potential | 4 | UK maternity software is a small pound market (about 600,000 births a year); value must come from multi-market and multi-payer design. |
| Global scalability | 6 | The continuity and messaging half scales to low-resource settings; the AI half does not. |
| Partnership attractiveness | 5 | Strong social mission; universities and charities will engage; vendors and trusts will not until claims are fixed. |
| Investor attractiveness | 3 | Today: pre-formation with device-level claims. Re-scoped with a pilot and a data strategy: 6–7 for impact and women's-health funds. |
| Competitive differentiation | 3 | "AI early warning" is undifferentiated. Equity-by-design and UK–Africa continuity are differentiators if built. |
| Intellectual property potential | 4 | Software patents are hard in the UK/EU; possible in the US for specific technical methods. Trade secrets, data and trademarks are the realistic IP. |
| Brand potential | 6 | "Materna-Link" is descriptive and warm; the "-Link" suffix is common; the parent brand Vytalix is stronger. |

**Overall: 3.7/10 as a concept, 7/10 as an instinct.** The instinct (continuity, equity, patient-generated signals) is the business. The instrument (a multimodal AI score) is the wrong first product and should be the last.

---

# PART 2 — MAKE IT "NEVER SEEN BEFORE"

## 2.1 The question
What can a system do that today's maternity systems cannot? Today's systems see a woman for minutes at appointments, hold a record the woman cannot carry, stop at six weeks postpartum, treat every woman with the same thresholds, cannot tell who they are failing, and do not learn.

## 2.2 Twenty ambitious ideas
| # | Idea | What is new |
|---|---|---|
| 1 | **Maternity Virtual Ward** for hypertension and high-risk pregnancy: validated home BP cuff + phone urinalysis + structured symptoms + MEWS-aligned escalation with a response SLA | Turns the NHS virtual-ward policy into a maternity service line |
| 2 | **The 365-day postpartum companion**: continuity from birth to one year with mental-health, BP, bleeding, infection and infant-feeding check-ins, and a scheduled GP handover | Nobody owns the postpartum year, where most late maternal deaths occur |
| 3 | **Personal baseline modelling**: each woman's own physiological and behavioural baseline, with deviation-from-self alerts instead of population thresholds | Personalisation that MEWS cannot do; a candidate technical method for patent assessment |
| 4 | **Woman-held continuity record** that follows her across trusts, community, private care and countries (UK ↔ Nigeria) with graduated consent | Portable, interoperable, patient-controlled |
| 5 | **Equity Intelligence**: live, anonymised dashboards for ICBs and ministries showing who is being reached, escalated, seen and missed, by ethnicity, deprivation and geography | Makes MBRRACE-style insight continuous rather than triennial |
| 6 | **Voice-first maternity companion** in Yoruba, Hausa, Igbo, Pidgin, Punjabi, Urdu, Polish: check-ins by voice call or WhatsApp voice notes, transcribed and structured | Reaches women current apps exclude |
| 7 | **Perinatal mental-health signal** from consented voice and text diaries, validated against EPDS/PHQ-9, as a screening prompt for the midwife (not a diagnosis) | The one voice use case with published evidence in adjacent fields |
| 8 | **Phone-camera measurements**: urinalysis strip reading (partner: Healthy.io), oedema and wound photos for postpartum infection review by a clinician | Computer vision as capture, not diagnosis |
| 9 | **Pharmacy as the maternity front door**: BP checks and dipsticks at community pharmacies feed the record; pharmacists escalate through the same queue | New access point; pharmacies already do NHS BP checks |
| 10 | **Emergency-services handover**: when a woman calls 999/112 or arrives at triage, the record's last 72 hours is available instantly with consent | Solves the "arrives with nothing" problem |
| 11 | **Family and partner mode**: partners see warning signs, appointments and how to act; birth companions get a role | Engages the household, safeguarding-aware |
| 12 | **Digital twin of the pregnancy** (research): a longitudinal model of expected trajectories by gestation, used for research and for explaining deviations | Long-term research asset; not a clinical claim |
| 13 | **Trial-ready cohort**: consented women can opt in to be told about relevant studies; pharma and diagnostics companies pay for recruitment and real-world evidence | Revenue that does not depend on NHS budgets |
| 14 | **Pre-eclampsia pathway integration**: FMF screening, PlGF testing, aspirin adherence reminders and home BP unified into one pathway | Complements guideline tools instead of competing |
| 15 | **Medication adherence and safety**: aspirin, iron, antihypertensives, anticoagulants with prompts and pharmacist review | Adherence is the cheap win no one owns |
| 16 | **Community health-worker mode** with USSD/SMS for feature phones and offline tablets | The low-resource layer |
| 17 | **Insurer and employer maternity benefit**: continuity as a covered benefit in private and US markets | Payer diversification |
| 18 | **Infant continuity**: newborn record, feeding, jaundice photos, immunisation prompts, linked to the mother | Extends lifetime value and impact |
| 19 | **Federated learning network** across trusts and countries so models improve without moving data | Data moat with privacy by design |
| 20 | **Open maternal data commons** with universities: a consented, governed research dataset ("a Biobank of pregnancy" for the digital era) | The long-term asset that makes the company hard to replicate |

## 2.3 The best five
### A. Maternity Virtual Ward (hypertension first)
- **What:** a trust-branded remote-monitoring service for women with or at risk of hypertensive disorders: validated BP cuff (Omron, Withings or A&D), urine dipstick via phone camera, structured symptom check-ins, thresholds set by the trust aligned to national MEWS and NICE NG133, an escalation queue with a response SLA, and GP/community handover.
- **Why different:** it is a service line with a clear budget (NHS virtual-ward funding and maternity safety funding), not a score. It uses validated inputs and guideline thresholds, so it is a decision-support tool under clinical governance rather than a predictive device on day one.
- **Why no one dominates:** general virtual-ward vendors lack maternity workflows; maternity record vendors lack home monitoring; Babyscripts is US-centric.
- **Technical:** device integration (Bluetooth/SDK), offline-first app, rules engine, FHIR interfaces to BadgerNet/K2, SMS fallback.
- **Clinical:** obstetric hypertension pathway owner, clinical safety officer, midwifery workflow design, escalation SLAs, training.
- **Regulatory:** the app displaying readings and rule-based escalation configured by the trust is decision support; classification must still be assessed (likely Class I or "not a device" if no interpretation; TO VALIDATE). BP devices carry their own certification.
- **Data:** BP, urine protein, symptoms, medications, appointments, escalation outcomes.
- **Partners:** one trust with a hypertension clinic; Health Innovation Network; device supplier; Healthy.io; NPEU/Oxford for evaluation design.
- **Revenue:** £40k–£90k pilots; £18–£36 per woman per year plus site licence; ICB-level contracts.
- **Defensibility:** workflow integration, evidence, escalation data, trust relationships.
- **Global:** the same design with cheaper cuffs and SMS in Nigeria and Kenya.

### B. The 365-day postpartum companion
- **What:** continuity from discharge to one year: scheduled check-ins on mood (EPDS-aligned prompts), BP after hypertensive pregnancy, bleeding, infection, pain, feeding, contraception, and a structured handover to the GP at 6–8 weeks and beyond; escalation to perinatal mental-health teams by rule.
- **Why different:** maternity care ends at 10–28 days for midwives; the year after is a gap where mental-health deaths cluster. No vendor owns it.
- **Why no one dominates:** the budget is split between maternity, primary care and mental health; a continuity product can be bought by the ICB rather than any one of them.
- **Technical:** app plus SMS/WhatsApp; rule engine; GP record integration (GP Connect, TO VALIDATE); mental-health service referral routes.
- **Clinical:** perinatal psychiatry and health-visiting input; safeguarding design; crisis routing.
- **Regulatory:** screening prompts using validated questionnaires are decision support; careful intended-use wording.
- **Data:** longitudinal postpartum data, largely absent from any dataset today.
- **Partners:** ICB perinatal mental-health leads, health-visiting services, Tommy's, Maternal Mental Health Alliance, a university (King's, Manchester).
- **Revenue:** per woman per year (£10–£20); ICB contracts; employer benefit.
- **Defensibility:** unique dataset; integration across three services.
- **Global:** postpartum follow-up is the weakest link in most systems; SMS-first version travels.

### C. Woman-held continuity record with graduated consent
- **What:** a portable maternity record the woman controls, readable by any care setting with her consent (QR, NHS login, or code), synchronising with the provider's system where one exists and standing alone where none does. Consent tiers: care, safety escalation, research, sponsorship.
- **Why different:** records today belong to institutions; women who move, migrate or use private and public care fall between them.
- **Why no one dominates:** interoperability is unglamorous and requires standards work; incumbents are institution-centric.
- **Technical:** FHIR UK Core resources, offline cache, identity verification, audit; integration engine.
- **Clinical:** minimum dataset agreed with RCOG/RCM; safety of partial records.
- **Regulatory:** record-keeping software; data-protection heavy; not a device.
- **Data:** the backbone for everything else.
- **Partners:** NHS England interoperability leads, PRSB (standards), trusts, Nigerian teaching hospitals.
- **Revenue:** platform licence; integration fees; programme contracts.
- **Defensibility:** each interface built raises switching costs; consent architecture is hard to copy.
- **Global:** the primary product for Africa (records that follow women between community and facility).

### D. Equity Intelligence for commissioners and ministries
- **What:** anonymised, continuous indicators of reach, engagement, escalation, response time and outcomes by ethnicity, deprivation and geography, with alerts when a group is being under-served; published as reports first, then a product.
- **Why different:** current equity insight is triennial (MBRRACE) and retrospective; this is monthly and actionable.
- **Why no one dominates:** requires patient-level continuity data across settings, which only a continuity layer holds.
- **Technical:** analytics warehouse, small-number suppression, differential privacy where needed.
- **Clinical:** definitions agreed with public-health and maternity leads.
- **Regulatory:** anonymisation standards (ICO code); not a device.
- **Data:** derived from A–C.
- **Partners:** ICBs, NHS Race and Health Observatory, Five X More, LMNS boards, state ministries.
- **Revenue:** commissioner subscriptions (£20k–£60k per ICB per year); report sponsorship.
- **Defensibility:** data and credibility.
- **Global:** the same layer for state programmes and donors who must report equity.

### E. The consented longitudinal maternal cohort (data flywheel)
- **What:** women using A–C can opt in to a governed research cohort; multimodal, longitudinal, diverse (UK and Nigeria); access for universities and, under strict rules, industry; the basis for any future predictive model.
- **Why different:** existing cohorts are small, single-country or historic; a diverse digital cohort with postpartum follow-up does not exist.
- **Why no one dominates:** it takes years and trust; it is not a product feature.
- **Technical:** research environment (trusted research environment model), de-identification, federated access.
- **Clinical/ethical:** ethics approvals, participant panels, benefit-sharing.
- **Regulatory:** research governance (HRA), not device law until a model is deployed.
- **Data:** everything above plus optional wearables and voice.
- **Partners:** NPEU, King's, UCL, Liverpool, Born in Bradford, HDR UK, Nigerian universities.
- **Revenue:** research licences, grant-funded studies, pharma real-world evidence, trial recruitment.
- **Defensibility:** the strongest long-term moat in the plan.
- **Global:** by design.

**The AI score from the 2025 deck lives inside E, not on the roadmap of A.**

---

# PART 3 — REDEFINE THE PRODUCT

## A. Ultimate vision (10 years)
The continuity and intelligence layer for pregnancy and the year after birth, used by health systems on three continents: every woman keeps one record that follows her, is never out of contact with a responsible human, is monitored at home with validated devices when her risk warrants it, is supported for a year after birth, and contributes, if she chooses, to a research cohort that makes care safer and fairer for the next woman. Predictive models exist, are validated, regulated and explainable, and are the last thing built rather than the first.

## B. Core product (years 1–3)
**MaternaLink Continuity**: registry and woman-held record; offline-first capture; daily and weekly check-ins; symptom and medication logs; validated home BP and phone urinalysis integration; rule-based escalation aligned to national MEWS and configured by the provider; escalation queue with SLA; notes, exports, integrations; postpartum year; equity analytics; consent tiers; EN/FR plus local languages.

## C. First MVP (see Part 13)
A **maternity virtual ward for hypertension** at one trust plus a **community continuity cohort** with one NGO in Nigeria, on the same codebase.

## D. 12-month roadmap
| Quarter | Deliverables |
|---|---|
| Q4 2026 | Entity, IP, intended-use statement, prototype audit, MVP build start, one trust and one NGO LOI, DPIA, hazard log, Cyber Essentials |
| Q1 2027 | MVP live in service evaluation (UK) and cohort (Nigeria); BP device integration; escalation SLA reporting; first equity report |
| Q2 2027 | Postpartum module v1; BadgerNet/K2 interface scoping; DTAC evidence pack; NICE ESF evidence plan; research cohort protocol to ethics |
| Q3 2027 | Evaluation read-out; second trust; ICB conversation with equity dashboard; grant-funded feasibility study; seed round preparation |

## E. 3-year roadmap
Year 1: continuity plus virtual ward, two UK sites, one Nigerian programme, evidence. Year 2: postpartum year, five to eight UK sites, two African programmes, equity product for two ICBs, research cohort open, seed round. Year 3: interoperability at scale, first personalised-baseline decision-support features under a documented device pathway, US or EU partner pilot, Series A.

## F. 5-year vision
Fifty UK maternity services, ten programmes across Africa, a research cohort of 250,000+ pregnancies, a regulated predictive module for hypertensive disorders, and equity intelligence used by national bodies.

## G. New product architecture
```
PATIENT  → the woman (and consented partner/companion), community health worker, midwife, pharmacist
   ↓
DATA     → validated devices (BP, urine, weight), structured check-ins, symptoms, medications, voice/text diaries, appointments, clinical record extracts (FHIR), social context she chooses to share; consent tier recorded on every item
   ↓
AI       → (1) capture intelligence: transcription, translation, structuring of free text and voice; (2) quality: outlier and device-error detection; (3) research models in the cohort environment only
   ↓
RISK ENGINE → deterministic, provider-owned rules aligned to national MEWS/NICE thresholds; personal-baseline deviation flags (v3, under device pathway); every rule has an owner, rationale, version and review date
   ↓
CLINICAL INTELLIGENCE → the escalation queue: who, what, why (explainable rule text), by when (SLA); context pack for the clinician (last 72 hours, trend, medications); never a treatment recommendation
   ↓
ACTION   → contact, review, test, referral, visit, admission; logged with time-to-action; woman informed; partner prompted where consented
   ↓
OUTCOME  → what happened (clinical outcome, admission, birth, postpartum events) captured from record and check-ins; equity slices
   ↓
LEARNING LOOP → rule performance (sensitivity, alert burden, time-to-action) reviewed monthly by the provider's clinical lead; cohort research improves models; validated improvements re-enter the risk engine only through the regulated pathway
```

---

# PART 4 — CREATE A NEW CATEGORY

| # | Category | Definition | Why large | Products beneath | Hard to replicate because | How we own it |
|---|---|---|---|---|---|---|
| 1 | **Maternal Continuity Infrastructure** | The record, channel and escalation layer that keeps every pregnant and postpartum woman connected to care across settings and countries | 130m births a year; continuity gaps are universal | Record, check-ins, virtual ward, postpartum, integrations | Interfaces, consent architecture, multi-setting trust | Define the standard, publish the minimum dataset, ship the integrations |
| 2 | **Perinatal Virtual Care** | Home-based, device-supported maternity care as a service line | NHS virtual-ward policy; US remote monitoring reimbursement | Virtual ward, devices, escalation | Clinical workflow depth | Own the hypertension pathway first |
| 3 | **The Postpartum Year** | Care and monitoring from birth to 12 months as its own category | Late maternal deaths; mental health; no incumbent | Postpartum companion, GP handover, mental-health routing | Cross-service integration | Name it, publish the evidence, sell to ICBs |
| 4 | **Equity Intelligence for Maternity** | Continuous measurement of who care reaches and fails | Policy mandate in UK; donor reporting globally | Dashboards, reports, alerts | Needs patient-level continuity data | Publish first, product second |
| 5 | **Woman-Held Health Records** | Patient-controlled, portable records starting with pregnancy | Portability across systems and borders | Record, consent tiers, identity | Standards work, trust | Start with maternity, extend to child and women's health |
| 6 | **Maternal Safety Operations** | The operational layer (queues, SLAs, audits) for maternity safety programmes | Every safety review demands it | Escalation queue, SLA analytics, audit | Workflow lock-in | Sell to safety leads and LMNS |
| 7 | **Community Maternal Care Platforms** | Tools for community health workers and midwives in low-resource settings | Where most births and deaths are | Offline app, USSD/SMS, training | Field-hardened design | Nigeria, Kenya, Ghana first |
| 8 | **Perinatal Research Infrastructure** | Consented digital cohorts and trusted research environments for pregnancy | Pharma, diagnostics and academia lack diverse longitudinal data | Cohort, TRE, recruitment | Years of consent and trust | University consortium |
| 9 | **Maternal Digital Twin** | Personal trajectory models for pregnancy | Long-term research and personalisation | Baseline models, explanations | Data and validation | Research first |
| 10 | **Life-course Women's Health Continuity** | Pregnancy as the entry to a lifelong continuity record (menopause, cardiovascular risk after pre-eclampsia) | Pre-eclampsia doubles later cardiovascular risk; no one follows up | Post-pregnancy cardiovascular follow-up | Longitudinal data | Extend from the postpartum year |

**Selected category: Maternal Continuity Infrastructure**, with Perinatal Virtual Care as the first commercial wedge and The Postpartum Year as the second. It is large, it is not what incumbents sell, it is regulator-safe on day one, and it produces the data that makes every later category (equity, research, prediction) possible.

---

# PART 5 — BUSINESS MODEL

## Who should pay (and who should not)
| Payer | Pays for | Willingness | Verdict |
|---|---|---|---|
| NHS trusts (maternity, digital budgets) | Virtual ward, continuity licence, integration | Medium; budgets tight; virtual-ward and safety funding help | Primary UK buyer year 1–2 |
| Integrated Care Boards | Postpartum year, equity intelligence, cross-provider continuity | Medium–high for inequality outcomes | Primary UK buyer year 2–3 |
| Private maternity providers and hospitals (UK, Gulf, Nigeria) | Premium continuity and virtual care | High per patient, small volume | Early revenue, good margins |
| Governments and state programmes (Africa) | Programme deployment, training | Low per woman, high volume, slow | Year 2+, via implementers |
| Donors and global-health funders | Programme costs, evaluation | High for evidence-generating pilots | Year 1–2 |
| Insurers and employers | Maternity benefit, continuity | Medium (UK), high (US) | Year 2–3 |
| Pharma and diagnostics | Trial recruitment, real-world evidence, adherence programmes | High, but only with a consented cohort | Year 2+ |
| Universities and research funders | Cohort access, studies | Grant-funded | Year 1+ |
| Patients | Nothing essential | Sponsors (diaspora, employers) may pay for others | Never the woman herself for safety features |

## Five revenue models
1. **Enterprise platform licence + per-woman fee** (trusts, hospitals, programmes): predictable, scales with births.
2. **Virtual-ward service fee** per enrolled high-risk woman per month, including device logistics: aligns with NHS virtual-ward economics.
3. **Commissioner subscription** (ICBs, ministries) for the postpartum year and equity intelligence: cross-provider value.
4. **Outcome-linked component** (10–25% of fee) tied to auditable process indicators (time-to-contact, postnatal completion, BP follow-up completion): buyer-friendly, evidence-generating.
5. **Research and evidence licensing**: cohort access, trial recruitment, real-world evidence for pharma and diagnostics; plus **sponsorship** revenue (diaspora and employer per-woman sponsorship in Africa).
Also: integration and implementation fees; training and e-learning; white-label for NGOs and insurers; API access for approved partners.

## Strongest model
**Enterprise licence + per-woman fee, sold first as a maternity virtual ward to trusts, then as a postpartum and equity subscription to ICBs, with an outcome-linked slice and research licensing layered on from year 2.** It matches how the NHS buys, produces evidence as it earns, and creates the dataset that funds the research line.

---

# PART 6 — PARTNER ECOSYSTEM

| Tier | Category | Why we need them | What we offer | What we ask | What they get | Approach | Stage | NDA? | Instrument |
|---|---|---|---|---|---|---|---|---|---|
| **1 Foundational** | One NHS trust maternity service (hypertension pathway) | Without a clinical home there is no product, evidence or credibility | A no-fee or low-fee service evaluation, configured to their pathway, with all safety artefacts | A named clinical lead, a midwifery lead, Caldicott sign-off, 100–300 women, evaluation co-authorship | First-mover recognition, a virtual-ward capability, publication | Via Health Innovation Network and a warm introduction to the obstetric hypertension lead | Now | Mutual NDA before data discussions; not before the first conversation | Service-evaluation agreement + data-sharing agreement |
| 1 | One African implementing NGO with a maternal programme | Low-resource validation and the second market | Free platform for a cohort, training, evaluation design | A cohort of 500–2,000 women, community health workers, ethics support | Better continuity data for their funders | Through programme directors and country leads | Now | Yes, mutual | MoU + evaluation protocol |
| 1 | Clinical safety officer and regulatory adviser | Nothing ships without them | Fractional retainer, equity in the option pool | Ownership of hazard log, intended use, classification opinion | Founding-team role | Referral via RCM/RCOG networks and Health Innovation Networks | Now | Contract | Consultancy agreement |
| 1 | A university perinatal research group | Evidence design, ethics, credibility, the cohort | Data access, co-investigator role, joint grant bids | Evaluation design, ethics sponsorship, PhD/fellow time | Publications, data, grant income | Directly to the professor leading maternal-health digital research | Now | Yes | Research collaboration agreement |
| **2 Technology** | Validated BP device makers (Omron, Withings, A&D) | Home readings must be from validated devices | Volume channel, integration showcase | SDK/API access, device pricing, loan stock for pilots | New channel into maternity | Partnerships or medical-channel managers | Month 2 | Standard | Supply and integration agreement |
| 2 | Smartphone urinalysis (Healthy.io) | Urine protein at home without building CV | Integration in a maternity pathway | API and per-test pricing | Maternity use case | BD lead | Month 3 | Standard | Commercial |
| 2 | Cloud (AWS, Microsoft Azure, Google Cloud) | Hosting, credits, health-data compliance | A reference health-tech start-up | Start-up credits, architecture review, UK-region compliance support | Case study | Start-up programmes | Month 1 | No | Credits agreement |
| 2 | Interoperability (FHIR integration engines, NHS APIs; maternity record vendors) | Data must flow to the legal record | Complementary product; joint customers | Interface specs, sandbox, partner listing | Extended value for their customers | Product partnership managers at Clevermed, K2, Magentus | Month 4–6 | Yes | Partner/interface agreement |
| 2 | Messaging (Twilio, Africa's Talking, Meta WhatsApp Business partners) | SMS/WhatsApp channels | Volume | Pricing, sandbox, compliance support | Volume | Self-serve then account manager | Month 2 | No | Commercial |
| 2 | Cybersecurity and assurance (Cyber Essentials body, pen-test firm, DSPT consultant) | Assurance evidence | Repeat work | Fixed-price packages | Revenue | Direct | Month 2 | Standard | Commercial |
| 2 | Voice/speech (transcription and translation APIs; academic speech labs) | Voice capture in many languages | Real-world multilingual maternity use case | On-device or UK-hosted options, language coverage | Data and case study | Direct | Month 6 | Yes | Commercial/research |
| **3 Clinical** | Additional trusts, private maternity providers, Nigerian teaching hospitals | Scale, diversity, evidence | Service evaluations, fair pricing | Sites, clinicians, data | Capability and evidence | Through the first site's clinicians and networks | Month 6+ | Yes | Service evaluation → commercial |
| 3 | Royal Colleges (RCOG, RCM), professional networks (digital midwives) | Legitimacy, guideline alignment | Alignment with national MEWS, training content | Review, endorsement of process (not product), events | Member value | Policy and innovation leads | Month 3 | No | Engagement, not contract |
| **4 Data** | NPEU/MBRRACE-UK, Born in Bradford, ALSPAC, HDR UK, NHS England data services | Validation data, benchmarks, methods | Prospective digital data; co-analysis | Access under governance, methods advice | New data flows | Directors and data-access committees | Month 6–12 | Yes | Data access agreements |
| 4 | Nigerian data partners (teaching hospitals, DHIS2 programmes) | Low-resource validation | Tools and training | Cohort data under ethics | Capability | Through implementers | Month 6 | Yes | Research/data agreement |
| **5 Commercial** | Health Innovation Networks, NHS Innovation Service, G-Cloud, procurement frameworks; NGO implementers; telecoms in Africa | Distribution into buyers we cannot reach alone | Evidence, a compliant product | Introductions, listings, bundling | Innovation adoption targets; new services | Innovation exchange leads; partnerships directors | Month 2 (HIN) / Month 9 (frameworks) | No | Listing/reseller agreements |
| **6 Strategic/corporate** | Diagnostics and pharma with maternal programmes (Roche Diagnostics, MSD for Mothers, Ferring, Organon), insurers (Bupa, AXA Health), telecoms (MTN, Airtel, Vodafone), device companies (Philips) | Capital, distribution, credibility, adherence and RWE programmes | Access to a consented cohort and pathway | Programme funding, co-development, pilots | Evidence, reach, ESG outcomes | Medical affairs, market access and partnerships leads | Month 9+ (after evidence) | Yes | Co-development / commercial |
| **7 Funding** | Angels and syndicates, women's-health and impact VCs, Innovate UK, SBRI Healthcare, NIHR i4i, Wellcome, Grand Challenges Canada, Gates, MSD for Mothers | Capital staged to evidence | A credible plan and data room | Pre-seed, grants, then seed | Returns, impact | See `/investors/` | Month 3+ | No | Investment / grant |

# PART 7 — PARTNER TARGET LIST (74 organisations)
The full list with all ten fields is in `investors/partners/PARTNER_TARGET_LIST.csv` and the Excel war room. Priorities (score /10) in summary:

**UK (priority 8–10):** Oxford University Hospitals + Oxford Nuffield Department of Primary Care (home BP research) · Guy's and St Thomas' · King's College Hospital + King's Department of Women & Children's Health · Imperial College Healthcare + Imperial · Birmingham Women's and Children's · Liverpool Women's + University of Liverpool · Manchester University NHS FT (Saint Mary's) + Tommy's Manchester centre · Leeds Teaching Hospitals · UCLH + UCL Institute for Women's Health · NPEU (Oxford; MBRRACE-UK) · Health Innovation Oxford & Thames Valley · Health Innovation Network South London · Health Innovation Manchester · Health Innovation West Midlands · NHS England Maternity and Neonatal programme · NHS Race and Health Observatory · RCOG · RCM · Tommy's · Five X More · Birthrights · Wellbeing of Women · Maternal Mental Health Alliance · Sands · PRSB · HDR UK · Born in Bradford · Clevermed (BadgerNet) · K2 Medical Systems · Magentus (Euroking) · Healthy.io · Omron Healthcare UK · Withings · Bupa · AXA Health · Microsoft UK / AWS / Google Cloud start-up programmes · Vodafone Business.
**Europe:** Philips (Netherlands) · Erasmus MC (Rotterdam) · Karolinska (Stockholm) · Nina Capital · Heal Capital · EIT Health.
**US:** March of Dimes · Babyscripts (benchmark, potential partner) · Mayo Clinic Platform · Rock Health · NIH NICHD (data) · Maven Clinic.
**Africa and global:** mDoc (complementarity partner in Nigeria) · Jacaranda Health · Praekelt (MomConnect) · Lagos State Ministry of Health · NPHCDA · SOGON · MTN Nigeria · Airtel Africa · Safaricom · PATH · Jhpiego · Society for Family Health · UNICEF Nigeria · WHO AFRO · Gates Foundation · MSD for Mothers · Grand Challenges Canada · Fondation Botnar · CIFF.

Decision-maker titles are given per organisation in the CSV (for example: Consultant Obstetrician and Clinical Lead for Hypertension in Pregnancy; Head of Midwifery; Chief Clinical Information Officer; Director of Innovation; Head of Research; Country Director; Head of Medical Affairs; Head of Partnerships).

# PART 8 — THE "IMPOSSIBLE PARTNERSHIP" EXERCISE
1. **NHS England (Maternity and Neonatal programme) + NPEU:** national MEWS alignment, equity measurement and evaluation design. Would make MaternaLink the reference continuity layer for the national safety agenda and give access to MBRRACE methodology. Transformational because it removes the "duplicates MEWS" objection and creates policy pull.
2. **Roche Diagnostics (pre-eclampsia PlGF testing):** a joint hypertension pathway where home BP and symptoms decide who is tested, and test results flow into the record. Transformational because it attaches a guideline-backed diagnostic to the pathway, brings market-access muscle and credibility in every NHS trust and export market.
3. **Gates Foundation or MSD for Mothers with a Nigerian state programme and mDoc as the incumbent partner:** funds the low-resource validation at scale, positions MaternaLink as the interoperable continuity layer beneath existing programmes rather than a competitor. Transformational for reach and for the cohort.
4. **Microsoft (UK Health) or Google Health with a university partner:** federated learning infrastructure, speech in African and South Asian languages, credits and go-to-market. Transformational for the AI and voice layer without building infrastructure.
5. **Bupa (UK, plus its international provider network):** the postpartum year and continuity as a covered maternity benefit across the UK, Gulf and other markets. Transformational because it creates a private payer at scale and a bridge to insurers globally.
(Runner-up: a UK telecom such as Vodafone with its African operations, for zero-rated maternity messaging.)

# PART 9 — DATA MOAT
**Collect (with tiered consent):** enrolment and consent events; appointments and attendance; validated device readings with device identity; structured check-ins and symptoms; medications and adherence prompts; escalation events and time-to-action; clinician notes (in the provider's record where one exists); outcomes (from record and check-ins); postpartum year events; language, channel and access data (to measure equity); optional research-tier voice and text diaries; optional wearable data.
**Never collect:** ethnicity or socioeconomic proxies as predictive features (collect ethnicity only for equity monitoring, with explicit purpose); free-text on partners' conduct without a safeguarding pathway; biometric identifiers beyond what authentication needs; location tracking; data from women who have not consented to the tier in question; anything "because it might be useful later".
**How data improves models:** rule performance (sensitivity, specificity, alert burden per rule per site) → rule tuning by clinical leads; longitudinal baselines → personal-deviation research; postpartum outcomes → the first credible dataset for late complications; multilingual diaries → speech and NLP research under ethics.
**Longitudinal datasets:** enrol at booking, follow to 12 months postpartum, link to child immunisation prompts; retain de-identified research copies under the cohort governance; re-contact consent for follow-up studies.
**Proprietary datasets:** the escalation and response dataset (what was flagged, what happened, how fast) and the postpartum-year dataset do not exist elsewhere; multi-country diversity (UK and Nigeria) is rare.
**Avoiding exploitation:** benefit-sharing (results returned to participants and communities), a participant panel, no sale of identifiable data ever, industry access only to de-identified, purpose-limited analyses in a trusted research environment, transparent registers of data use.
**Privacy protection:** data minimisation, pseudonymisation at source, encryption, role-based access, break-glass logging, UK residency for UK data, in-country options for Nigeria, DPIA per deployment, retention schedules, independent audit.
**Consent architecture:** four tiers (care; safety escalation; research; sponsorship visibility), each separately revocable, recorded on every data item; plain-language and voice consent; partner access controlled by the woman.
**Hard to replicate:** interfaces to record systems, the escalation-response dataset, the postpartum cohort, and the trust of clinicians and communities, accumulated over years.

**The MaternaLink data flywheel:** more sites → more continuity data → better rule performance and equity insight → better outcomes and evidence → more sites and commissioners → a larger consented cohort → validated research models → regulated decision support → higher value per woman → more sites.

# PART 10 — AI MOAT
**Use existing infrastructure for:** cloud, transcription and translation base models, OCR for dipsticks (partner), speech-to-text, standard ML tooling, federated-learning frameworks, monitoring.
**Make proprietary:**
1. **The escalation-response model**: predicting which flags need faster contact given site capacity and history (operational, not diagnostic; lower regulatory burden).
2. **Personal-baseline temporal modelling**: deviation-from-self for BP, symptoms and engagement, with explanations; the candidate for the first regulated module.
3. **Multilingual maternity language models** fine-tuned on consented diaries for structuring, not diagnosis.
4. **Fairness monitoring**: subgroup performance dashboards, drift detection, alert-burden equity.
5. **Clinical reasoning layer**: rule-text explanations, context packs, and audit of clinician actions to learn which flags mattered.
6. **Continual and federated learning pipelines** across sites and countries with governance gates; models retrained only through documented change control.
7. **Human-in-the-loop by design**: every model output is a prompt to a human with a recorded decision; that decision is training signal.
Rules for the moat: models never ship without subgroup validation; explainability is a product feature; the AI roadmap follows the data flywheel, not the pitch deck.

# PART 11 — REGULATORY REALITY CHECK (UK)
| Stage | What it is | Governance | Timing (ESTIMATE) |
|---|---|---|---|
| IDEA → PROTOTYPE | Continuity platform; rule-based escalation configured by the provider; no interpretation | Intended-use statement; DPIA; DCB0129 clinical safety case; Cyber Essentials; DSPT; hazard log; classification assessment documented (likely not a device or Class I as record-keeping and provider-configured rules; TO VALIDATE with MHRA guidance) | Months 0–4 |
| RESEARCH | Cohort studies, model development in a research environment | HRA/REC ethics approval via IRAS; research governance; no clinical deployment of models | Months 4–24 |
| PILOT | Service evaluation at a trust (not research), then feasibility studies | Trust governance, Caldicott, DTAC evidence pack, NICE ESF Tier A/B evidence plan, evaluation registered | Months 4–12 |
| VALIDATION | Prospective validation of any predictive module across subgroups | Clinical investigation under MHRA rules if the module is a device; ISO 14155-style conduct | Months 18–36 |
| REGULATORY | UKCA marking of the predictive module as SaMD (likely Class IIa or higher under the forthcoming UK regime aligned with EU MDR Rule 11; TO VALIDATE); QMS ISO 13485; post-market surveillance; MHRA AI Airlock sandbox as an option | Notified/approved body engagement | Months 24–40 |
| NHS DEPLOYMENT | Procurement via framework; DTAC pass; clinical safety case DCB0160 by the deploying trust; AI governance (explainability, human oversight, bias monitoring, incident reporting) | Ongoing | Month 12 (continuity) / Month 36+ (predictive module) |
**Distinguish clearly:** *Research tool* (cohort environment; no patient-facing outputs) · *Decision-support tool* (displays data, applies provider-owned rules, explains; may still be a device depending on claims; keep claims to workflow) · *Clinical software* (record-keeping, communication; data-protection and clinical-safety governed) · *Medical device/SaMD* (any output that predicts, diagnoses or recommends for an individual; full pathway).

# PART 12 — CLINICAL VALIDATION
**Study 1 (year 1): a service evaluation, then a feasibility study, of the Maternity Virtual Ward for hypertensive disorders.**
- **Participants:** pregnant women ≥ 20 weeks with chronic hypertension, gestational hypertension, or high risk of pre-eclampsia per NICE NG133, plus postpartum women with hypertensive disorders up to 6 weeks; at one trust; community and clinic settings.
- **Sample size:** service evaluation 100–150 women (descriptive); feasibility study 200–300 to estimate recruitment, adherence, escalation rates and time-to-action with adequate precision; a later effectiveness trial would need ~1,500–3,000 women for process outcomes and far more for rare clinical outcomes (statistician to confirm).
- **Inclusion/exclusion:** able to consent; smartphone or SMS access (or supported alternative); excludes women already under inpatient care; language support provided rather than exclusion.
- **Data:** home BP (validated cuff), urine protein (phone dipstick or clinic), symptoms, medications, appointments, escalations, actions, admissions, birth outcomes, satisfaction, midwife time.
- **Primary endpoint (feasibility):** proportion of clinically significant readings (above trust thresholds) with documented clinician contact within the agreed SLA (e.g., 4 hours).
- **Secondary:** adherence to monitoring schedule; time from reading to contact; unplanned attendances; admissions; antenatal appointments saved; women's and midwives' experience; equity of reach and response by ethnicity and deprivation; safety events; alert burden per midwife.
- **Bias analysis:** subgroup reporting by ethnicity, deprivation, language, age, BMI; missingness analysis; device access.
- **Safety monitoring:** hazard log, incident reporting, clinical safety officer review weekly, stopping rules.
- **Comparator:** usual care (historical controls for the evaluation; concurrent control site or stepped-wedge for the feasibility study).
- **Success:** ≥ 80% adherence; ≥ 90% of significant readings contacted within SLA; no safety signal; equitable reach; midwives willing to continue; a publishable evaluation; a trust that wants to renew.
**What makes a trust take you seriously:** a clinical safety case, a DTAC evidence pack, a named clinician co-author, an evaluation protocol reviewed by a university, subgroup data, and a price that maps to a budget they already have.

---

# PART 13 — MVP (limited funding)
**The smartest first product:** the **Maternity Virtual Ward for hypertension** at one UK trust, sharing a codebase with a **community continuity cohort** in Nigeria. It is buildable in 16–20 weeks, produces evidence a trust and an investor both value, creates the escalation-response dataset, and is the wedge into the continuity platform.

| Item | Specification |
|---|---|
| **Features** | Enrolment and consent tiers; woman app (PWA) and SMS fallback; validated BP cuff pairing (Bluetooth) with manual entry; phone dipstick via partner API (or manual entry in MVP); symptom and medication check-ins; provider-configured thresholds aligned to national MEWS/NICE; escalation queue with SLA timers and contact logging; timeline and notes; exports; equity report; audit log; EN plus one local language |
| **Tech stack** | TypeScript/Next.js PWA; Node (NestJS) API; PostgreSQL; Redis; object storage; Auth0 or Keycloak; AWS eu-west-2 (UK); Twilio/Africa's Talking; FHIR export; Terraform; observability; automated tests; no patient data to third-party AI |
| **Team** | Founder (product/commercial), fractional CTO/lead engineer, one full-stack engineer, one mobile/front-end engineer (contract), clinical safety officer (fractional), midwifery adviser (sessional), designer (contract), evaluation lead (university partner) |
| **Timeline** | Weeks 1–4 discovery, intended use, DPIA, hazard log, design; weeks 5–14 build; weeks 15–18 testing, Cyber Essentials, safety case, training; weeks 19–20 go-live; 12-week evaluation thereafter |
| **Cost range (ESTIMATE)** | £140k–£260k to first evaluation read-out (UK-led build), or £95k–£180k with a blended UK/Nigeria team; devices £8k–£15k for 100 women; assurance £10k–£20k |
| **Partners** | One trust; Health Innovation Network; university evaluation partner; BP device supplier; Healthy.io (optional in MVP); one Nigerian NGO; cloud credits |
| **Pilot** | 100–150 women over 12 weeks at the trust; 500 women in the Nigerian cohort; weekly service reviews; evaluation report at week 16 |
| **Success metrics** | ≥ 80% monitoring adherence; ≥ 90% significant readings contacted within SLA; median time-to-contact under 2 hours; zero unmitigated safety incidents; equitable reach; NPS ≥ 40 among midwives; trust renewal intent; investor-ready evidence pack |

# PART 14 — PARTNER PITCH
**One sentence:** "We keep every pregnant and postpartum woman connected to a responsible clinician between appointments, with home readings and rules your own team sets, and we measure who care reaches and who it misses."
**30 seconds:** "Most maternal harm happens between appointments, and after discharge, where today's systems are blind. MaternaLink is a continuity layer: home blood-pressure and symptom monitoring, escalation rules your clinicians own, a queue with a response time, and a record that follows the woman for a year after birth. It works offline and on any phone, and it reports equity of reach by ethnicity and deprivation. We're inviting one maternity service to co-design and evaluate the first hypertension virtual ward with us, with a university evaluation partner and the safety artefacts done properly."
**2 minutes:** add the honest status (pre-seed, prototype under audit, no claims), the evidence plan (service evaluation → feasibility → validation), what you ask (a clinical lead, 100–150 women, 12 weeks), what they get (a working virtual ward, co-authorship, first-mover access, no licence fee for the evaluation), why now (national MEWS, virtual-ward policy, inequality mandate, MBRRACE findings), why you (Vytalix's discipline: intended use, hazard log, DPIA before code; UK–Africa design), what it could become (the continuity infrastructure for maternity, with research and equity intelligence built on top).
**Partnership email (trust clinical lead):** Subject: Co-designing a hypertension virtual ward for [Trust] maternity, 12-week evaluation. Dear Dr [Name], I'm the founder of Vytalix, a UK health-technology group. We are building MaternaLink, a continuity and home-monitoring layer for maternity. Rather than sell you software, I'd like to co-design and evaluate a hypertension virtual ward with your team: validated home BP, symptom check-ins, escalation thresholds you set, a queue with a response time, and equity reporting, evaluated with [university] and with the clinical safety case and DPIA done first. No licence fee for the evaluation; we ask for a clinical lead, midwifery time and 100–150 women. Could we have 20 minutes? Honest status: we are pre-seed and have not yet deployed in the NHS. [Signature]
**LinkedIn (under 300 characters):** "Dr [Name], I'm building a maternity continuity and home-monitoring layer (home BP, symptom check-ins, escalation rules your team owns, equity reporting). Looking for one clinical lead to co-design a 12-week evaluation. May I send a one-pager?"
**WhatsApp (warm introductions only, never cold):** "Hi [Name], [Introducer] suggested I reach out. I'm building MaternaLink, a continuity layer for maternity: home BP monitoring plus escalation rules the team owns, and postpartum follow-up. We're looking for a first evaluation site. Could I send a one-page summary and find 20 minutes next week?"
**Meeting opening:** "Thank you for the time. I'd like to leave with two things: your view on whether the between-appointment gap is where you lose women, and whether an evaluation like this could fit your pathway. I'll be honest about where we are, and I'd rather hear your objections now than in six months."
**Proposal structure:** 1 Context and the gap (their data, their words) · 2 What we propose (pathway, features, thresholds owned by them) · 3 Safety and governance (intended use, hazard log, DPIA, DTAC plan) · 4 Evaluation design and co-authorship · 5 What we ask · 6 What they get · 7 Timeline · 8 Costs (evaluation fee or none; device costs) · 9 What happens after (commercial terms, no obligation) · 10 Appendices (security, data flows, consent materials).
**Why us / why now / why you / why it matters / what we want / what you get / what it could become** are answered in that order in every pitch.

# PART 15 — PARTNER OFFER (founding packages)
| Package | Role | Contribution | Benefits and recognition | Access | Commercial | Equity? | Exclusivity |
|---|---|---|---|---|---|---|---|
| **Founding Clinical Partner** (1–3 UK sites, 1–2 African) | Co-design and evaluate | Clinical lead, midwives, women, governance | Named founding partner; co-authorship; input into roadmap | Early features; steering group seat | No licence fee during evaluation; 40% discount for 3 years after | No equity to institutions; individual clinicians may join the advisory board with small option grants | None; "founding" is a title, not exclusivity |
| **Founding Technology Partner** (device, cloud, messaging, urinalysis) | Provide integrations and credits | SDKs, devices, credits, engineering support | Reference partner; joint case studies | Roadmap input | Preferred-supplier status at fair market prices | No | Category exclusivity for 12 months only if they fund it |
| **Founding Research Partner** (1–2 universities) | Evaluation and cohort | Design, ethics, analysis, grant bids | Co-authorship; data access under governance | Cohort governance seat | Grant-funded; no fees to Vytalix | No; joint IP on research outputs defined in the agreement | None |
| **Founding Data Partner** (cohorts, HDR UK, trusts) | Data access and linkage | Governed datasets, methods | Acknowledgement; joint publications | Research environment | Data-access fees to them, not from them | No | None |
| **Founding Commercial Partner** (implementers, HINs, insurers, telecoms) | Distribution | Introductions, bundling, channel | Revenue share; joint marketing | Partner portal | Referral or reseller margin 10–25% | No | Territory exclusivity only with volume commitments |
| **Founding Strategic Partner** (diagnostics, pharma, corporate) | Co-development and funding | Programme funding, market access | Board observer if investing; joint pathways | Cohort access under governance | Co-development fees; RWE licences | **Equity only for cash investment at market terms** (strategic round), never for "help" | Field-limited, time-limited, never global |
**Rules:** equity is exchanged for cash, for a founding executive's time, or for a small advisory grant (0.1–0.5% each, vesting); everything else is paid or commercial. No institution receives equity. Exclusivity is sold, not given, and always narrow and time-boxed.

# PART 16 — BRAND
**Assessment of "MATERNA-LINK":** descriptive, warm, and clear in English; the hyphen is untidy and the prototype uses three spellings (Materna-Link, MaternalLink, Maternal Link); "-Link" is common (dozens of "-Link" health products) and hard to trademark distinctively; it does not travel into French/Yoruba/Hausa contexts badly, but it says "app", not "infrastructure". Also a search must check "Maternalink"/"MaternaLink" conflicts in classes 9, 42, 44 (TO VALIDATE).
**Recommendation:** keep **Vytalix** as the parent (strong, distinctive, already designed); keep **MaternaLink** (one word, no hyphen) as the product family name for now because it has recognition with your existing contacts; plan a product-family architecture: *MaternaLink Continuity* (record and check-ins), *MaternaLink Home* (virtual ward), *MaternaLink Year* (postpartum), *MaternaLink Equity* (commissioner intelligence), *MaternaLink Research* (cohort). Re-evaluate the master brand at Series A with a professional naming study if the category positioning needs a less descriptive name.
**Twenty alternatives (all TO VALIDATE for trademark and domain):** Contina · Amara Health · Nurta · Velia · Kindra · Orla Health · Lumea · Tessera · Continuum Maternity · Harbour · Bridgewell · Amaryllis · Solace Health · Kaira · Vita Materna · Everline · Tenda · Cradle Continuity · Wellspring Maternal · Halo Maternity. Shortlist for a category-defining brand: **Contina** (continuity; short; distinctive), **Nurta** (nurture; global), **Velia**, **Tessera** (pieces joined into one record). None should be adopted without clearance.

# PART 17 — GLOBAL SCALE
| Market | What changes | Sequence |
|---|---|---|
| UK | Trust and ICB buyers; DTAC/MEWS alignment; NHS virtual-ward economics; equity mandate | Years 1–3 |
| Europe | EU MDR for any predictive module; GDPR; national procurement; Netherlands, Nordics and Ireland as first markets via partners (Philips, Erasmus MC, Karolinska) | Year 3+ |
| North America | Reimbursement for remote monitoring (CPT codes) and Medicaid maternal programmes; Babyscripts as incumbent; partner-led entry via a health system or insurer | Year 3–4 |
| Africa | Programme and donor buyers; SMS/USSD/WhatsApp-first; community health-worker mode; in-country hosting; DHIS2 alignment; sponsorship model | Year 1 (Nigeria) → Year 2–3 (Kenya, Ghana, Rwanda) |
| Middle East | Private hospital groups and national digital-health programmes; premium virtual care; Arabic | Year 3+ |
| Asia-Pacific | India and Bangladesh via NGO and government programmes; ASHA-type workforce mode | Year 4+ |
**Low-resource design:** the same continuity record on a feature phone through USSD and SMS; offline tablets for community health workers; cheap validated cuffs shared at community posts; paper-to-digital bridging; local-language voice; in-country data residency; results-based and sponsorship funding. **Global infrastructure layer:** achievable if the record and consent architecture are standards-based, the escalation engine is provider-owned, and every market adds interfaces rather than forks.

# PART 18 — THE £1 BILLION TEST
**Honest answer: possible but improbable on maternity software alone; plausible only as maternal continuity infrastructure with research and multi-market revenue.** UK maternity software at £30 per birth is an £18m annual market. A £1bn valuation needs roughly £100m+ recurring revenue at a 8–10× multiple, or a data and research franchise that commands more. That requires millions of women a year across several continents, plus research and pharma revenue, plus a regulated predictive module. The realistic strong outcome is a £50–150m company; the £1bn path exists and is set out below so the choices that keep it open are made early.
| Stage | Product | Customers | Revenue | Team | Data | Partnerships | Geography | Capital | Valuation logic |
|---|---|---|---|---|---|---|---|---|---|
| £0 → £1M | Continuity + virtual ward; advisory services | 3–5 UK sites; 1–2 African programmes; advisory clients | £1m ARR-equivalent (mix of services, pilots, licences) | 6–8 | 5,000 pregnancies | HIN, university, device, NGO | UK, Nigeria | Pre-seed £0.4m + grants | Pre-seed/seed 3–5× forward |
| £1M → £10M | Postpartum year; equity intelligence; integrations | 25 UK sites; 3 ICBs; 3 programmes; first insurer | £10m | 35 | 100,000 pregnancies; cohort open | Diagnostics co-development; telecom | UK, Nigeria, Kenya, Ghana | Seed £2–3m, Series A £8–12m | 6–10× ARR |
| £10M → £50M | Regulated predictive module; research licensing; sponsorship at scale | 100 UK sites; 10 ICBs; 10 programmes; 2 US health systems via partner; 2 insurers | £50m | 150 | 1m pregnancies | Pharma RWE; national programmes | + EU, US, Gulf | Series B £30–50m | 8–12× with data premium |
| £50M → £100M | Life-course women's-health continuity; federated network | National contracts; payers | £100m | 300 | 3m+ | Government-scale | 6+ countries | Series C or profitability | 8–10× |
| £100M → £1B | Global maternal continuity infrastructure standard | Multi-national systems, payers, pharma | £120–150m+ with 25%+ margins | 400+ | Largest consented perinatal cohort | Standards bodies, global funders | Global | Growth equity / IPO | 8–10× revenue plus strategic premium |
**What must change for this path:** the concept must move from "AI score" to "infrastructure"; the company must own consent and interoperability; research revenue must be designed in from year 2; a US or insurer partner is needed by year 3; and the founder must build a team with a clinician, an ML lead and a commercial lead who have done this before.

# PART 19 — 90-DAY EXECUTION PLAN (partner-first)
**Weeks 1–2**
- Legal blockers: name clearance; incorporate; IP heads of terms with David Agunede; retire the 2025 deck; prototype behind auth with synthetic data. (Do not pitch anyone until the deck is retired.)
- Write the one-page **intended-use statement** and the **virtual-ward evaluation concept** (2 pages) using Part 12.
- Contact: the **Innovation Exchange lead at your regional Health Innovation Network** (ask: "Which two trusts in the region have active hypertension-in-pregnancy remote-monitoring interest or a digital midwife?"); the **Head of Research at Tommy's** (ask: "Would you review an evaluation design and connect us to a clinical champion?"); **Five X More co-founders** (ask: "Would you be a community partner on the equity design?"); one **professor leading maternal-health digital or hypertension research** (Oxford primary-care BP group; King's Women & Children's Health) (ask: "Would you be the evaluation partner and ethics sponsor for a feasibility study?").
- Build: nothing new; audit the prototype; set up the partner war room (Part 20).
- Do not: build AI models; attend generic start-up events; cold-message 50 people.
**Weeks 3–4**
- Meetings: two trust conversations (Consultant Obstetrician hypertension lead + Head of Midwifery/Digital Midwife) via HIN introductions; one university; one device supplier (Omron/Withings medical channel manager) for loan stock.
- Documents: clinical safety plan (DCB0129 outline), DPIA template, partner proposal (Part 14 structure), one-pager, data-room v0.
- Evidence: 10 discovery interviews with midwives and obstetricians (questions: "What happened the last time a woman's BP rose between appointments?" "How do you find out?" "Who calls her back and how fast?" "What would make home readings safe for you?").
- Nigeria: reply to Ekiti with a complementarity proposal; approach one implementer (Society for Family Health, Jhpiego Nigeria) about a 500-woman continuity cohort.
**Month 2**
- Secure: one trust LOI for a service evaluation; one university partner letter; one NGO MoU draft; cloud credits; device loan agreement.
- Build: MVP sprint 1–4 (enrolment, check-ins, BP entry, thresholds, queue) with the fractional CTO.
- Investor prep: update one-pager and deck with the reframe; SEIS/EIS advance assurance submitted; Call List 1 verified.
- Grants: Innovate UK Smart or SBRI Healthcare application outline with the trust's letter.
**Month 3**
- Sign: service-evaluation agreement and data-sharing agreement; Cyber Essentials; pen-test booked.
- Build: sprints 5–8; safety case v1; training materials.
- Partners: Roche Diagnostics medical affairs conversation (pathway alignment, not money); NHS England maternity programme contact via the HIN; Bupa maternity lead exploratory call.
- Investors: first 10 calls (angels, GC Angels/NorthInvest-type syndicates, women's-health funds) only after the LOI exists.
- Evidence: interview synthesis; first equity report design.

# PART 20 — THE PARTNER WAR ROOM
**CRM columns:** Organisation · Country · Category · Partner Tier · Decision Maker · Job Title · LinkedIn · Email · Phone · Relationship Status · Priority (/10) · Strategic Value (/10) · What We Want · What We Offer · Last Contact · Next Action · Meeting Date · Partnership Stage · Probability (%) · Potential Value (£) · Notes · Source · Owner · NDA status · Instrument (LOI/MoU/SEA/DSA/commercial) · Consent to contact (GDPR basis).
**Pipeline:** TARGET → RESEARCHED → CONTACTED → RESPONSE → MEETING → DISCOVERY → PROPOSAL → PILOT → MOU → PARTNERSHIP → SCALE. Rules: RESEARCHED requires a named title and a reason; CONTACTED requires a personalised message; PROPOSAL requires the Part 14 structure; PILOT requires safety artefacts; MOU/agreements go through a solicitor.
**KPIs (monthly):** targets researched (≥ 30); contacted (≥ 20); response rate (≥ 30%); meetings (≥ 8); discovery-to-proposal conversion (≥ 40%); proposals out (≥ 3); pilots/LOIs signed (1 in month 2, 2 by month 3); time from first contact to meeting (≤ 14 days); partner NPS after meetings; pipeline value weighted by probability; number of Tier-1 partners secured (target 4 by Day 90: trust, university, NGO, CSO).
The Excel version (`investors/partners/PARTNER_WAR_ROOM.xlsx`) contains the CRM, the 74-organisation target list pre-loaded at stage TARGET/RESEARCHED, the pipeline definitions and a KPI sheet.

---

# FINAL OUTPUT

### THE NEW MATERNA-LINK
MaternaLink should become the maternal continuity infrastructure for health systems: a woman-held record, a channel that never goes silent, validated home monitoring when risk warrants it, escalation rules owned by the clinicians who carry the liability, a year of postpartum follow-up, and equity intelligence that shows who care reaches and who it misses, all built to work offline on any phone in Birmingham and in Ekiti alike. The predictive AI from the 2025 deck becomes the research programme that sits on top of a consented cohort, validated and regulated before it ever touches a clinical decision. Vytalix is the parent; MaternaLink is the family of products; the first product is a hypertension virtual ward evaluated properly at one trust.

### THE BIG IDEA
Close the 99% of pregnancy and the year after birth that maternity systems cannot see, by keeping every woman connected to a responsible clinician with a record that follows her.

### THE CATEGORY
Maternal Continuity Infrastructure, entered through Perinatal Virtual Care and The Postpartum Year.

### THE MOAT
The escalation-and-response and postpartum datasets no one else holds, the interfaces and consent architecture that make switching costly, and the clinical trust earned by never over-claiming.

### THE FIRST PRODUCT
A hypertension-in-pregnancy virtual ward: validated home BP, phone urinalysis, symptom check-ins, provider-owned thresholds aligned to national MEWS, an escalation queue with a response time, and equity reporting.

### THE FIRST CUSTOMER
One NHS trust maternity service with an obstetric hypertension lead and a digital midwife, bought as a 12-week service evaluation that converts to a licence.

### THE FIRST PARTNER
The regional Health Innovation Network's Innovation Exchange lead, who opens the trust door, followed within the same fortnight by a university perinatal research group as evaluation partner.

### THE FIRST £1M
Roughly: £250k–£400k from Vytalix Advisory and Consulting (investment-readiness, DTAC-readiness and Africa market-entry sprints for health-tech companies and NGOs) in the first 12–15 months; £150k–£250k from two or three paid pilots and first-year licences after the free evaluation (UK trusts at £40k–£90k pilots converting to £100k+ licences); £150k–£300k from one African programme or NGO contract via an implementer; £100k–£250k of grant income (Innovate UK, SBRI Healthcare) if won; and £50k–£100k from early sponsorship and training. That is the first £1m: services first, pilots second, programme third, grants alongside.

### THE 10 MOST IMPORTANT PARTNERS (ranked)
1. Regional Health Innovation Network (door-opener). 2. One NHS trust with a hypertension pathway (first customer). 3. A university perinatal research group (Oxford NPEU/primary-care BP group or King's Women & Children's Health) (evidence). 4. A fractional clinical safety officer and regulatory adviser (licence to operate). 5. Tommy's and Five X More (community legitimacy and equity design). 6. A validated BP device maker (Omron/Withings/A&D) (inputs). 7. A Nigerian implementer (Society for Family Health, Jhpiego Nigeria or mDoc as complementarity partner) (second market). 8. Maternity record vendor (Clevermed/K2) (interoperability). 9. Roche Diagnostics medical affairs (pathway credibility, later co-development). 10. A lead angel syndicate or women's-health fund (capital).

### THE 10 MOST IMPORTANT ACTIONS (ranked)
1. Sign IP heads of terms with David Agunede. 2. Clear the name and incorporate. 3. Retire the 2025 deck and put the prototype behind authentication. 4. Write and get clinical sign-off on the intended-use statement. 5. Book the Health Innovation Network conversation. 6. Approach one university evaluation partner. 7. Recruit the clinical safety officer. 8. Run 10 discovery interviews with the four questions above. 9. Secure a trust LOI for the hypertension virtual-ward evaluation. 10. Submit SEIS/EIS advance assurance and prepare Call List 1.

### THE BIGGEST RISK
That you keep pitching the AI score. It is the part of the concept that is scientifically unsupported, regulatorily heaviest and commercially weakest, and every clinician, regulator and serious investor will see it. The second risk is doing everything alone: without a clinician and an engineer beside you, the partner network will not believe the plan.

### THE BIGGEST OPPORTUNITY
To own the continuity of maternity care between appointments and after birth, in the UK and across Africa, as the infrastructure other systems plug into, and to hold the most diverse consented perinatal dataset in the world within five years, which is what would make a validated predictive model, and a category-defining company, possible.

### MY NEXT 72 HOURS
**Day 1 (morning):** message David Agunede to fix a call this week; draft IP heads of terms from `02_GROUP_STRUCTURE.md`; run trademark knock-out searches for Vytalix and MaternaLink; stop circulating the 2025 deck. **Day 1 (afternoon):** write the one-page intended-use statement (draft in `product/MATERNALINK_FEATURE_ADDENDUM.md`); ask David to put the prototype behind a login and remove photos. **Day 2 (morning):** find your regional Health Innovation Network's Innovation Exchange contact and send the Part 14 email adapted to them; send LinkedIn notes to Tommy's Head of Research and to the Five X More co-founders. **Day 2 (afternoon):** identify the professor leading home BP-in-pregnancy research (Oxford) and the King's Women & Children's Health digital lead; send the research-partner email; open the partner war room and enter the 74 targets with owners and next actions. **Day 3 (morning):** call two device makers' medical-channel teams (Omron, Withings) for loan stock and SDK access; email one Nigerian implementer with the complementarity proposal. **Day 3 (afternoon):** rewrite the one-pager with the continuity framing; list ten midwives and obstetricians for discovery interviews and send the first five requests; book the incorporation with your accountant for the day the name clears.
