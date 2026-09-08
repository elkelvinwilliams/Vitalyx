# VYTALIX — Business Plan

**Technology for Life** · Version 1.0 · 8 September 2026 · Status: PROPOSED (pre-formation plan; no figure is an actual)
Owner: Founder · Governed by `/FACTS_BASE.md` (labels KNOWN / VERIFIED / ASSUMPTION / ESTIMATE / PROPOSED / TO VALIDATE apply throughout). This plan stitches together the strategy documents in `/docs/`; it references them by path rather than repeating them, and it adds nothing that is not in them.

## Executive view

1. Vytalix is a pre-seed, pre-formation UK health-technology group with four pillars — Advisory, Consulting, Health Solutions and E-Learning — built in two layers: a **cash layer** (services that can invoice within 90 days of incorporation) and an **equity layer** (MaternaLink, in development, which consumes cash for 18–30 months before it can earn).
2. Today there is a name (spelled two ways), a brief, one concept deck, one unsolicited government proposal, one prototype of unknown provenance and no legal entity, revenue, customers, partners, approvals or team beyond the founder (VERIFIED). The audit scores the business 11/100 as a pre-formation score, not a judgement on the idea (`/docs/00_MASTER_AUDIT.md`).
3. The plan for the next 36 months: incorporate and clear the name; document MaternaLink IP; sell founder-led services to fund the company (base case £118k in year 1, range £55k–£210k, ESTIMATE); close the four product gates; win an unpaid UK design partnership and an NGO-funded Nigerian cohort; raise a £150k–£300k SEIS/EIS pre-seed on evidence (ESTIMATE); reach paid pilots in months 18–36.
4. MaternaLink is re-based from an unvalidated "AI risk score" to a non-diagnostic maternal care-coordination, communication, education and monitoring-support platform (v1), with the AI concept retained as a gated research track (v3+). This is the single decision that makes the venture fundable, sellable and regulatorily safe.
5. The plan collapses if either of two things fails: the founder cannot sell and deliver 8–10 billable days a month, or the MaternaLink IP cannot be brought into the company on acceptable terms. Both are tested within 90 days, with explicit kill/pivot signals.

---

## 1. Executive summary

Vytalix ("Technology for Life") is a UK health-technology group being formed to advise, build, deliver and teach, so that technology earns its place in care. It will operate as one English company with four divisions:

- **Vytalix Advisory** — founder-led strategic advice on digital-health strategy, UK↔Africa market entry, regulation and funding readiness.
- **Vytalix Consulting** — ten fixed-price packages: discovery sprints, business cases, digital maternity readiness, DTAC and evidence readiness, market-entry playbooks, health-inequalities reviews and programme evaluation.
- **Vytalix Health Solutions** — products designed for real care settings, starting with **MaternaLink (in development)**, a non-diagnostic maternal care-coordination and communication platform for NHS and low-connectivity settings.
- **Vytalix E-Learning** — practical courses, a subscription library and corporate and university licences on digital health, care coordination and safe AI.

