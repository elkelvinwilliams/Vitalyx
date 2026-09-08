# Page bodies for the MaternaLink site. Regenerate with: python3 maternalink-site/_shell.py
INDEX = '''
<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="status-pill" data-i18n="status">In development · pilot partners invited</span>
      <h1 data-i18n="hero_h1" style="margin-top:1rem">Offline-first maternal and newborn care coordination for health systems</h1>
      <p class="lead" data-i18n="hero_lead">MaternaLink helps maternity programmes enrol women, stay in contact between appointments, record what matters at the point of care without a connection, and route every reported concern to a responsible clinician.</p>
      <div class="hero-actions"><a class="btn btn-primary" href="pilot.html" data-i18n="hero_cta1">Request a pilot</a><a class="btn btn-secondary" href="platform.html" data-i18n="hero_cta2">See how it works</a></div>
    </div>
    <div class="preview" aria-label="Programme overview, demo data">
      <div class="preview-head"><strong data-i18n="preview_title">Programme overview</strong><span data-i18n="preview_sub">Demo data</span></div>
      <div class="row"><span class="avatar" style="background:#153892">AA</span><div class="who"><b>Adaeze A.</b><span>34 weeks · Community midwife: T. Bello</span></div><span class="badge badge-flag">Flag: BP review</span></div>
      <div class="row"><span class="avatar" style="background:#C93D63">RO</span><div class="who"><b>Rebecca O.</b><span>Newborn, day 6 · Postnatal visit due</span></div><span class="badge badge-medium">Follow-up</span></div>
      <div class="row"><span class="avatar" style="background:#1B7F4B">FK</span><div class="who"><b>Funmi K.</b><span>22 weeks · Daily check-in complete</span></div><span class="badge badge-low">On track</span></div>
      <div class="row"><span class="avatar" style="background:#4B5568">SM</span><div class="who"><b>Sarah M.</b><span>28 weeks · Glucose diary (clinician targets)</span></div><span class="badge badge-low">On track</span></div>
      <p class="help" style="margin:.6rem 0 0">Flags are programme-configured rules for human review. Synthetic names; no real patient data.</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head"><h2 data-i18n="ch_h2">System-level challenges in maternal and newborn care</h2><p class="lead" data-i18n="ch_lead">Public-sector maternity programmes often operate where clinical risk is real but timely detection and escalation are structurally constrained.</p></div>
    <div class="grid grid-2">
      <div class="card"><span class="num">01</span><h3 data-i18n="ch1_h">Late detection of complications</h3><p data-i18n="ch1_p">Vital signs and symptoms are recorded infrequently or reviewed too late, so warning signs surface after the window for early action.</p></div>
      <div class="card"><span class="num">02</span><h3 data-i18n="ch2_h">Low-connectivity environments</h3><p data-i18n="ch2_p">Many community and primary-care settings lack reliable internet, which limits real-time digital systems.</p></div>
      <div class="card"><span class="num">03</span><h3 data-i18n="ch3_h">Fragmented data between community and facility</h3><p data-i18n="ch3_p">Information is spread across paper records, devices and facilities, reducing continuity of care.</p></div>
      <div class="card"><span class="num">04</span><h3 data-i18n="ch4_h">Delayed escalation and avoidable harm</h3><p data-i18n="ch4_p">Without clear escalation pathways, early warning signs may not trigger timely clinical action.</p></div>
    </div>
  </div>
</section>

<section class="band" id="how">
  <div class="container">
    <div class="section-head"><h2 data-i18n="how_h2">How the system works</h2><p class="lead" data-i18n="how_lead">Designed to function reliably in low-connectivity environments while giving programme leads oversight and structured escalation.</p></div>
    <div class="grid grid-3 steps">
      <div class="card step"><h3 data-i18n="how1_h">Offline data capture</h3><p data-i18n="how1_p">Symptoms and vitals are recorded at the point of care without an internet connection.</p></div>
      <div class="card step"><h3 data-i18n="how2_h">Secure local storage</h3><p data-i18n="how2_p">Data is encrypted on the device until connectivity returns.</p></div>
      <div class="card step"><h3 data-i18n="how3_h">Automatic synchronisation</h3><p data-i18n="how3_p">Once online, records sync to the central platform and conflicts are resolved with a full audit trail.</p></div>
      <div class="card step"><h3 data-i18n="how4_h">Programme escalation rules</h3><p data-i18n="how4_p">Rules configured and owned by your clinical governance flag records for human review. MaternaLink does not diagnose or recommend treatment.</p></div>
      <div class="card step"><h3 data-i18n="how5_h">Alerts to the responsible clinician</h3><p data-i18n="how5_p">Flags reach the named clinician or supervisor, with contact and outcome logged against the record.</p></div>
      <div class="card step"><h3>Timeline and exports</h3><p>One shared timeline per woman and newborn; CSV and PDF exports for audit, handover and evaluation.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head"><h2 data-i18n="who_h2">Who the platform is designed for</h2><p class="lead" data-i18n="who_lead">Built for maternity services and programme operators responsible for maternal and newborn care at scale.</p></div>
    <div class="grid grid-3">
      <div class="card tint"><h3 data-i18n="who1_h">Government and state programmes</h3><p data-i18n="who1_p">Population-level enrolment, facility oversight and indicators aligned to your health-information system.</p><a href="programmes.html#government">Programme deployment →</a></div>
      <div class="card tint"><h3 data-i18n="who2_h">Hospitals and maternity units</h3><p data-i18n="who2_p">Continuity between appointments, structured intake, and a shared timeline for the care team.</p><a href="programmes.html#hospitals">Hospital deployment →</a></div>
      <div class="card tint"><h3 data-i18n="who3_h">NGO and donor-supported initiatives</h3><p data-i18n="who3_p">Cohort management, community health-worker workflows and evaluation-ready data exports.</p><a href="programmes.html#ngo">NGO deployment →</a></div>
    </div>
  </div>
</section>

<section>
  <div class="container two-col">
    <div><h2 data-i18n="honest_h">What MaternaLink is, and is not</h2><p class="lead">We would rather you hear this from us than find it in due diligence.</p></div>
    <div>
      <ul class="ticks"><li data-i18n="honest_is">A care-coordination and communication platform, in development, being designed with clinicians and subject to validation.</li><li>Offline-first, low-bandwidth, with SMS and WhatsApp channels on the roadmap for settings without smartphones.</li><li>Built with a clinical-safety approach: intended-use statement, hazard log, data-protection impact assessment.</li></ul>
      <ul class="ticks crosses" style="margin-top:1rem"><li data-i18n="honest_not">Not a medical device, not a diagnostic or prediction tool, not an emergency service, and not yet approved, assessed or validated by any regulator or health system.</li><li>Not an electronic patient record: where your organisation has one, MaternaLink integrates and your record remains the record.</li></ul>
    </div>
  </div>
</section>

<section class="band">
  <div class="container two-col" style="align-items:center">
    <div><h2 data-i18n="cta_h2">Design the pilot with us</h2><p class="lead" data-i18n="cta_lead">We are inviting a small number of maternity services and programmes to co-design a 12-week evaluation.</p></div>
    <div style="text-align:right"><a class="btn btn-rose" href="pilot.html" data-i18n="cta_btn">Request a pilot</a></div>
  </div>
</section>
'''

