# 15 — VYTALIX LEGAL, REGULATORY AND COMPLIANCE FRAMEWORK

**Owner:** Founder (acting Risk & Compliance lead) · **Status:** PROPOSED · **Version:** 1.0 (7 September 2026) · **Governed by:** `/FACTS_BASE.md` · **Related:** `/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §§15–21, `/docs/13_SALES_ENGINE.md` §9

> **This document is not legal advice.** It is a founder's compliance map. Every item marked **[SOLICITOR]**, **[ACCOUNTANT]** or **[REG-CONSULTANT]** requires qualified professional advice before action. Fees quoted with a URL were checked on 7 September 2026 via web search (6 searches used); everything else is ESTIMATE or TO VALIDATE.

## Executive view
1. Vytalix has no legal entity, no ICO registration, no trademark, no contracts, no insurance and no policies (VERIFIED absence, FACTS_BASE §1). Nothing can be sold, banked, insured or granted until an entity exists; incorporation is therefore the first legal act, gated only by name clearance.
2. The two highest-consequence legal issues are (a) the undocumented MaternaLink IP relationship with David Agunede and (b) the naming conflict with VITALIX LTD (UK), Vytalyx Inc. (US) and Vytalize Health (US). Both must be resolved before any brand spend, investor conversation or pilot contract.
3. MaternaLink (in development) v1 is deliberately scoped as non-diagnostic care-coordination software so that it sits outside UK medical-device regulation; that position holds only while the intended-use statement is enforced feature by feature. Any predictive or alerting feature triggers UK MDR 2002 / MHRA SaMD obligations.
4. Health data is special-category data under UK GDPR. Advisory and consulting work should be designed to process **no** patient data; MaternaLink will require a DPIA, ICO registration, a Clinical Safety Officer, DSPT and Cyber Essentials before any real-world deployment, and NDPA 2023 registration before any Nigerian deployment.
5. Budget for year-1 legal and compliance (ESTIMATE): £9k–£18k, of which solicitor fees for IP/shareholder documents £4k–£8k, trademark £1.5k–£3k including adviser, insurance £1.5k–£3.5k, ICO/Cyber Essentials/registrations £0.5k–£1k, contracts £2k–£4k. Non-negotiable items are flagged P0 in §14.

---

## 1. Corporate formation (Companies House)

| Item | Position (PROPOSED) | Fact / cost | Flag |
|---|---|---|---|
| Entity type | Private company limited by shares, England and Wales | Standard for SEIS/EIS and investor readiness | [ACCOUNTANT] on group structure timing |
| Name | "Vytalix Group Ltd" or "Vytalix Health Technologies Ltd" (FACTS_BASE A1), subject to §8 clearance; the "Vitalyx" spelling is retired | Companies House rejects names "same as" an existing name; "similar" names can be challenged post-registration; VITALIX LTD ×2 exist (VERIFIED via search; registry TO VALIDATE) | [SOLICITOR] if a name objection risk is material |
| Incorporation fee | Digital incorporation | **£100** (digital) from 1 February 2026; £124 paper. Source: https://www.gov.uk/government/news/companies-house-fees-are-changing-from-1-february-2026 ; https://www.icaew.com/insights/viewpoints-on-the-news/2025/nov-2025/significant-hikes-to-companies-house-fees-in-2026 | — |
| Confirmation statement | Annual | **£50** digital (£110 paper) from 1 February 2026 (same sources) | — |
| Registered office | Founder's address or a registered-office service (ESTIMATE £30–£100/yr) | Address appears on the public register | — |
| Directors / PSCs | Founder as sole director initially; identity verification for directors/PSCs under the Economic Crime and Corporate Transparency Act (TO VALIDATE current mandatory date and process) | — | [ACCOUNTANT] |
| Share capital | e.g. 10,000 ordinary shares at £0.01 (ESTIMATE); leave headroom for an option pool and for any equity granted under the IP settlement (§8.3) | Model articles or bespoke articles | [SOLICITOR] if bespoke articles / share classes |
| Articles and shareholders' agreement | Model articles at incorporation; shareholders' agreement drafted before any second shareholder (including David Agunede if equity is the settlement) | ESTIMATE £1.5k–£4k | [SOLICITOR] |
| Bank account | Open immediately after incorporation (challenger banks are fastest; TO VALIDATE) | £0–£10/month | — |
| Accountant | Appoint on incorporation; Corporation Tax registration, PAYE if salaried, VAT decision (threshold £90,000 taxable turnover in 12 months — TO VALIDATE current threshold), R&D tax relief eligibility later | ESTIMATE £80–£200/month | [ACCOUNTANT] |
| SEIS/EIS advance assurance | Apply once incorporated and a plan and prospective investor exist (HMRC generally expects an identified investor — TO VALIDATE) | £0 HMRC fee; adviser ESTIMATE £500–£1,500 | [ACCOUNTANT] |
| Group structure | Single company first; subsidiaries (Health Solutions, E-Learning) only when revenue, IP or investors require them | Each subsidiary adds £100 + £50/yr + accounts | [ACCOUNTANT] |
| Statutory registers, PSC register, board minutes | Maintain from Day 1 in a "corporate" folder; first board minute records adoption of policies and IP assignments | — | — |

Pre-incorporation selling: any engagement signed before the company exists is a personal contract of the founder (sole trader). Keep it short, insured (PI can be bought as a sole trader) and novate to the company on incorporation. [SOLICITOR] for the novation wording.

---

## 2. Data protection — UK GDPR and Data Protection Act 2018

### 2.1 Regulator and registration
- **ICO data-protection fee** (payable by most controllers): **Tier 1 £52** (max turnover £632k or ≤10 staff), **Tier 2 £78** (turnover ≤£36m or ≤250 staff), **Tier 3 £3,763**; £5 discount for direct debit; unchanged since February 2025. Sources: https://ico.org.uk/for-organisations/data-protection-fee/data-protection-fee/ ; https://ico.org.uk/for-organisations/data-protection-fee/ . Vytalix is Tier 1. Register within 21 days of starting to process personal data as a controller (TO VALIDATE that an exemption does not apply — it will not once a CRM and newsletter exist).
- **Data (Use and Access) Act 2025**: Royal Assent 19 June 2025; provisions phased in to June 2026, many effective 5 February 2026; amends UK GDPR, DPA 2018 and PECR (e.g. "recognised legitimate interests", complaints handling, some cookie changes). Sources: https://ico.org.uk/about-the-ico/what-we-do/legislation-we-cover/data-use-and-access-act-2025/ ; https://www.farrer.co.uk/news-and-insights/data-use-and-access-act-2025-five-key-changes-for-businesses/ . Policies must be drafted against the amended law. [SOLICITOR] or a data-protection consultant to confirm the current text.

### 2.2 Roles and processing inventory (PROPOSED)

| Activity | Vytalix role | Data | Lawful basis (Art. 6) | Special-category condition (Art. 9 + DPA 2018 Sch. 1) |
|---|---|---|---|---|
| Sales CRM, outreach to business contacts | Controller | Business contact data | Legitimate interests (LIA documented) | n/a |
| Newsletter, webinar registration | Controller | Name, email, employer | Consent (PECR requires consent for marketing email to individuals; corporate-subscriber rules TO VALIDATE) | n/a |
| Report interviews and surveys (professionals) | Controller | Opinions, role | Consent | n/a (avoid health data about the participant) |
| Advisory/consulting engagements | Usually neither (no personal data) or processor if client shares data | Ideally none; client documents | Contract (with client); processor terms if any personal data | Design engagements to exclude patient data; if unavoidable, DPA + client's Art. 9 basis |
| MaternaLink (in development) — UK deployment | Processor for the deploying NHS/private provider (controller); Vytalix controller for account/telemetry data | Health data, contact data, messages | Processor acts on controller instructions; controller's basis typically public task / legitimate interests + Art. 9(2)(h) health/social care with DPA 2018 Sch. 1 para 2 | Health or social care purposes; confidentiality duty; common-law duty of confidentiality also applies in the NHS |
| MaternaLink — NGO/state deployment (Nigeria) | Processor or joint controller depending on programme design | Health data | NDPA 2023 (see §12) + UK GDPR if any processing in the UK | Explicit consent likely to be required under NDPA for sensitive data; TO VALIDATE |
| Employees/contractors | Controller | HR data | Contract / legal obligation | Where relevant (e.g. health, right-to-work) |

### 2.3 Required documents and controls (P0 before MaternaLink processes any real data; P1 for services)

| Control | Trigger | Owner | Deadline (PROPOSED) |
|---|---|---|---|
| ICO registration (Tier 1) | Incorporation + CRM live | Founder | Day 14 |
| Privacy notice (website, CRM, newsletter) | Website live | Founder [SOLICITOR review] | Day 21 |
| Record of processing activities (RoPA) | ICO registration | Founder | Day 30 |
| Legitimate-interests assessment for B2B outreach | CRM live | Founder | Day 14 |
| Data-retention schedule | RoPA | Founder | Day 30 |
| Data-subject request procedure | RoPA | Founder | Day 30 |
| Breach-response procedure (72-hour ICO notification rule) | RoPA | Founder | Day 30 |
| **DPIA for MaternaLink** (mandatory: large-scale special-category data, vulnerable individuals, new technology) | Before design freeze; updated before each deployment | Product lead + DPO/adviser | Day 60 (v0.1), Day 90 (v1) |
| Data Protection Officer | Mandatory where core activities involve large-scale processing of special-category data — likely once MaternaLink is live; appoint an outsourced DPO (ESTIMATE £200–£500/month) at first deployment; until then a named "data-protection lead" (founder) | Founder | First deployment |
| Processor contracts (Art. 28) with hosting, SMS/WhatsApp gateway, email, CRM, analytics | Any vendor touching personal data | Founder | Before use with personal data |
| International transfers: UK → Nigeria (no UK adequacy decision for Nigeria) | Any Nigeria deployment or in-country team access | Founder [SOLICITOR] | Before deployment: International Data Transfer Agreement (IDTA) or UK Addendum + transfer risk assessment; consider in-country hosting so that data does not leave Nigeria at all |
| UK → EU / EU → UK | EU clients or EU hosting | Founder | EU adequacy for the UK exists (TO VALIDATE renewal status); standard clauses where required |
| Cookies / PECR | Website analytics | Founder | Consent banner only if non-essential cookies are used; recommendation: privacy-preserving analytics with no cookies (see §10) |
| Training | Any hire/contractor | Founder | On joining; annual |

### 2.4 NHS-specific data rules (apply to any MaternaLink UK deployment)
- Caldicott Principles; common-law duty of confidentiality; the deploying organisation's Caldicott Guardian sign-off.
- National Data Opt-Out applies to uses beyond individual care (e.g. research/evaluation) — TO VALIDATE applicability.
- DSPT annual submission ("Standards Met") for suppliers processing NHS patient data (see §3).
- Section 251 / Confidentiality Advisory Group approval if identifiable data is used for research without consent — avoid by design.

---

## 3. Healthcare regulation applicable in the UK

| Regime | Does it apply to Vytalix? | Position |
|---|---|---|
| **CQC registration** (Health and Social Care Act 2008) | Only if Vytalix itself carries on a regulated activity (e.g. providing treatment, triage by clinicians it employs). Advisory/consulting and software supply are not regulated activities. | v1 design keeps clinical decisions and communications ownership with the deploying provider (who is CQC-registered). If Vytalix ever employs clinicians who give advice to women, re-assess. [REG-CONSULTANT] TO VALIDATE at v2 |
| **NHS DTAC** | Applies to any digital tool bought by NHS organisations | Build the DTAC evidence pack in parallel with the MVP (see product strategy §21.3). Not a certification; assessed per buyer |
| **DCB0129** (manufacturer clinical risk management) | Applies to Vytalix as the manufacturer of MaternaLink | Appoint a Clinical Safety Officer (registered clinician with training; contract ESTIMATE £300–£600/day, 2–4 days/month during build), open a hazard log, produce a clinical safety case report before any deployment |
| **DCB0160** (deploying organisation) | Applies to the NHS trust deploying; Vytalix supports | Provide DCB0129 outputs to the trust's CSO |
| **DSPT** | Suppliers with access to NHS patient data | Register and submit before first deployment; target "Standards Met" |
| **NICE Evidence Standards Framework** | Not law; buyers use it | v1 → Tier B evidence expectations (TO VALIDATE mapping) |
| **Procurement** (Procurement Act 2023 regime; Provider Selection Regime for clinical services) | Applies to buyers | Understand direct-award thresholds; G-Cloud listing TO VALIDATE (see business model §2 #6) |
| **Consumer law** (Consumer Rights Act 2015; Digital Markets, Competition and Consumers Act 2024 consumer provisions) | E-Learning B2C sales | Refund/cancellation terms; clear pricing; auto-renewal transparency [SOLICITOR] for T&Cs |
| **Advertising** (CAP Code; ASA) | All marketing | No unsubstantiated health or efficacy claims; "MaternaLink (in development)" |

---

## 4. Medical-device regulation — UK MDR 2002, MHRA, UKCA

| Item | Position |
|---|---|
| Qualification | The UK Medical Devices Regulations 2002 (as amended) define a device by manufacturer's intended purpose. MaternaLink v1's intended-use statement (product strategy §21.1) excludes diagnosis, monitoring, prediction, prognosis and treatment, and excludes clinical decision support. **Document the qualification decision** with MHRA's software/AI-as-a-medical-device guidance cited (https://www.gov.uk/guidance/regulating-medical-devices-in-the-uk). [REG-CONSULTANT] to confirm the decision in writing — ESTIMATE £1,500–£4,000 for a qualification/classification opinion. |
| Intended-use control | Product charter rule: no feature ships that (a) applies thresholds to individual observations, (b) scores questionnaires for clinical purposes, (c) prioritises or triages by algorithm, or (d) produces a risk score, without a documented re-qualification. Change control owned by the product lead; CSO countersigns. |
| If a feature crosses the line | Likely Class I (UKCA self-declaration, MHRA registration, technical file, post-market surveillance) or Class IIa+ (UK Approved Body; ISO 13485 QMS, IEC 62304, ISO 14971, clinical evaluation). ESTIMATE £40k–£150k and 9–18 months for Class IIa. Post-market surveillance regulations in force since June 2025 (TO VALIDATE). |
| 2026 reform | MHRA has published draft Medical Devices (Amendment) Regulations 2026 (pre-market reform: international reliance, updated classification, PCCP pathway for software, cybersecurity) and consulted (Feb 2026) on extending or making indefinite the recognition of CE-marked devices (current deadlines 30 June 2028 for MDD devices, 30 June 2030 for MDR/IVDR devices). Sources: https://www.hoganlovells.com/en/publications/uk-medical-devices-reform-mhra-publishes ; https://www.lw.com/en/insights/uk-mhra-launches-consultation-on-indefinite-recognition-of-ce-marked-medical-devices ; https://www.gov.uk/guidance/regulating-medical-devices-in-the-uk . An AI-as-a-medical-device framework is expected in 2026. All TO VALIDATE at the time of any device decision. |
| v3 AI research track | Research use under ethics approval is not placing a device on the market; any clinical investigation of a device requires MHRA notification/approval and HRA/REC approval. |
| Nigeria (NAFDAC) | NAFDAC regulates medical devices; position on standalone software TO VALIDATE (§12). |

---

## 5. AI regulation

| Jurisdiction | Position |
|---|---|
| UK | No horizontal AI statute (as at the last verified position; TO VALIDATE for 2026 developments). Sector regulators apply five principles (safety, transparency, fairness, accountability, contestability) — MHRA for devices, ICO for data (automated decision-making rules under UK GDPR Art. 22 as amended by the DUAA 2025), CQC/NHS for deployment. v1 uses no clinical AI; any non-clinical AI (e.g. translation, message drafting) must be disclosed, human-reviewed and excluded from clinical content without sign-off. |
| EU (only if EU sales) | EU AI Act (Regulation (EU) 2024/1689): AI that is a medical device or a safety component is "high-risk"; obligations phase in through 2026–2027 (TO VALIDATE dates). Avoid EU deployment of any AI feature until assessed. [SOLICITOR] with EU expertise if EU sales are pursued. |
| Nigeria | National AI strategy in development; NDPA 2023 governs automated decisions on personal data (TO VALIDATE). |
| Internal policy | AI-use policy (§9) covering: no patient data into third-party AI tools; disclosure; bias review for any model; model cards; human accountability. |

---

## 6. Clinical governance

- **Clinical Advisory Group**: 3–5 clinicians (obstetrician, senior midwife, GP/public health, Nigerian clinician, lived-experience representative); terms of reference; conflicts register; minutes. Recruit from Day 30; first meeting by Day 90 (PROPOSED).
- **Clinical Safety Officer**: contracted before build week 1; owns DCB0129 outputs.
- **Content governance**: two-person sign-off (clinical author + reviewer), sources cited (NICE, RCOG, WHO, Nigeria FMoH), version and review date, content-incident route.
- **Incident management**: safety incidents to CSO within 24 hours; to deploying organisation per contract; MHRA Yellow Card if ever a device; lessons log.
- **Evaluation ethics**: service evaluation (no REC approval usually) vs research (HRA/REC approval); use the HRA decision tool; in Nigeria, NHREC/institutional ethics approval for any evaluation involving participants.

---

## 7. Safeguarding

- Adopt a safeguarding policy (adults and children) even though Vytalix does not deliver care: MaternaLink users may disclose abuse, self-harm or risk in messages; the deploying organisation's safeguarding lead owns the response; the platform must route and record, not assess.
- Under-18 users (pregnant adolescents): parental/guardian and competence considerations; product design for consent (product strategy §11 and §19).
- Staff/contractors with any user contact: DBS checks where applicable (TO VALIDATE; usually not required for non-contact software roles).
- Named safeguarding lead at Vytalix (founder until a clinical lead exists); training annually.

---

## 8. Intellectual property

### 8.1 Trademark clearance and filing
- **Conflicts identified (VERIFIED via search; registry status TO VALIDATE):** VITALIX LTD (UK company nos. 16813455 and 15155964), VITALX LTD, VYTAL(UK) LIMITED, Vytalyx Inc. (Austin, Texas; AI/blockchain health-tech; vytalyx.io), Vytalize Health (New Jersey; value-based care). Phonetic and visual similarity is high in Classes 9, 42 and 44.
- **Clearance process (Day 1–5):** (1) UK IPO trade-mark search for "Vytalix"/"Vitalyx"/"Vitalix"/"Vytalyx" in Classes 9, 35, 41, 42, 44; (2) EUIPO and USPTO knock-out searches; (3) Companies House name check; (4) domain and social-handle check; (5) written opinion from a trade-mark attorney (ESTIMATE £500–£1,500). [SOLICITOR / trade-mark attorney]
- **Decision rule:** if a registered UK/EU mark exists in Class 9/42/44 for a confusingly similar sign, or a US health-tech company with the near-identical name is active in the UK, **rename** before any brand spend. The brand system (`/docs/03_BRAND_SYSTEM.md`) is built for a low-cost rename.
- **Filing:** UK IPO fees from 1 April 2026: **£205 for one class, £60 per additional class** (previously £170/£50). Sources: https://www.reddie.co.uk/2026/03/09/uk-trade-mark-fee-increases-from-1-april-2026/ ; https://www.citma.org.uk/resources/uk-ipo-announces-first-trade-mark-fee-increase-in-nearly-three-decades-mb25.html ; https://www.ipo.gov.uk/tm3-servicesfees . Four classes (9, 41, 42, 44) ≈ £385 official fees (ESTIMATE) plus attorney fees £600–£1,200. File "MaternaLink" separately once ownership is settled (§8.3); clear it against "Maternal Link" usage by David Agunede and third parties.
- Nigeria trademark (Trademarks Registry, Federal Ministry of Industry, Trade and Investment) once a Nigeria deployment is likely: TO VALIDATE fees and process; local agent required.

### 8.2 Copyright, code and content
- Copyright in code, decks, content and this repository vests in the author (or employer). The founder's own work is personal IP until assigned to the company: sign a **founder IP assignment** at incorporation (nominal consideration). [SOLICITOR] template.
- All contractors and developers: written contracts with present assignment of IP, moral-rights waiver, confidentiality (§9). No code merged without a signed agreement.
- Clinical/educational content: authorship and licence terms with every clinical co-author.

### 8.3 MaternaLink IP — David Agunede
- **Facts:** David Agunede signs as "Founder & CEO, Maternal Link"; authored/sent the Ekiti proposal, decks, charge sheet and negotiation sheet; a Vercel prototype exists with unknown authorship (VERIFIED, FACTS_BASE §1). No agreement exists (VERIFIED gap).
- **Objective:** a signed written agreement by Day 30 (heads of terms by Day 7) that gives Vytalix clear title or an exclusive licence to the MaternaLink name, code, materials and relationships, and defines David's role.
- **Options (to be negotiated; [SOLICITOR] drafts):**

| Option | Structure | Pros | Cons | When |
|---|---|---|---|---|
| A. Assignment for equity | David assigns all MaternaLink IP to Vytalix; receives shares (vesting, good/bad-leaver) and a defined role | Clean title; investor-ready | Dilution; needs shareholders' agreement | Preferred if David wants to build together |
| B. Assignment for cash + royalty | Assignment; modest cash and/or capped royalty on MaternaLink revenue | Clean title; no dilution | Cash now; royalty complicates later financing | If David wants out |
| C. Exclusive licence | Vytalix gets exclusive, worldwide, perpetual licence; David retains title | Faster | Investors dislike licensed core IP; termination risk | Interim only (≤6 months) |
| D. Joint venture | New entity co-owned | Shares risk | Two cap tables; complexity | Not recommended pre-seed |
| E. Rebuild cleanly | Vytalix builds v1 from scratch under its own name; no use of David's code, decks or "Maternal Link" name | No dependency | Loses prototype and relationships; possible confusion with "Maternal Link" mark | If no agreement by Day 60 |

- **Heads of terms must cover:** scope of IP (code, repos, hosting accounts, domain, name, decks, proposals, data); warranties on authorship and third-party code; no real patient data warranty; transfer of the Vercel project and any accounts; the Ekiti relationship (who speaks for what); confidentiality; non-compete/non-solicit reasonableness; role, time and compensation; dispute resolution; governing law (England and Wales).
- **Prototype audit before acceptance:** code provenance, licences of dependencies, secrets in repo, data held, security posture (product strategy §25).

### 8.4 Open-source hygiene
- Licence policy: permissive (MIT/Apache-2.0/BSD) allowed; copyleft (GPL/AGPL) only with approval; keep an SBOM; automated dependency and licence scanning in CI; no copied code of unknown origin.
- Vytalix's own repos: private by default; contribution agreement for any external contributor.

### 8.5 Trade secrets and confidentiality
- NDAs before sharing product detail; access controls; "confidential — draft" marking on decks; no proprietary detail in public posts beyond what is intended.

---

## 9. Contracts and policy set

### 9.1 Contract templates (all [SOLICITOR] before first use; ESTIMATE £2k–£4k for a starter set from a fixed-fee firm or a vetted template service)

| Template | Use | Key Vytalix positions (PROPOSED) |
|---|---|---|
| Master Services Agreement (MSA) | Every consulting client | See `/docs/13_SALES_ENGINE.md` §9: fees, IP (Vytalix retains methods; client owns deliverables on payment), liability cap = fees paid in 12 months, mutual confidentiality, no patient data unless DPA, E&W law, publicity only with consent |
| Statement of Work (SOW) | Per engagement | Scope, deliverables, acceptance, milestones, change control, dependencies |
| Mutual NDA | Pre-sales, partners, investors (many investors will not sign — do not insist) | 2–3 years; carve-outs; no non-compete |
| Consultancy/associate agreement | Associates delivering client work | IR35 status determination (client-side rules for medium/large clients; TO VALIDATE) [ACCOUNTANT]; IP assignment; confidentiality; no client solicitation |
| Contractor / developer agreement | Any code or design | Present IP assignment; moral-rights waiver; open-source policy; security obligations; data-protection clause |
| Advisory board letter | Advisers | Role, time (e.g. 2 hours/month), expenses, confidentiality, conflicts, optional equity (advisory shares with vesting — TO VALIDATE EMI/unapproved option treatment) [ACCOUNTANT] |
| Data Processing Agreement (Art. 28) | Any personal data processed for a client or by a vendor | Subject matter, duration, instructions, sub-processors, security, deletion, audit |
| Pilot / evaluation agreement (MaternaLink) | Design partners | Free or cost-recovery pilot; no clinical claims; DPIA and DPA annexed; CSO named on both sides; data ownership; publication rights; termination for safety |
| Letter of intent / MoU | Partners, ministries, NGOs | Non-binding except confidentiality; no exclusivity; no financial commitment |
| Heads of terms — IP (David Agunede) | §8.3 | Non-binding except confidentiality and exclusivity of negotiation (30 days) |
| Website terms, privacy notice, cookie notice, acceptable-use policy | Website, newsletter | §10 |
| E-Learning terms of sale | B2C/B2B courses | Consumer cancellation rights (14 days unless waived for immediate digital access), refund policy, no accreditation claims |
| Employment contract + staff handbook | First hire | Statutory minimum plus IP, confidentiality, data protection; pensions auto-enrolment [ACCOUNTANT] |

### 9.2 Information-security and governance policy set (adopt at first board meeting; review annually)

| # | Policy | Minimum content | Status |
|---|---|---|---|
| 1 | Information security policy | Scope, roles, risk approach, acceptable use, incident reporting | P0 (Day 30) |
| 2 | Access control and identity | MFA everywhere, least privilege, joiner/mover/leaver, password manager | P0 |
| 3 | Device and endpoint | Encryption, auto-updates, screen lock, no personal devices for patient data | P0 |
| 4 | Data classification and handling | Public / internal / confidential / special-category; storage locations; encryption | P0 |
| 5 | Backup and business continuity | RPO/RTO targets; tested restores; offline-first sync rules for MaternaLink | P1 (Day 60) |
| 6 | Incident response and breach notification | 72-hour ICO rule; client notification; NDPC notification (72 hours, TO VALIDATE) | P0 |
| 7 | Secure development lifecycle | Code review, dependency scanning, secrets management, pen test before deployment, OWASP ASVS target | P1 |
| 8 | Supplier / sub-processor management | Due diligence, DPAs, register, annual review | P1 |
| 9 | Data protection policy + retention schedule | §2 | P0 |
| 10 | AI-use policy | §5 | P1 |
| 11 | Clinical safety management policy | DCB0129 alignment; CSO; hazard log | P1 (before build) |
| 12 | Safeguarding policy | §7 | P1 |
| 13 | Anti-bribery and corruption (Bribery Act 2010 — extraterritorial; relevant to government sales in Nigeria) | Gifts/hospitality register; agents due diligence; no facilitation payments | P0 before any government interaction |
| 14 | Conflicts of interest | Register (founder's other venture Kemek Enterprise Ltd; advisers) | P0 |
| 15 | Equality, diversity and inclusion; whistleblowing; health and safety (from first employee) | Statutory | P2 |
| 16 | Business ethics / claims policy | FACTS_BASE language rules as company policy | P0 |

---

## 10. Website terms, privacy and cookies

- **Company details** (Companies Act 2006 / E-Commerce Regulations): registered name, number, registered office and (if VAT-registered) VAT number on the website and emails once incorporated.
- **Privacy notice**: who we are; what we collect (forms, newsletter, analytics); purposes and lawful bases; retention; recipients/processors; international transfers; rights; ICO complaint route; DPO/contact.
- **Cookies**: preferred design is no non-essential cookies (privacy-preserving, cookieless analytics — TO VALIDATE that the chosen tool sets no identifiers); then no consent banner is needed, only a short cookie notice. If marketing pixels are ever added, a compliant consent tool is required (DUAA 2025 changed some low-risk cookie rules — TO VALIDATE).
- **Terms of use**: no clinical advice; content for information only; MaternaLink is in development; limitation of liability; governing law.
- **Accessibility statement**: WCAG 2.2 AA target; not a public-sector obligation but expected by NHS buyers.
- **Forms**: state where data goes and how long it is kept, at the point of capture.

---

## 11. Insurance (ESTIMATE premiums for a pre-revenue, one-person UK consultancy; TO VALIDATE with a broker; buy PI before the first paid engagement)

| Cover | Limit (PROPOSED) | Why | Annual premium (ESTIMATE) | When |
|---|---|---|---|---|
| Professional indemnity (PI) | £1m (rising to £2m–£5m when NHS contracts require) | Advisory errors; contract requirement; MSA references it | £400–£900 | Before first paid engagement (Day 14–21) |
| Public liability (PL) | £2m | Client sites, events | £100–£250 | With PI |
| Cyber and data | £500k–£1m | Breach costs, notification, extortion; NHS buyers increasingly require it | £500–£1,500 | Before any personal data at scale; P0 before MaternaLink deployment |
| Directors' and officers' (D&O) | £1m | Personal liability; investors often require on investment | £400–£1,000 | On first external investment or first non-founder director |
| Employers' liability (EL) | £10m (statutory minimum £5m) | Legally required once there is an employee (including some contractors/volunteers — TO VALIDATE) | £150–£400 | First employee |
| Product liability / technology E&O extension | £1m–£2m | Software supply to health providers | Included/added to PI package; £300–£800 | Before first MaternaLink deployment |
| Clinical trials / medical malpractice | n/a in v1 | Only if Vytalix clinicians give advice or a device study runs | TO VALIDATE | If ever applicable |
| Travel (Nigeria) | Business travel incl. medical evacuation | Founder travel | £150–£400 | Before first trip |

Total year-1 ESTIMATE: £1.5k–£3.5k (PI + PL + cyber), rising to £3k–£6k with D&O and EL.

---

## 12. International

### 12.1 Nigeria
| Item | Position | Flag |
|---|---|---|
| Corporate presence | Options: (a) contract via a local implementing partner (NGO or company) — preferred for pilots; (b) register a Nigerian subsidiary with the Corporate Affairs Commission (CAC) once a state contract is realistic; foreign-owned companies have minimum share-capital and permit requirements (business permit, expatriate quota if staff relocate) — TO VALIDATE current thresholds and CAC fees (search did not return a reliable current figure) | Nigerian counsel [SOLICITOR] |
| Data protection — NDPA 2023 | Nigeria Data Protection Act 2023 (in force 12 June 2023); regulator NDPC; General Application and Implementation Directive (GAID) 2025. **Registration** required for "data controllers/processors of major importance" — includes any entity processing personal data of **more than 200 data subjects in six months** (per NDPC guidance) — so MaternaLink at any pilot scale must register; annual compliance audit returns are filed via a licensed Data Protection Compliance Organisation (DPCO); penalties for late registration (waiver possible within 6 months of incorporation). Sources: https://ndpc.gov.ng/wp-content/uploads/2025/07/NDP-ACT-GAID-2025-MARCH-20TH.pdf ; https://www.lexology.com/library/detail.aspx?g=84330fb0-4a3f-4588-8a60-89951306f7e5 ; https://kpmg.com/ng/en/home/insights/2024/03/nigeria-data-protection-commissions-guidance-notice-on-registration-of-data-processors-controllers-of-major-importance.html ; https://ndpc.gov.ng/dpco-registration-requirements/ . Fees TO VALIDATE. Sensitive (health) data: explicit consent and other conditions; DPO likely required for major-importance entities; cross-border transfer rules (adequacy/consent/contract) apply to Nigeria → UK flows | Nigerian counsel; DPCO |
| NAFDAC | Medical-device regulator; software treatment TO VALIDATE; v1 non-diagnostic scope intended to stay outside | [REG-CONSULTANT] |
| NHREC | National Code of Health Research Ethics; any evaluation with participants needs NHREC-registered committee approval (state/institutional HREC) | Before any pilot evaluation |
| Telecoms (NCC) | Sender-ID registration, DND rules, bulk SMS licensing via gateway; WhatsApp Business policy | Gateway vendor to confirm |
| Anti-bribery | UK Bribery Act 2010 applies to Vytalix conduct abroad; Nigerian ICPC/EFCC laws; agents and "facilitators" need due diligence and written contracts | Policy §9.2 #13 |
| Tax | Withholding tax on service fees paid from Nigeria (rates TO VALIDATE); UK–Nigeria double-tax treaty; VAT on digital services; permanent-establishment risk if founder works in-country for extended periods | [ACCOUNTANT] with Nigeria expertise |
| FX and payment | Invoice in GBP/USD; mobilisation ≥30% before work (sales engine §16); FX controls TO VALIDATE | — |

### 12.2 South Africa (if scored as third market)
- POPIA (in force 1 July 2021): Information Regulator; information-officer registration; special personal information (health) requires authorisation/consent conditions; cross-border transfer rules (s.72); prior authorisation for certain processing. Health Professions and NDoH digital-health strategy; SAHPRA for devices (software TO VALIDATE). [SOLICITOR] South African counsel.

### 12.3 Kenya (if scored as third market)
- Data Protection Act 2019: Office of the Data Protection Commissioner; **registration of data controllers/processors** (mandatory above thresholds; fees TO VALIDATE); health data is sensitive personal data; Health Data Regulations; cross-border transfer conditions (s.48–49). Kenya Digital Health Act 2023 (TO VALIDATE current status) governs health information systems; Pharmacy and Poisons Board for devices. [SOLICITOR] Kenyan counsel.

### 12.4 EU
- Only relevant if EU customers/data: EU GDPR representative (Art. 27) if no EU establishment; EU AI Act (§5); EU MDR for devices; CE marking.

---

## 13. Risk register (legal, regulatory and compliance)

Scale: Likelihood L/M/H · Impact L/M/H · Score = L×I (1–9)

| # | Risk | L | I | Score | Mitigation | Owner | Review |
|---|---|---|---|---|---|---|---|
| R1 | MaternaLink IP dispute or no agreement with David Agunede | H | H | 9 | Heads of terms Day 7; solicitor Day 10; Option E fallback at Day 60 | Founder | Weekly |
| R2 | Name/trademark conflict forces rename or opposition | M | H | 6 | Clearance before spend; attorney opinion; rename plan | Founder | Day 5, then monthly |
| R3 | Over-claiming (clinical/AI/partner) in materials or posts | M | H | 6 | FACTS_BASE language policy; deck review; claims sign-off | Founder | Every publication |
| R4 | Feature creep makes MaternaLink a medical device without a pathway | M | H | 6 | Intended-use control; qualification decision; CSO countersign | Product lead + CSO | Each release |
| R5 | Processing patient data without lawful basis/DPIA (e.g. prototype holding real data) | M | H | 6 | Prototype audit; no real data rule; DPIA before any deployment | Founder | Day 30 |
| R6 | Breach or security incident on a weak prototype | M | H | 6 | Move to controlled hosting; MFA; pen test; cyber insurance | Founder/CTO | Day 30 |
| R7 | Selling without entity/insurance → personal liability | H | M | 6 | Incorporate Day 14; PI before first engagement; short pre-incorporation contracts | Founder | Day 14 |
| R8 | Nigeria: NDPA non-registration, unlawful transfers, ethics gaps | M | M | 4 | Local partner; NDPC registration; in-country hosting; NHREC approval | Founder + counsel | Before pilot |
| R9 | Bribery/agent risk in government sales | L | H | 3 | Policy; due diligence; no agents on success fees without counsel | Founder | Before any agent |
| R10 | IR35 / employment-status misclassification of associates | M | M | 4 | Status determinations; written contracts; accountant advice | Founder | Per associate |
| R11 | Consumer-law breach in e-learning sales | L | M | 2 | Terms reviewed; cancellation rights; no accreditation claims | Founder | Before launch |
| R12 | SEIS/EIS eligibility lost through structure or activity | M | M | 4 | Advance assurance; accountant review before any non-qualifying activity | Accountant | On incorporation |
| R13 | Contractor code with incompatible open-source licences | M | M | 4 | Licence policy; scanning; contractor warranties | CTO | Each release |
| R14 | Conflicts of interest with founder's other venture (Kemek) | M | L | 2 | Register; time-allocation rule; separate CRMs | Founder | Quarterly |
| R15 | Regulatory change (MHRA 2026 reform, DUAA, NDPA guidance) | H | M | 6 | Quarterly regulatory watch; adviser check before each major release | Founder | Quarterly |

---

## 14. Compliance calendar (first 12 months)

| When | Action | Priority | Professional |
|---|---|---|---|
| Day 1–5 | Trademark/name clearance; IP heads of terms with David Agunede | P0 | Attorney; solicitor |
| Day 5–14 | Incorporate (£100); bank; accountant; founder IP assignment; conflicts register; anti-bribery and claims policies | P0 | Accountant; solicitor |
| Day 14 | ICO registration (£52); LIA for outreach; PI + PL insurance quotes | P0 | — |
| Day 21 | Website legal pages; privacy notice; MSA/SOW/NDA sent to solicitor | P0 | Solicitor |
| Day 30 | IP agreement signed; prototype audit complete; security policy set (P0 items); RoPA; SEIS/EIS advance-assurance application | P0 | Solicitor; accountant |
| Day 45 | Trademark application filed (£205 + £60/class); CSO identified; regulatory qualification opinion commissioned | P1 | Attorney; reg consultant |
| Day 60 | DPIA v0.1; clinical safety management policy; contractor agreements in use; Cyber Essentials self-assessment started (£300 + VAT micro tier; sources: https://www.ncsc.gov.uk/cyberessentials/overview ; https://www.isms.online/cyber-essentials/cost/ ) | P1 | — |
| Day 90 | Cyber Essentials certified; DSPT registration; DTAC evidence pack skeleton; advisory board letters | P1 | — |
| Month 6 | Cyber Essentials Plus (ESTIMATE £1,500–£3,000 + VAT); pen test (ESTIMATE £3k–£8k); DPO appointed if deployment imminent; D&O on first investment | P1 | Certification body |
| Month 9 | NDPC registration via DPCO if Nigeria pilot; Nigerian counsel; IDTA/transfer risk assessment | P1 | Nigerian counsel |
| Month 12 | Annual policy review; confirmation statement (£50); ICO renewal; insurance renewal; ISO 27001 gap assessment (certification later, ESTIMATE £8k–£20k) | P2 | Accountant |

---

## Priorities / Risks / Next actions

**Priorities**
1. Resolve IP with David Agunede (heads of terms Day 7; signed Day 30) and clear the name (Day 5) — nothing else is safe until these are done.
2. Incorporate, insure, register with the ICO, adopt the P0 policy set (Day 14–30).
3. Lock MaternaLink's intended use and clinical-safety governance before any build work (CSO, hazard log, DPIA, qualification opinion by Day 60).

**Risks** — see §13; the top four (R1, R2, R3, R4) are all founder-controllable within 60 days.

**Next actions**
| Action | Owner | Deadline | Professional |
|---|---|---|---|
| Run UK IPO/EUIPO/USPTO/Companies House searches; brief a trade-mark attorney | Founder | Fri 18 Sept 2026 | Attorney |
| Hold the David Agunede conversation; send draft heads of terms | Founder | Wed 16 Sept 2026 | Solicitor from Day 10 |
| Shortlist 3 fixed-fee start-up solicitors and 3 accountants; instruct one each | Founder | Fri 18 Sept 2026 | — |
| Incorporate and open bank account | Founder | Fri 25 Sept 2026 | Accountant |
| ICO registration; PI/PL insurance bound | Founder | Fri 2 Oct 2026 | Broker |
| Adopt P0 policies at first board minute | Founder | Tue 13 Oct 2026 | — |