The problem Vytalix addresses is a coordination problem before it is a clinical one. In the UK, public inquiries into maternity services (Ockenden 2022; Kirkup 2022) repeatedly found failures to listen to women, to escalate and to hand over, alongside persistent mortality disparities by ethnicity and deprivation reported by MBRRACE-UK. In Nigeria, the largest absolute maternal-death burden in the world is driven by delays in seeking, reaching and receiving care. Both are documented in `/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §2, with every citation marked TO VALIDATE against the live source before external use.

The business model is sequenced deliberately: **services fund the company; MaternaLink is the equity story** (FACTS_BASE A6). Services must reach roughly £10k/month within six months to pay for the founder's time and the legal, clinical-safety and data-protection groundwork the product needs (`/docs/01_BUSINESS_MODEL.md` §1). First product revenue is realistically a paid UK pilot or an African donor-funded programme in months 18–30, at £20k–£150k per pilot (ESTIMATE).

Funding follows the same sequence (FACTS_BASE A7): bootstrapped services and grants → a £150k–£300k SEIS/EIS pre-seed from angels and impact investors once the entity, IP and first evidence exist (ESTIMATE) → an impact or health-tech seed round on pilot evidence in 2028. A scenario model (Conservative / Base / High-growth, January 2027 to December 2029) is built by `/finance/build_model.py`; its narrative summary is `/docs/08_FINANCIAL_MODEL.md` (to be written from the workbook). No number in this plan is an actual.

What must be true, and how it is tested, is in §15. The 90-day execution plan and the first-30-days plan are referenced from `/README.md` (`/docs/18_90_DAY_EXECUTION_PLAN.md`, `/docs/19_FIRST_30_DAYS.md` — to be written).

## 2. Company and structure

### 2.1 Current state (VERIFIED, from `/FACTS_BASE.md` §1)
- No registered company found for "Vytalix" or "Vitalyx" (registration status TO VALIDATE); similar names exist (VITALIX LTD ×2, VITALX LTD, VYTAL(UK) LIMITED in the UK; Vytalyx Inc. and Vytalize Health in the US), creating naming and trademark risk.
- No website, domain, trademark, bank account, employees, contracts, revenue, customers, grants, partnerships, ethics approvals, regulatory classification, ICO registration or insurance.
- The founder also runs a separate venture, Kemek Enterprise Ltd (property finance), which is a declared interest and is kept entirely separate.
- The repository spelling "Vitalyx" is treated as a typo; the trading name is "Vytalix" (FACTS_BASE A1).

### 2.2 Proposed structure (`/docs/02_GROUP_STRUCTURE.md` §1–§2)
- **One company now, not a group:** "Vytalix Group Ltd" (reserve: "Vytalix Health Technologies Ltd"), a private company limited by shares in England and Wales, with the four pillars as divisions with their own P&L owner, cost centre and charter. A holding-company structure is a Phase 2 decision with explicit triggers (first live deployment holding real patient data; product-only investment; a contract requiring a dedicated entity; regulated device status; a product co-founder).
- **All IP assigned to the company:** founder IP at incorporation; MaternaLink IP by agreement (§8.3); contractor IP by clause.
- **Registrations in month 1:** Companies House, HMRC, ICO fee, SEIS/EIS advance assurance, professional indemnity and public liability insurance, a business bank account (all TO VALIDATE for exact requirements).
- **Nigeria:** contract through a local implementing partner until a signed pilot or funded programme exists; a local entity is trigger-based.

### 2.3 Share structure (PROPOSED; `/docs/02_GROUP_STRUCTURE.md` §2)
Founder holds 100% at incorporation. Planned, written, vested dilution over the first 12–15 months: 8–12% for the MaternaLink IP settlement (vesting), a 10–15% option pool, and 8–15% for a £150k–£300k SEIS/EIS pre-seed (ESTIMATE; pre-money placeholder £1.5m–£4m, TO VALIDATE against comparable rounds). No equity is promised verbally.

## 3. Vision, mission and values

**Vision (PROPOSED):** Technology for Life. A world in which every person — beginning with every mother — is connected to care that knows them, hears them and acts in time, wherever they live.

**Mission (25 words, PROPOSED):** Vytalix is a UK health-technology group that helps health organisations, founders and governments make technology work in real care — beginning with maternal care coordination.

**Brand promise:** Technology that earns its place in care (`/docs/03_BRAND_SYSTEM.md` §2).

**Values:** Truth before traction · Safety before speed · Build with, not for · Both markets, one standard · Evidence is the product.

**Division missions** are set out in `/docs/02_GROUP_STRUCTURE.md` §5; the five mission variants (one sentence, 25 words, website, investor, healthcare organisation) are in §6 of the same document and are the only approved wordings.

## 4. Market

`/docs/05_MARKET_STRATEGY.md` scores sixteen markets on eleven criteria with a feasibility gate; the findings that drive this plan:

| Market | Role | Score (raw / feasibility-adjusted, desk ESTIMATE) | What it means for the plan |
|---|---|---|---|
| United Kingdom | Home and credibility market | 67.9 / 67.9 | Services now; product design partnership months 6–18; paid pilots months 18–36. NHS product sales cycles are 9–18 months; policy pull (MBRRACE-UK disparities, national maternity investigation, digital maternity record standard) is strong but slow. |
| Nigeria | Volume and impact market | 61.3 / 55.2 | Only African market with a live conversation (Ekiti, status unknown). Ekiti has a funded incumbent (mDoc's Digital Mom Project, MSD for Mothers-funded, ~24,000 women onboarded, 500+ providers trained as of January 2026 — VERIFIED via public reporting). The play is partner, complement or move state — never displace on price. NGO- and donor-funded cohorts preferred until willingness to pay is validated. |
| Kenya | Third market, 2028+ | 58.9 / 47.1 | Strongest digital and mobile-money rails; the incumbent benchmark (Jacaranda Health's PROMPTS, <$1 per mother) sets the price expectation; position on facility coordination and referral, not messaging. |
| Ghana, Rwanda | Prepare, do not enter until 2028 | 54.6 / 38.2; 54.5 / 32.7 | Via a regional implementing partner after evidence. |
| Europe, Gulf, North America, South Asia, Indonesia, South Africa, Ethiopia | Consulting and e-learning only | ≤ 26.7 adjusted | Never enter direct with the product before 2029; the US naming collision blocks any North American product ambition until resolved. |

Founder capacity rule: no more than two active product markets before 2028; each additional market costs ~20 unbilled founder days a year (ESTIMATE).

Market size figures for UK maternity digital spend, Nigerian state health budgets and donor flows are not stated here because none has been verified in this build; they are TO VALIDATE and will be added to `/docs/05_MARKET_STRATEGY.md` with sources before any external use.

## 5. Customers

Six segments, in priority order, from `/docs/13_SALES_ENGINE.md` §1 (a fuller treatment is planned in `/docs/06_CUSTOMER_SEGMENTS.md`):

| # | Segment | Buyer | What they buy | Typical deal (ESTIMATE) | Cycle (ESTIMATE) |
|---|---|---|---|---|---|
| S1 | UK digital-health start-ups and scale-ups (pre-seed to Series A) | Founder / COO | Go-to-market, NHS readiness, regulatory pathway, investor readiness | £2.5k–£5k/month retainer; £7.5k–£15k sprint | 2–6 weeks |
| S2 | Health-tech investors, accelerators, incubators | Programme director / partner | Portfolio workshops, due-diligence support, cohort training | £5k–£20k per programme | 4–8 weeks |
| S3 | NHS-adjacent organisations (ICBs, trusts' innovation teams, Health Innovation Networks, charities) | Innovation lead / programme manager | Digital-maternity research, procurement-readiness, inequalities reviews, training | £5k–£25k project | 8–16 weeks |
| S4 | African ministries, state governments, NGOs, donors | Commissioner / programme officer | Digital-health strategy, programme design, MaternaLink pilot scoping | £10k–£50k study; pilot TO VALIDATE | 3–9 months |
| S5 | Corporates, employers, insurers with women's-health agendas | HR / benefits / CSR lead | Education content, programme design | £5k–£15k | 4–10 weeks |
| S6 | Individual learners and health professionals | Nurse, midwife, health-tech professional | Courses, subscriptions | £49–£299 per learner | Self-serve |

Rule: the founder spends at least 60% of selling time on S1–S2 in the first 90 days (shortest cycle, cash first), at most 25% on S3–S4, and treats S5–S6 as opportunistic until Q2 2027.

For MaternaLink (in development), the buyers and users are personas P1–P6 in `/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §3: the expectant mother in Lewisham and in Ikere-Ekiti; the community midwife; the consultant obstetrician and clinical lead; the state Director of Family Health; the NGO programme officer. These are illustrative (ASSUMPTION) and are validated in discovery with at least 20 women and 10 professionals per market.

