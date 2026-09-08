# 11 — Brand and websites

**What the company is called, what it looks like, how to write as it, and what is already built online.**

## In one minute
- The group is Vytalix. The first product is MaternaLink. Each is spelled one way only.
- The repository is spelled "Vitalyx". That is a typo and needs fixing.
- Other companies already use names close to Vytalix. Clear this before you spend money.
- The logo, the colours and the two fonts are settled. Nothing there needs redesigning.
- Two websites are built and live, but both are full of placeholders and not launch-ready.

## What to do

| Action | Who | By when |
|---|---|---|
| Order a trade-mark search in classes 9, 42 and 44 | You, with a trade-mark attorney | Within 30 days |
| Check the name at Companies House and buy the domain | You | Within 30 days |
| Change every "Vitalyx" to "Vytalix" in the repository | You | Within 14 days |
| Fill in every square-bracket placeholder on both websites | You | Before any public launch |
| Get a solicitor to read the privacy, terms and cookie pages | Solicitor | Before any public launch |

## The name

| Thing | The decision |
|---|---|
| The group | Vytalix — the parent company that owns everything |
| The product | MaternaLink — one product inside the group, in development |
| Spelling | One word. No hyphen, no space. Capital V, and capital M and L. |
| Product spelling | MaternaLink with one "l" in the middle, not "MaternalLink" |
| Tagline | Technology for Life |
| Repository | The name "Vitalyx" is wrong. Fix it. |

The prototype site says "Maternal Link" and "MaternalLink". Both spellings are retired.

**Names that already exist and must be cleared.** All VERIFIED (we saw them in public records).

| Name | Where it is | Why it matters |
|---|---|---|
| Vytalyx Inc. | United States, Austin, Texas — health technology | Nearly the same name in nearly the same trade. Highest risk. |
| Vytalize Health | United States, New Jersey — health care | Sounds identical when spoken aloud. |
| VITALIX LTD, two companies | UK, numbers 16813455 and 15155964 | Companies House can refuse a name that is too similar. |
| VITALX LTD and VYTAL(UK) LIMITED | UK | Lower risk, but any search will find them. |

TO VALIDATE (not checked yet, so treat as unknown): whether Companies House will accept the name, and whether a trade mark can be registered. Do not order signs, printed paper, or a trade-mark filing until an attorney has said yes.

If the name has to change, the cost is a new wordmark and a find-and-replace. The colours, fonts and writing rules below all still work.

## The look

The logo is real and is the founder's own. It is a heart outline whose right-hand stroke becomes a circuit line ending in a dot, next to the word Vytalix and the line "Technology for Life".

Do not redraw it, recolour it, or stretch it. Leave clear space around it equal to the height of the "V". Use the heart on its own only where the logo would be under 120 pixels wide. The files are `website/assets/img/vytalix-logo.png` (whole logo) and `vytalix-mark.png` (heart only).

The main blue was sampled straight from the logo file, so the brand matches the logo rather than the other way round.

| Colour | Hex | Where it goes |
|---|---|---|
| Vytalix Blue | `#153892` | The logo, links, main buttons |
| Blue Dark | `#0E2A70` | A button when the mouse is over it |
| Deep | `#0F2354` | Dark panels behind headings |
| Ink | `#0F2233` | Body text |
| Slate | `#46545F` | Smaller, less important text |
| Ember | `#BF3E27` | The one warm accent. Never more than 5% of a page. |
| Bone | `#F7F4EE` | Page background |
| Mist | `#E9EDF8` | Tinted bands between sections |
| Signal Blue | `#9DB8FF` | Highlights on dark panels. Never text on white. |

| Typeface | Used for | If it cannot be installed |
|---|---|---|
| Fraunces | Headings and big numbers | Georgia |
| Manrope | Body text, buttons, labels | Arial |

## How to write as Vytalix

1. Say the stage you are at. You are pre-seed and founder-led. Say so.
2. Keep sentences under 25 words. One idea per paragraph.
3. Never claim a customer, partner, approval, clinician or result that does not exist.
4. Every number carries its source. If you cannot cite it, delete it.
5. Write "we" and "you". Not "the company" and not "it is recommended".
6. Put anything unknown in square brackets, so it cannot be published by accident.

| Say this | Not this |
|---|---|
| "MaternaLink is in development. It supports coordination. It is not a diagnostic tool." | "MaternaLink predicts and prevents maternal complications." |
| "We are founder-led and pre-seed. Here is what we can do today." | "Trusted by leading NHS trusts." |
| "We will tell you if your idea should not be built." | "We turn every vision into reality." |
| "Accreditation is being explored. Our courses are not accredited yet." | "CPD-certified courses." |
| "Register your interest. We will post roles when we can pay for them." | "Join our fast-growing team." |
| "[Registered office address — add after incorporation]" | An address you do not have |

Banned words in anything you publish: revolutionary, cutting-edge, world-class, seamless, leverage, and "solutions" used as filler.

## The two websites

Both are plain HTML. There is nothing to compile and no third-party code beyond the fonts.

| Site | Live address | What is on it |
|---|---|---|
| Vytalix group | https://elkelvinwilliams.github.io/Vitalyx/ | 14 pages: home, about, the four pillars (advisory, consulting, health solutions, e-learning), MaternaLink, partnerships, insights, careers, contact, privacy, terms, cookies. Folder: `website/`. |
| MaternaLink product | https://elkelvinwilliams.github.io/Vitalyx/maternalink/ | 8 pages: home in English and French, platform, programmes, security, pricing, pilot request form, plus a demo login and a demo dashboard with made-up data. Folder: `maternalink-site/`. |

The MaternaLink pages were rewritten so that nothing claims a medical device or a clinical decision. The rules that raise an alert are described as settings the health provider chooses, reviewed by a human.

**Placeholders to fill before a real launch.** Search each page for the character `[` to find them all.

| Placeholder | Note |
|---|---|
| Registered company name and number | Needs the company to exist first |
| Registered office address | Same |
| ICO registration number | ICO is the UK data-protection regulator you must register with |
| Contact email and social links | No phone number until a real business line exists |
| The domain in `sitemap.xml`, `robots.txt` and the page headers | Buy the domain first |
| The contact form and the pilot form addresses | Point them at a real form service and test them |
| The sharing image used when a link is posted | Render it from `assets/img/og-image.svg` |
| The legal entity line in the MaternaLink footer | Needs the company to exist first |

Also before launch: a solicitor reads the three legal pages, the French translation gets a professional check, the demo login goes behind real security, and someone checks every claim against `/FACTS_BASE.md`.

## What still needs making

| Item | Status |
|---|---|
| Slide template for decks | TO DO — the layout is specified, nobody has built the file |
| Letterhead and proposal template in Word | TO DO |
| Email signature | TO DO — name, role, "Vytalix · Technology for Life", no phone yet |
| LinkedIn post templates | TO DO — three layouts specified |
| Photography | NONE — use the drawn illustrations until real photos are paid for |
| Sharing image for links | TO DO — render from the SVG already in the repository |

Never buy stock photographs of doctors in white coats. They suggest a clinical partnership you do not have.

## Words explained

| Word | What it means |
|---|---|
| Wordmark | The company name drawn as artwork, rather than typed in a font |
| Hex | The six-character code that tells a screen exactly which colour to show |
| Placeholder | Text in square brackets standing in for a fact you do not have yet |
| Trade mark | A registered legal right to use a name in a defined line of business |
| ICO | The Information Commissioner's Office, the UK data-protection regulator |
| Static site | A website of finished pages, with no database and nothing to run on a server |
