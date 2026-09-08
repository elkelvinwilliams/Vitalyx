#!/usr/bin/env python3
"""Branded PDF documents: Markdown -> styled HTML (title page, contents, tables, callouts) -> PDF via Chromium.
Run: python3 exports/build_pdfs.py   Outputs: exports/pdf/*.pdf"""
import os,re,glob,html,base64,asyncio,json,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(ROOT,'exports','pdf'); os.makedirs(OUT,exist_ok=True)
LOGO=base64.b64encode(open(os.path.join(ROOT,'website','assets','img','vytalix-logo.png'),'rb').read()).decode()
MARK=base64.b64encode(open(os.path.join(ROOT,'website','assets','img','vytalix-mark.png'),'rb').read()).decode()
CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
DATE='8 September 2026'
FONT_CSS=os.environ.get('VX_FONT_CSS','')

# --- document registry: file -> (title, subtitle, series) ---
def meta(path):
    name=os.path.splitext(os.path.basename(path))[0]
    first=open(path,encoding='utf-8').readline().strip('# ').strip()
    first=re.sub(r'^\d+\s*[—-]\s*','',first)
    series={'docs':'Strategy & Operations','product':'Product','investors':'Investors & Partners','assets':'Business Assets','exports':'Guide'}.get(os.path.basename(os.path.dirname(path)),'Company')
    if name=='FACTS_BASE': series='Foundation'
    return name, first.title() if first.isupper() else first, series

def inline(t):
    t=html.escape(t,quote=False)
    t=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'\1 <span class="url">(\2)</span>',t)
    t=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',t)
    t=re.sub(r'`([^`]+)`',r'<code>\1</code>',t)
    t=re.sub(r'(?<![\w*])\*([^*\n]+)\*(?![\w*])',r'<em>\1</em>',t)
    t=t.replace('✓','<span class="ok">✓</span>').replace('✗','<span class="no">✗</span>')
    return t

