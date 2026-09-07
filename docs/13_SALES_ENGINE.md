# 13 — VYTALIX SALES ENGINE

**Owner:** Founder (acting Head of Sales) · **Status:** PROPOSED · **Version:** 1.0 (7 Sept 2026) · **Governed by:** `/FACTS_BASE.md` (language rules apply to every template below)

## Executive view
1. Vytalix has no customers, no pipeline and no CRM today (VERIFIED absence, FACTS_BASE §1). First revenue is expected from founder-led Advisory/Consulting, not MaternaLink (ASSUMPTION A6).
2. The sales engine is built for one seller (the founder) selling three things: advisory retainers, fixed-scope consulting sprints and, later, e-learning; MaternaLink (in development) is sold as a pilot conversation, never as a finished product.
3. Targets for the first 90 days (PROPOSED): 150 qualified contacts, 40 discovery calls, 12 proposals, 3 signed engagements, £15k–£30k contracted revenue (ESTIMATE range, not a forecast).
4. Tooling is deliberately cheap: HubSpot Free CRM (or Notion) + LinkedIn + Google Workspace; total tooling cost < £100/month (ESTIMATE).
5. Every template in this document obeys FACTS_BASE language rules: no invented clients, no "proven platform", no NHS/government "partner" claims.

---

## 1. Who we sell to (segments, in priority order)