## 6. Competition

A full competitive-intelligence document is planned at `/docs/11_COMPETITIVE_INTELLIGENCE.md`; the competitive facts established in this build are:

| Arena | Who is there (public information; no relationship claimed) | Vytalix position |
|---|---|---|
| Nigeria state maternal digital programmes | mDoc "Digital Mom Project" (CompleteHealth platform, NaviHealth AI), MSD for Mothers-funded, live in Lagos and Ekiti (VERIFIED) | Complement, not compete: care-coordination/handover and CHEW-workflow layer; interoperability (DHIS2 exports); or a different state. One complementarity conversation is planned. |
| African maternal messaging programmes | Jacaranda Health PROMPTS (Kenya; 2.8m+ women; <$1 per mother), MomConnect-style national programmes (per `/docs/05_MARKET_STRATEGY.md`) | Price expectation for messaging alone is near zero; Vytalix prices the coordination and facility workflow to the programme, not the message. |
| UK maternity record systems | Maternity EPRs such as BadgerNet, Euroking, K2 (market shares TO VALIDATE) | Record systems, not relationship systems; MaternaLink does not touch the EPR in v1 and provides pasteable summaries; integration is a v2 promise. |
| UK employer women's-health benefits | Established fertility and family benefits vendors (e.g. Peppy — TO VALIDATE) | Employer route is a later, non-clinical channel; not a launch market. |
| Digital-health consultancies | Large consultancies with NHS frameworks; boutique digital-health advisers; freelancers | Vytalix's differentiation is the UK–Africa corridor, fixed-price packages with published methods, and the safety-first product posture. The "both sides of the corridor" claim is usable only once the founder's credentials and first engagements support it (TO VALIDATE). |
| Name collisions (not competitors, but confusion risk) | Vytalyx Inc. (US health-tech), Vytalize Health (US), VITALIX LTD (UK) | Trademark clearance before brand spend; rename within five days if clearance fails (`/docs/02_GROUP_STRUCTURE.md` §7). |

Buildable advantages (PROPOSED): artefacts rather than adjectives (intended-use statement, hazard log, DPIA template, DTAC readiness pack in the first meeting); designing for what already exists in-country; a published research report as the credibility anchor (`/docs/14_MARKETING_AND_CONTENT_ENGINE.md` §9); and a stage-honest brand that investors and trusts can diligence without surprises.

## 7. Products and services

### 7.1 Services (cash layer)
The full catalogue with scope, deliverables, duration, price, buyer and outcomes is `/assets/SERVICE_CATALOGUE.md`; pricing rules are in `/assets/PRICING_STRUCTURE.md`. In summary (all ESTIMATE, ex-VAT):

- **Advisory:** founder-led days £1,200–£1,800; retainers £2,500–£6,000/month (standard £4,000 for two days, three-month minimum); fractional Chief Digital/Strategy Officer £5,500–£8,000/month.
- **Consulting:** C1 Digital Health Discovery Sprint £14,000 · C2 Business Case & Funding Sprint £18,000 · C3 Digital Maternity Readiness Review £24,000 · C4 UK Market-Entry Playbook £22,000 · C5 Africa Market-Entry & Partner Scan £20,000 · C6 DTAC & Evidence Readiness Sprint £15,000 · C7 Grant & Investor Readiness Sprint £9,500 · C8 Health Inequalities & Maternity Outcomes Review £28,000 · C9 Programme Evaluation Lite £26,000 · C10 Corporate Workshop £4,000.
- **Rules:** fixed price, fixed scope, written change control; 50% on signing under £20k, 40/30/30 above; every engagement produces a reusable asset; no patient data; packages gated on capability (clinical adviser, Clinical Safety Officer, in-country associates, community partners) are not sold until it exists.

### 7.2 E-Learning (cash layer, from month 9, ESTIMATE)
Four courses (Health-Tech Commercialisation in the NHS and Grants & Investor Readiness first, as founder-authored and lowest clinical risk; Digital Maternity Essentials and Care Coordination in Low-Resource Settings from months 12–15 with clinical co-authors), a £19/month subscription library, corporate licences (£2,500–£25,000) and university and co-branded NGO licences (TO VALIDATE). Content build £8k–£15k per course; year-1 target from launch £20k–£47k (ESTIMATE). No accreditation is held or claimed; the route to accreditation is budgeted at £3k–£8k and 6–9 months (`/docs/01_BUSINESS_MODEL.md` §6).

