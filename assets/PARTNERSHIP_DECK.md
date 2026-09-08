# VYTALIX — Partnership Deck: MaternaLink (in development) Pilot Partnership (10 slides)

**Audience:** prospective pilot and design partners — NHS trusts and LMNS maternity leads; NGOs and implementing partners (Nigeria, later Kenya); university maternity research groups; telecom and messaging partners. **Length:** 10 slides, 20 minutes plus discussion. **Version:** 1.0 · 8 September 2026 · Status: PROPOSED.
Design per `/docs/03_BRAND_SYSTEM.md` §13. Language per `/FACTS_BASE.md` §4: MaternaLink is always "in development"; no "partner" is claimed until an agreement is signed; an MoU or LOI is never described as a partnership in investor material.

## Executive view

1. This deck asks for a design partnership or a scoped pilot, not a purchase: an unpaid UK service evaluation, an NGO-funded cohort in Nigeria, a research collaboration, or a messaging-channel arrangement.
2. It leads with the problem partners already own (Ockenden and Kirkup actions, CNST safety actions, donor logframes, the three delays) and maps the v1 scope to it.
3. The non-diagnostic intended use and the four gates (IP, prototype audit, Clinical Safety Officer and hazard log, DPIA) are stated on their own slide, before any ask.
4. Each partner type gets a tailored "what we offer / what we ask / what we will not do" slide; the founder shows only the slide relevant to the room.
5. The ask is one specific, low-cost next step with a date: a scoping call, a letter of intent, a complementarity conversation, or a data-sharing pre-discussion.

---

## Slide 1 — Title

**Copy**
- MaternaLink (in development)
- A care-coordination and communication platform for maternity services — designed with the people who use it.
- A pilot-partnership conversation with [Partner organisation]
- Vytalix · Technology for Life · [Date] · Confidential — draft

**Speaker note:** "We are not here to sell you software. We are here to ask whether you would help us design and evaluate it, and to be explicit about what that involves and what it doesn't."

**Visual:** Deep title slide; product lockup with the "(in development)" tag as part of the mark; subtitle in Signal Mint; no partner logo without permission.

---

## Slide 2 — The problem you already own

**Copy**
- UK: inquiries into maternity services (Ockenden 2022; Kirkup 2022) repeatedly found failures to listen to women, to escalate, and to hand over between teams. Persistent disparities by ethnicity and deprivation are reported by MBRRACE-UK (cite the current report before use).
- Nigeria: the largest absolute maternal-death burden in the world (WHO/UNICEF estimates; cite the current edition); the "three delays" — deciding to seek care, reaching care, receiving adequate care.
- Common to both: a woman's own account is under-used; information is lost at handover; education arrives in the wrong language; programmes cannot see who has fallen out of contact.
- Existing maternity records are record systems, not relationship systems. The gap is the communication and coordination layer.

**Speaker note:** two minutes; the partner knows this better than we do — invite correction.

**Visual:** two columns UK / Nigeria; monoline "gap" diagram; source line at 16px listing the reports; no statistic without its citation on the slide.

---

## Slide 3 — What MaternaLink (in development) is intended to be

**Copy**
- Intended use (PROPOSED; TO VALIDATE with regulatory counsel): a software platform intended to support communication, education, appointment scheduling and information handover between women receiving maternity care and their care teams, and to support programme administration. It is not intended to diagnose, prevent, monitor, predict, prognose, treat or alleviate any condition, nor to provide clinical decision support.
- v1 features: enrolment and granular consent · personalised contact schedule and reminders · clinically signed-off education by gestation, language and literacy · secure asynchronous messaging with a named owner and acknowledgement SLA · self-recorded diary displayed, not interpreted · care-team console · structured handover summary · single-entry escalation log · missed-contact lists · programme dashboard with CSV and DHIS2-compatible exports · web app (offline-capable) plus SMS, with voice and WhatsApp on the roadmap.
- The system escalates unread messages to humans; it never decides clinical urgency.

**Speaker note:** three minutes; read the "not intended to" sentence in full. This is the sentence that lets a Clinical Safety Officer and a Caldicott Guardian engage with us.

**Visual:** intended-use statement in a Mist-tinted box at the top; features in two columns below; persistent tag "Non-diagnostic — in development" in Ember.

---

## Slide 4 — Where we are, honestly

**Copy**
- Exists today: a concept; an early prototype dashboard of unknown maturity; a re-based v1 scope; a PRD, MVP specification and roadmap (`/product/`).
- Does not exist today: a deployed product; any real-world data; a clinical partner; ethics approval; regulatory classification; a Clinical Safety Officer; a signed IP agreement.
- Four gates we are closing before anything goes live: (1) IP ownership documented · (2) prototype audited for code ownership, security and data · (3) Clinical Safety Officer appointed and DCB0129 hazard log opened · (4) DPIA and lawful-basis analysis complete (UK GDPR; Nigeria Data Protection Act 2023).
- Design targets, not claims: DTAC-ready pack; DSPT "Standards Met"; Cyber Essentials Plus; penetration test before go-live; UK-region hosting with a Nigeria deployment cell option.

