"""Shared page shell for the MaternaLink site. Run: python3 maternalink-site/_shell.py (regenerates pages from _pages/*.html bodies)."""
import os,glob,re
ROOT=os.path.dirname(os.path.abspath(__file__))
NAV=[("platform.html","nav_platform","Platform"),("programmes.html","nav_programmes","Programmes"),("security.html","nav_security","Security &amp; data"),("pricing.html","nav_pricing","Pricing")]
def shell(fname,title,desc,body,extra_head="",extra_js="",app=False):
    CUR=' aria-current="page"'
    nav="".join(f'<li><a href="{h}" data-i18n="{k}"{CUR if h==fname else ""}>{t}</a></li>' for h,k,t in NAV)
    return f'''<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#153892">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website"><meta property="og:site_name" content="MaternaLink by Vytalix"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="https://maternalink.example/{fname}"><meta property="og:image" content="https://maternalink.example/assets/img/og-image.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,400;9..144,500;9..144,600&family=Manrope:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="assets/css/maternalink.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"SoftwareApplication","name":"MaternaLink","applicationCategory":"HealthApplication","operatingSystem":"Web","description":"{desc}","creator":{{"@type":"Organization","name":"Vytalix","slogan":"Technology for Life"}},"offers":{{"@type":"Offer","description":"Pilot programmes by invitation; pricing on request"}}}}</script>
{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="index.html" aria-label="MaternaLink by Vytalix — home">
      <img src="assets/img/vytalix-mark.png" alt="" width="66" height="80">
      <span><span class="name">Materna<em>Link</em></span><span class="by">by Vytalix · Technology for Life</span></span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav id="site-nav" class="nav" aria-label="Primary">
      <ul>{nav}
        <li><a class="btn btn-secondary btn-sm" href="login.html" data-i18n="nav_login">Operator access</a></li>
        <li><a class="btn btn-primary btn-sm" href="pilot.html" data-i18n="nav_pilot">Request a pilot</a></li>
      </ul>
      <div class="lang" role="group" aria-label="Language"><button type="button" data-lang="en" aria-pressed="true">EN</button><button type="button" data-lang="fr" aria-pressed="false">FR</button></div>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div><h4>MaternaLink by Vytalix</h4><p>A maternal and newborn care-coordination platform, in development. Designed with clinicians, subject to validation. Not a medical device.</p><p class="tag">Technology for Life</p></div>
      <div><h4>Product</h4><ul><li><a href="platform.html">Platform</a></li><li><a href="programmes.html">Programmes</a></li><li><a href="security.html">Security &amp; data</a></li><li><a href="pricing.html">Pricing</a></li></ul></div>
      <div><h4>Work with us</h4><ul><li><a href="pilot.html">Request a pilot</a></li><li><a href="login.html">Operator access</a></li><li><a href="dashboard.html">Demo dashboard</a></li><li><a href="../website/index.html">Vytalix group</a></li></ul></div>
      <div><h4>Legal</h4><ul><li><a href="../website/privacy.html">Privacy</a></li><li><a href="../website/terms.html">Terms</a></li><li><a href="../website/cookie-policy.html">Cookies</a></li></ul></div>
    </div>
    <div class="footer-note">© 2026 Vytalix. [Legal entity name and company number — add after incorporation]. MaternaLink is in development and is not approved, assessed or validated by any regulator or health system. In an emergency, contact local emergency services.</div>
  </div>
</footer>
<div id="cookie-banner" class="cookie" role="region" aria-label="Cookie preference"><p>We use only essential storage for language and this preference. No tracking cookies are set.</p><button class="btn btn-primary btn-sm" data-cookie="essential">OK</button></div>
<script src="assets/js/i18n.js"></script><script src="assets/js/main.js"></script>{extra_js}
</body>
</html>'''
if __name__=="__main__":
    import importlib.util,sys
    spec=importlib.util.spec_from_file_location("pages",os.path.join(ROOT,"_pages.py")); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for fname,args in m.PAGES.items():
        open(os.path.join(ROOT,fname),"w",encoding="utf-8").write(shell(fname,*args))
        print("wrote",fname)