### 7.3 Revenue streams (`/docs/01_BUSINESS_MODEL.md` §2)
Of fifteen streams examined, four are launchable now (consulting projects, advisory retainers, grant preparation, and — from month 6 — corporate training and partnerships); e-learning and UK public contracts follow at 6–12 months; everything product-related (implementation, SaaS, licensing, government programme contracts, white-label, technology licensing) is 12–24 months away and gated by IP ownership, regulation and evidence.

## 8. MaternaLink (in development)

### 8.1 What exists (VERIFIED, `/FACTS_BASE.md` §1)
A 13-slide concept deck (Oct/Nov 2025) proposing a multimodal AI "Maternal Instability Score"; a March 2026 proposal to the Ekiti State Ministry of Health signed by David Agunede as "Founder & CEO, Maternal Link" (Phase 1 15,000 women at £4.5m, i.e. £300 per woman per year; outcome unknown); a live prototype dashboard on Vercel of unknown maturity, hosting, security and data handling; an "Investors PPT". No data, no model, no validation, no clinical partner, no ethics approval, no deployment.

### 8.2 The re-basing decision (FACTS_BASE A4; `/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §1)
v1 is a **non-diagnostic maternal care-coordination, communication, education and monitoring-support platform**: enrolment and granular consent; personalised contact schedules and reminders (NICE NG201 in the UK; WHO eight-contact model in Nigeria); clinically signed-off education by gestation, language and literacy; secure asynchronous messaging with a named human owner and an acknowledgement SLA; a self-recorded diary displayed, not interpreted; a care-team console; a structured handover summary; a single-entry escalation log; missed-contact lists; a programme dashboard with CSV and DHIS2-compatible exports; web app (offline-capable) plus SMS. It escalates unread messages to humans; it never decides clinical urgency. The intended-use statement (§21.1 of the product strategy) is designed to keep v1 outside medical-device classification, TO VALIDATE with regulatory counsel.

The AI concept is retained as a **v3 research track** (month 15+; not a product commitment) with prerequisites in order: data partnership with an NHS trust or academic unit and a Nigerian teaching hospital under approvals; retrospective development with pre-registered protocols and fairness analysis; MHRA qualification and classification (expect Class IIa or higher, TO VALIDATE); prospective validation; only then any clinical claim. Presented to investors as an option costing an ESTIMATE 24–36 months and £1.5m–£4m.

### 8.3 The four gates before anything is sold
1. **IP ownership documented.** The relationship between Vytalix, the founder, David Agunede and the MaternaLink IP is undocumented (VERIFIED gap). Preferred route: IP assignment for 8–12% vested ordinary shares with warranties and a defined role; fallback: exclusive licence with an option to acquire; a joint venture is not recommended (`/docs/02_GROUP_STRUCTURE.md` §3). A solicitor is instructed before any term is offered; a mutual standstill and confidentiality letter is the week-one step. If no agreement by month 4, the fallback is a clean-room rebuild of v1 under Vytalix.
2. **Prototype audited** for code ownership and licences, real data, security and architecture fit (`/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §25). Until then it is a demo asset, not a product asset, and processes no real data.
3. **Clinical Safety Officer appointed and DCB0129 hazard log opened** (ESTIMATE 0.2 FTE contracted); a Clinical Advisory Group of 3–5 members formed.
4. **DPIA and lawful-basis analysis completed** under UK GDPR and the Nigeria Data Protection Act 2023; ICO registration once incorporated.

### 8.4 Product and commercial roadmap (PROPOSED; `/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §22–§23; `/product/MATERNALINK_ROADMAP.md`)
- **Q4 2026:** discovery (20 women + 10 professionals per market), PRD sign-off, gates 1–4 in progress; Ekiti status call; mDoc complementarity conversation; two alternative states scored.
- **Q1 2027:** MVP complete (weeks 7–16 from funded start); penetration test; safety case v1; DTAC readiness pack; grant applications; one NGO programme LOI.
- **Q2 2027:** v1.0 live in a UK service evaluation (n≈50–150); first paid pilot (private maternity or NGO programme licence, £10k–£40k ESTIMATE); Nigeria pilot design.
- **Q3 2027:** Nigeria pilot start (1–2 LGAs, 500–2,000 women), funded by donor or state at £0.1m–£0.3m (ESTIMATE); USSD and DHIS2 export.
- **Q4 2027 – Q2 2028:** v2 (FHIR read facade, partner access, mental-health instruments if cleared, Hausa/Igbo/Pidgin); UK feasibility study (two sites); first NHS paid-contract discussion; G-Cloud listing (TO VALIDATE); 2–3 UK sites; one state-scale agreement (10k+ women); seed round on evidence.
- **Q3 2028:** ARR scenario £0.4m–£0.9m (ESTIMATE, not a forecast).

### 8.5 Pricing (ESTIMATE; `/assets/PRICING_STRUCTURE.md` §5)
UK design partnership £0–£5k; first paid pilot £10k–£40k; UK trust pilot £20k–£60k; UK site licence £40k–£120k/yr plus implementation £15k–£40k; private maternity £30–£80 per woman per episode; Africa platform layer £6–£40 per woman per year plus SMS pass-through, implementation £50k–£150k; NGO programme £8k–£60k/yr; insurers £3–£12 per enrolled pregnancy. The Ekiti £300/woman/year figure is unvalidated and retired; a credible Phase 1 programme is £0.4m–£0.6m per year, not £4.5m.

## 9. Go-to-market

