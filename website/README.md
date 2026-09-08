# Vytalix website (static)

Fourteen hand-written HTML pages, one stylesheet, one script, SVG assets. No build step, no external JavaScript. Open `index.html` locally or deploy the folder as-is.

## Deploy
- **Netlify:** drag the `website/` folder into the Netlify dashboard, or connect the repo with publish directory `website`. Enable Netlify Forms and add `data-netlify="true"` to the contact form, or point the form `action` at a Formspree endpoint.
- **Vercel:** import the repo; framework preset "Other"; output directory `website`.
- **GitHub Pages:** copy the folder to a `gh-pages` branch root, or set Pages to serve from `/website` on this branch via an action.
- Add a custom domain after name and trademark clearance (see `/docs/00_MASTER_AUDIT.md`). Until then the site should stay unpublished or password-protected.

## Placeholders to fill before launch
Search the pages for `[` to find every bracketed placeholder. The main ones: registered company name and number, registered office address, ICO registration number, contact email, phone (only once a business line exists), social links, the `sitemap.xml` / `robots.txt` placeholder domain, the JSON-LD Organization block in each page head, the contact form `action`, and the OG image URL.

## Pre-launch checklist
1. Entity incorporated; name and trademark cleared; domain owned.
2. Privacy, Terms and Cookie Policy reviewed by a solicitor (they are marked Draft).
3. Contact form wired to a real endpoint and tested; spam protection enabled.
4. Every claim on the site traceable to `/FACTS_BASE.md` (no clients, partners, approvals, outcomes or team members that are not real).
5. Accessibility pass: keyboard navigation, focus states, contrast, alt text, reduced-motion.
6. Performance: images optimised, fonts limited to the two families, no third-party scripts beyond fonts.
7. Analytics only after the cookie banner is verified to gate non-essential cookies; prefer a cookieless option.
8. Run the link check: `python3 -c "..."` in `/website` (see the build session notes) or any static link checker.
9. Publish `sitemap.xml`, submit to Search Console, set canonical URLs.
10. Add the Insights articles as they are written; remove "coming soon" states.