**Speaker note:** two minutes; this slide has lost us nothing with serious partners and everything with unserious ones. Keep it.

**Visual:** two-column "Exists / Does not exist"; four gate markers in Ember beneath; design targets in Slate.

---

## Slide 5 — What a pilot looks like (the shape, before the ask)

**Copy**
- UK: a 3–6-month service evaluation with one community midwifery team, under DCB0160 on the trust side, with a defined cohort (ESTIMATE n≈50–150), no fee or nominal fee; Vytalix provides the safety case, DPIA template, training and support. The EPR remains the record; MaternaLink provides pasteable summaries; no integration in v1.
- Nigeria: a 12-month pilot in 1–2 named LGAs with an implementing partner's existing cohort (ESTIMATE 500–2,000 women), two-way SMS and defaulter tracing, DHIS2-compatible exports, data owned by the state or programme, a defined exit. Programme envelope under £0.5m/year; platform layer priced at £6–£40 per woman per year (ESTIMATE), SMS at pass-through.
- Both: a co-authored evaluation protocol; operational metrics only (contact completion, acknowledgement times, defaulters traced, reach); no outcome claims without a formal evaluation.
- Success metrics are design targets (`/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §24), reported honestly per period.

**Speaker note:** three minutes; the pilot is small, bounded and ends. Say "exit" out loud.

**Visual:** two pilot cards UK / Nigeria; a timeline bar under each; Ember marker at "evaluation report".

---

## Slide 6 — For NHS trusts and LMNS (show to NHS audiences)

**Copy**
- What we offer: a non-diagnostic tool that maps to actions you already own — Ockenden immediate and essential actions on listening and escalation; CNST Maternity Incentive Scheme safety actions (current year's actions TO VALIDATE); complaints about communication. Artefacts in the first meeting: intended-use statement, DCB0129 hazard log, DPIA template, DTAC readiness pack, penetration-test summary once complete.
- What we ask: a digital midwife or Head of Midwifery sponsor; a Clinical Safety Officer for DCB0160; one community team; a 3–6-month service-evaluation window; a letter of intent first, then an evaluation agreement.
- What we will not do: touch the EPR in v1; process data before the DPIA and Data Processing Agreement are signed; make any clinical or outcome claim; describe you as a "partner" or "customer" without written consent.
- Procurement: no purchase obligation; any later contract via G-Cloud or direct award under threshold (routes TO VALIDATE).

**Speaker note:** trusts have been burnt by unvalidated maternity apps; artefacts are the differentiator.

**Visual:** three-row "Offer / Ask / Will not" layout; NHS terminology kept plain; no NHS logo.

---

## Slide 7 — For NGOs, implementing partners and donors (show to Nigeria/Africa audiences)

**Copy**
- What we offer: enrolment and follow-up tracking for your cohort; two-way SMS at scale without your team typing messages; defaulter-tracing lists for CHEWs; logframe-ready indicators and DHIS2-compatible exports; Yoruba content subset first, Hausa/Igbo/Pidgin on the roadmap; data owned by you or the state; local-hosting option (Nigerian data centre or nearby cloud region, TO VALIDATE).
- What we ask: an existing cohort in 1–2 LGAs; CHEW supervision and training capacity; a programme budget line or a joint grant application (Grand Challenges, UNFPA innovation calls, FCDO-funded programmes, Innovate UK/NIHR global health where a UK institution leads — eligibility TO VALIDATE); co-authorship of the evaluation protocol; NHREC/state ethics approval for any evaluation.
- What we will not do: arrive with a state-wide proposal; compete on price with an incumbent programme (we are aware of mDoc's Digital Mom Project in Ekiti and Lagos and will explore complementarity first); share individual-level data with any insurer or third party.
- Price shape: programme licence £8k–£60k per programme per year depending on cohort size (ESTIMATE), or per-woman platform pricing, plus SMS pass-through; training and devices priced separately or by partners.

**Speaker note:** the NGO is the fastest route to a Nigerian cohort; the killer feature is "who has missed a contact and who is chasing them".

**Visual:** same three-row layout; a small SMS-flow diagram (enrol → remind → reply → defaulter list → CHEW visit).

---

## Slide 8 — For universities and research groups (show to academic audiences)

**Copy**
- What we offer: a real-world care-coordination deployment to study; co-designed evaluation protocols; shared authorship; a defined, later research track (v3) on multimodal risk signals that we will only pursue with a data partnership, HRA/REC (UK) or NHREC (Nigeria) approval, pre-registered protocols, TRIPOD+AI-style reporting and fairness analysis by ethnicity and deprivation.
- What we ask: methodological partnership for the UK service evaluation and feasibility study (2027–28); a data-sharing conversation for the research track only when v1 evidence exists; joint grant applications where a UK institution leads (NIHR, Innovate UK, Wellcome, Grand Challenges — eligibility TO VALIDATE).
- What we will not do: train any model on patient data without approvals; make predictive claims before prospective validation and a UK MDR / MHRA pathway; treat the research track as a product commitment (ESTIMATE 24–36 months and £1.5m–£4m to do properly).
- Institutions we intend to approach are named in `/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §10 as institutions, not as commitments; no relationship exists today.

**Speaker note:** universities convert the 2025 concept into fundable research; they also keep us honest.

**Visual:** timeline: service evaluation → feasibility study → formal evaluation → research track (dotted); gate markers at ethics and data-sharing points.

---

## Slide 9 — For telecom and messaging partners (show to telecom/gateway audiences)

**Copy**
- What we offer: a maternal-health messaging and coordination use case with programme and NGO buyers; content-neutral SMS on shared phones (safeguarding by design); voice reminders in local languages on the roadmap; a data-residency-aware architecture; a white-label option for health propositions later (ESTIMATE set-up £25k–£75k plus £2–£8 per user per year; TO VALIDATE).
- What we ask: gateway access and pricing (SMS, voice, USSD, WhatsApp Business), sender-ID and DND compliance guidance (NCC rules TO VALIDATE), zero-rating or bundled data for enrolled women where possible, and a named contact for a pilot.
- What we will not do: pass identifiable health data to a telecom partner; send diagnosis or pregnancy status in SMS without explicit opt-in; commit volumes before a funded pilot exists.
- Working assumptions to test together: ~60 SMS per woman per year; ₦4–₦6 per SMS (TO VALIDATE current rates); cost per woman per year for messaging well under £1 (ESTIMATE).

**Speaker note:** telecom partners are a year-2 scale channel (`/docs/00_MASTER_AUDIT.md` §6, opportunity 10); the ask now is pricing and a contact, not a contract.

**Visual:** architecture strip: app/PWA — gateway — feature phone; lock icon on the data boundary; cost assumptions in a small table labelled ESTIMATE.

---

## Slide 10 — Next step

**Copy**
- One specific step, one date: [NHS: 45-minute scoping call with the digital midwife and CSO] · [NGO: cohort and budget-line conversation; joint grant outline] · [University: methods meeting on the evaluation protocol] · [Telecom: pricing sheet and sender-ID guidance].
- Then: letter of intent or MoU (described as such, never as a partnership) → pilot or evaluation agreement with DPA → kick-off after the four gates close.
- What you can expect from us: the intended-use statement, hazard-log starter, DPIA template and evaluation-protocol outline within one week of this meeting.
- Contact: [founder email] · [LinkedIn] · [website]

**Speaker note:** ask for the one step; offer the documents; set the date. Then stop.

**Visual:** Deep background; partner-type tabs; Ember CTA style on the date line; footer "Vytalix — Technology for Life".

---

## Using this deck

| Rule | Detail |
|---|---|
| One partner slide per room | Show slide 6, 7, 8 or 9 — not all four |
| Gates before asks | Slide 4 is never removed |
| MoU ≠ partnership | An LOI/MoU is described as an LOI/MoU in all investor and marketing material |
| Ekiti | Do not present the March 2026 proposal figures; hold one status conversation with the ministry and one complementarity conversation with the incumbent (`/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §12.2) |
| Data | No real data is processed in any demonstration; the prototype is a demo asset, not a product asset, until audited |

---

## Priorities / Risks / Next actions

**Priorities**
1. Close gates 1–2 (IP agreement; prototype audit) before the first NHS meeting; appoint the Clinical Safety Officer and open the hazard log so slide 4 can move items from "does not exist" to "exists".
2. Approach ten UK maternity services via Health Innovation Networks, LMNS leads and clinical advisers (target: one LOI by month 9), and one Nigerian implementing partner with an existing cohort.
3. Prepare the partner document pack (intended-use statement, hazard-log starter, DPIA template, evaluation-protocol outline) so the slide 10 promise can be kept within a week.

**Risks**
- An enthusiastic partner asks for a feature that crosses into medical-device territory (threshold alerts, scored questionnaires); mitigation: the qualification-decision process in `/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §21.2 and CSO sign-off.
- The Ekiti relationship proves non-transferable or the state has moved on; mitigation: state scorecard and NGO cohorts that do not depend on one ministry.
- A partner is named publicly before consent; mitigation: written consent rule; announcements only after signature.

**Next actions**
- Founder, by Day 30: partner document pack v1; slide master version of this deck.
- Founder + clinical adviser (to recruit), by Day 60: ten UK approaches made; two scoping calls held.
- Founder, by Day 90: Ekiti status call and mDoc complementarity conversation held; two alternative states scored; one NGO conversation with a defined cohort.
