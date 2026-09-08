# 02 — Every feature, and what we are allowed to say about it

**This document is for your developer.**

**It maps every feature the founder has described to a version number, a legal position and the proof needed before anyone claims it works.**

## In one minute

- Most of the founder's ideas fit version 1 as coordination and education, with no clinical judgement.
- Three ideas carry medical-device risk: triage sorting, blood-sugar interpretation, and any wearable.
- Voice tracing of baby movements is a research idea. It must never appear in sales material as a feature.
- Replacing a hospital system and joining one are two settings of the same product, not two products.
- The old prototype already suggests clinical actions. That must be removed before anyone sees it again.

## What to do

| Action | Who | By when |
|---|---|---|
| Get a clinician to review the intended-use statement below | Founder | Day 14 |
| Make the four prototype changes at the end of this document | Developer | Day 14 |
| Scope a regulatory opinion on triage and blood sugar | Founder and counsel | Day 21 |
| Remove voice movement tracing from every deck and page | Founder | Day 7 |
| Build version 1 as Core plus Engage plus voice storage only | Developer | Build start |

## The feature map

Version 1 is what we build now. Version 2 needs a regulatory opinion first. Version 3 is research, not product.

| What the founder described | What we actually build | Version | Legal position | Proof needed before we claim it | Price code |
|---|---|---|---|---|---|
| E-care patient database, the "maternity watch" record | Core register: mother and newborn, timeline, notes, exports, fields the provider can configure | v1 | Record support, no clinical judgement. Never the legal record where one already exists | DPIA, security certification, audit log tests | ML-CORE |
| Given at the week-16 midwife appointment, returned after postnatal discharge | Enrolment and discharge workflow: consent, onboarding, device issue and return log, offboarding, retention rules | v1 software, device later | Software: nothing beyond data protection. Device: see the wearable row | Onboarding time and completion rates in the pilot | ML-CORE, plus ML-WATCH |
| Midwife can explain things better | Education library signed off by clinicians, delivered in the app and by SMS or WhatsApp, more languages later | v1 | Educational content under a sign-off process | Comprehension and engagement measures | ML-ENGAGE |
| Shorten the appointment | Pre-appointment check-in and a symptom summary for the clinician; structured handover | v1 | A summary with no judgement. The clinician reads the raw entries | A time-and-motion study in the pilot. Do not claim minutes saved before they are measured | ML-CORE |
| Maternity triage, maternity A&E | Triage intake: structured capture of what she is presenting with, contact and outcome logging, and sorting rules owned by the site's own clinical governance | v2, test first | Likely clinical decision support if Vytalix ships the rules. Safe position: ship the rule editor with no default rules. Get an MHRA classification opinion | Regulatory opinion, then a service evaluation at one site | ML-TRIAGE |
| Daily questionnaire, like a period app | Daily check-in with configurable questions, streaks and reminders. Answers visible to the care team | v1 | No clinical judgement. Every concerning answer goes to a human within a set deadline | Engagement rates; an audit of how escalations were handled | ML-ENGAGE |
| Quizzes and a section for partners | Partner account linked with her consent; education quizzes; prompts such as appointment companion and warning signs | v1 | Consent and safeguarding. She controls partner access and can revoke it silently, for domestic-abuse safety | Safeguarding review; user testing with charities | ML-ENGAGE |
| Log symptoms such as itching hands and feet, or vomiting | Symptom log with plain-language prompts. Information only: "itching of hands and feet in pregnancy should be reported to your midwife today", with one-tap contact. The software never produces a diagnosis label | v1 | No clinical judgement as long as the software neither scores nor interprets. Wording reviewed by clinicians | Content sign-off; a hazard log entry for each symptom | ML-ENGAGE |
| Women with diabetes enter blood-sugar readings | Self-reported glucose diary with targets set by the clinician, a trend view, and a threshold notification to the care team | v2, deferred | Threshold alerting on physiological data moves towards being a medical device. Get an opinion before building | Regulatory opinion; design work with clinicians | ML-GLUCOSE |
| Voice tracing of babies' movements | Not a feature. A research question: capturing movement patterns needs a validated sensor, ethics approval, a clinical partner and a device pathway | v3 research | A medical device by its purpose, if it informs care | Ethics approval, a protocol, a data partnership, a validation study | none |
| Voice diaries | Storage and playback attached to the timeline. Transcription and translation later | v1 | Storage only. No analysis | Consent flows; retention policy | ML-VOICE |
| Maternity watch, the wearable | Joining a certified wearable to the record for prompts and, where the device is certified for it, readings shown without interpretation | v2 or v3, partner device | The device carries its own UKCA or CE marking. We display, we do not interpret | Supplier checks; the device's regulatory status; DPIA update | ML-WATCH |
| Replacing hospital systems | Deployment mode A: MaternaLink Core as the programme's working record where none exists | v1 | Needs a data-protection and clinical-safety case for record keeping. Still not a certified hospital record system | Clinical safety case | ML-CORE plus implementation |
| Joining hospital systems | Deployment mode B: interfaces to BadgerNet, K2, Euroking, DHIS2 or the state health information system, and single sign-on | v1 to v2 | Standard integration work under vendor agreements | Interface tests; vendor sign-off | ML-INTEGRATE |