### 9.1 Sales (`/docs/13_SALES_ENGINE.md`)
One seller (the founder) selling advisory retainers, fixed-scope sprints and, later, e-learning; MaternaLink only as a pilot conversation. 90-day targets (PROPOSED): 150 qualified contacts, 40 discovery calls, 12 proposals, 3 signed engagements, £15k–£30k contracted (ESTIMATE). Weekly minimums from week 3: 40 new contacts, 20 conversations, 5 discovery calls, 2 proposals. Tooling: HubSpot Free (or Notion), LinkedIn, Google Workspace, under £100/month. Pipeline stages, lead scoring, the 30-minute discovery call, follow-up sequences and the MSA/SOW structure are defined there; the sales deck is `/assets/SALES_DECK.md` and the proposal template `/assets/PROPOSAL_TEMPLATE.md`.

### 9.2 Marketing (`/docs/14_MARKETING_AND_CONTENT_ENGINE.md`)
Founder-led, LinkedIn-first, evidence-led; the only marketing KPI that matters in the first 90 days is qualified conversations booked for the sales engine. Five content pillars (digital maternity and inequality; UK go-to-market and regulation; the UK–Africa corridor; building Vytalix in public; learning and method). Supporting assets: website (`/website`), fortnightly newsletter, one research report ("The State of Digital Maternal Care Coordination: UK and Nigeria, 2026", week 9), one webinar (week 10), three long-form articles. Cost £0–£150/month tooling plus £2k–£4k optional one-off (ESTIMATE); no paid media before month 6. The 12-week calendar is `/assets/CONTENT_CALENDAR.csv`; the 90-day campaign is `/assets/LAUNCH_CAMPAIGN.md`.

### 9.3 Partnerships (`/assets/PARTNERSHIP_DECK.md`; `/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §10–§14; a fuller plan is planned at `/docs/12_PARTNERSHIP_STRATEGY.md`)
- UK: one maternity service as an unpaid design partner via Health Innovation Networks, LMNS leads and clinical advisers (ten approaches; LOI by month 9); university maternity research groups for evaluation methods and the later research track; content partners for signed-off education (licensing TO VALIDATE).
- Nigeria: an implementing NGO with an existing cohort; one status conversation with the Ekiti ministry; one complementarity conversation with mDoc; state scorecard for Ondo, Osun, Oyo, Kwara (Yoruba content reuse) and Kaduna/Kano (burden).
- Channels for later: messaging gateways, telecoms and HMOs (year 2); accelerators and consultancies for referrals and sub-contracting (from month 6).
- Rule: an LOI or MoU is described as an LOI or MoU, never as a partnership, in investor and marketing material.

### 9.4 Entry sequence (`/docs/05_MARKET_STRATEGY.md` §8)
Wave 0 (now–month 6): UK services only. Wave 1 (months 6–18): UK design partner; Nigeria NGO/donor cohort or Ekiti complementarity. Wave 2 (months 18–36): UK paid pilots; Kenya county or NGO programme. Wave 3 (2028+): Ghana, Rwanda via a regional partner; a second Nigerian state. Each wave has go and no-go signals; e.g. fewer than one signed engagement by month 3 triggers the services no-go review.

## 10. Operations

### 10.1 Delivery model
Founder-led delivery with a hard cap of ten billable days a month; associates engaged only on signed work (no bench); a part-time product lead only from services surplus or grant income. Every engagement follows the 14-day onboarding in `/docs/13_SALES_ENGINE.md` §10 and produces at least one reusable asset. Advisory and consulting process no patient data.

### 10.2 Technology (`/docs/07_TECHNOLOGY_ARCHITECTURE.md`)
A lean year-1 stack: static website, free-tier CRM, Google Workspace, a course platform from month 9, and a MaternaLink build with UK-region hosting and a Nigeria deployment-cell option; a group-wide AI/LLM usage policy (no patient data to model endpoints in v1; contractual no-training clauses); cybersecurity, data-governance, backup and continuity principles; and an explicit "what not to build yet" list.

### 10.3 Legal, regulatory and compliance (`/docs/15_LEGAL_AND_REGULATORY.md`)
Year-1 budget ESTIMATE £9k–£18k: solicitor fees for IP and shareholder documents £4k–£8k; trademark £1.5k–£3k; insurance £1.5k–£3.5k (professional indemnity, public liability, cyber); ICO, Cyber Essentials and registrations £0.5k–£1k; contract templates £2k–£4k. Before any MaternaLink deployment: DPIA, ICO registration, Clinical Safety Officer, DSPT and Cyber Essentials; before any Nigerian deployment: NDPA 2023 registration where required and NHREC ethics approval for any evaluation. Anti-bribery policy applies to all Nigeria dealings (UK Bribery Act).

### 10.4 Founder operating cadence
A weekly rhythm — selling first, content batched, Friday pipeline clean, monthly KPI review — is specified in `/docs/17_FOUNDER_OPERATING_SYSTEM.md` (to be written); organisation design and SOPs in `/docs/16_ORGANISATION_AND_SOPS.md` (to be written); KPI and pipeline trackers in `/operations/` (to be created). A time-allocation rule between Vytalix and the founder's other venture (e.g. 70% Vytalix) is adopted in week 2 (`/docs/00_MASTER_AUDIT.md` §5, problem 10).

## 11. Team and governance

### 11.1 Team today (KNOWN)
The founder, [Founder name — confirm display name], is the only person. Role, time commitment, capital available and domain expertise are TO VALIDATE and must be stated in this section before the plan is shown externally. No employees, associates or advisers are appointed.

