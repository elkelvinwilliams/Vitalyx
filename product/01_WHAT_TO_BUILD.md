# 01 — MaternaLink: what to build first

**This document is for your developer.**

**It says what the first version of MaternaLink must do, what it must never do, and what it costs.**

## In one minute

- MaternaLink helps a pregnant woman and her care team stay in touch between appointments.
- It never diagnoses, never predicts and never advises. That rule shapes every screen.
- The first build takes 12 to 16 weeks with a team of three or four people.
- It works offline, and it works on a plain phone in Nigeria by text message.
- Cost is £220k–£320k with a UK team, or £140k–£210k with a UK and Nigeria team (ESTIMATE: our best guess, not a fact).

## What to do

| Action | Who | By when |
|---|---|---|
| Settle who owns the old prototype code and the name | Founder | Before build week 1 |
| Get a lawyer to confirm this is not a medical device | Founder and counsel | Build week 2 |
| Appoint a Clinical Safety Officer and open the hazard log | Founder | Build week 2 |
| Choose UK-led or UK-plus-Nigeria team, and fund it | Founder | Before build week 1 |
| Book the security test and accessibility audit | Developer | Build week 4, for weeks 13–14 |

## Safety rules for whoever builds this

1. The software never diagnoses. It never says what a symptom or a reading means.
2. The software never predicts. No risk score, no probability, no forecast.
3. The software never recommends treatment. It shows information and it moves messages to people.
4. Every rule that flags a record belongs to the hospital's own clinicians. We ship the rule editor, not the rules.
5. Every rule stores a named owner and a review date. No owner, no rule.
6. Every flag goes to a named human with a deadline. If the deadline passes, it goes to another named human.
7. If you are unsure whether a feature interprets data, assume it does. Stop and ask the Clinical Safety Officer.

## Goals, and what we deliberately will not build

| # | Goal at first release | How we know it is met (design target, ESTIMATE) |
|---|---|---|
| G1 | A woman and her team complete a whole pregnancy episode in the product | All acceptance scenarios pass in staging |
| G2 | Every message has a human owner and is acknowledged in time | 95% acknowledged in time; no unowned messages in the audit |
| G3 | Handover between professionals uses a structured summary | 60% of births at the test site have a summary |
| G4 | A Nigeria group can be enrolled and run on text message alone | 80% of texts delivered; defaulter list produced daily |
| G5 | The product ships with its paperwork | Safety case signed, DPIA done, security test passed, accessibility audit passed, DTAC form filled, Cyber Essentials certified |
| G6 | It works offline and on poor connections | Core woman-side screens work offline; under 1% of synced records clash |

| # | Not building now | Why |
|---|---|---|
| NG1, NG2 | Any risk score or "instability score"; threshold alerts on blood pressure, weight or movements | Research track only. A monitoring purpose makes it a medical device |
| NG3, NG4 | Automatic sorting of messages by urgency; symptom checker, chatbot, generated advice, any model output shown to a woman | The software would be deciding clinical urgency. Content is pre-approved by clinicians only |
| NG5, NG6 | Scored mental-health questionnaires; writing into hospital record systems, NHS login, demographics lookup | Version 2. Version 1 gives text you can paste and print |
| NG7, NG8 | Partner accounts; video calls, wearables, device pairing, payments | Safeguarding design must come first; the rest is out of scope |
| NG9, NG10 | Being the legal record of care; native iPhone and Android apps | The hospital or facility record stays the legal record. A web app only, until after the first evaluation |

## Who uses it

| Role | Who they are | What they see |
|---|---|---|
| `mother` | The enrolled woman. UK: web app. Nigeria: text message, or web app | Home, schedule, learn, diary, messages, my team, settings |
| `partner` | Companion, with her consent and revocable by her | Nothing in version 1. Designed in version 2 only |
| `midwife`, and `care_worker` with fewer rights | Community midwife; Nigeria community health worker | Caseload, inbox, contact log, handover, escalation, defaulters |
| `clinician` | Obstetrician, facility doctor or nurse-midwife | Caseload for the site, handover, escalation, care notes |
| `programme_manager` | Head of midwifery, ministry officer, NGO lead (the supervisor role) | Dashboard, exports, rotas, content library |
| `operator_admin` | Hospital IT, state IT, partner admin | Organisations, sites, users, roles, consent texts, content, audit |
| `vytalix_support` | Vytalix support and safety staff | Break-glass only: time-boxed, reason recorded, customer told |

## What it must do

