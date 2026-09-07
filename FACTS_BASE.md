# VYTALIX — FACTS BASE (single source of truth for all workstreams)

Audit date: 7 September 2026. Every document in this repository must be consistent with this file.
Label every non-verified statement as ASSUMPTION, ESTIMATE, PROPOSED or TO VALIDATE. Never present a proposal as a fact.

## 1. What is VERIFIED (seen directly during the audit)

### Company / repository
- GitHub repository `elkelvinwilliams/Vitalyx` contained ONE file before this build: `README.md` with the single line "# Vitalyx". No code, no documents, no website, no brand assets. (VERIFIED)
- The founder's brief uses the spelling **VYTALIX**; the repository uses **Vitalyx**. Two spellings are in circulation. (VERIFIED)
- No Companies House registration for "Vytalix" or "Vitalyx" was found via public search. Similar names that DO exist and create naming/trademark risk: VITALIX LTD (two UK companies, nos. 16813455 and 15155964), VITALX LTD, VYTAL(UK) LIMITED, plus **Vytalyx Inc.** (Austin, Texas, AI/blockchain health-tech, vytalyx.io) and **Vytalize Health** (New Jersey, value-based care). (VERIFIED via search results; Companies House pages could not be opened directly from this environment, so registration status of Vytalix itself is TO VALIDATE)
- Founder email: elkelvinwilliams@gmail.com (the user). Founder name as it appears in the repo: Kelvin Williams (ASSUMPTION on the display name; confirm).
- The founder also runs a separate venture, **Kemek Enterprise Ltd** (Company no. 16766198, property bridging / "Project Harwood Manor"), with an investor CRM of 128 property-finance targets built August 2026. This is NOT Vytalix material and must not be mixed into the Vytalix investor CRM. (VERIFIED from Drive)

### MaternaLink — what actually exists
1. **"Black Maternal health" deck** (Google Slides + PPTX, Oct/Nov 2025, 13 slides), titled "MATERNA-LINK: Multimodal AI for Predicting and Preventing Maternal Complications". Concept: combine clinical data (BP, HR, urine protein, labs), voice/emotional biomarkers (diaries, consultations) and social/demographic data to produce a "Maternal Instability Score (MIS)" that "predicts pre-eclampsia, sepsis, haemorrhage, thromboembolism" and alerts a clinician dashboard. Proposed stack: Python, XGBoost, Librosa/OpenSMILE, TensorFlow/PyTorch, Hugging Face BERT, Streamlit/Dash, Fairlearn. States "Expand to multiple NHS trusts" as a future goal. Cites "Black women are 3x more likely to die during childbirth in the UK" (this is broadly consistent with MBRRACE-UK reporting but must be cited to the current MBRRACE-UK report before external use). **No data, no model, no validation, no clinical partner, no ethics approval is evidenced.** (VERIFIED as a concept deck only)
2. **Ekiti State (Nigeria) Ministry of Health proposal**, sent by **David Agunede, signing as "Founder & Chief Executive Officer, Maternal Link"** (davidagunede1@hotmail.co.uk) on 18 March 2026 following a meeting the previous Thursday; re-forwarded to the founder on 6 Sept 2026. Attachments: "Maternal Link Ekiti state.pptx", "Maternal_Link_Nigeria_Government_Proposal.pptx", "Charge sheet.docx", "MATERNAL LINK Nego sheet.odt", a "Lang Switcher" demo video. Proposed commercial structure: Phase 1 pilot 15,000 women (£4,500,000); Phase 2 30,000 women (£9,000,000); full state 120,000 women (£36,000,000); i.e. **£300 per woman per year** ("roughly $1 per day per mother"). Claims made in the email: target uptime 99.5–99.9%, offline-first architecture, cloud backups. Outcome of the proposal: **unknown / no evidence of acceptance, contract or payment.** (VERIFIED as a proposal only)
3. **Live prototype dashboard** at https://maternal-health-psi.vercel.app/ ("Maternal-link-dashboard"), with an "operator access" registration flow; shared with the founder on 6 Sept 2026. Could not be opened from this environment; treat as an early prototype of unknown maturity, hosting, security and data handling. (VERIFIED that it exists; contents TO VALIDATE)
4. An "Investors PPT" (Oct 2025) exists from David Agunede — content not reviewed here beyond the "Black Maternal health" deck it forwarded.