def md_to_html(src):
    lines=open(src,encoding='utf-8').read().split('\n')
    out=[]; toc=[]; i=0; tbl=[]; lst=None; hid=0
    def close_list():
        nonlocal lst
        if lst: out.append(f'</{lst}>'); lst=None
    def flush_tbl():
        nonlocal tbl
        rows=[r for r in tbl if not re.match(r'^\|?\s*:?-{2,}',r)]
        if rows:
            cells=[[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]
            n=max(len(c) for c in cells)
            h='<div class="tbl"><table><thead><tr>'+''.join(f'<th>{inline(c)}</th>' for c in cells[0]+['']*(n-len(cells[0])))+'</tr></thead><tbody>'
            for r in cells[1:]: h+='<tr>'+''.join(f'<td>{inline(c)}</td>' for c in r+['']*(n-len(r)))+'</tr>'
            out.append(h+'</tbody></table></div>')
        tbl=[]
    while i<len(lines):
        l=lines[i].rstrip()
        if l.startswith('|'): close_list(); tbl.append(l); i+=1; continue
        if tbl: flush_tbl()
        if l.startswith('```'):
            close_list(); i+=1; buf=[]
            while i<len(lines) and not lines[i].startswith('```'): buf.append(lines[i]); i+=1
            out.append('<pre>'+html.escape('\n'.join(buf))+'</pre>'); i+=1; continue
        m=re.match(r'^(#{1,6})\s+(.*)',l)
        if m:
            close_list(); lvl=len(m.group(1)); txt=re.sub(r'[*`]','',m.group(2)).strip()
            if lvl==1 and i<3: i+=1; continue  # document title handled by cover
            hid+=1; anchor=f'h{hid}'
            if lvl<=2: toc.append((lvl,txt,anchor))
            out.append(f'<h{min(lvl,4)} id="{anchor}">{inline(txt)}</h{min(lvl,4)}>'); i+=1; continue
        bm=re.match(r'^\s*[-*]\s+(.*)',l); nm=re.match(r'^\s*\d+\.\s+(.*)',l)
        if bm or nm:
            kind='ul' if bm else 'ol'
            if lst!=kind: close_list(); out.append(f'<{kind}>'); lst=kind
            out.append(f'<li>{inline((bm or nm).group(1))}</li>'); i+=1; continue
        if l.startswith('>'):
            close_list(); q=[]
            while i<len(lines) and lines[i].startswith('>'): q.append(lines[i].lstrip('> ')); i+=1
            out.append('<div class="callout">'+inline(' '.join(q))+'</div>'); continue
        if l.strip() in ('---','***'): close_list(); out.append('<hr>'); i+=1; continue
        if l.strip():
            close_list(); out.append(f'<p>{inline(l)}</p>')
        else: close_list()
        i+=1
    close_list()
    if tbl: flush_tbl()
    return '\n'.join(out), toc

CSS='''
@page{size:A4;margin:22mm 18mm 22mm 18mm}
:root{--blue:#153892;--blue-dark:#0E2A70;--ink:#10192B;--slate:#4B5568;--line:#D9DEE9;--tint:#E9EDF8;--rose:#C93D63}
*{box-sizing:border-box}
body{font-family:"Source Sans 3","Source Sans Pro","Liberation Sans","DejaVu Sans",Arial,sans-serif;font-size:10.5pt;line-height:1.5;color:var(--ink);margin:0}
h1,h2,h3,h4,.display{font-family:"Source Serif 4","Source Serif Pro","Bitstream Charter","Liberation Serif",Georgia,serif;color:var(--blue);font-weight:600;line-height:1.2}
h1{font-size:22pt;margin:18pt 0 8pt;page-break-before:always;border-bottom:2px solid var(--blue);padding-bottom:4pt}
h1.first{page-break-before:auto}
h2{font-size:15pt;margin:16pt 0 6pt}h3{font-size:12pt;margin:12pt 0 4pt;color:var(--blue-dark)}h4{font-size:10.5pt;margin:10pt 0 3pt;font-family:inherit;font-weight:700;color:var(--ink)}
p{margin:0 0 7pt;text-align:left}ul,ol{margin:0 0 8pt;padding-left:18pt}li{margin:0 0 3pt}
strong{color:var(--ink)}code{font-family:"Liberation Mono","DejaVu Sans Mono",monospace;font-size:9pt;background:var(--tint);padding:0 3pt;border-radius:3px}
pre{font-family:"Liberation Mono","DejaVu Sans Mono",monospace;font-size:8.5pt;background:#F3F5FA;border:1px solid var(--line);border-radius:6px;padding:8pt;white-space:pre-wrap;page-break-inside:avoid}
.tbl{margin:6pt 0 10pt;page-break-inside:auto}table{width:100%;border-collapse:collapse;font-size:8.6pt;line-height:1.35}
th{background:var(--blue);color:#fff;text-align:left;padding:5pt 6pt;font-weight:600;font-size:8pt;letter-spacing:.03em}
td{padding:4.5pt 6pt;border-bottom:1px solid var(--line);vertical-align:top}tr:nth-child(even) td{background:#F7F8FC}tr{page-break-inside:avoid}
.callout{border-left:4px solid var(--rose);background:#FBF0F3;padding:8pt 10pt;margin:8pt 0 10pt;border-radius:0 6px 6px 0;font-size:9.8pt;color:var(--slate)}
hr{border:0;border-top:1px solid var(--line);margin:12pt 0}
.url{color:var(--slate);font-size:8.5pt}.ok{color:#1B7F4B;font-weight:700}.no{color:#B3261E;font-weight:700}
/* cover */
.cover{height:253mm;display:flex;flex-direction:column;justify-content:space-between;page-break-after:always;position:relative}
.cover .logo{width:62mm}.cover .series{font-size:9pt;letter-spacing:.18em;text-transform:uppercase;color:var(--rose);font-weight:700;margin-top:30mm}
.cover h1.title{font-size:30pt;border:0;margin:6mm 0 4mm;padding:0;page-break-before:auto;line-height:1.15;color:var(--blue)}
.cover .sub{font-size:13pt;color:var(--slate);max-width:140mm;font-family:"Source Serif 4","Bitstream Charter",Georgia,serif}
.cover .band{background:var(--blue);color:#fff;padding:10mm 12mm;border-radius:6px;font-size:9.5pt;display:grid;grid-template-columns:1fr 1fr 1fr;gap:6mm}
.cover .band b{display:block;font-size:8pt;letter-spacing:.14em;text-transform:uppercase;color:#C7D0E8;margin-bottom:2pt}
.cover .rule{height:3px;background:linear-gradient(90deg,var(--blue),var(--rose));margin:8mm 0 0}
.cover .status{font-size:8.5pt;color:var(--slate);margin-top:6mm;max-width:150mm}
/* contents */
.toc{page-break-after:always}.toc h1{page-break-before:auto;border:0;font-size:18pt}.toc ol{list-style:none;padding:0;margin:0}.toc li{display:flex;justify-content:space-between;border-bottom:1px dotted var(--line);padding:4pt 0;font-size:10pt}
.toc li.l2{padding-left:14pt;font-size:9.4pt;color:var(--slate)}.toc a{color:inherit;text-decoration:none}
'''
def build_html(src):
    name,title,series=meta(src); body,toc=md_to_html(src)
    body=re.sub(r'<h1 id="h(\d+)">','<h1 class="first" id="h\\1">',body,count=1)
    toc_html=''.join(f'<li class="l{lvl}"><a href="#{a}">{html.escape(t)}</a><span>{i+1}</span></li>' for i,(lvl,t,a) in enumerate(toc[:60]))
    tocblock=f'<section class="toc"><h1>Contents</h1><ol>{toc_html}</ol></section>' if len(toc)>3 else ''
    return f'''<!DOCTYPE html><html lang="en-GB"><head><meta charset="utf-8"><title>{html.escape(title)}</title>{FONT_CSS}<style>{CSS}</style></head><body>
<section class="cover">
  <div><img class="logo" src="data:image/png;base64,{LOGO}" alt="Vytalix — Technology for Life"><div class="series">{series}</div><h1 class="title">{html.escape(title)}</h1><div class="sub">Vytalix company-build documentation · reference {name}</div><div class="rule"></div>
  <div class="status">Status labels apply throughout: KNOWN, VERIFIED, ASSUMPTION, ESTIMATE, TO VALIDATE, PROPOSED. Nothing in this document claims traction, approvals, partners or revenue that do not exist. Governing file: FACTS_BASE.</div></div>
  <div class="band"><div><b>Prepared for</b>The Founder, Vytalix</div><div><b>Date</b>{DATE}</div><div><b>Version</b>1.0 · Confidential draft</div></div>
</section>
{tocblock}
{body}
</body></html>'''

async def render(items):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path=CHROME,args=['--no-sandbox'])
        pg=await b.new_page()
        for src,dst,title in items:
            await pg.set_content(build_html(src),wait_until='load')
            await pg.pdf(path=dst,format='A4',print_background=True,display_header_footer=True,
                header_template=f'<div style="font-family:Liberation Sans,Arial,sans-serif;font-size:7.5pt;color:#4B5568;width:100%;padding:0 18mm;display:flex;justify-content:space-between"><span>Vytalix · Technology for Life</span><span>{html.escape(title)}</span></div>',
                footer_template='<div style="font-family:Liberation Sans,Arial,sans-serif;font-size:7.5pt;color:#4B5568;width:100%;padding:0 18mm;display:flex;justify-content:space-between"><span>Confidential draft · every figure is an estimate unless labelled verified</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>',
                margin={'top':'22mm','bottom':'22mm','left':'18mm','right':'18mm'})
            print('pdf',os.path.basename(dst))
        await b.close()

if __name__=='__main__':
    srcs=[os.path.join(ROOT,'FACTS_BASE.md'),os.path.join(ROOT,'exports','START_HERE.md')]+sorted(glob.glob(os.path.join(ROOT,'docs','*.md')))+sorted(glob.glob(os.path.join(ROOT,'product','*.md')))+sorted(glob.glob(os.path.join(ROOT,'investors','*.md')))+sorted(glob.glob(os.path.join(ROOT,'assets','*.md')))
    items=[]
    for s in srcs:
        name,title,series=meta(s); items.append((s,os.path.join(OUT,name+'.pdf'),title))
    asyncio.run(render(items)); print('done',len(items))