M = must have, the build cannot ship without it. S = should have, drop to version 1.1 if time runs short. C = could have, later. W = not in this release.

| Group | Requirements (M must, S should, C could, W not now) | Level |
|---|---|---|
| F1 Enrolment and consent | FR-001 staff enrol with name, date of birth, phone, language, channel, site, due date and consent, with a duplicate check on phone and date of birth. FR-003 consent recorded in five separate parts (platform, contact, SMS wording, research, reporting), each versioned and withdrawable. FR-004 withdraw in app or by texting STOP, effective within one sync, staff told. FR-005 under-18 starts the site's safeguarding steps. FR-006 interpreter need is a flag with free text. Should-have: FR-002 self-enrol by invitation link or keyword with staff confirmation, FR-007 her own reminder window and quiet days, FR-008 offline enrolment with a temporary ID, FR-009 bulk enrolment from CSV with a validation report | M, S |
| F2 Pregnancy profile | FR-011 due date and its source, parity, care team, planned place of birth, birth preferences, language, allergies and conditions entered by staff only, and "things I want my team to know". FR-012 changing the due date rebuilds the schedule, cancels superseded reminders and shows what changes. FR-013 recording the outcome switches to postnatal; a loss stops all pregnancy content within one sync and opens the bereavement pathway. FR-014 every change audited, old value to new value. FR-015 one episode at a time | M |
| F3 Schedule and reminders | FR-016 templates per organisation: UK follows NICE NG201, Nigeria follows the WHO 8-contact model, both signed off by a clinician first. FR-017 dated contacts with type and status. FR-018 reminders at set offsets on her channel inside her window. FR-019 neutral SMS wording by default. FR-020 staff add, move, cancel, mark attended; she can ask to rebook. FR-021 a missed contact goes to the defaulter list. FR-022 two-way SMS confirmation, "reply 1 to confirm" (S). FR-023 calendar export (C). FR-024 booking into facility diaries (W) | M |
| F4 Education | FR-025 every item carries author, clinical reviewer, version, review-by date, language and status. FR-026 served by week of pregnancy, language and country. FR-027 about 40 UK items, 20 Nigeria items, at least 10 Yoruba items if a Yoruba pilot is confirmed (ESTIMATE). FR-028 a permanent emergency banner on every woman-facing screen. FR-029 danger-sign content is general education, never about her own readings. FR-030 an SMS digest for plain phones. FR-032 retiring an item clears it everywhere within one sync. FR-033 text for this and next window cached offline; audio and video only on Wi-Fi | M |
| F5 Messaging | FR-034 she sends a message and picks a plain type: question, appointment, tell my team, important. FR-035 every message has a named owner and an acknowledgement deadline, default 4 working hours. FR-036 a missed deadline reassigns to on-call and tells the manager; a second miss escalates again; all audited. FR-037 acknowledgement is separate from replying and she sees it. FR-039 "important" and "I am not safe" show the emergency banner and phone number at once and reach a human at any hour. FR-040 the system never judges urgency. FR-041 content stays inside the customer boundary; notifications say only "you have a new message". FR-042 her SMS replies land in her thread. FR-043 out of hours, an auto-reply gives service hours and the emergency instruction. FR-044 nothing is deleted; staff mark "sent in error" with a reason. FR-038 approved reply templates (S). FR-045 compressed image attachments (S). FR-046 voice notes (C). FR-047 live chat (W) | M |
| F6 Diary, display only | FR-048 she records feeling, symptoms, movements, blood pressure, weight and questions. FR-049 values are shown exactly as entered with time and "recorded by the woman": no colour, no threshold, no trend reading, no alert anywhere. FR-051 visible on the staff timeline and pre-visit view. FR-052 works offline and queues. FR-050 a plain chart with no reference bands (S). FR-053 diary by SMS keyword (C). FR-054 scored questionnaires (W) | M |
| F7 Care-team console | FR-055 caseload with weeks pregnant, next and last contact, unread messages, missed contacts and flags. FR-056 one chronological timeline per woman. FR-057 team inbox with filters; bulk acknowledge is forbidden. FR-058 contact log. FR-059 care notes, versioned, copyable for pasting into the hospital record. FR-060 rota with on-call and lead, used by the deadline clock. FR-063 reassign a woman, audited. FR-061 offline read and offline notes (S). FR-062 pre-visit summary card (S). FR-064 hospital record integration (W) | M |
| F8 Handover summary | FR-065 built from recorded data, carrying three identifiers and a visible identity-check warning. FR-066 editable before issue; issued versions locked and numbered. FR-067 on screen, print or PDF, copyable text, and a receipt acknowledgement. FR-068 no score and no assessment; a footer says the receiving clinician assesses. FR-069 an on-call handover list (S). FR-070 FHIR export (W) | M |
| F9 Escalation log | FR-071 record it once: to whom, by what means, when, why, outcome, follow-up owner. FR-072 open escalations show on caseload, timeline and handover until closed. FR-073 managers see counts and time-to-close only, never content. FR-074 Nigeria: notify a receiving facility by SMS (S). F10 defaulter tracing: FR-075 a daily list per team, each row assignable to a person with a status, FR-077 CSV export, FR-076 field mode sorted by locality and working offline (S) | M |
| F11 Dashboard | FR-078 operational numbers only: enrolments, active women, contact completion, missed and traced, deadlines met, escalations, content reach, SMS delivered and failed, withdrawals. FR-079 no cell below 5 shown or exported. FR-080 aggregate CSV export; row-level export is admin-only, purpose-bound and audited. FR-081 DHIS2 export (C). FR-082 clinical outcome reporting (W) | M |
| F12 Admin and audit | FR-083 organisation, then sites, then teams; no query crosses organisations. FR-084 invite, assign, deactivate, two-factor for all staff. FR-085 versioned consent texts and schedule templates with a sign-off state. FR-086 content publishing with a two-person rule. FR-087 audit viewer, filterable, unchangeable. FR-088 break-glass with reason, time limit and customer notice. FR-090 per-organisation settings: emergency wording and numbers, hours, deadlines, channels, languages. FR-089 tools to export, correct or delete a woman's data (S) | M |
| F13 Channels | FR-091 woman web app, installable and offline-capable. FR-092 staff console with offline read. FR-093 SMS out and in through one gateway interface with swappable providers. FR-094 UK email and SMS notices carrying no personal or clinical content. FR-095 web push (S). FR-096 WhatsApp, FR-097 USSD, FR-098 voice (C). FR-099 app-store apps (W) | M |
| F14 Safeguarding | FR-100 discreet mode: neutral name and icon, no sensitive previews, quick exit, PIN or fingerprint lock. FR-101 "I am not safe" reaches a named human at once. FR-103 safeguarding records visible only to care roles and the lead; elsewhere only a flag that one exists. FR-104 no partner access; any third party on SMS needs explicit consent. FR-102 staff prompt to confirm the routine safety question (S) | M |
| Across everything | FR-105 every woman-facing screen says "This app helps you and your care team stay in touch. It does not check your health or tell you if something is wrong." FR-107 staff confirm name and date of birth before acting on a searched record. FR-108 timezone-safe dates for Europe/London and Africa/Lagos. FR-109 feature flags per organisation for every S and C item. FR-106 she can see who viewed her record (S). FR-110 full data export if a customer leaves (S) | M |

