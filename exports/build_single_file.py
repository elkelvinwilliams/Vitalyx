#!/usr/bin/env python3
"""Bundle a multi-page static site into one HTML file with hash routing (for hosted artifact publishing).
Usage: python3 exports/build_single_file.py <site_dir> <out_file> <title> [cross_link_base]"""
import sys,os,re,glob,base64,mimetypes
site,out,title=sys.argv[1],sys.argv[2],sys.argv[3]
cross=sys.argv[4] if len(sys.argv)>4 else ''
def read(p): return open(p,encoding='utf-8').read()
def data_uri(path):
    mt=mimetypes.guess_type(path)[0] or 'application/octet-stream'
    if path.endswith('.svg'): mt='image/svg+xml'
    return f"data:{mt};base64,"+base64.b64encode(open(path,'rb').read()).decode()
pages=sorted(glob.glob(os.path.join(site,'*.html')))
names=[os.path.splitext(os.path.basename(p))[0] for p in pages]
idx=read(os.path.join(site,'index.html'))
def between(s,start_re,end_tag):
    m=re.search(start_re,s); 
    if not m: return ''
    e=s.find(end_tag,m.start()); return s[m.start():e+len(end_tag)]
header=between(idx,r'<header[^>]*class="site-header"',' </header>') or between(idx,r'<header',' </header>')
footer=between(idx,r'<footer',' </footer>')
cookie=between(idx,r'<div id="cookie-banner"','</div>')
skip=between(idx,r'<a class="skip"','</a>')
def links(html):
    def rep(m):
        q,href=m.group(1),m.group(2)
        if href.startswith('../website/'):
            tgt=os.path.splitext(href.split('/')[-1])[0]
            return f'href={q}{cross}#{tgt}{q}' if cross else f'href={q}#index{q}'
        mm=re.match(r'^([a-z0-9-]+)\.html(#[^"\']*)?$',href)
        if mm: return f'href={q}#{mm.group(1)}{q}'
        return m.group(0)
    return re.sub(r'href=(["\'])([^"\']+)\1',rep,html)
def assets(html):
    def rep(m):
        q,src=m.group(1),m.group(2)
        p=os.path.join(site,src)
        return f'src={q}{data_uri(p)}{q}' if os.path.exists(p) else m.group(0)
    return re.sub(r'src=(["\'])(assets/img/[^"\']+)\1',rep,html)
sections=[]; titles={}
for p,n in zip(pages,names):
    h=read(p)
    t=re.search(r'<title>(.*?)</title>',h,re.S); titles[n]=(t.group(1).strip() if t else n)
    m=re.search(r'<main[^>]*>(.*)</main>',h,re.S); body=m.group(1) if m else ''
    sections.append(f'<section class="page" data-page="{n}"{"" if n=="index" else " hidden"}>{body}</section>')
css=''
for c in glob.glob(os.path.join(site,'assets/css/*.css')): css+=read(c)+'\n'
css=re.sub(r'url\((["\']?)(assets/img/[^)"\']+)\1\)',lambda m: f'url("{data_uri(os.path.join(site,m.group(2)))}")',css)
js=''
for j in ['assets/js/i18n.js','assets/js/main.js','assets/js/dashboard.js']:
    p=os.path.join(site,j)
    if os.path.exists(p): js+=read(p)+'\n'
router='''
(function(){
  var pages=document.querySelectorAll('section.page');var titles=%s;
  function show(){var n=(location.hash||'#index').slice(1).split('?')[0];if(!document.querySelector('section.page[data-page="'+n+'"]'))n='index';
    pages.forEach(function(s){s.hidden=s.getAttribute('data-page')!==n;});
    document.querySelectorAll('a[href^="#"]').forEach(function(a){var h=a.getAttribute('href').slice(1);if(titles[h]!==undefined){if(h===n)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');}});
    document.title=titles[n]||document.title;var nav=document.getElementById('site-nav')||document.getElementById('primary-nav');if(nav)nav.classList.remove('open');window.scrollTo(0,0);}
  window.addEventListener('hashchange',show);show();
})();
'''%(__import__('json').dumps(titles))
doc=f'''<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,400;9..144,500;9..144,600&family=Manrope:wght@400;500;600;700;800&display=swap">
<style>
{css}
section.page[hidden]{{display:none}}
</style>
{assets(links(skip))}
{assets(links(header))}
<main id="main">
{assets(links(''.join(sections)))}
</main>
{assets(links(footer))}
{assets(links(cookie))}
<script>
{js}
{router}
</script>
'''
open(out,'w',encoding='utf-8').write(doc)
print(out,len(doc)//1024,'KB','pages',names)