### 11.2 Planned roles (PROPOSED; `/docs/02_GROUP_STRUCTURE.md` §5; `/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §20)
- Clinical Safety Officer (contracted, ~0.2 FTE) — before any MaternaLink build.
- Product Lead / CTO (fractional from months 4–6; equity-based) — after the IP settlement and prototype audit.
- Clinical adviser (midwife or obstetrician) — month 1–2; unlocks C3, C8 and pilot conversations.
- Consulting Director — from services surplus, months 9–15.
- Learning Lead (contracted) — month 9+.
- In-country associates (Nigeria, later Kenya) — on signed work.
- Option pool sized for a CTO/product lead (4–6%), clinical lead (1–2%), advisers (0.25–0.5% each ×5), first three hires (2–3%).

### 11.3 Governance (`/docs/02_GROUP_STRUCTURE.md` §4)
- Statutory board: founder plus one independent non-executive director (unpaid or £3k–£6k/yr, ESTIMATE); monthly; reserved matters include share issues, contracts over £50k, any clinical or regulatory claim in external material, any government proposal.
- Advisory board: six profiles — consultant obstetrician; senior/digital midwife; NHS digital and commissioning leader; Nigerian health-system leader; regulatory and clinical-safety adviser; health-tech operator/investor — plus an optional paid lived-experience adviser. Compensation 0.25–0.5% options over 24 months or £500–£1,000 per meeting. Recruited by discovery conversation, written brief, three-month trial, letter of appointment; announced only with written consent.
- Policies at incorporation: conflicts of interest (Kemek Enterprise Ltd declared), anti-bribery, data protection, clinical-claims sign-off, delegated authorities.
- Decision rights: external clinical or regulatory claims require clinical-adviser sign-off; pricing changes over 20% require the division P&L owner; government proposals require the board.

## 12. Financial summary

The three-year scenario model (Conservative / Base / High-growth; January 2027 to December 2029; GBP; formula-driven with a Python-verified static summary and a sensitivity sheet) is built by `/finance/build_model.py` into `/finance/Vytalix_Financial_Model_3yr.xlsx`. Its narrative is `/docs/08_FINANCIAL_MODEL.md`, which does not yet exist in this repository; this section therefore describes the scenarios qualitatively and quotes only figures already published in `/docs/01_BUSINESS_MODEL.md`, `/docs/02_GROUP_STRUCTURE.md`, `/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` and `/docs/15_LEGAL_AND_REGULATORY.md`. Every figure is a SCENARIO built from stated assumptions (FACTS_BASE A8); none is an actual, a forecast or a commitment.

### 12.1 Year-1 services build (`/docs/01_BUSINESS_MODEL.md` §4)
| Scenario | 12-month services revenue (ESTIMATE) | Assumptions | Cash implication |
|---|---|---|---|
| Downside | £55k | One retainer for six months, two sprints, 20 advisory days, no e-learning | Founder cannot draw a salary; MaternaLink work stalls; decide by month 6 whether to take employment |
| Base | £118k | ~85–87 founder billable days (~42% utilisation) at £1,200–£1,800/day, two to three retainers, probability-weighted (73% projects, 90% retainers) | Covers a £3k/month founder draw, legal/IP £8k–£12k, brand/web £5k, insurance/accountancy £3k; ~£20k surplus toward MaternaLink |
| Upside | £210k | Three concurrent retainers by month 6, one NHS/ICB review via sub-contract, e-learning at 150 sales | Funds a part-time product lead (£30k) and a Clinical Safety Officer contract; positions for Innovate UK match funding |

Services break-even (ESTIMATE): fixed monthly costs of ~£4,500 require ~£7,500 revenue a month at 60% gross margin — five founder billable days or two retainers a month. Sensitivity: each additional retainer adds ~£36k/year; each ten-point change in utilisation moves revenue ~£30k; a 20% day-rate change moves it ~£18k.

### 12.2 Unit economics (ESTIMATE; `/docs/01_BUSINESS_MODEL.md` §3)
Founder advisory day contribution £850 (57% margin at £1,500); discovery sprint contribution £7,700 (55%); retainer month £2,500 (63%); e-learning course sale £104 (70% rising to 88%); workshop £2,950 (74%); a future UK MaternaLink site-year £36,000 contribution (60%) only after three or more sites; a future Africa enrolled woman-year at £15 donor-funded yields ~£5.50 (37%) and needs 20k+ women to cover a ~£110k fixed team. Grants: expected value per bid ~£12k–£15k at 15–20% success; write at least four bids a year.