## How it works offline and syncs

The server is the record. Clients are caches with an outbox. Every write is repeat-safe. Conflicts are resolved by written rules, never silently.

| Rule | What it means |
|---|---|
| Scope | Woman offline: read schedule, content, own diary and messages; write diary, messages, rebooking requests, consent withdrawal. Staff offline: read caseload; write contact logs and notes |
| Storage | IndexedDB encrypted with a key from her PIN or fingerprint. Purge women no longer on the caseload. Cap 50 MB of text per staff device (ESTIMATE). A lost device has its token revoked; the cache expires after 7 days without sync |
| Outbox | Every offline write carries a client UUID v7 and client timestamp, queues in order, and the server accepts each one once only. Consent withdrawal jumps the queue |
| Append-only | Messages, diary, escalations, contact logs and audit events can only be added to, so no conflict is possible. Server receipt time orders them; client time is shown beside it, and skew over 10 minutes is flagged |
| Versioned | Profile, care notes, birth preferences and schedule contacts carry a version. A stale write is rejected and the user chooses between the two versions. Nothing is ever overwritten automatically. Schedule generation, rota, deadline timers, consent state and content publication are computed on the server only |
| Triggers and failure | Sync on reconnect, on app foreground, every 15 minutes online, and on pull. The user always sees unsent items; anything older than 24 hours warns, and for messages tells her to phone her team |

Low bandwidth: a lite mode switches on by itself on 2G, 3G or Save-Data. App shell under 300 KB compressed on first load, each screen's data under 50 KB, offline content bundles under 200 KB per window, changed records only, compression through the CDN.