| # | Segment | Buyer persona | What they buy from Vytalix | Typical deal (ESTIMATE) | Sales cycle (ESTIMATE) |
|---|---|---|---|---|---|
| S1 | UK digital-health start-ups / scale-ups (pre-seed to Series A) | Founder / COO | Go-to-market, NHS-readiness, regulatory-pathway advisory; investor-readiness | £2.5k–£5k/month retainer or £7.5k–£15k sprint | 2–6 weeks |
| S2 | UK health-tech investors, accelerators, incubators | Programme director / partner | Portfolio support workshops, due-diligence support, cohort training | £5k–£20k per programme | 4–8 weeks |
| S3 | NHS-adjacent organisations (ICBs, trusts' innovation teams, AHSNs/Health Innovation Networks, charities) | Innovation lead / programme manager | Digital-maternity landscape research, procurement-readiness reviews, training | £5k–£25k project | 8–16 weeks (procurement rules) |
| S4 | African ministries of health, state governments, development partners (NGOs, donors) | Commissioner / programme officer | Digital-health strategy, maternal-health programme design, MaternaLink (in development) pilot scoping | £10k–£50k study; pilot TO VALIDATE | 3–9 months |
| S5 | Corporates / employers / insurers with women's-health agendas | HR / benefits / CSR lead | Education content, women's-health programme design | £5k–£15k | 4–10 weeks |
| S6 | Individual learners and health professionals (E-Learning) | Nurse, midwife, health-tech professional | Courses, cohorts | £49–£299 per learner (ESTIMATE) | Self-serve |

Rule: the founder spends ≥60% of selling time on S1–S2 in the first 90 days (shortest cycle, cash first), ≤25% on S3–S4, and treats S5–S6 as opportunistic until Q2 2027.

---

## 2. Lead generation — channels and weekly targets

| Channel | Activity | Weekly target (PROPOSED) | Owner | KPI |
|---|---|---|---|---|
| LinkedIn outbound | Personalised connection + message to ICP contacts | 40 connection requests, 20 messages | Founder | ≥30% accept, ≥15% reply |
| LinkedIn content | 3 founder posts/week (see `/docs/14_MARKETING_AND_CONTENT_ENGINE.md`) | 3 posts, 20 comments on others' posts | Founder | 5 inbound conversations/month |
| Warm intros | Ask existing network for named intros | 5 asks/week | Founder | 2 intros/week |
| Cold email | Sequenced, 3-touch, to public business addresses only | 25 new contacts/week | Founder | ≥8% reply rate |
| Events / meetups | Attend 1 UK health-tech event or meetup per fortnight (see marketing doc for named events, dates TO VALIDATE) | 10 new conversations/event | Founder | 3 follow-up meetings/event |
| Investor network | Every investor call ends with "who else should I talk to?" | 1 referral/call | Founder | 2 customer referrals/month |
| Partnerships | Accelerators, incubators, health-innovation networks | 2 new partner conversations/week | Founder | 1 referral agreement/quarter |
| Website / SEO | Inbound form (from Day 30) | — | Founder | 2 inbound leads/month by Month 3 |

Weekly activity minimums (non-negotiable): **40 new contacts, 20 conversations, 5 discovery calls, 2 proposals** in steady state from Week 3.

---

## 3. CRM setup

**Recommendation:** HubSpot Free CRM (contacts, companies, deals, email tracking, sequences on Starter) — upgrade to Starter (ESTIMATE £15–£20/seat/month, TO VALIDATE) only when sequences are needed. Alternative: Notion database if the founder already lives in Notion. Do **not** mix with the Kemek Enterprise investor CRM (FACTS_BASE §1).

### 3.1 Pipeline stages (Deals)

| Stage | Definition / exit criteria | Probability weight |
|---|---|---|
| 0. Identified | Matches ICP; no contact yet | 0% |
| 1. Contacted | First outbound touch sent | 5% |
| 2. Engaged | Reply received or meeting accepted | 15% |
| 3. Discovery done | Discovery call held; pain, budget, timeline, authority captured | 30% |
| 4. Proposal sent | Written proposal delivered with price and start date | 50% |
| 5. Negotiation | Verbal intent; terms being agreed | 70% |
| 6. Closed-won | Signed SOW + first invoice raised | 100% |
| 7. Closed-lost | Explicit no or 30 days silent after 3 follow-ups; reason coded | 0% |

### 3.2 Required fields

| Object | Field | Values |
|---|---|---|
| Contact | Name, role, organisation, LinkedIn URL, email (public/business only), country, segment (S1–S6), source, lead score, last touch, next action, next action date | — |
| Company | Type, size, funding stage, decision cycle, NHS/government relationship (yes/no/unknown), maternal-health relevance (H/M/L) | — |
| Deal | Offer (Advisory / Consulting / E-Learning / MaternaLink pilot scoping), value (£), stage, close date, probability, loss reason, proposal link, SOW link | — |
| Activity | Type (call/email/LinkedIn/meeting), date, summary, next step | — |

### 3.3 Hygiene rules
- Every open deal has a **next action with a date**; none older than 7 days.
- Friday 30-minute pipeline clean (see `/docs/17_FOUNDER_OPERATING_SYSTEM.md`).
- Loss reasons coded: price / timing / no budget / no need / chose competitor / no decision / not ICP.

---

## 4. Lead scoring model (0–100)

| Dimension | Weight | Scoring |
|---|---|---|
| Fit: segment | 25 | S1/S2 = 25; S3/S5 = 15; S4 = 12; S6 = 5 |
| Fit: authority | 15 | Decision-maker 15; influencer 8; user 3 |
| Fit: budget signal | 15 | Funded (raised in last 18 months / has programme budget) 15; unknown 7; no budget 0 |
| Need: stated problem | 20 | Explicit problem in our scope 20; adjacent 10; none 0 |
| Timing | 15 | Needs outcome < 3 months 15; 3–6 months 8; > 6 months 3 |
| Engagement | 10 | Replied / met 10; opened / viewed profile 5; none 0 |

**Thresholds:** ≥70 = A (call within 48 h) · 45–69 = B (nurture, weekly touch) · < 45 = C (monthly content only). Rescore after every discovery call.

---

## 5. Discovery call (30 minutes)

| Minute | Block | Purpose |
|---|---|---|
| 0–3 | Open | Thank, agenda, permission to ask questions, confirm time |
| 3–8 | Context | Their role, organisation, what prompted the call |
| 8–18 | Problem | Current situation, what's been tried, cost of the problem |
| 18–23 | Decision | Budget range, authority, timeline, success criteria |
| 23–27 | Fit | Summarise; describe 1–2 ways Vytalix could help (no hard pitch) |
| 27–30 | Next step | Agree specific next action and date (proposal / second call / no) |

### 20 discovery questions
1. What prompted you to take this call now?
2. How is [digital health / maternal health / market entry] currently handled in your organisation?
3. What does success look like for you in the next 6 months?
4. What have you already tried, and what happened?
5. Who else is affected by this problem internally?
6. What happens if nothing changes by [date]?
7. How is this problem costing you today — time, money, missed opportunity, risk?
8. Who signs off on external advisory or consulting spend?
9. Is there an allocated budget, or would this need a business case?
10. What range have you paid for comparable work before?
11. What is your timeline — is there a board meeting, funding round, tender or deadline driving it?
12. What would make this a "no" for you?
13. Which other options are you considering (in-house, other advisers, doing nothing)?
14. How do you prefer to work with advisers — retainer, fixed project, workshops?
15. What evidence would you need to see before committing?
16. Are there regulatory, clinical-safety or data-protection constraints we must respect from Day 1?
17. Who would be our day-to-day counterpart?
18. If we started on [date], what would the first two weeks need to deliver?
19. What is the single biggest risk you see in working with a young firm like ours?
20. If this works, what would you want to do next?

Capture answers in the CRM under: Problem / Impact / Authority / Budget / Timeline / Success criteria / Risks / Next step.

---

## 6. Sales presentation outline (20 minutes, use `/assets/SALES_DECK.md`)

1. Who we are (30 s) — Vytalix, "Technology for Life", four pillars, pre-seed UK health-tech group.
2. Your problem as we heard it (3 min) — restate discovery findings.
3. Why it matters (2 min) — cost of inaction, sector context (cited).
4. How we work (3 min) — advisory / consulting / e-learning; MaternaLink (in development) only if relevant.
5. Proposed approach (5 min) — phases, deliverables, timeline.
6. Team and credibility (2 min) — founder background (KNOWN facts only), advisers (only if signed), method.
7. Commercials (2 min) — options (Good / Better / Best), price, terms.
8. Next steps (2 min) — decision date, kick-off date, what we need from them.

---

## 7. Proposal structure

| Section | Content | Length |
|---|---|---|
| 1. Cover + executive summary | Problem, outcome, price, timeline in 5 lines | ½ page |
| 2. Understanding of your situation | Discovery findings in their words | ½ page |
| 3. Objectives and success criteria | Measurable | ½ page |
| 4. Approach and deliverables | Phases, activities, outputs | 1 page |
| 5. Timeline | Gantt table | ½ page |
| 6. Team | Who does the work | ¼ page |
| 7. Investment | Options table, payment schedule | ½ page |
| 8. Assumptions, exclusions, dependencies | Explicit | ½ page |
| 9. Terms | MSA reference, validity date | ¼ page |
| 10. Acceptance | Signature block | ¼ page |

Full template: Appendix A and `/assets/PROPOSAL_TEMPLATE.md`.

---

## 8. Follow-up sequences

| Sequence | Touch 1 | Touch 2 | Touch 3 | Touch 4 | Close-out |
|---|---|---|---|---|---|
| Cold outbound | Day 0 email/LinkedIn | Day 3 value add (article/insight) | Day 7 short bump | Day 14 different angle | Day 21 break-up; move to nurture |
| Post-discovery | Same-day summary email | Day 2 proposal | Day 5 check-in call | Day 9 "what would help?" | Day 21 close-lost/nurture |
| Post-proposal | Day 0 cover email | Day 3 offer walkthrough call | Day 7 address objections | Day 12 adjust scope/option | Day 21 final; validity expiry |
| Re-engagement | Month 1 news/insight | Month 2 case/lesson | Month 3 direct ask | — | Quarterly content |

Rule: every touch adds something (insight, article, relevant news); never "just checking in".

---

## 9. Contracting — MSA + SOW structure (TO VALIDATE with a solicitor; see `/docs/15_LEGAL_AND_REGULATORY.md`)

**Master Services Agreement (MSA)** — signed once per client. Key clauses:

| Clause | Vytalix position (PROPOSED) |
|---|---|
| Services | Defined by SOWs; MSA governs all |
| Fees and payment | 50% on signature for projects < £10k; monthly in advance for retainers; 14-day terms; late-payment interest (Late Payment of Commercial Debts Act) |
| IP | Vytalix retains pre-existing IP and methods; client owns deliverables on full payment; licence-back of generic know-how |
| Confidentiality | Mutual; 3 years post-termination |
| Data protection | UK GDPR clause; DPA annex where personal data is processed; no patient data in advisory engagements |
| Liability | Capped at fees paid in preceding 12 months; exclusions for indirect loss; no cap for fraud/death/injury (statutory) |
| Insurance | PI cover stated (once purchased — see legal doc) |
| Non-solicitation | 12 months, mutual |
| Termination | 30 days' notice on retainers; for-cause immediately; fees to date payable |
| Governing law | England and Wales |
| Publicity | Client name usable only with written consent (protects FACTS_BASE rule: no invented or unconsented customer claims) |

**Statement of Work (SOW)** — per engagement: scope, deliverables, timeline, acceptance criteria, team, fees, assumptions, change-control, client dependencies.

---

## 10. Onboarding (first 14 days of an engagement)

| Day | Step | Output |
|---|---|---|
| 0 | Signed SOW; invoice issued; welcome email | Invoice, shared folder |
| 1–2 | Kick-off (60 min): goals, stakeholders, cadence, comms channels | Kick-off note |
| 3–5 | Information request fulfilled; access granted | Data/doc register |
| 5 | Engagement plan confirmed | 1-page plan with milestones |
| 10 | First quick win delivered | Early deliverable |
| 14 | First check-in; satisfaction pulse (1–5) | CRM note; risk log |

## 11. Retention and expansion

- Fortnightly written progress note to sponsor; monthly value review (what changed because of us).
- 30 days before end: renewal/expansion conversation with three options.
- Post-engagement: case study **only with written consent** (anonymised otherwise); referral ask; testimonial ask.
- Targets (PROPOSED): retainer renewal ≥ 60%; 1 in 3 projects leads to a follow-on; NPS collected on every close.

---

## 12. Email templates (replace [brackets]; never invent facts)

**E1 — Cold (S1 founder)**
> Subject: [Company]'s NHS route — one question
>
> Hi [First name], I read your [post/announcement about X]. One question: have you mapped the DTAC / clinical-safety evidence you'll need before an NHS pilot conversation, or is that still ahead of you?
>
> I'm Kelvin, founder of Vytalix, a UK health-tech advisory group (early-stage ourselves — we're building a maternal care-coordination platform, MaternaLink, in development, so we've been living the regulatory and go-to-market questions first-hand). I help founders turn that into a 6-week plan.
>
> If useful, I can share the one-page checklist I use. Worth a 20-minute call next week?
>
> Kelvin Williams · Vytalix · Technology for Life

**E2 — Warm intro follow-up**
> Subject: Following [Introducer]'s intro
>
> Hi [First name], thanks to [Introducer] for connecting us. [Introducer] mentioned you're [working on X]. I'm building Vytalix, a UK health-tech advisory and product group focused on digital health and maternal health. I'd value 20 minutes to understand what you're tackling and whether anything I'm working on is useful to you — no pitch. Would [day/time] or [day/time] suit?

**E3 — Follow-up 1 (value add, Day 3)**
> Subject: Re: [original subject] — thought this was relevant
>
> [First name], sharing [article/report/regulatory update] in case it's useful for [their topic]. The point I'd highlight: [one specific insight]. Happy to compare notes if helpful.

**E4 — Post-meeting summary (same day)**
> Subject: Notes and next steps from today
>
> [First name], thank you for the time today. What I heard: (1) [problem], (2) [impact], (3) [timeline/constraint]. You'd consider it a success if [criteria]. Proposed next step: I'll send a short proposal with two options by [date]; we then decide by [date]. Anything I've misread, tell me now and I'll correct it.

**E5 — Proposal cover**
> Subject: Proposal: [engagement title] — [Company] × Vytalix
>
> [First name], attached is the proposal we discussed. The short version: [outcome] in [duration] for £[price] (Option B), starting [date]. Section 8 lists assumptions and what we'd need from you. This proposal is valid until [date]. I've kept 30 minutes on [day] to walk through it — does that work?

**E6 — Re-engagement (60+ days silent)**
> Subject: [Topic] — a quick update from Vytalix
>
> [First name], since we last spoke, [genuine update: e.g., "we published our maternal digital-health landscape note" / "we've refined our NHS-readiness sprint"]. Is [their problem] still on your list for this quarter? If it is, I can share what's changed in our approach; if not, I'll stop nudging and just send our newsletter.

---

## 13. LinkedIn scripts

**L1 — Connection request (≤ 300 characters)**
> Hi [Name], I follow your work on [topic]. I'm building Vytalix, a UK health-tech advisory and product group (maternal health focus). Would be glad to connect and learn from what you're doing at [Org].

**L2 — First message after accept**
> Thanks for connecting, [Name]. I'm curious: what's the hardest part of [their current challenge] right now at [Org]? I'm asking founders and leaders this as we shape Vytalix's advisory offers — happy to share back what I'm hearing.

**L3 — Content-led touch**
> [Name], I wrote a short piece on [topic] — [link]. Your point about [their comment/post] shaped part of it. If you disagree with anything in it, I'd genuinely like to hear it.

**L4 — Meeting ask**
> [Name], based on what you said about [problem], I think a 20-minute call would be useful — I'd share how we're approaching [solution area] and you'd tell me if it's wrong. [Two time options]?

---

## 14. Call scripts

**C1 — Cold/warm outreach call (5 minutes)**
> "Hi [Name], it's Kelvin Williams from Vytalix. Did I catch you at an OK moment? [If yes] I'll be brief. I work with health-tech founders and health organisations on [advisory area]. The reason for the call: [specific trigger you saw]. Is [problem] something on your desk this quarter? [Listen.] Would it be worth 20 minutes where I share how others are approaching this and you tell me if it applies to you? [Book it.] If not, who in your team owns this?"

**C2 — Proposal walkthrough call (30 minutes)**
> Open (2 min): "Goal today: make sure the proposal matches what you need, and agree a decision path." · Recap (3 min): restate their objectives. · Walk through options (10 min): differences between A/B/C. · Questions and objections (10 min): use Section 15. · Close (5 min): "Which option feels closest? What would need to be true for a yes by [date]? Who else needs to see this?" Agree written next step.

---

## 15. Objection-handling table

| # | Objection | Response |
|---|---|---|
| 1 | "You're too new / no track record." | "True — Vytalix is early, and I won't pretend otherwise. What I bring is [KNOWN founder experience] and a fixed-scope, milestone-based engagement: you pay on delivery, and the first milestone is small. If it doesn't land, you stop." |
| 2 | "Too expensive." | "Compared with what alternative? If it's in-house time, let's cost that. If it's budget, Option A is scoped to £[x] and we can phase the rest." |
| 3 | "No budget this quarter." | "Understood. Would a smaller diagnostic (£[x]) that builds the business case for next quarter be useful? Otherwise let's diarise for [month]." |
| 4 | "We can do this ourselves." | "You can; the question is speed and opportunity cost. We'd compress [x] weeks of learning into [y]. If you'd rather build capability, our workshop format transfers the method to your team." |
| 5 | "Send me some information." | "Happy to. So I send the right thing: is the priority [A] or [B]? I'll send a one-pager and suggest a 15-minute slot to discuss." |
| 6 | "We're talking to a bigger consultancy." | "Good — compare us on who actually does the work, speed, and price. We're founder-delivered, and I'll put that in writing." |
| 7 | "Is MaternaLink live? Can we see it?" | "MaternaLink is in development; there's an early prototype. I'll show it as a concept, not a product. Today's conversation is about [advisory scope], which doesn't depend on it." |
| 8 | "Are you NHS-approved / CE-marked?" | "No, and we don't claim to be. Advisory work doesn't require it. For any software we'd deploy in the NHS we'd go through DTAC and clinical-safety processes first — that's exactly the pathway we help clients plan." |
| 9 | "Not the right time." | "When would be? What changes by then? If [trigger] happens earlier, would you want to move faster?" |
| 10 | "We need a procurement process / framework." | "Understood. Below £[threshold] many organisations can direct-award — can you check your scheme of delegation? Otherwise we'll respond to a mini-tender; tell me the route." |
| 11 | "How do I know you'll deliver?" | "Milestones with acceptance criteria, weekly written updates, and a termination right at 30 days. Plus PI insurance (once in place — I'll confirm the certificate)." |
| 12 | "Can you do it for free / for equity / for exposure?" | "I'll do a free 30-minute session. Paid work stays paid — it's how I stay independent. For equity, only alongside cash and only where there's a strategic fit." |

---

## 16. Pricing and discount guardrails (all prices ESTIMATE — see `/assets/PRICING_STRUCTURE.md`)

| Rule | Guardrail |
|---|---|
| List prices | Advisory day rate £900 (range £800–£1,200); retainers £2.5k–£5k/month; consulting sprints £7.5k–£25k; e-learning £49–£299/learner |
| Discount authority | Founder only; maximum 15% for volume/prepayment; never discount without removing scope or gaining a concession (case-study consent, referral, longer term) |
| Floor | Never below £650/day equivalent (ESTIMATE floor covering founder opportunity cost) |
| Free work | 1 free 30-minute session per prospect; no free proposals beyond 4 pages; no free workshops |
| Payment | Projects: 50% upfront; retainers: monthly in advance; e-learning: prepaid |
| Pilots (MaternaLink, in development) | Never free of cost recovery; minimum £10k pilot fee (ESTIMATE) plus data-protection/clinical-safety preconditions |
| Government (Nigeria) | Quote in GBP or USD; milestone payments with mobilisation fee ≥ 30%; no work before mobilisation payment |
| Equity-for-services | Only with cash component ≥ 50% of list and founder written approval |

---

## Appendix A — Proposal TEMPLATE (copy to `/assets/PROPOSAL_TEMPLATE.md` for client use)

```
VYTALIX — PROPOSAL
[Engagement title]
Prepared for: [Client organisation] — [Sponsor name, role]
Prepared by: Kelvin Williams, Founder, Vytalix (Technology for Life)
Date: [DD Month YYYY] · Valid until: [DD Month YYYY] · Version: [1.0]

1. EXECUTIVE SUMMARY
• The problem: [one sentence in the client's words]
• The outcome: [measurable result by date]
• Our approach: [phases in one line]
• Investment: £[x] (Option B) · Timeline: [n] weeks from [date]
• Decision needed by: [date]

2. YOUR SITUATION (what we heard)
[3–5 bullets from discovery; cite the client's own words]

3. OBJECTIVES AND SUCCESS CRITERIA
| Objective | Success measure | By when |
| | | |

4. APPROACH AND DELIVERABLES
Phase 1 — [name] (Weeks 1–2): activities; deliverable D1
Phase 2 — [name] (Weeks 3–4): activities; deliverable D2
Phase 3 — [name] (Weeks 5–6): activities; deliverable D3

5. TIMELINE
| Week | 1 | 2 | 3 | 4 | 5 | 6 |
| Phase 1 | ■ | ■ | | | | |
| Phase 2 | | | ■ | ■ | | |
| Phase 3 | | | | | ■ | ■ |
Milestone review: end of each phase (30 minutes with sponsor).

6. TEAM
Kelvin Williams — Founder, Vytalix — lead consultant, [KNOWN experience only]
[Associate — only if contracted and named with consent]

7. INVESTMENT
| Option | Scope | Fee (ex VAT) | Payment |
| A — Essential | Phases 1–2 | £[ ] | 50% on signature, 50% on D2 |
| B — Recommended | Phases 1–3 | £[ ] | 50% on signature, 25% on D2, 25% on D3 |
| C — Extended | B + 3 months advisory retainer | £[ ] | as B + monthly in advance |
VAT: [applicable / not applicable — TO VALIDATE at incorporation/VAT registration].

8. ASSUMPTIONS, EXCLUSIONS, DEPENDENCIES
• Client provides [documents/access] by [date]
• Excludes [x]
• No personal or patient data is processed in this engagement unless a DPA is signed
• Change control: scope changes agreed in writing with fee impact

9. TERMS
Governed by the Vytalix Master Services Agreement dated [ ] (or attached). Vytalix retains pre-existing IP and methods; client owns deliverables on full payment. Confidentiality mutual. Liability capped at fees paid. Governing law: England and Wales.

10. ACCEPTANCE
Signed for [Client]: ____________  Name/Role: ________  Date: ______
Signed for Vytalix:  ____________  Kelvin Williams, Founder   Date: ______
```

---

## Priorities / Risks / Next actions

**Priorities**
1. Stand up the CRM and the S1/S2 target list (150 contacts) — Week 1.
2. Run the first 5 discovery calls and send 2 proposals — by Day 14.
3. Sign 1 engagement by Day 30; 3 by Day 90.

**Risks**
| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Founder time split between sales, investors and product | High | High | Time-blocking in `/docs/17_FOUNDER_OPERATING_SYSTEM.md`; sales first in the morning |
| Selling before incorporation/insurance | High | Medium | Contract in personal/sole-trader name only with solicitor sign-off; incorporate by Day 14 (`/docs/18_90_DAY_EXECUTION_PLAN.md`) |
| Overclaiming MaternaLink | Medium | High | FACTS_BASE language rules; deck review before every meeting |
| Pricing too low to sustain | Medium | Medium | Floor and guardrails (Section 16) |

**Next actions**
| Action | Owner | Deadline |
|---|---|---|
| Create HubSpot Free account, import pipeline stages and fields | Founder | Tue 15 Sept 2026 |
| Build 150-contact ICP list (S1/S2) with source URLs | Founder | Fri 18 Sept 2026 |
| Adapt E1/L1 templates and send first 40 touches | Founder | Fri 18 Sept 2026 |
| Draft MSA/SOW for solicitor review | Founder → solicitor | Fri 25 Sept 2026 |