PLATFORM = '''
<section class="hero"><div class="container"><span class="eyebrow">Platform</span><h1>One shared timeline from booking to postnatal discharge</h1><p class="lead">MaternaLink brings enrolment, contact, self-reported information, clinician notes and programme escalation rules into one place that works offline. Every capability below is described as designed, not as validated; see the roadmap.</p></div></section>
<section><div class="container">
  <h2>Core capabilities (v1)</h2>
  <div class="grid grid-3">
    <div class="card"><h3>Enrolment and discharge</h3><p>Consent-led enrolment at the booking or week-16 appointment; linked newborn records at birth; structured offboarding at postnatal discharge with retention rules applied automatically.</p></div>
    <div class="card"><h3>Offline capture</h3><p>Symptoms, vitals and notes recorded on phones or tablets without connectivity; encrypted on device; synchronised with a full audit trail when online.</p></div>
    <div class="card"><h3>Daily check-in</h3><p>A short, configurable daily questionnaire for the woman, with streaks and reminders. Concerning answers route to a named human within the programme's response time.</p></div>
    <div class="card"><h3>Symptom log</h3><p>Plain-language prompts for symptoms such as itching of the hands and feet, persistent vomiting, headache, visual disturbance or reduced movements, with one-tap contact to the care team. The software records and routes; it does not interpret.</p></div>
    <div class="card"><h3>Partner engagement</h3><p>With the woman's consent, a partner or birth companion receives education, appointment prompts and short quizzes. She controls access and can revoke it silently.</p></div>
    <div class="card"><h3>Education library</h3><p>Content signed off by the programme's clinicians, delivered in-app and by message, with local-language versions on the roadmap.</p></div>
    <div class="card"><h3>Escalation queue</h3><p>Flags raised by programme-configured rules appear in a queue with assignment, contact logging and outcome; nothing is closed without a human.</p></div>
    <div class="card"><h3>Clinician notes and exports</h3><p>Structured notes on the timeline; CSV and PDF exports for handover, audit and evaluation.</p></div>
    <div class="card"><h3>Voice diaries</h3><p>Women can leave voice notes attached to their timeline for the care team to hear; storage and playback only.</p></div>
  </div>
  <div class="notice blue"><strong>About flags and rules</strong>Programme escalation rules (for example, "blood pressure recorded above a threshold set by your clinical lead") are configured, owned and reviewed by the deploying organisation's clinical governance. MaternaLink supplies the rule editor and the queue, not clinical rules, and never generates a diagnosis or treatment recommendation.</div>
</div></section>
<section><div class="container">
  <h2>Roadmap</h2>
  <div class="table-wrap"><table><thead><tr><th>Version</th><th>Scope</th><th>Gate before release or claim</th></tr></thead><tbody>
  <tr><td><span class="tag">v1</span></td><td>Core registry, offline capture, daily check-in, symptom log, partner engagement, education, escalation queue, notes, exports, voice diaries, EN/FR</td><td>Clinician sign-off of intended use and content; DPIA; hazard log; one service evaluation site</td></tr>
  <tr><td><span class="tag">v2</span></td><td>Maternity triage intake module (rules owned by the site), diabetes glucose diary with clinician-set targets, integrations to maternity record systems and DHIS2, SMS/WhatsApp channels, local languages</td><td>Regulatory opinion on triage and glucose modules; interface agreements; safeguarding review</td></tr>
  <tr><td><span class="tag rose">v3 · research</span></td><td>Certified wearable integration ("Maternity Watch"); analysis of voice or movement data; any risk-scoring model</td><td>Ethics approval, clinical partner, validation study and a medical-device pathway before any clinical claim</td></tr>
  </tbody></table></div>
</div></section>
<section class="band"><div class="container two-col" style="align-items:center"><div><h2>See it working</h2><p class="lead">The demo dashboard uses synthetic data and mirrors the operator experience: patients, escalation queue, timeline, notes and analytics.</p></div><div style="text-align:right"><a class="btn btn-rose" href="dashboard.html">Open the demo dashboard</a></div></div></section>
'''