### Ownership and structure — CRITICAL GAP
- David Agunede presents himself as Founder & CEO of "Maternal Link". Vytalix's brief describes MaternaLink as Vytalix's first product. **The legal relationship between Vytalix, the founder, David Agunede and the MaternaLink IP (code, brand, proposals, prototype) is undocumented.** No shareholders' agreement, IP assignment, licence, JV or partnership agreement was found. Until resolved, Vytalix cannot truthfully tell investors it owns MaternaLink. (VERIFIED gap)
- No evidence found of: a registered company for Vytalix, a website/domain, a trademark, a bank account, employees, contracts, revenue, customers, grants, NHS or government partnerships, clinical partners, ethics approvals, regulatory classification, data-protection registration (ICO), or insurance. Everything is pre-formation. (VERIFIED absence in the materials reviewed; the founder may hold items not shared)

### Competitive fact that changes the Ekiti/Nigeria strategy
- Ekiti State already runs a maternal digital-health programme: **mDoc's "Digital Mom Project"** (CompleteHealth™ platform + NaviHealth AI), funded by **MSD for Mothers**, launched in Lagos on 10 Nov 2023 and extended to Ekiti; ~24,000 women onboarded and 500+ providers trained in Ekiti as of January 2026. mDoc also works with the Lagos State Ministry of Health. Source: Nigeria Health Watch (2026), Vanguard (Nov 2023), mDoc blog. **MaternaLink's Ekiti proposal is therefore entering a state with an incumbent, funded programme.** (VERIFIED via public reporting)

## 2. What is NOT known (must be asked or validated)
- Whether Vytalix is incorporated, where, and who the shareholders are.
- The founder's exact role, time commitment, capital available, and personal domain expertise (clinical? commercial? technical?).
- The agreement (if any) between the founder and David Agunede.
- Who wrote the code for the Vercel dashboard and who owns it; what data (if any) it holds; whether real patient data has ever been entered.
- Whether the Ekiti proposal is live, dead or in negotiation; whether any other government has been approached.
- Any letters of intent, pilots, advisors, clinicians or institutions attached to MaternaLink.

## 3. Working decisions taken in this build (ASSUMPTIONS, stated so they can be overturned)
- A1. Trading name: **Vytalix** (per the founder's brief). Legal entity name TO VALIDATE; recommendation is "Vytalix Group Ltd" (or "Vytalix Health Technologies Ltd") registered in England & Wales, subject to name/trademark clearance. The repository name "Vitalyx" should be treated as a typo to fix.
- A2. Home market: United Kingdom. Second market: Nigeria (via existing government conversations) and one further African market to be scored. Vytalix is UK-domiciled and GBP-reporting.
- A3. Stage: **pre-seed / pre-formation**. No revenue. No product in production. Everything in this repository is a build plan and asset set, not a record of achievement.
- A4. MaternaLink product positioning is **re-based** for credibility and regulatory safety: v1 is a maternal care-coordination, communication, education and monitoring-support platform (non-diagnostic; no automated clinical risk prediction). The multimodal AI "Maternal Instability Score" from the 2025 deck is retained as a **research and development track (v3+)** that requires data partnerships, ethics approval, clinical validation and a UK MDR / MHRA software-as-a-medical-device (SaMD) pathway before any clinical claim. This re-basing is a recommendation, not a fact about the current prototype.
- A5. Pricing in the Ekiti proposal (£300/woman/year) is treated as an UNVALIDATED ESTIMATE from a proposal, not a market price. Comparable programmes (e.g. donor-funded mDoc) suggest government willingness to pay at that level is TO VALIDATE.
- A6. First revenue is most likely to come from **Advisory/Consulting** (founder-led services) rather than from MaternaLink. MaternaLink is the venture/equity story; services are the cash story.
- A7. Funding path: bootstrapped services + grants (Innovate UK, NIHR i4i where eligible, SBRI Healthcare, Wellcome, Grand Challenges) → angels/SEIS-EIS pre-seed → impact/health-tech seed. SEIS/EIS advance assurance is a priority action once incorporated (TO VALIDATE eligibility).
- A8. No numbers in this repository are actuals. All financials are scenarios built from stated assumptions.

## 4. Language rules for every document
- Say "MaternaLink (in development)" — never "MaternaLink, our proven platform".
- Never say NHS-approved, clinically validated, CE/UKCA-marked, MHRA-registered, government partner, or "reduces maternal mortality" as a claim about MaternaLink.
- Allowed: "designed to support", "intended to", "we aim to", "subject to validation", "proposed".
- Investor CRM: only real, publicly identifiable investors; phone numbers only when found in a public source during research, with the source URL and date; otherwise "PHONE NOT PUBLICLY AVAILABLE". Never invent emails: use only addresses found in public sources, otherwise "NOT PUBLICLY AVAILABLE".
- Distinguish KNOWN / ASSUMPTION / ESTIMATE / TO VALIDATE / PROPOSED / VERIFIED / NOT PUBLICLY AVAILABLE throughout.