## The intended-use statement

This is the draft wording. A clinician and a lawyer must review it before it appears anywhere.

> "MaternaLink is a care-coordination and communication platform that helps maternity programmes enrol women, keep in contact between appointments, record self-reported information and clinician notes, and route reported concerns to the responsible clinician. It does not diagnose, predict, triage or recommend treatment. Any prioritisation rules are configured, owned and reviewed by the deploying organisation's clinical governance."

Every screen, every deck and every proposal must stay inside that sentence. If a feature cannot be described within it, the feature needs a regulatory opinion first.

## The four changes the prototype needs before anyone reuses it

The prototype running on Vercel already produces a risk score and suggests clinical actions. That is the single biggest gap between what exists and what we are allowed to claim.

| # | Change | Why |
|---|---|---|
| 1 | Remove or relabel the "suggested actions" output so no clinical recommendation is produced by default. Replace it with "Programme escalation rule: [name] — contact the responsible clinician" | The software must not recommend treatment |
| 2 | Remove identifiable photographs and real-looking test identities. Use synthetic data | Nobody should be able to mistake demo data for a real person |
| 3 | Put the public URL behind a login, and confirm no real patient data was ever entered | An open URL with patient-like data is a data-protection incident waiting to happen |
| 4 | Rename it to MaternaLink, add the Vytalix mark, and match the wording in this document | The old naming and copy claim more than we can support |

## What to build first, and what to hold

| Position | Detail |
|---|---|
| Build now | Core, Engage and voice storage. These are the version 1 product |
| Hold | Triage and glucose, until a regulatory opinion is written down |
| Partner, do not build | The wearable. Someone else carries the device certification |
| Never claim | Voice movement tracing as a feature; any reduction in minutes, risk or harm that has not been measured |

Risks to watch: features creeping back towards decision support; partner access failing a safeguarding test; over-promising the watch to an investor.

## Words explained

| Word | What it means |
|---|---|
| Medical device | Software that diagnoses, predicts, monitors or guides treatment. It needs approval and a quality system before sale |
| Clinical decision support | Software that tells a clinician what to do or how urgent something is. That is a device |
| MHRA | The UK regulator that decides whether software counts as a medical device |
| UKCA or CE marking | The mark showing a device has passed the approval route. MaternaLink has neither and does not need one while it stays non-diagnostic |
| DPIA | The written check that a product handles personal data lawfully |
| Clinical safety case | The written argument, signed by a named safety officer, that the software is safe to use in care |
| Service evaluation | Watching a service that is already running. It is not research and it proves nothing about effectiveness |
| Synthetic data | Invented records that look real but belong to nobody |
| PROPOSED | This is a plan we have written down, not a decision anyone has approved |