PROGRAMMES = '''
<section class="hero"><div class="container"><span class="eyebrow">Programmes</span><h1>Deployed the way your system already works</h1><p class="lead">MaternaLink is designed for government programmes, hospitals and maternity units, and NGO or donor-supported initiatives. Two deployment modes: as the working programme record where none exists, or integrated with the record system you already run.</p></div></section>
<section id="government"><div class="container two-col">
  <div><h2>Government and state programmes</h2><p>Population-level enrolment across facilities and community health workers, supervisor oversight by facility and local government area, and indicators aligned to your health-information system (DHIS2 alignment on the roadmap).</p><ul class="ticks"><li>Works alongside existing programmes: we design for complementarity, not replacement, where a programme is already running</li><li>Data residency options and local data-protection registration support</li><li>Phased, evidence-generating rollout: pilot, evaluate, expand</li></ul></div>
  <div class="card tint"><h3>Typical phase 1</h3><dl class="kv"><dt>Cohort</dt><dd>2,000–15,000 women</dd><dt>Facilities</dt><dd>10–20</dd><dt>Duration</dt><dd>6–12 months</dd><dt>Evaluation</dt><dd>Reach, engagement, contact completion, defaulter tracing time, cost per woman</dd><dt>Indicative year-1 cost</dt><dd>See <a href="pricing.html">pricing</a> (worked example)</dd></dl></div>
</div></section>
<section id="hospitals"><div class="container two-col">
  <div class="card tint"><h3>Replace or integrate?</h3><p><strong>Replace (working record):</strong> where the maternity service has no digital record, MaternaLink Core holds the programme's working record with a clinical-safety case for record-keeping. It is not a certified electronic patient record.</p><p><strong>Integrate:</strong> where a maternity record exists (for example, BadgerNet, K2 or Euroking in the UK), MaternaLink exchanges data through agreed interfaces and your record remains the legal record.</p></div>
  <div><h2>Hospitals and maternity units</h2><p>Continuity between appointments, a structured intake for maternity assessment or triage areas (rules owned by your clinical governance), shorter and better-prepared appointments through pre-visit check-ins, and one timeline the whole team can see.</p><ul class="ticks"><li>Service-evaluation pilot on one pathway (for example, hypertension monitoring or postnatal follow-up)</li><li>Single sign-on and role-based access; audit logs for every view and change</li><li>Designed for NHS DTAC, DSPT and clinical-safety expectations (assessment pending; not yet assessed)</li></ul></div>
</div></section>
<section id="ngo"><div class="container two-col">
  <div><h2>NGO and donor-supported initiatives</h2><p>Cohort management for community programmes, community health-worker workflows on low-cost devices, SMS and WhatsApp channels for women without smartphones (roadmap), and evaluation-ready exports for funders.</p><ul class="ticks"><li>Offline-first by design for rural and peri-urban settings</li><li>Consent, safeguarding and discreet-mode design for shared phones</li><li>Training and train-the-trainer packages</li></ul></div>
  <div class="card tint"><h3>What we ask of a pilot partner</h3><ul class="ticks"><li>A named clinical lead who owns escalation rules and content sign-off</li><li>A data-sharing and evaluation agreement</li><li>Baseline data and a willingness to publish the results, whatever they show</li></ul><a class="btn btn-primary" href="pilot.html" style="margin-top:.6rem">Request a pilot</a></div>
</div></section>
'''

