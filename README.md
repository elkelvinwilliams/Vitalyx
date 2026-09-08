# Vytalix — Technology for Life

A UK health technology company being built from scratch. Four parts: advice, consulting, health products (MaternaLink, in development) and training.

**Start with [`docs/00_START_HERE.md`](docs/00_START_HERE.md). It is one page and it tells you what to do this week.**

Everything here is written in plain English. Nothing claims a customer, partner, approval or pound of revenue that does not exist.

## The two websites are live

- Vytalix: https://elkelvinwilliams.github.io/Vitalyx/
- MaternaLink, with a demonstration dashboard: https://elkelvinwilliams.github.io/Vitalyx/maternalink/

## The fourteen documents

| # | Document | What it answers |
|---|---|---|
| 00 | [Start here](docs/00_START_HERE.md) | What to do first |
| 01 | [Where you stand](docs/01_WHERE_YOU_STAND.md) | What exists today, honestly. Score: 11 out of 100 |
| 02 | [What we are building](docs/02_WHAT_WE_ARE_BUILDING.md) | MaternaLink, and why the AI idea is parked |
| 03 | [Who buys it](docs/03_WHO_BUYS_IT.md) | Buyers, budgets, and who else is out there |
| 04 | [How we make money](docs/04_HOW_WE_MAKE_MONEY.md) | Every price, and the first £1,000,000 |
| 05 | [The money](docs/05_THE_MONEY.md) | Three-year numbers, how much to raise, and when |
| 06 | [The plan](docs/06_THE_PLAN.md) | The first 90 days, and how to decide anything |
| 07 | [Getting customers](docs/07_GETTING_CUSTOMERS.md) | Where clients come from, and what to say |
| 08 | [Running the company](docs/08_RUNNING_THE_COMPANY.md) | Your week, your numbers, who to hire when |
| 09 | [Legal, data and safety](docs/09_LEGAL_AND_SAFETY.md) | What you must do, and where software becomes a medical device |
| 10 | [Partners](docs/10_PARTNERS.md) | The seven kinds, and the first four to get |
| 11 | [Brand and websites](docs/11_BRAND_AND_WEBSITES.md) | The name, the look, the two sites |
| 12 | [Structure and markets](docs/12_STRUCTURE_AND_MARKETS.md) | How to set the company up, and which countries |
| 13 | [The investor list](docs/13_THE_INVESTOR_LIST.md) | How to use the 316 names |

Plus [the facts](FACTS_BASE.md), which says what is proven and what is a guess. If any document disagrees with it, that file wins.

## Everything else

| Folder | What is in it |
|---|---|
| `product/` | Four documents to hand to a software developer |
| `assets/` | What you send out: company profile, service list, proposal template, one-pager, four slide decks |
| `finance/` | The three-year financial model |
| `investors/` | 316 investors, top 25, call lists, scripts, and 74 partner organisations |
| `operations/` | Weekly numbers and pipeline trackers |
| `diagrams/` | The 18 charts used in the documents |
| `website/`, `maternalink-site/` | The two websites |
| `exports/` | Everything as PDF, Word, Excel and PowerPoint, plus two zip files |

## Ready-made files

- **`exports/pdf/Vytalix_Executive_Pack.pdf`** — the six documents to read first, in one branded PDF
- `exports/pdf/` — every document as a PDF with a title page and page numbers
- `exports/pdf/decks/` — the four slide decks
- `exports/xlsx/` — investor list, financial model, partner tracker, pricing calculator, readiness scorecard
- `exports/Vytalix_Pack_1_Documents.zip` and `exports/Vytalix_Pack_2_Sites_Data_Source.zip`

## Rebuilding after you edit something

Edit the Markdown files, then run one command:

```
bash exports/rebuild_all.sh
```

That rebuilds the diagrams, PDFs, decks, spreadsheets, Word files and both zips.

## House style

Every document follows [`docs/_STYLE.md`](docs/_STYLE.md): short sentences, no consultancy jargon, jargon explained in brackets, a one-minute summary at the top, and a maximum of about 200 lines. Keep it that way when you edit.
