# 03 — The eight-quarter plan, and what each stage lets you say

**This document is for your developer.**

**It shows what ships each quarter from late 2026 to late 2028, what has to be true before it can ship, and what you are allowed to claim afterwards.**

## In one minute

- Eight quarters take MaternaLink from an unaudited prototype to a version 2 product with real evidence.
- Nothing on this plan is real until the code and name ownership is settled, in late 2026.
- Each quarter is blocked by something outside our control: a hospital site, a partner, a gateway, an ethics committee.
- What you may say is set by the evidence stage you have reached, not by what the software can do.
- Every date here is a plan, not a promise. Slippage in one gate moves everything after it.

## What to do

| Action | Who | By when |
|---|---|---|
| Settle code and name ownership, and audit the prototype | Founder | December 2026 |
| Find the UK evaluation site and the Nigeria partner, in parallel with the build | Founder | March 2027 |
| Treat the safety case, DPIA, DTAC form and certificates as build deliverables | Developer | March 2027 |
| Design the version 2 flagging feature early so the device decision is made on paper | Developer | September 2027 |
| Enforce the permitted-claims table in every deck, page and proposal | Founder | Always |

## The eight quarters

| Quarter | What ships | What must be true first | What it lets you say |
|---|---|---|---|
| Q4 2026, Oct–Dec | Discovery with 20 women and 10 professionals per market; requirements signed off; design system; infrastructure and pipelines; build weeks 1–6 (login, tenancy, enrolment, consent, schedule, reminders, gateway adapters) | Company incorporated; code and name ownership documented; prototype audited; safety officer contracted; hazard log opened; build funded at £220k–£320k UK-led or £140k–£210k blended | Nothing about the product. Only: "we are building, informed by interviews with 20 women and 10 professionals" |
| Q1 2027, Jan–Mar | Build weeks 7–16: messaging and the deadline engine, rota, diary, content library (about 40 UK and 20 Nigeria items), offline sync, console, handover, escalation, defaulters, dashboard, admin and audit. Internal alpha on invented data | Each must-have feature has a written decision that it is not a medical device; the safety case is signed; the DPIA is approved; the DTAC form is filled; Cyber Essentials certified; penetration test and accessibility audit passed | "The first version is complete and entering a service evaluation." Nothing more |
| Q2 2027, Apr–Jun | Version 1.0 live in one UK community midwifery team. Version 1.1: WhatsApp, Yoruba content and interface, recorded voice reminders, pre-visit summary | The site has done its own safety assessment; the NHS toolkit submission is in; the Nigeria data-protection registration is done if the thresholds apply; the SMS sender ID is live | "In use in a service evaluation at [site]", with their written permission, plus plain usage numbers. No effectiveness language |
| Q3 2027, Jul–Sep | Version 1.2: USSD menus, DHIS2 export, referral notice to the receiving facility, field mode for defaulter tracing, cost tuning for SMS volume | Nigeria pilot funded at £0.1m–£0.3m; Cyber Essentials Plus certified; Nigeria ethics approval; USSD short code leased; state data-sharing agreement signed | Service evaluation results as plain descriptions, for example "median acknowledgement time X hours". "Pilot under way in [state] with [partner]", never "government partner" |
| Q4 2027, Oct–Dec | Version 2.0: read-only FHIR view for future hospital integration, demographics lookup, audit and reporting improvements. Rule-based flagging of self-recorded readings is designed but not released | A written decision with counsel on whether flagging and scored questionnaires make it a medical device. If yes, the Class I route is resourced. UK feasibility study has ethics approval | No change. Feasibility results do not exist yet |
| Q1 2028, Jan–Mar | Version 2.1: partner access with consent and safeguarding controls; mental-health questionnaires only if the device decision cleared them; Hausa, Igbo and Pidgin libraries; transport and emergency-fund tracking for Nigeria | UKCA Class I registration if it applies; safety case version 2; DPIA version 2 for partner access; toolkit resubmission; translation partners for Hausa and Igbo | Nigeria pilot interim numbers, with the partner's permission. "Feasibility study under way" |
| Q2 2028, Apr–Jun | Version 2.2: hospital record export interfaces where the vendor supports them, FHIR handover export, the version 3 research design, analytics hardening | Multi-site formal evaluation started; an academic partner found; data-sharing agreements and ethics applications for the research track | "Formal evaluation under way." Feasibility results once published |
| Q3 2028, Jul–Sep | Version 2.3: hardening, cost work, Nigeria hosting cell if a contract requires it, accessibility re-audit. Version 3 retrospective modelling, in a separate research environment under approvals | The decision on whether to build a quality system for a version 3 prediction device (24–36 months and £1.5m–£4m to a clinical claim); annual penetration test; certificate renewals | Still no prediction or outcome claims. Research is described as research |

If funding is only partial in Q4 2026, build the Nigeria SMS slice first: enrolment, schedule, SMS and the defaulter list. It needs the least screen work and can earn a programme licence soonest.

## The evidence stages, and what each one permits