SECURITY = '''
<section class="hero"><div class="container"><span class="eyebrow">Security &amp; data</span><h1>Privacy by design, safety by governance</h1><p class="lead">How MaternaLink is designed to handle health data, and the assurance work that is planned before any live deployment. Design targets are stated as targets, not as certifications.</p></div></section>
<section><div class="container grid grid-2">
  <div class="card"><h3>Consent-driven collection</h3><p>Data is collected within the programme's consent policy and local law. Women see what is recorded about them and who can see it. Partner access is granted and revoked by the woman.</p></div>
  <div class="card"><h3>Encrypted on device and in transit</h3><p>Records are encrypted at rest on devices and servers and in transit between them. Device loss is mitigated by remote revocation and encrypted local storage.</p></div>
  <div class="card"><h3>Data minimisation and retention</h3><p>Only the fields a programme needs are collected; retention periods are configured per programme and applied automatically at discharge.</p></div>
  <div class="card"><h3>Audit and access control</h3><p>Role-based access (woman, partner, midwife or community health worker, clinician, supervisor, programme administrator, Vytalix support with break-glass logging). Every view and change is logged.</p></div>
  <div class="card"><h3>Data residency</h3><p>UK hosting in a UK region for UK deployments; in-country or regional hosting options for programmes with residency requirements; documented international transfer arrangements where needed.</p></div>
  <div class="card"><h3>No patient data to third-party AI</h3><p>Patient data is not sent to third-party AI services without a data-protection impact assessment, a contract and the programme's approval. There is no automated clinical decision-making.</p></div>
</div></section>
<section><div class="container">
  <h2>Assurance roadmap</h2>
  <div class="table-wrap"><table><thead><tr><th>Item</th><th>Status</th><th>Target</th></tr></thead><tbody>
  <tr><td>Intended-use statement (non-diagnostic care coordination)</td><td><span class="tag">Drafted</span></td><td>Clinician and legal review before pilot</td></tr>
  <tr><td>Data-protection impact assessment (UK GDPR)</td><td><span class="tag">Planned</span></td><td>Before any live data</td></tr>
  <tr><td>Clinical-safety case and hazard log (DCB0129 approach)</td><td><span class="tag">Planned</span></td><td>Before pilot; maintained continuously</td></tr>
  <tr><td>Cyber Essentials, then NHS DSPT</td><td><span class="tag">Planned</span></td><td>Cyber Essentials before pilot; DSPT before NHS deployment</td></tr>
  <tr><td>NHS DTAC evidence pack</td><td><span class="tag">Planned</span></td><td>Before any NHS procurement</td></tr>
  <tr><td>Nigeria data-protection registration and in-country hosting decision</td><td><span class="tag">Planned</span></td><td>Before any Nigerian programme deployment</td></tr>
  <tr><td>Penetration test</td><td><span class="tag">Planned</span></td><td>Before pilot and annually</td></tr>
  <tr><td>Medical-device classification opinion for triage and glucose modules</td><td><span class="tag rose">Required</span></td><td>Before those modules are configured or claimed</td></tr>
  </tbody></table></div>
  <div class="notice"><strong>Plain statement</strong>MaternaLink has not yet been assessed or certified under any of the schemes above. We publish this roadmap so partners can hold us to it.</div>
</div></section>
'''