## Nigeria: text message and WhatsApp

Feature phones are common outside cities (ASSUMPTION: we believe it, we have not proved it). So SMS is a must-have, not an extra.

| Channel | When | Use | Constraints |
|---|---|---|---|
| SMS, two-way | Version 1 | Reminders, digests, replies, keywords CONFIRM, STOP, HELP, MORE | Sender ID registered with MTN, Glo, Airtel and 9mobile, up to 11 characters. The Do-Not-Disturb service on 2442 blocks promotional traffic; transactional messages still go by a corporate route. ₦4–₦6 per message (ESTIMATE, TO VALIDATE) |
| WhatsApp | Version 1.1 | Richer reminders, content cards, two-way chat | Needs a Business Solution Provider, pre-approved templates, per-conversation pricing. Data flows through Meta, so the DPIA and a cross-border check come first |
| USSD and voice | Version 1.1 or 2 | Menus for next appointment, confirm and call-back; recorded reminders in Yoruba, Hausa, Igbo and Pidgin | Short code leased through an aggregator, sessions time out at about 180 seconds, works on any phone with no data. Use recorded human audio, not machine voice |

Gateways: Africa's Talking first for Nigeria, Termii as failover, Twilio for UK SMS, Infobip as the enterprise alternative. All prices and coverage TO VALIDATE (nobody has checked yet). Build one `ChannelProvider` interface (send, inbound webhook, delivery status, opt-out sync) so a provider is configuration, not a code change, and record the cost of each message so it can be billed on.

Compliance: record opt-in before the first SMS; handle STOP in every language; respect the Do-Not-Disturb list; register the sender ID before the pilot; keep clinical content out of SMS. The Nigeria Data Protection Act 2023 applies, and registration with the NDPC is likely because health is a designated sector (TO VALIDATE).

## Accessibility and languages

| Item | Requirement |
|---|---|
| Standard | WCAG 2.2 AA on both web apps, audited by an outside assessor before go-live (£3k–£6k ESTIMATE) |
| Reading and audio | Woman-facing English at reading age 9 to 11, checked with a readability tool and with real users. An audio version of every must-have item in each language |
| Controls | Touch targets 44px or more, high-contrast theme, scalable text, screen-reader labels, no meaning carried by colour alone. Discreet mode and quick exit work by keyboard and screen reader |
| Phones and devices | Every must-have woman-side function has an SMS equivalent: reminder, confirm, message, STOP. Works on low-end Android with 2 GB RAM on Android 9+, iOS 15+ Safari, and the last two versions of Chrome, Edge, Firefox and Safari on desktop |
| Languages | Now: English interface for every role, a Yoruba content subset if a Yoruba pilot is confirmed, SMS templates in English and Yoruba. Next: Yoruba interface and Pidgin for SMS and voice in 1.1, Hausa in 1.2 or 2, Igbo in 2, UK community languages by content only |
| Translation | Professional translator, then back-translation, then a clinician signs off in that language, then testing with at least 5 women per language. Machine translation may draft internal first passes only, never published unreviewed |
| Cost | £0.10–£0.20 per word, about 15,000 words per language, so £2k–£4k per language, plus £1k–£3k for review and audio recording (ESTIMATE) |

## The data, as a list of things stored

Every table has an ID, an organisation ID and timestamps. Fields holding direct identifiers are encrypted separately.

| Group | Entities |
|---|---|
| Tenancy | `organisation`, `site`, `team`, `user`, `feature_flag`, `channel_config` |
| The woman | `woman`, `episode`, `clinical_note_field`, `consent_text`, `consent_record` |
| Schedule and messages | `schedule_template`, `contact`, `reminder`, `delivery_attempt`, `message_thread`, `message`, `acknowledgement`, `sla_event` |
| Care records | `diary_entry`, `contact_log`, `care_note`, `escalation`, `handover_summary`, `handover_ack`, `defaulter_item` |
| Content and staffing | `content_item`, `content_version`, `content_engagement`, `rota`, `rota_shift` |
| Restricted and system | `safeguarding_record`, `data_subject_request`; `audit_event` (insert-only, its own schema), `analytics_event` (no personal data), `job` |

Rules: row-level security on every table that has an organisation ID, checked by a nightly test. Append-only tables give the application INSERT rights only, so a correction is a new row. Versioned writes reject a stale version with HTTP 409 and return both. A unique index on organisation plus client UUID makes writes repeat-safe. Small-cell suppression lives in the SQL views, not the interface. A nightly job anonymises or deletes closed episodes per each customer's retention policy.