| Stage | What it is | Who governs it | What it answers | What you may say afterwards | What you may never say at this stage |
|---|---|---|---|---|---|
| Discovery, Q4 2026 | Interviews, watching, designing together. No patient data | Consent for the interviews only | What women and staff need, which channels, which languages, what deadlines are normal | "Designed with input from 20 women and 10 professionals" | Anything about how the product performs |
| Service evaluation, Q2–Q3 2027 | One site, operational measures before and after, plus a usability score | The trust's own service-evaluation governance, its safety assessment, and the DPIA | Is it usable, is it safe in operation, do staff adopt it, how fast are messages acknowledged, how many contacts are completed | "In use in a service evaluation at [site]", usability scores, plain operational numbers | Effectiveness, "improves outcomes", "validated", "proven" |
| Feasibility study, Q4 2027–Q1 2028 | Two sites, mixed methods, registered in advance | Health research ethics approval, a sponsor, patient and public involvement | Is a full evaluation feasible: recruitment, retention, data completeness, acceptability | "Feasible and acceptable in a study of N women across two sites" | Efficacy, "proven", any outcome claim |
| Nigeria pilot, Q3 2027–Q3 2028 | One or two local government areas, 500–2,000 women, compared with similar areas where possible | Nigerian ethics approval, a state data-sharing agreement, the data-protection act | Reach, engagement, contact completion against baseline, defaulter tracing time, cost per woman | "Pilot in [areas] with [partner]: reach X%, contact completion up Y points against baseline", as observed, with caveats | "Reduces maternal mortality"; "government partner" |
| Formal evaluation, from Q2 2028 | Multi-site, registered in advance, analysed independently | Health research ethics, a sponsor, trial registration, data monitoring | Effect on process measures and on women's experience; safety events; cost | "Associated with [effect] on [process measure] in a multi-site evaluation" | Any reduction in death or serious illness, unless a study is powered for it. That is beyond this plan |
| Version 3 research | Retrospective modelling under data-sharing agreements, with a fairness analysis | Ethics approval in both countries; no production data without an approved data flow | Is a signal detectable, and is it fair across groups | Research findings, in publications only | Any clinical claim; any product feature |

## The gates that block everything

| Gate | What must be true | Who owns it | When |
|---|---|---|---|
| G0 Ownership | Written assignment of code, brand and proposals; prototype audited; company name cleared | Founder | Q4 2026 |
| G1 Classification | Intended-use statement adopted; a written decision per feature that it is not a device | Developer and counsel | Q1 2027 |
| G2 Clinical safety | Hazard log complete; safety case report signed by the safety officer; the site does its own assessment | Safety officer | Q1 2027 |
| G3 Data protection | DPIA approved; data-processing agreements; records of processing; ICO registration; privacy notices in her languages | Data protection officer | Q1 2027 |
| G4 DTAC | The NHS assessment form completed across its five areas. It applies before a pilot, not only before a purchase | Developer | Q1 2027 |
| G5 Cyber Essentials, then Plus | The five controls evidenced, then tested by an assessor | Developer | Q1 2027, then Q3 2027 |
| G6 NHS toolkit | Supplier submission for the current cycle, as a Category 3 supplier | Developer and DPO | Q2 2027, then yearly |
| G7 Nigeria registration | Registered with the NDPC if the thresholds apply; a named officer; a Nigerian DPIA | Nigeria lead and counsel | Q2 2027 |
| G8 Device decision | A written decision on flagging and scored questionnaires. If it is a device, the Class I route is funded | Developer, safety officer, counsel | Q4 2027 |
| G9 UKCA Class I | Technical file, self-declaration, MHRA registration, post-market plan with 15-day incident reporting | Regulatory lead | Q1 2028, if it applies |
| G10 Quality system | Decision on building a full quality system for a version 3 prediction device | Founder | Q3 2028 |

## What would change this plan

| Signal | Change |
|---|---|
| Discovery shows UK women overwhelmingly prefer WhatsApp to an app | Pull WhatsApp into the first build, in place of web push. Do the DPIA earlier |
| A northern Nigerian state partner appears first | Hausa content moves to version 1.1 and Yoruba to 1.2 |
| Counsel judges the diary display or the handover summary to be a device | Redesign those features before go-live and add a Class I route to Q2 2027 |
| The prototype audit is clean and ownership is assigned | Reuse some interface components; the build shortens by about two weeks |
| No academic partner can be found for the formal evaluation | Run a rigorous internal evaluation with an independent evaluator, and label it as exactly that |

## Words explained

| Word | What it means |
|---|---|
| Gate | Something that must be finished before the next stage can start |
| Service evaluation | Watching a service already running. It is not research and proves nothing about effectiveness |
| Feasibility study | A small study asking whether a bigger study would work |
| Formal evaluation | The real study, planned and registered in advance, analysed by someone independent |
| Powered | A study with enough people in it to detect the effect it claims. Ours are not |
| DTAC | The NHS checklist a digital product must pass before a hospital can buy or pilot it |
| NHS toolkit (DSPT) | The annual data-security self-assessment NHS suppliers must submit |
| NDPC | Nigeria's data protection regulator |
| UKCA Class I | The lowest-risk UK medical device route, self-declared and registered with the MHRA |
| ESTIMATE / TO VALIDATE | Our best guess, not a fact / nobody has checked this yet |
