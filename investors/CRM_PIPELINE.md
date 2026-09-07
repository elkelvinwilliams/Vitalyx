# CRM PIPELINE AND FIELD DICTIONARY

## Pipeline (18 stages)
1 Identified → 2 Researched → 3 Qualified → 4 Priority A → 5 Outreach Ready → 6 Contacted → 7 Called → 8 Email Sent → 9 Responded → 10 Meeting Requested → 11 Meeting Booked → 12 Meeting Completed → 13 Due Diligence → 14 Investment Discussion → 15 Term Sheet → 16 Closed → 17 Passed → 18 Future Opportunity

Rules: every record enters at Researched. Qualified requires stage and ticket fit confirmed from a public source. Priority A is Tier A only. Outreach Ready requires the pre-conditions in `OUTREACH_ENGINE.md`. Passed requires a stated reason in Notes. Future Opportunity is revisited quarterly.

## Scores
- **Vytalix Investor Fit /100** = Sector 20 + Stage 15 + Ticket 15 + Geographic 10 + Strategic 15 + MaternaLink 10 + Accessibility 5 + Network 10.
- **Contactability /10** = verified phone 3 + direct route 2 + named decision maker 1 + professional email 1 + LinkedIn 1 + warm-intro possibility 1 + information quality 1.
- **Overall** = 0.85 × Fit + 1.5 × Contactability (max 100). Used to rank within tiers and to build call lists.
- **Tiers** (by Fit): A 80–100 immediate personalised outreach; B 65–79 targeted relationship development; C 50–64 maintain and monitor; below 50 not prioritised.
- **Investment probability**: High (Fit ≥ 75 and Contactability ≥ 6), Medium (Fit ≥ 60 and Contactability ≥ 4), otherwise Low. A heuristic, not a forecast.

## Truth standards
- Phone numbers appear only when captured from an official source in public search during research, with the source URL and date. Otherwise PHONE NOT PUBLICLY AVAILABLE. Nothing is guessed; personal mobiles are never recorded.
- Emails appear only when published on official pages. Otherwise NOT PUBLICLY AVAILABLE.
- Decision makers are named only in their public roles; entries marked "confirm on team page" must be checked before use.
- Last Verified shows 2026-09-07 for fields checked in this build, otherwise "Unverified (prior knowledge)". Re-verify any record before outreach; funds change teams and mandates.

## Maintenance
Edit `investors/raw/*.csv` (or add a new CSV with the same headers), then run `python3 investors/build_crm.py` to regenerate the CRM, Top 25, call lists, outreach scripts and dashboard.
