#!/usr/bin/env python3
"""Branded slide decks as PDF (16:9) from the Markdown deck outlines, rendered with Chromium.
Run: python3 exports/build_deck_pdfs.py   Outputs: exports/pdf/decks/*.pdf"""
import os,re,html,base64,asyncio
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(ROOT,'exports','pdf','decks'); os.makedirs(OUT,exist_ok=True)
LOGO=base64.b64encode(open(os.path.join(ROOT,'website','assets','img','vytalix-logo.png'),'rb').read()).decode()
MARK=base64.b64encode(open(os.path.join(ROOT,'website','assets','img','vytalix-mark.png'),'rb').read()).decode()
CHROME='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
DECKS=[('INVESTOR_PITCH_DECK','Investor pitch','Pre-seed · September 2026 · Draft for discussion'),('CORPORATE_PRESENTATION','Vytalix corporate presentation','Technology for Life · September 2026'),('SALES_DECK','Advisory & Consulting','Services for healthcare organisations, founders and public bodies'),('PARTNERSHIP_DECK','MaternaLink partnership proposal','Co-designing the first evaluation · in development')]
CSS='''
@page{size:13.333in 7.5in;margin:0}
:root{--blue:#153892;--deep:#0F2354;--ink:#10192B;--slate:#4B5568;--line:#D9DEE9;--tint:#E9EDF8;--rose:#C93D63}
body{margin:0;font-family:"Source Sans Pro","Liberation Sans",Arial,sans-serif;color:var(--ink)}
.slide{width:13.333in;height:7.5in;page-break-after:always;position:relative;overflow:hidden;padding:.75in .9in .6in;box-sizing:border-box;background:#fff}
.slide:last-child{page-break-after:auto}
.bar{position:absolute;top:0;left:0;right:0;height:.14in;background:linear-gradient(90deg,var(--blue) 70%,var(--rose))}
.logo{position:absolute;top:.42in;right:.9in;width:1.7in}
.mark{position:absolute;bottom:.45in;right:.9in;width:.55in;opacity:.9}
.foot{position:absolute;bottom:.4in;left:.9in;font-size:9.5pt;color:var(--slate)}
.num{position:absolute;bottom:.4in;right:1.7in;font-size:9.5pt;color:var(--slate)}
h1{font-family:"Source Serif Pro","Bitstream Charter",Georgia,serif;font-weight:600;color:var(--blue);font-size:30pt;line-height:1.15;margin:.2in 0 .15in;max-width:9.6in}
h2.kicker{font-size:10.5pt;letter-spacing:.16em;text-transform:uppercase;color:var(--rose);margin:0;font-weight:700}
.head{font-family:"Source Serif Pro",Georgia,serif;font-size:19pt;color:var(--ink);margin:0 0 .25in;max-width:10.5in;line-height:1.3}
ul{margin:0;padding-left:.28in;font-size:15pt;line-height:1.45;max-width:10.6in;columns:1}ul.two{columns:2;column-gap:.5in}li{margin:0 0 .09in;break-inside:avoid}
.visual{position:absolute;left:.9in;bottom:1in;font-size:10.5pt;color:var(--slate);background:var(--tint);padding:.12in .18in;border-radius:6px;max-width:11in}
.title{background:var(--deep);color:#fff;display:flex;flex-direction:column;justify-content:center}
.title h1{color:#fff;font-size:44pt;max-width:10in}.title .sub{font-size:16pt;color:#C7D0E8;margin-top:.1in}.title .logo{filter:brightness(0) invert(1)}
.title .strap{position:absolute;bottom:.6in;left:.9in;font-size:11pt;letter-spacing:.16em;text-transform:uppercase;color:#9DB8FF}
'''
def parse(src):
    txt=open(src,encoding='utf-8').read()
    parts=re.split(r'\n(?=##+\s+(?:Slide\s*)?\d+)',txt)
    slides=[]
    for p in parts:
        if not re.match(r'##+\s+(?:Slide\s*)?\d+',p.strip()): continue
        lines=[x.rstrip() for x in p.strip().split('\n')]
        head=re.sub(r'^#+\s+(?:Slide\s*)?\d+\s*[—:\-–.]*\s*','',lines[0]).strip().strip('*')
        headline='';body=[];visual='';mode='body'
        for ln in lines[1:]:
            if not ln.strip(): continue
            low=ln.lower()
            if low.startswith(('**notes','**speaker','speaker notes','notes:')): mode='notes'; continue
            if low.startswith(('**visual','visual:')): mode='visual'; ln=re.sub(r'^\**visual\**\s*[:：]?\s*','',ln,flags=re.I); visual+=ln.replace('**','')+' '; continue
            if mode=='notes': continue
            if mode=='visual': visual+=ln.replace('**','')+' '; continue
            if low.startswith(('**headline','headline:')): headline=re.sub(r'^\**headline\**\s*[:：]?\s*','',ln,flags=re.I).strip('*'); continue
            if low.startswith(('**body','body:')): ln=re.sub(r'^\**body\**\s*[:：]?\s*','',ln,flags=re.I)
            for piece in re.split(r'\s+·\s+',ln):
                piece=re.sub(r'^[-*]\s+','',piece).replace('**','').strip()
                if piece: body.append(piece)
        slides.append((head,headline,body,visual.strip()))
    return slides
def build(name,title,sub):
    slides=parse(os.path.join(ROOT,'assets',name+'.md'))
    h=f'<section class="slide title"><div class="bar"></div><img class="logo" src="data:image/png;base64,{LOGO}"><h2 class="kicker">Vytalix</h2><h1>{html.escape(title)}</h1><div class="sub">{html.escape(sub)}</div><div class="strap">Technology for Life · Confidential draft · in development; no claims beyond those stated</div></section>'
    for i,(head,headline,body,visual) in enumerate(slides,1):
        if head.lower().startswith('title'): continue
        lis=''.join(f'<li>{html.escape(b)}</li>' for b in body[:10])
        cls='two' if len(body)>6 else ''
        h+=f'<section class="slide"><div class="bar"></div><img class="logo" src="data:image/png;base64,{LOGO}"><h2 class="kicker">{html.escape(head)}</h2><h1>{html.escape(headline or head)}</h1><ul class="{cls}">{lis}</ul>{f"<div class=visual>Visual: {html.escape(visual[:260])}</div>" if visual else ""}<div class="foot">Vytalix · {html.escape(title)} · Confidential draft</div><div class="num">{i}</div><img class="mark" src="data:image/png;base64,{MARK}"></section>'
    return f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{h}</body></html>'
async def main():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path=CHROME,args=['--no-sandbox']); pg=await b.new_page()
        for name,title,sub in DECKS:
            await pg.set_content(build(name,title,sub),wait_until='load')
            await pg.pdf(path=os.path.join(OUT,name+'.pdf'),width='13.333in',height='7.5in',print_background=True,margin={'top':'0','bottom':'0','left':'0','right':'0'})
            print('deck pdf',name)
        await b.close()
asyncio.run(main())