### 12.3 Three-year scenarios, qualitatively
- **Conservative:** services-led; the founder draws nothing until first invoices are paid; MaternaLink progresses only as far as grants and design partnerships allow; product revenue is small and late (from month 18 or later); headcount stays fractional; the funding requirement is met by services, grants and a small pre-seed.
- **Base:** services reach the £118k year-1 build and grow with associates; the pre-seed (£150k–£300k, ESTIMATE) funds the MVP, the Clinical Safety Officer and a fractional product lead; the first paid pilots land in 2027 (£10k–£40k) and a Nigeria pilot is donor- or state-funded (£0.1m–£0.3m); the UK NHS licence conversation begins after the service evaluation; a seed round on evidence is modelled for 2028.
- **High-growth:** associates deliver more of the services work (lower delivery cost share); 2–3 UK sites and a state-scale Nigeria agreement by 2028; ARR in the £0.4m–£0.9m scenario range by Q3 2028 (`/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §23); a later Series A appears only in this scenario.

Peak cash need, break-even month and runway per scenario are computed on the model's "Funding requirement" sheet and will be quoted in `/docs/08_FINANCIAL_MODEL.md` once that document is written; they are not restated here to avoid inventing numbers. Year-1 legal and compliance cost is ESTIMATE £9k–£18k (`/docs/15_LEGAL_AND_REGULATORY.md`); marketing tooling £0–£150/month plus £2k–£4k optional (`/docs/14_MARKETING_AND_CONTENT_ENGINE.md`); the v3 research track, if ever pursued, is £1.5m–£4m over 24–36 months and is outside the base case.

## 13. Funding

Funding path (FACTS_BASE A7; `/docs/09_FUNDING_STRATEGY.md` and `/docs/10_INVESTOR_PROPOSITION.md` to be written):

| Stage | Source | Amount (ESTIMATE) | Timing (PROPOSED) | Conditions |
|---|---|---|---|---|
| Bootstrapping | Services revenue | £55k–£210k in year 1 | From month 2 | Incorporation; insurance; first two engagements |
| Non-dilutive | Innovate UK (Smart, Biomedical Catalyst), NIHR i4i where eligible, SBRI Healthcare, Wellcome, Grand Challenges, MSD for Mothers (note: funds the Ekiti incumbent), FCDO-funded programmes, UKRI | Realistic year-1 target £50k–£150k; £25k feasibility to £500k–£1m collaborative R&D | Prepare now; first award realistic at 6–12 months | Incorporated UK entity; clinical partner letter; NIHR requires an NHS partner; ethics approvals for studies |
| Pre-seed | Angels, SEIS/EIS funds, impact and women's-health investors | £150k–£300k for 8–15% at a £1.5m–£4m pre-money placeholder | Months 9–15 | Entity; IP settled; SEIS/EIS advance assurance (TO VALIDATE eligibility; consultancy-heavy trades are scrutinised); first evidence (design partner LOI, safety case, report) |
| Seed | Impact / health-tech seed funds | Not sized in this plan | 2028, on pilot evidence | UK service-evaluation evidence; Nigeria pilot interim results; 2–3 sites |

The investor CRM (`/investors/`) holds 300 real, publicly identifiable investors with fit and contactability scores; outreach to the top 25 begins only after the entity and IP are fixed (`/docs/00_MASTER_AUDIT.md` §6, opportunity 5). Investor-facing assets (`/assets/INVESTOR_ONE_PAGER.md`, `/assets/INVESTOR_PITCH_DECK.md`) are separate from this plan. Use of funds for the pre-seed (PROPOSED): MVP build and penetration test; Clinical Safety Officer and clinical advisory group; DPIA, DSPT, Cyber Essentials; discovery research in both markets; a fractional product lead; grant match funding.

## 14. Risks

The consolidated register draws on the risk sections of each strategy document; likelihood and impact are the authors' desk ESTIMATES.

| # | Risk | Likelihood | Impact | Mitigation | Source |
|---|---|---|---|---|---|
| 1 | MaternaLink IP cannot be brought into Vytalix on acceptable terms; dispute with David Agunede | Medium | Critical | Standstill letter week 1; solicitor-led heads of terms; assignment preferred, licence fallback; clean-room rebuild of v1 if no agreement by month 4 | `/docs/02_GROUP_STRUCTURE.md` §3 |
| 2 | Founder cannot win 8–10 billable days a month | Medium | Critical | 30 conversations, 6 proposals, 2 signed in 90 days; kill signal: <1 signed by month 3 → part-time, seek fractional role | `/docs/01_BUSINESS_MODEL.md` §8 |
| 3 | Name and trademark conflict (VITALIX LTD, Vytalyx Inc., Vytalize Health) | Medium–High | High | Five-step clearance by Day 10; rename within five days if it fails; no brand spend before clearance | `/docs/02_GROUP_STRUCTURE.md` §7 |
| 4 | Over-claimed clinical AI positioning leaks into external use | Medium | High | 2025 deck retired; intended-use statement; FACTS_BASE language rules; clinical-adviser sign-off on claims | `/docs/00_MASTER_AUDIT.md` §5 |
| 5 | Prototype has processed real data unlawfully or contains third-party IP | Unknown | High | Audit and remediate immediately; no real data until audited | `/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §25 |
| 6 | A v1 feature is judged a medical device | Medium | High | Qualification decisions documented feature by feature; regulatory counsel; CSO sign-off | `/docs/15_LEGAL_AND_REGULATORY.md` |
| 7 | No UK clinical partner willing to evaluate | Medium | High | Lead with artefacts; ten approaches; no-fee evaluation; fallback to Africa/private first | `/docs/05_MARKET_STRATEGY.md` §8 |
| 8 | Ekiti relationship non-transferable or the state has moved on; incumbent programme | High | Medium | Partner/complement/move-state decision within one quarter; NGO cohorts independent of any ministry | `/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §12 |
| 9 | Government/donor willingness to pay per woman is far below the Ekiti figure | High | Medium | Re-based £6–£40 range; cost-to-serve model; Africa treated as a donor-funded evidence market until validated | `/docs/01_BUSINESS_MODEL.md` §8 |
| 10 | Funding runway; SEIS/EIS advance assurance refused | Medium | High | Services and grants first; structure the application around product R&D plus services trade; reduce R&D scope if 0/4 grants | FACTS_BASE A7 |
| 11 | Founder bandwidth across services, product, fundraising, grants and a second venture | High | High | Ten-day billable cap; time-allocation rule; fractional hires from surplus or grant | `/docs/01_BUSINESS_MODEL.md` risks |
| 12 | Safeguarding failure on shared phones; unread urgent message | Low–Medium | Critical | Discreet mode; content-neutral SMS; SLA escalation to humans; hazard-log controls | `/docs/04_MATERNALINK_PRODUCT_STRATEGY.md` §19 |
| 13 | Client concentration | Medium | Medium | No client >40% of trailing six-month revenue by month 9 | `/docs/01_BUSINESS_MODEL.md` risks |
| 14 | Advisers or partners named without consent | Low | High | Written consent rule; announcements only after signature | `/docs/02_GROUP_STRUCTURE.md` §4 |

## 15. Milestones and "what must be true"

### 15.1 Milestones (PROPOSED; dates from Monday 14 September 2026)
| When | Milestone | Evidence of completion |
|---|---|---|
| Day 3 | 2025 deck retired from external use; intended-use statement adopted | Written product charter |
| Day 7 | Standstill letter with David Agunede; IP audit questionnaire sent | Signed letter |
| Day 10 | Name clearance decision; incorporation; founder IP assignment | Companies House number |
| Day 14–21 | Bank, ICO, SEIS/EIS application, PI/PL insurance; time-allocation rule | Certificates and policies |
| Day 30 | Website live; service catalogue and prices published; prototype audit complete; CRM live with 150 contacts | Site URL; audit report |
| Day 45 | First paid engagement signed | Signed SOW; first invoice |
| Day 60 | Heads of terms on MaternaLink IP signed; clinical adviser and Clinical Safety Officer conversations concluded; 15 UK discovery interviews done | Signed heads of terms; appointment letters |
| Day 63 (week 9) | Research report 1 published | Download page |
| Day 90 | 3 signed engagements, £15k–£30k contracted (ESTIMATE); first grant bid drafted; Ekiti status and mDoc conversations held; two states scored; Day-90 scorecard published | CRM export; scorecard post |
| Month 6 | Services at ~£10k/month; hazard log and DPIA in progress; associates identified; e-learning build started; 10 UK trust approaches made | Monthly KPI review |
| Month 9 | Two e-learning courses live; three retainers active; one UK design-partner LOI; one Nigeria NGO LOI; pre-seed conversations opened | LOIs; course pages |
| Month 12 | MVP complete and penetration-tested; safety case v1; DTAC readiness pack; first grant decision; pre-seed closed or in progress | Artefacts; term sheet |
| Month 18 | UK service evaluation live; first paid pilot; Nigeria pilot funded | Evaluation protocol; contract |
| Month 24–36 | 2–3 UK sites; one state-scale Nigeria agreement; Kenya partner; seed round on evidence | Contracts; evaluation reports |

### 15.2 What must be true (`/docs/01_BUSINESS_MODEL.md` §8)
1. The founder can win 8–10 billable days a month within 90 days.
2. Buyers accept £1,200–£1,800 a day for founder-led work.
3. MaternaLink IP can be brought into Vytalix on acceptable terms by month 4.
4. A UK maternity unit will act as an unpaid design partner by month 9.
5. The prototype is safe and usable enough to demonstrate (month 2 audit).
6. Government or donor willingness to pay per woman in Nigeria is materially above £5–£15 a year (month 9).
7. A grant can be won within 12 months (at least four bids).
8. E-learning can acquire learners at a CAC below £60 (month 10).
9. The Vytalix name is clearable (month 1).
10. SEIS/EIS advance assurance is obtainable (months 2–3).

Each has a test, an owner and a kill or pivot signal in the source document. This plan is reviewed against them at the Day-90 and month-6 reviews and re-labelled from PROPOSED to ADOPTED section by section as items are executed.

---

## Priorities / Risks / Next actions

**Priorities**
1. Resolve the two existential items first: MaternaLink IP (standstill letter, IP audit, solicitor) and the legal entity (name clearance, incorporation, SEIS/EIS, insurance).
2. Sell Tier-1 services to the base-case build: 30 conversations, 6 proposals, 2 signed engagements and £15k booked by Day 90.
3. Close the four product gates in order (IP, prototype audit, CSO and hazard log, DPIA) and open one UK design-partner and one Nigerian NGO conversation.
4. Write `/docs/08_FINANCIAL_MODEL.md` from the workbook so that §12 can quote peak cash need, break-even and runway per scenario.
5. Keep every external document stage-honest; this plan is the reference for what may and may not be claimed.

**Risks**
- The plan is read as a record of achievement; mitigation: the label line at the top of every section and the FACTS_BASE truth standard.
- Documents referenced by path (06, 08–12, 16–20) do not yet exist; mitigation: they are listed in `/README.md` as the build order and this plan is updated when each lands.
- The founder's role, time and capital (TO VALIDATE) turn out to be smaller than the plan assumes; mitigation: the month-3 and month-6 kill/pivot signals.

**Next actions**
- Founder, Day 1–3: standstill letter; retire the 2025 deck; name searches; time-allocation rule.
- Founder + solicitor, Day 3–10: incorporation; founder IP assignment; heads-of-terms drafting.
- Founder, Day 10–30: bank, ICO, SEIS/EIS, insurance; website and catalogue live; 150-contact list; prototype audit commissioned.
- Founder, Day 30–90: engagements delivered; report 1 and webinar 1; clinical adviser and CSO contracted; Ekiti/mDoc conversations; Day-90 review of §15.2.
- Finance owner, by Day 30: `/docs/08_FINANCIAL_MODEL.md` written from `/finance/Vytalix_Financial_Model_3yr.xlsx`; §12 of this plan updated.