PRICING = '''
<section class="hero"><div class="container"><span class="eyebrow">Pricing</span><h1>Priced per product and per year of service</h1><p class="lead">A platform licence plus optional modules, plus an annual service plan. Hardware is always a separate line. All figures are indicative and subject to validation with pilot partners; final pricing is agreed per contract.</p></div></section>
<section><div class="container">
  <h2>United Kingdom price book (indicative, per year)</h2>
  <div class="grid grid-3">
    <div class="card"><span class="tag">Core platform</span><p class="price">£18–£36 <small>per enrolled woman</small></p><p>Plus a site licence of £12k–£30k by annual births. Registry, offline capture, timeline, escalation queue, notes, exports, EN/FR.</p></div>
    <div class="card"><span class="tag">Engagement module</span><p class="price">£8–£14 <small>per enrolled woman</small></p><p>Daily check-in, symptom log, partner engagement, education and reminders by app or message.</p></div>
    <div class="card"><span class="tag">Maternity triage module</span><p class="price">£15k–£35k <small>per site</small></p><p>Structured intake and prioritisation rules owned by your clinical governance. Available after regulatory opinion.</p></div>
    <div class="card"><span class="tag">Diabetes glucose diary</span><p class="price">£20–£30 <small>per woman with the condition</small></p><p>Clinician-set targets and trend view. Available after regulatory opinion.</p></div>
    <div class="card"><span class="tag">Maternity Watch</span><p class="price">£4–£7 <small>per device per month</small></p><p>Lease of a certified third-party wearable, or purchase with a service plan. Never bundled into the software price.</p></div>
    <div class="card"><span class="tag">Integration pack</span><p class="price">£15k–£40k <small>setup per interface</small></p><p>Plus £4k–£8k per year. Maternity record systems, single sign-on, DHIS2.</p></div>
  </div>
  <h3 style="margin-top:2rem">Annual service plans</h3>
  <div class="table-wrap"><table><thead><tr><th>Plan</th><th>Price</th><th>Includes</th></tr></thead><tbody>
  <tr><td><strong>Standard</strong></td><td>18–22% of annual licence (minimum £8,000)</td><td>Business-hours support, quarterly releases, security patching, hazard-log maintenance, 99.5% availability design target</td></tr>
  <tr><td><strong>Enhanced</strong></td><td>25–28%</td><td>Standard plus extended hours, named account manager, two configuration changes per quarter, quarterly service review, DSPT evidence pack</td></tr>
  <tr><td><strong>Premium</strong></td><td>30–35%</td><td>Enhanced plus 24/7 severity-1 response, clinical-safety officer on call, annual clinical-safety case refresh, dedicated environment option, 99.9% design target</td></tr>
  </tbody></table></div>
  <h3 style="margin-top:2rem">Worked example: 5,000-birth maternity service, Coordinate + Triage bundle</h3>
  <div class="table-wrap"><table><tbody><tr><td>Core licence £20,000 + 5,000 × £22</td><td>£130,000</td></tr><tr><td>Engagement 5,000 × £10</td><td>£50,000</td></tr><tr><td>Triage module</td><td>£25,000</td></tr><tr><td>Analytics</td><td>£8,000</td></tr><tr><td>Enhanced service (26%)</td><td>£55,400</td></tr><tr><td>Implementation (year 1 only)</td><td>£45,000</td></tr><tr><td><strong>Year 1</strong></td><td><strong>£313,400</strong> · year-2 run-rate £268,400</td></tr></tbody></table></div>
</div></section>
<section class="band"><div class="container">
  <h2>Programme price book (Africa and donor-funded programmes, indicative)</h2>
  <div class="grid grid-4">
    <div class="card"><h3>Core</h3><p>£10 per woman per year up to 5,000 · £7 to 25,000 · £5 to 100,000 · £4 beyond. Site licences waived for public programmes.</p></div>
    <div class="card"><h3>Engagement (SMS/WhatsApp)</h3><p>£3–£5 per woman per year; message costs above 40 per pregnancy passed through at cost.</p></div>
    <div class="card"><h3>Implementation</h3><p>£40k–£120k per state or programme: data-protection registration support, hosting decision, baseline evaluation design, training.</p></div>
    <div class="card"><h3>Annual service</h3><p>20% Standard · 28% Enhanced · 35% Premium of software value; minimum £12,000. In-country support partner above 25,000 women.</p></div>
  </div>
  <p class="lead" style="margin-top:1.5rem">Worked example: a 15,000-woman state programme is approximately <strong>£373,000 in year 1 (about £25 per woman)</strong> and <strong>£275,000 a year thereafter (about £18 per woman)</strong>, including triage at 20 facilities, training and Enhanced service.</p>
</div></section>
<section><div class="container two-col">
  <div><h2>Commercial rules</h2><ul class="ticks"><li>Pilot first: fixed price, evaluation report, 50% of pilot fees credited against year one</li><li>Minimum contract £40,000 (UK) or £25,000 (programme)</li><li>3-year terms: 5% discount; annual uplift capped at CPI + 2%</li><li>Volume discounts only through published tiers</li><li>Hardware always itemised separately</li></ul></div>
  <div class="card tint"><h3>Pilot (12 weeks, one site, up to 300 women)</h3><p class="price">£40k–£90k <small>UK</small></p><p>Includes configuration, training, clinical-safety artefacts and an evaluation report. Programme pilots priced on scope.</p><a class="btn btn-primary" href="pilot.html">Request a pilot</a></div>
</div></section>
'''