## The main API endpoints

REST, OpenAPI 3.1, under `/v1`. Everything needs a login except health checks, OTP start and signed gateway webhooks.

| Area | Endpoints |
|---|---|
| Login | `POST /auth/otp/start`, `/auth/otp/verify`, `/auth/pin/unlock`, `/auth/refresh`, `/auth/logout`; `GET /auth/oidc/callback` for staff |
| Admin | `GET/PUT /org`; `/org/sites`, `/org/teams`, `/org/users`, `/org/roles`, `/org/consent-texts`, `/org/schedule-templates`, `/org/channel-config`, `/org/feature-flags`; `GET /org/audit` |
| Women and episodes | `POST /women`, `GET/PUT /women/{id}`, `POST /women/import`, `POST /women/{id}/episodes`, `PUT /episodes/{id}`, `POST /episodes/{id}/outcome`, `GET /episodes/{id}/timeline` |
| Consent and schedule | `GET/POST /women/{id}/consents`, `POST /me/consents`; `GET/POST /episodes/{id}/contacts`, `PATCH /contacts/{id}`, `GET /me/contacts`, `POST /me/contacts/{id}/reschedule-request` |
| Content | `GET /me/content`, `GET /content/{slug}`, `GET /me/content/bundle`, `POST /me/content/{id}/engagement`; `/content-items` with submit, approve, retire |
| Messages, diary and notes | `GET /me/thread`, `POST /me/messages`, `GET /threads`, `POST /messages/{id}/acknowledge`, `POST /threads/{id}/messages`, `POST /messages/{id}/sent-in-error`, `POST /threads/{id}/reassign`; `GET/POST /me/diary`, `GET /episodes/{id}/diary`, `POST /episodes/{id}/contact-logs`, `GET/POST /episodes/{id}/notes`, `PUT /notes/{id}`, `GET /episodes/{id}/pre-visit` |
| Escalation and handover | `POST /episodes/{id}/escalations`, `PATCH /escalations/{id}`, `GET /escalations`; `POST /episodes/{id}/handover`, `PUT /handover/{id}`, `POST /handover/{id}/issue`, `GET /handover/{id}.pdf`, `POST /handover/{id}/acknowledge` |
| Defaulters, rota, reports | `GET /defaulters`, `PATCH /defaulters/{id}`, `GET /defaulters/export.csv`; `GET/POST /teams/{id}/rota`, `GET /teams/{id}/on-call/now`; `GET /reports/summary`, `/reports/export.csv`, `/reports/escalations/aggregate`. Platform: `GET /health`, `/ready`, `/version`, `/openapi.json` |
| Sync and restricted | `POST /sync/push`, `GET /sync/pull?cursor=`, `GET /sync/status`; `POST /episodes/{id}/safeguarding`, `GET /safeguarding/queue`, `POST /women/{id}/dsr`, `POST /support/break-glass` |
| Webhooks | `POST /webhooks/{provider}/inbound-sms`, `/delivery-status`, `/ussd`, signature or IP checked and repeat-safe by provider message ID |

Conventions: cursor pagination, a version field on every update, an `Idempotency-Key` header accepted on every POST, RFC 9457 error bodies, rate limits per token and per IP, and a request ID on every response that also appears in the audit log.

## Security controls

| Control | What to build |
|---|---|
| Boundary, configuration and access | CloudFront with a web application firewall, private subnets, no public database or cache, outbound traffic only to allow-listed gateways, everything built from Terraform, hardened images, no default credentials. Two-factor login for all staff, role and scope checks in the API with row-level security as a second line, quarterly access reviews, break-glass always audited |
| Encryption | TLS 1.2 or higher in transit. Customer-managed KMS keys for database, storage, cache and disks, separate per environment. Names, phone numbers and dates of birth wrapped in a per-organisation key, with hashed index columns so duplicates can be found without decrypting. On device, IndexedDB encrypted from the PIN, expiring after 7 days |
| Audit | Every detail-view read, every write, every login, every export, every break-glass session. Insert-only role, hash-chained, copied nightly to write-once storage, kept at least 6 years |
| Malware, patching and monitoring | Container image scanning, attachment scanning before storage, managed devices, critical updates within 14 days; central logs, GuardDuty, alerts to an on-call engineer and on unusual bulk or out-of-hours reads |
| Backup and recovery | Daily snapshots plus point-in-time recovery to 5 minutes, kept 35 days, copied to a separate UK backup account. Target: lose at most 15 minutes of data and restore within 4 hours. Test the restore every quarter. If the API is down, her app still shows the cached schedule, content and emergency banner, and a static page carries the site's phone numbers |
| Certification targets | Cyber Essentials (£300–£600 plus VAT), then Cyber Essentials Plus (£1,500–£3,000 plus VAT), then the NHS Data Security and Protection Toolkit as a Category 3 supplier (35 assertions, 42 evidence items). None of these exist today |

