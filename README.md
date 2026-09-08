# VYTALIX — Technology for Life

**Company build repository.** Vytalix is a pre-seed UK health-technology group with four pillars: Advisory, Consulting, Health Solutions (first product **MaternaLink**, in development) and E-Learning. This repository is the operating system for building the company: audit, strategy, product, finance, brand, website, investor CRM and execution plans.

> Truth standard: nothing here is a record of achievement unless labelled VERIFIED or KNOWN. Everything else is ASSUMPTION, ESTIMATE, PROPOSED or TO VALIDATE. Start with `FACTS_BASE.md`.

## Start here
| Order | File | What it is |
|---|---|---|
| 0 | `FACTS_BASE.md` | Single source of truth: what was verified, what is unknown, working assumptions, language rules |
| 1 | `docs/00_MASTER_AUDIT.md` | Master audit, area scores /10, business score /100, SWOT, top 10 problems, top 10 opportunities |
| 2 | `docs/19_FIRST_30_DAYS.md` | Day-by-day plan from Monday 14 September 2026 |
| 3 | `docs/18_90_DAY_EXECUTION_PLAN.md` | 90-day plan with owners, deadlines, KPIs, decision gates |

## Strategy
- `docs/01_BUSINESS_MODEL.md` — revenue streams, pricing, service catalogue, unit economics
- `docs/02_GROUP_STRUCTURE.md` — legal structure, IP options for MaternaLink, governance, vision and missions
- `docs/05_MARKET_STRATEGY.md` — UK, Africa, Europe, Middle East, North America, emerging markets scored
- `docs/06_CUSTOMER_SEGMENTS.md` — B2B and B2C segments, ICP, first target archetypes
- `docs/11_COMPETITIVE_INTELLIGENCE.md` — direct, indirect, adjacent competitors; buildable advantages
- `docs/12_PARTNERSHIP_STRATEGY.md` — ecosystem map, scoring, 12-month plan
- `docs/20_DECISION_FRAMEWORK.md` — BUILD / TEST / DEFER / KILL scoring applied to live ideas
- `docs/24_MATERNALINK_REINVENTION.md` — brutal audit of the 2025 AI concept, the reinvented product, category, business model, partner ecosystem, data and AI moats, regulatory pathway, validation study, MVP, pitches, brand, global scale, £1bn test, 90-day plan and war room
- `investors/partners/` — 74-organisation partner target list, CRM template and Excel war room
- `docs/23_INVESTOR_READINESS_AND_WINNING_CONCEPT.md` — readiness scorecard, data-room index, the Maternal Continuity Layer concept, government-contract playbook
- `exports/` — Word and PowerPoint versions of every document and deck, plus `START_HERE.md` and the zip pack (`python3 exports/build_exports.py` regenerates)
- `docs/22_UPDATE_LOG_2026-09-08.md` — what changed after the logo, prototype recording and expanded scope were received

## Product and technology
- `docs/04_MATERNALINK_PRODUCT_STRATEGY.md` — vision, personas, journeys, MVP→v3, regulatory, data, safety
- `product/MATERNALINK_PRD.md`, `product/MATERNALINK_MVP_SPEC.md`, `product/MATERNALINK_ROADMAP.md`
- `docs/07_TECHNOLOGY_ARCHITECTURE.md` — group stack, costs, lean year-1 stack
- `product/MATERNALINK_FEATURE_ADDENDUM.md` — founder's feature list mapped to version and regulatory posture (8 Sept 2026)
- `docs/21_MATERNALINK_PRICING.md` — MaternaLink pricing per product and annual service
- `maternalink-site/` — rebuilt MaternaLink product site (EN/FR landing, platform, programmes, security, pricing, pilot request, operator login, demo dashboard)

## Finance and funding
- `finance/Vytalix_Financial_Model_3yr.xlsx` (built by `finance/build_model.py`) — Conservative / Base / High-growth
- `docs/08_FINANCIAL_MODEL.md`, `docs/09_FUNDING_STRATEGY.md`, `docs/10_INVESTOR_PROPOSITION.md`
- `assets/INVESTOR_ONE_PAGER.md`, `assets/INVESTOR_PITCH_DECK.md`

## Investors (300-investor CRM, investor-only, phone-first)
- `investors/VYTALIX_INVESTOR_CRM.xlsx` and `.csv` — master CRM with fit /100, contactability /10, tiers
- `investors/TOP_25_INVESTORS.md`, `investors/CALL_LISTS.md`, `investors/OUTREACH_TOP25.md`
- `investors/OUTREACH_ENGINE.md`, `investors/CRM_PIPELINE.md`, `investors/INVESTOR_DASHBOARD.md`
- `investors/NON_DILUTIVE_FUNDING_ROUTES.md` — grant programmes kept outside the investor-only CRM
- Rebuild after edits: `python3 investors/build_crm.py` (raw research in `investors/raw/`)

## Brand, website, go-to-market
- `docs/03_BRAND_SYSTEM.md` — positioning, voice, palette, typography, logo direction, design systems
- `website/` — 14-page static site (open `website/index.html`; deploy notes in `website/README.md`)
- `docs/13_SALES_ENGINE.md`, `docs/14_MARKETING_AND_CONTENT_ENGINE.md`
- `assets/` — company profile, service catalogue, decks, proposal template, pricing, business plan, content calendar, launch campaign

## Operations, legal, people
- `docs/15_LEGAL_AND_REGULATORY.md`, `docs/16_ORGANISATION_AND_SOPS.md`, `docs/17_FOUNDER_OPERATING_SYSTEM.md`
- `operations/KPI_DASHBOARD.csv`, `operations/PIPELINE_TRACKERS.csv`

## Live websites
- Vytalix: https://claude.ai/code/artifact/cc65bf98-acb9-451e-a9d4-eed9553ac632
- MaternaLink (with demo dashboard): https://claude.ai/code/artifact/39a7187c-c6d5-4eaf-9c6b-38dab166ce40

## Exports
`exports/pdf` (branded PDFs and `Vytalix_Executive_Pack.pdf`), `exports/pdf/decks`, `exports/xlsx` (branded workbooks, pricing calculator, readiness scorecard), `exports/pptx`, `exports/docx`, `exports/live`. Rebuild with `python3 exports/build_pdfs.py`, `build_deck_pdfs.py`, `build_xlsx.py`, `build_exports.py`.

## Naming
The repository is named "Vitalyx"; the brand in the founder's brief is "Vytalix". Treat the repository name as a typo pending name and trademark clearance (see the audit).