PILOT = '''
<section class="hero"><div class="container"><span class="eyebrow">Request a pilot</span><h1>Tell us about your service or programme</h1><p class="lead">We reply within three working days. Pilots are co-designed with a named clinical lead and run for 12 weeks with an evaluation report at the end.</p></div></section>
<section><div class="container two-col">
  <form id="pilot-form" class="card" action="#" method="post" novalidate>
    <p class="help">TODO before launch: point <code>action</code> at Formspree, Netlify Forms or your CRM endpoint (see README). Until then the form shows a confirmation without sending.</p>
    <div class="field-row"><div class="field"><label for="name">Your name</label><input id="name" name="name" autocomplete="name" required></div><div class="field"><label for="role">Role</label><input id="role" name="role" placeholder="e.g., Head of Midwifery, Programme Manager"></div></div>
    <div class="field-row"><div class="field"><label for="org">Organisation</label><input id="org" name="organisation" autocomplete="organization" required></div><div class="field"><label for="country">Country</label><input id="country" name="country" autocomplete="country-name"></div></div>
    <div class="field-row"><div class="field"><label for="email">Work email</label><input id="email" name="email" type="email" autocomplete="email" required></div><div class="field"><label for="type">Organisation type</label><select id="type" name="type"><option>NHS trust or maternity unit</option><option>Private maternity provider</option><option>Government or state programme</option><option>NGO or donor-supported programme</option><option>Insurer or HMO</option><option>Other</option></select></div></div>
    <div class="field"><label for="births">Approximate births per year or cohort size</label><input id="births" name="cohort" inputmode="numeric"></div>
    <div class="field"><label for="msg">What problem would the pilot address?</label><textarea id="msg" name="message" placeholder="For example: postnatal follow-up completion; hypertension monitoring between appointments; continuity for community-based women"></textarea></div>
    <div class="field"><label><input type="checkbox" name="consent" required style="width:auto;margin-right:.5rem">I agree to be contacted about this request. No patient information should be entered in this form.</label></div>
    <button class="btn btn-primary" type="submit">Send request</button>
    <p id="form-ok" class="notice blue" hidden tabindex="-1"><strong>Thank you.</strong>Your request has been recorded locally in this demo. Once the form endpoint is connected, you will receive a confirmation email.</p>
  </form>
  <div>
    <div class="card tint"><h3>What a pilot includes</h3><ul class="ticks"><li>Co-design workshops with your clinical lead and midwives</li><li>Configuration of enrolment, check-ins, content and escalation rules you own</li><li>Training for the team; train-the-trainer for community programmes</li><li>Clinical-safety artefacts and a data-protection impact assessment</li><li>Weekly service reviews and an evaluation report you can publish</li></ul></div>
    <div class="card" style="margin-top:1.2rem"><h3>What a pilot does not include</h3><ul class="ticks crosses"><li>Any diagnostic, predictive or treatment-recommendation feature</li><li>Replacement of your legal patient record</li><li>Claims of clinical outcomes before they are measured</li></ul></div>
  </div>
</div></section>
'''