## How it is tested

| Level | Tools | What must be covered |
|---|---|---|
| Unit | Vitest and schema tests | Schedule generation, deadline timers, consent state machine, suppression, encryption helpers |
| Contract and integration | Tests generated from the OpenAPI file, recorded gateway fixtures, Testcontainers with Postgres, Redis and Keycloak | Every endpoint and adapter; row-level security on every table, repeat-safe and versioned writes, retention jobs |
| End to end | Playwright on both web apps, including offline and throttled networks | All 20 acceptance scenarios, including sync conflicts |
| Safety | Test cases written against the hazard log | Every hazard control, before every release, recorded in the safety case |
| Accessibility and performance | axe-core in the pipeline, manual screen-reader passes, outside audit; k6 load tests and Lighthouse budgets | No AA failures left open; reads under 500 ms and writes under 1 second at the 95th percentile |
| Security | CodeQL, dependency and image scans, secret scanning, ZAP baseline, outside penetration test (£6k–£12k) | No high or critical findings left open |
| Resilience and language | Gateway failure injection, cache loss, database failover drill; pseudo-localisation and native-speaker review | Queue replay and failover proven; every published string reviewed |

Capacity the design must reach without rework: 5 organisations, 20 sites, 200 staff, 20,000 enrolled women and 2 million SMS a year (ESTIMATE). Availability target 99.5% at first release. Reminders handed to the gateway within 5 minutes of the scheduled time, 99% of the time.

## What it costs to build

Sixteen weeks. A twelve-week version drops the should-have items and staff offline writing.

| Item | UK-led | UK plus Nigeria |
|---|---|---|
| Tech lead and architect, full time, 80 days | £60,000 | £60,000 |
| Two full-stack engineers, full time | £88,000 | £32,000–£48,000 |
| Product designer, half time | £20,000 | £12,000 |
| Test automation engineer, half time | £16,000 | £6,000–£8,000 |
| DevOps and security engineer, 15 days | £10,500 | £10,500 |
| Clinical Safety Officer, 16 days | £12,800 | £12,800 |
| Clinical content authors and reviewers | £10,000 | £12,000 |
| Yoruba translation and audio | £4,000–£8,000 | £3,000–£6,000 |
| Penetration test | £6,000–£12,000 | £6,000–£12,000 |
| Accessibility audit | £3,000–£6,000 | £3,000–£6,000 |
| Regulatory and data-protection counsel | £8,000–£15,000 | £8,000–£15,000 |
| Cyber Essentials and Plus, plus cloud and tools during the four-month build | £4,000–£7,600 | £4,000–£7,600 |
| Contingency, 15% | about £36,000 | about £23,000 |
| **Total (ESTIMATE)** | **£220,000–£320,000** | **£140,000–£210,000** |

Running cost after launch, each month (ESTIMATE): cloud £350–£700, tools £50–£150, messaging billed on as used, and £3,000–£4,500 for a support engineer at 0.3 of a person plus a safety officer at 0.1. Once a year: penetration test, Cyber Essentials Plus, accessibility re-audit and Toolkit effort, £15,000–£25,000. The blended team assumes the UK tech lead owns architecture, security and the safety-critical parts, and reviews every merge. None of this is funded today.

## Words explained

| Word | What it means |
|---|---|
| PWA (web app) | A website that installs like an app and works offline |
| Append-only, row-level security | Rows can be added but never changed, so the record cannot be quietly rewritten; and the database itself refuses to show one customer's rows to another |
| Tenant and break-glass | One customer organisation and all of its data; and emergency support access to it, time-limited, recorded, with the customer told |
| DPIA | The written check that a product handles personal data lawfully |
| DCB0129 and DTAC | The NHS standard for proving software is clinically safe, and the NHS checklist a product must pass before a hospital can buy or pilot it |
| WCAG 2.2 AA | The accessibility standard public services must meet |
| ESTIMATE / TO VALIDATE / ASSUMPTION | Our best guess, not a fact / nobody has checked this yet / we believe it but have not proved it |