LOGIN = '''
<div class="login-wrap"><div class="container" style="display:grid;place-items:center">
  <form class="card login-card" action="dashboard.html" method="get">
    <span class="eyebrow">Operator access</span>
    <h2>Sign in to MaternaLink</h2>
    <p class="help">Demo environment. Any values open the demo dashboard with synthetic data. Production sign-in will use single sign-on or email with multi-factor authentication.</p>
    <div class="field"><label for="u">Work email</label><input id="u" name="u" type="email" autocomplete="username" placeholder="name@organisation.org"></div>
    <div class="field"><label for="p">Password</label><input id="p" name="p" type="password" autocomplete="current-password"></div>
    <button class="btn btn-primary" type="submit">Sign in</button>
    <p class="help">No account? <a href="pilot.html">Request access</a> · In an emergency, contact local emergency services; this system is not monitored around the clock.</p>
  </form>
</div></div>
'''

DASHBOARD = '''
<div class="container">
<div class="demo-banner"><strong>Demo dashboard.</strong> Synthetic data only; nothing here is a real patient. Flags are examples of programme-configured rules for human review; MaternaLink does not diagnose, predict or recommend treatment.</div>
<div class="app">
  <nav class="side-nav" aria-label="Dashboard">
    <div class="who"><strong>Demo operator</strong><br>Community Maternity Programme · Site A</div>
    <button data-view="patients" aria-current="page">Patients</button>
    <button data-view="alerts">Escalation queue <span id="alert-count" class="badge badge-high" style="margin-left:auto">0</span></button>
    <button data-view="analytics">Analytics</button>
    <button data-view="admin">Admin</button>
    <hr style="border:0;border-top:1px solid var(--border);margin:.8rem 0">
    <a class="btn btn-secondary btn-sm" href="login.html">Sign out</a>
  </nav>
  <div class="main-panel" id="view"></div>
  <aside>
    <div class="aside-card"><h4>Recently flagged</h4><div id="aside-flags"></div></div>
    <div class="aside-card"><h4>Needs contact today</h4><div id="aside-contact"></div></div>
    <div class="aside-card"><h4>Sync status</h4><p class="help" style="margin:0">Device: <strong>online</strong> · last sync 2 min ago · 0 records pending</p></div>
  </aside>
</div>
</div>
'''

PAGES = {
 "index.html": ("MaternaLink by Vytalix — maternal and newborn care coordination, offline-first","MaternaLink is an offline-first maternal and newborn care-coordination platform in development by Vytalix for health systems, hospitals and programmes. Not a medical device.", INDEX),
 "platform.html": ("Platform — MaternaLink by Vytalix","How MaternaLink works: enrolment, offline capture, daily check-in, symptom log, partner engagement, escalation queue, exports, and the roadmap with regulatory gates.", PLATFORM),
 "programmes.html": ("Programmes — MaternaLink by Vytalix","Deployment for government programmes, hospitals and maternity units, and NGO initiatives; replace or integrate with existing records.", PROGRAMMES),
 "security.html": ("Security and data — MaternaLink by Vytalix","Privacy by design, encryption, access control, data residency and the assurance roadmap for MaternaLink.", SECURITY),
 "pricing.html": ("Pricing — MaternaLink by Vytalix","Indicative pricing per product and per year of service for the UK and for programme deployments, with worked examples.", PRICING),
 "pilot.html": ("Request a pilot — MaternaLink by Vytalix","Request a 12-week co-designed pilot of MaternaLink for your maternity service or programme.", PILOT),
 "login.html": ("Operator access — MaternaLink by Vytalix","Operator sign-in for MaternaLink (demo environment).", LOGIN),
 "dashboard.html": ("Demo dashboard — MaternaLink by Vytalix","Demo operator dashboard with synthetic data: patients, escalation queue, timeline, notes, analytics.", DASHBOARD, "", '<script src="assets/js/dashboard.js"></script>', True),
}
