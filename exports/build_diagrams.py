#!/usr/bin/env python3
"""Vytalix diagram library. Generates brand-consistent SVGs used in the documents and PDFs.
Run: python3 exports/build_diagrams.py   Output: diagrams/*.svg"""
import os
R=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'diagrams')
os.makedirs(R,exist_ok=True)
BLUE='#153892'; DEEP='#0F2354'; ROSE='#C93D63'; INK='#10192B'; SLATE='#5A6472'; LINE='#D9DEE9'
TINT='#E9EDF8'; PAPER='#FFFFFF'; GREEN='#1B7F4B'; AMBER='#B76A00'; RED='#B3261E'; MIST='#F5F7FC'
F='Source Sans Pro, Segoe UI, Helvetica, Arial, sans-serif'
FS='Source Serif Pro, Georgia, serif'
def svg(w,h,body,title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{title}">'
            f'<rect width="{w}" height="{h}" fill="{PAPER}"/>{body}</svg>')
def T(x,y,t,size=13,fill=INK,anchor='start',weight='400',font=F,op=1):
    t=str(t).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" opacity="{op}">{t}</text>'
def head(w,t,sub=''):
    s=T(0,20,t,17,BLUE,weight='600',font=FS)
    if sub: s+=T(0,40,sub,12,SLATE)
    return f'<g transform="translate(24,24)">{s}</g>'
def money(v):
    return f'£{v/1_000_000:.2f}m' if abs(v)>=1_000_000 else (f'£{round(v/1000)}k' if abs(v)>=1000 else f'£{v:.0f}')
def write(name,content): open(os.path.join(R,name),'w',encoding='utf-8').write(content); print('diagram',name)

# 1 — business score gauge
def business_score():
    w,h=760,220; b=head(w,'Where the business stands today','A score out of 100. Anything under 20 means the company has not started trading.')
    x0,y=60,120; bw=640
    b+=f'<rect x="{x0}" y="{y}" width="{bw}" height="26" rx="13" fill="{MIST}" stroke="{LINE}"/>'
    bands=[(0,20,'#F3D9D6','Not started'),(20,40,'#FCE9CF','Trading'),(40,60,'#DCEBDD','Fundable'),(60,100,'#CFE3D8','Scaling')]
    for a,bn,c,lbl in bands:
        b+=f'<rect x="{x0+bw*a/100}" y="{y}" width="{bw*(bn-a)/100}" height="26" rx="0" fill="{c}"/>'
        b+=T(x0+bw*(a+bn)/200,y+45,lbl,10.5,SLATE,'middle')
    b+=f'<rect x="{x0}" y="{y}" width="{bw}" height="26" rx="13" fill="none" stroke="{LINE}"/>'
    px=x0+bw*11/100
    b+=f'<circle cx="{px}" cy="{y+13}" r="12" fill="{ROSE}" stroke="#fff" stroke-width="3"/>'
    b+=T(px,y-16,'You are here: 11',14,ROSE,'middle',weight='700')
    tx=x0+bw*38/100
    b+=f'<line x1="{tx}" y1="{y-4}" x2="{tx}" y2="{y+30}" stroke="{BLUE}" stroke-width="2" stroke-dasharray="4 3"/>'
    b+=T(tx,y-16,'Target by December: 38',12,BLUE,'middle',weight='600')
    for v in (0,20,40,60,80,100): b+=T(x0+bw*v/100,y+70,v,10,SLATE,'middle')
    write('business-score.svg',svg(w,h,b,'Business score 11 out of 100'))

# 2 — four pillars
def pillars():
    w,h=760,300; b=head(w,'The four parts of Vytalix','Services pay the bills today. The product is the long-term value.')
    items=[('Advisory','Senior advice for health organisations and founders','Earns money now',GREEN),
           ('Consulting','Fixed-price projects: NHS readiness, Africa entry','Earns money now',GREEN),
           ('Health Solutions','MaternaLink, the maternity product','In development',AMBER),
           ('E-Learning','Training for midwives and health workers','Year two',SLATE)]
    x=24; cw=172; gap=10
    for i,(t,d,s,c) in enumerate(items):
        cx=x+i*(cw+gap)
        b+=f'<rect x="{cx}" y="80" width="{cw}" height="150" rx="10" fill="{MIST}" stroke="{LINE}"/>'
        b+=f'<rect x="{cx}" y="80" width="{cw}" height="5" rx="2" fill="{BLUE}"/>'
        b+=T(cx+14,112,t,14,BLUE,weight='700')
        words=d.split(); ln=[]; cur=''
        for wd in words:
            if len(cur+' '+wd)>26: ln.append(cur); cur=wd
            else: cur=(cur+' '+wd).strip()
        ln.append(cur)
        for j,l in enumerate(ln): b+=T(cx+14,134+j*16,l,11.5,SLATE)
        b+=f'<rect x="{cx+14}" y="196" width="{len(s)*6.4+16}" height="20" rx="10" fill="{c}" opacity="0.12"/>'
        b+=T(cx+22,210,s,10.5,c,weight='700')
    b+=f'<path d="M 210 250 L 380 250" stroke="{ROSE}" stroke-width="2" marker-end="url(#a)"/>'
    b+=f'<defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 z" fill="{ROSE}"/></marker></defs>'
    b+=T(295,242,'money from services funds the build',10.5,ROSE,'middle',weight='600')
    write('four-pillars.svg',svg(w,h,b,'Four parts of Vytalix'))

# 3 — revenue by year, three scenarios
def revenue():
    w,h=760,340; b=head(w,'Money coming in, three versions of the future','These are scenarios, not forecasts. Nothing has been sold yet.')
    data={'Careful':[71519,145840,195156],'Middle':[166012,488042,820235],'Ambitious':[477947,1695612,3076156]}
    cols={'Careful':'#9FB0D6','Middle':BLUE,'Ambitious':ROSE}
    x0,y0,ch,cw=80,270,180,600; mx=3_200_000
    for gy in range(0,4):
        v=mx*gy/3; yy=y0-ch*gy/3
        b+=f'<line x1="{x0}" y1="{yy}" x2="{x0+cw}" y2="{yy}" stroke="{LINE}"/>'
        b+=T(x0-10,yy+4,money(v),10.5,SLATE,'end')
    gw=cw/3
    for gi,yr in enumerate(['Year 1 (2027)','Year 2 (2028)','Year 3 (2029)']):
        gx=x0+gi*gw
        for si,(name,vals) in enumerate(data.items()):
            bw=42; bx=gx+gw/2-((3*bw+16)/2)+si*(bw+8); v=vals[gi]; bh=ch*v/mx
            b+=f'<rect x="{bx}" y="{y0-bh}" width="{bw}" height="{bh}" rx="3" fill="{cols[name]}"/>'
            b+=T(bx+bw/2,y0-bh-6,money(v),9.5,SLATE,'middle',weight='600')
        b+=T(gx+gw/2,y0+20,yr,11.5,INK,'middle',weight='600')
    b+=f'<line x1="{x0}" y1="{y0}" x2="{x0+cw}" y2="{y0}" stroke="{INK}"/>'
    lx=x0
    for name,c in cols.items():
        b+=f'<rect x="{lx}" y="{y0+38}" width="12" height="12" rx="2" fill="{c}"/>'+T(lx+18,y0+48,name,11,SLATE)
        lx+=len(name)*7+40
    write('revenue-3yr.svg',svg(w,h,b,'Revenue by year across three scenarios'))

# 4 — revenue mix (middle case)
def mix():
    w,h=760,300; b=head(w,'Where the money comes from (middle case)','Services are most of the money for the first two years.')
    rows=[('Advisory',423748,BLUE),('Consulting',443333,'#3E5FB0'),('E-learning',220208,'#7E93CE'),('MaternaLink',387000,ROSE)]
    tot=sum(r[1] for r in rows); x0,y=90,100; bw=580
    cx=x0
    for name,v,c in rows:
        seg=bw*v/tot
        b+=f'<rect x="{cx}" y="{y}" width="{seg}" height="46" fill="{c}"/>'
        if seg>70: b+=T(cx+seg/2,y+28,f'{round(v/tot*100)}%',13,'#fff','middle',weight='700')
        cx+=seg
    b+=f'<rect x="{x0}" y="{y}" width="{bw}" height="46" fill="none" stroke="{LINE}"/>'
    ly=y+90
    for i,(name,v,c) in enumerate(rows):
        yy=ly+i*30
        b+=f'<rect x="{x0}" y="{yy-11}" width="14" height="14" rx="3" fill="{c}"/>'
        b+=T(x0+22,yy,name,12.5,INK,weight='600')+T(x0+200,yy,money(v)+' over three years',12,SLATE)
    b+=T(x0,y-16,f'Total three-year revenue {money(tot)}',12,SLATE)
    write('revenue-mix.svg',svg(w,h,b,'Revenue mix, middle case'))

# 5 — cash needed
def cash():
    w,h=760,290; b=head(w,'How much cash you need before money comes in','The deepest point of the hole, before any investment.')
    rows=[('Careful',228872,'£250k raise covers it'),('Middle',1058035,'needs a seed round in year 2'),('Ambitious',144705,'pays for itself from month 31')]
    x0,y0=180,110; bw=520; mx=1_100_000
    for i,(n,v,note) in enumerate(rows):
        yy=y0+i*56; bl=bw*v/mx
        b+=T(x0-14,yy+20,n,13,INK,'end',weight='600')
        b+=f'<rect x="{x0}" y="{yy}" width="{bw}" height="30" rx="4" fill="{MIST}"/>'
        b+=f'<rect x="{x0}" y="{yy}" width="{bl}" height="30" rx="4" fill="{BLUE if i==1 else "#9FB0D6"}"/>'
        b+=T(x0+bl+10,yy+20,money(v),12.5,INK,weight='700')
        b+=T(x0+bl+80,yy+20,note,11.5,SLATE)
    b+=T(x0,y0+180,'Read it this way: in the middle case the company deliberately spends on building MaternaLink,',11.5,SLATE)
    b+=T(x0,y0+197,'so it needs about £1m of investment across three years. The careful case needs £250k.',11.5,SLATE)
    write('cash-needed.svg',svg(w,h,b,'Cash needed by scenario'))

# 6 — 90 day plan
def plan90():
    w,h=760,320; b=head(w,'The first 90 days','Four blocks. Do them in order. Dates run from Monday 14 September 2026.')
    rows=[('Days 1–7','Fix the blockers','Company registered, ownership agreed',ROSE),
          ('Days 8–30','Set up to sell','Offers live, 40 conversations, website up',BLUE),
          ('Days 31–60','Find proof','15 midwife interviews, first paying client',BLUE),
          ('Days 61–90','Investors and pilot','Hospital trial agreed, data room built',GREEN)]
    x0,y0=150,90; bw=560
    for i,(t,title,detail,c) in enumerate(rows):
        yy=y0+i*54
        seg=bw*[0.08,0.25,0.33,0.34][i]; off=sum([0,0.08,0.33,0.66][:i+1][-1:]) if False else bw*[0,0.08,0.33,0.66][i]
        b+=T(x0-14,yy+22,t,12,SLATE,'end',weight='600')
        b+=f'<rect x="{x0+off}" y="{yy+6}" width="{seg}" height="30" rx="6" fill="{c}" opacity="0.16"/>'
        b+=f'<rect x="{x0+off}" y="{yy+6}" width="4" height="30" rx="2" fill="{c}"/>'
        b+=T(x0+off+14,yy+19,title,12,c,weight='700')
        b+=T(x0+off+14,yy+33,detail,10.5,SLATE)
    b+=f'<line x1="{x0}" y1="{y0-8}" x2="{x0+bw}" y2="{y0-8}" stroke="{LINE}"/>'
    for i,m in enumerate(['Sept','Oct','Nov','Dec']):
        b+=T(x0+bw*i/4+bw/8,y0-14,m,10.5,SLATE,'middle')
    write('plan-90-days.svg',svg(w,h,b,'The first 90 days'))

# 7 — maternity journey
def journey():
    w,h=760,260; b=head(w,'What MaternaLink covers','From the first appointment to a year after the birth. The last part is where nobody else goes.')
    steps=[('Booking','~10 weeks'),('16 weeks','cuff issued'),('Pregnancy','checks at home'),('Birth',''),('6 weeks','handover to GP'),('1 year','follow-up ends')]
    x0,y=60,140; span=640
    b+=f'<line x1="{x0}" y1="{y}" x2="{x0+span}" y2="{y}" stroke="{LINE}" stroke-width="4"/>'
    b+=f'<line x1="{x0}" y1="{y}" x2="{x0+span*0.55}" y2="{y}" stroke="{BLUE}" stroke-width="4"/>'
    b+=f'<line x1="{x0+span*0.55}" y1="{y}" x2="{x0+span}" y2="{y}" stroke="{ROSE}" stroke-width="4"/>'
    for i,(t,s) in enumerate(steps):
        cx=x0+span*i/(len(steps)-1)
        c=BLUE if i<3 else (INK if i==3 else ROSE)
        b+=f'<circle cx="{cx}" cy="{y}" r="9" fill="#fff" stroke="{c}" stroke-width="3"/>'
        b+=T(cx,y-24,t,12,c,'middle',weight='700')
        if s: b+=T(cx,y-10,s,10,SLATE,'middle')
    b+=T(x0+span*0.27,y+34,'Pregnancy: stay in contact between appointments',11.5,BLUE,'middle',weight='600')
    b+=T(x0+span*0.78,y+34,'The year after birth: where most late deaths happen',11.5,ROSE,'middle',weight='600')
    b+=T(x0+span*0.78,y+50,'and where no other product goes',11.5,ROSE,'middle')
    write('maternity-journey.svg',svg(w,h,b,'What MaternaLink covers'))

# 8 — how it works
def how():
    w,h=760,270; b=head(w,'How it works','A person decides, not the software. That is what keeps it safe and legal.')
    steps=[('She takes a reading','at home, works offline',BLUE),('The hospital rule checks it','rules your clinicians set',BLUE),
           ('A midwife is told','with a deadline to call',ROSE),('The midwife decides','and calls her',GREEN),('It is written down','who, when, what happened',INK)]
    x0,y=30,110; bw=136; gap=12
    for i,(t,s,c) in enumerate(steps):
        cx=x0+i*(bw+gap)
        b+=f'<rect x="{cx}" y="{y}" width="{bw}" height="92" rx="9" fill="{MIST}" stroke="{LINE}"/>'
        b+=f'<circle cx="{cx+18}" cy="{y+22}" r="11" fill="{c}"/>'+T(cx+18,y+26,i+1,11,'#fff','middle',weight='700')
        ws=t.split(); ln=[]; cur=''
        for wd in ws:
            if len(cur+' '+wd)>16: ln.append(cur); cur=wd
            else: cur=(cur+' '+wd).strip()
        ln.append(cur)
        for j,l in enumerate(ln): b+=T(cx+12,y+52+j*15,l,11.5,INK,weight='600')
        b+=T(cx+12,y+52+len(ln)*15+4,s,10,SLATE)
        if i<len(steps)-1:
            ax=cx+bw+2
            b+=f'<path d="M {ax} {y+46} l 8 0" stroke="{SLATE}" stroke-width="2" marker-end="url(#ar)"/>'
    b+=f'<defs><marker id="ar" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 z" fill="{SLATE}"/></marker></defs>'
    b+=f'<rect x="30" y="220" width="700" height="30" rx="6" fill="#FBF0F3"/>'
    b+=T(44,239,'The software never diagnoses, predicts or recommends treatment. It moves information to a human quickly.',11.5,'#8A2B47')
    write('how-it-works.svg',svg(w,h,b,'How MaternaLink works'))

# 9 — pricing comparison
def pricing():
    w,h=760,330; b=head(w,'What to charge, per woman per year','The old proposal was far above anything comparable. These are the new numbers.')
    rows=[('Old Ekiti proposal',300,300,ROSE,'withdrawn'),('UK hospital',18,36,BLUE,'plus a site licence'),('African programme',4,10,'#3E5FB0','at scale')]
    x0,y0=190,100; bw=480; mx=310
    for i,(n,lo,hi,c,note) in enumerate(rows):
        yy=y0+i*60
        b+=T(x0-14,yy+18,n,12.5,INK,'end',weight='600')
        b+=f'<line x1="{x0}" y1="{yy+16}" x2="{x0+bw}" y2="{yy+16}" stroke="{MIST}" stroke-width="10" stroke-linecap="round"/>'
        a=x0+bw*lo/mx; z=x0+bw*hi/mx
        b+=f'<line x1="{a}" y1="{yy+16}" x2="{max(z,a+4)}" y2="{yy+16}" stroke="{c}" stroke-width="10" stroke-linecap="round"/>'
        lbl=f'£{lo}' if lo==hi else f'£{lo}–£{hi}'
        b+=T(max(z,a+4)+12,yy+21,lbl,12.5,c,weight='700')
        b+=T(x0-14,yy+34,note,10.5,SLATE,'end')
    for v in (0,50,100,150,200,250,300):
        xx=x0+bw*v/mx
        b+=f'<line x1="{xx}" y1="{y0-6}" x2="{xx}" y2="{y0+186}" stroke="{LINE}" stroke-dasharray="2 4"/>'
        b+=T(xx,y0+202,f'£{v}',10,SLATE,'middle')
    b+=T(x0-100,y0+240,'A 15,000-woman programme is about £373,000 in year one, not £4.5m.',12,INK,weight='600')
    write('pricing-compare.svg',svg(w,h,b,'Pricing comparison'))

# 10 — funding staircase
def funding():
    w,h=760,340; b=head(w,'How to raise money, in stages','Each step is unlocked by proof, not by time passing.')
    steps=[('Grants and services','now','£0 dilution','Innovate UK, SBRI, first clients',GREEN),
           ('Pre-seed','after a hospital says yes','£250k–£500k','angels, SEIS/EIS tax relief',BLUE),
           ('Seed','after a trial and first revenue','£1.5m–£3m','health-tech funds',BLUE),
           ('Series A','after real evidence','£6m–£12m','2029 decision, not a plan',SLATE)]
    x0,y0=70,244; sw=160; sh=44
    for i,(t,when,amt,who,c) in enumerate(steps):
        x=x0+i*sw; y=y0-i*sh
        bh=max(sh*(i+1),86)
        b+=f'<rect x="{x}" y="{y}" width="{sw-8}" height="{bh}" rx="6" fill="{c}" opacity="{0.10+0.05*i}"/>'
        b+=f'<rect x="{x}" y="{y}" width="{sw-8}" height="4" rx="2" fill="{c}"/>'
        b+=T(x+12,y+22,t,12.5,c,weight='700')
        b+=T(x+12,y+38,amt,12,INK,weight='600')
        b+=T(x+12,y+54,when,10,SLATE)
        b+=T(x+12,y+68,who,10,SLATE)
    b+=f'<rect x="{x0-40}" y="{y0+46}" width="680" height="30" rx="6" fill="#FBF0F3"/>'
    b+=T(x0-26,y0+66,'Do not raise before the ownership agreement is signed and the old AI claims are withdrawn.',12,'#8A2B47',weight='600')
    write('funding-stairs.svg',svg(w,h,b,'Funding stages'))

# 11 — investor list breakdown
def investors():
    w,h=760,280; b=head(w,'Your investor list: 316 organisations','Sorted by how well they fit and how easily you can reach them.')
    tiers=[('A — approach first',4,ROSE),('B — build the relationship',87,BLUE),('C — keep warm',147,'#7E93CE'),('Below the line',78,'#C3CBDA')]
    x0,y=60,110; bw=640; tot=316; cx=x0
    for n,v,c in tiers:
        seg=bw*v/tot
        b+=f'<rect x="{cx}" y="{y}" width="{seg}" height="44" fill="{c}"/>'
        b+=T(cx+seg/2,y+29,v,14,'#fff','middle',weight='700')
        cx+=seg
    ly=y+80
    for i,(n,v,c) in enumerate(tiers):
        col=i%2; row=i//2
        xx=x0+col*330; yy=ly+row*26
        b+=f'<rect x="{xx}" y="{yy-11}" width="13" height="13" rx="3" fill="{c}"/>'+T(xx+20,yy,f'{n} ({v})',12,SLATE)
    st=[('43','phone numbers found in public sources'),('51','email addresses published officially'),('220','named decision makers')]
    for i,(n,d) in enumerate(st):
        xx=x0+i*215
        b+=T(xx,ly+80,n,22,BLUE,weight='700',font=FS)+T(xx,ly+98,d,10.5,SLATE)
    write('investor-tiers.svg',svg(w,h,b,'Investor list breakdown'))

# 12 — partner tiers
def partners():
    w,h=760,360; b=head(w,'The partners you need, in order','Start at the top. The first four are the ones that unlock everything else.')
    tiers=[('Must have','A hospital, a university, a safety officer, an NGO',ROSE,4),
           ('Technology','Blood-pressure cuffs, cloud, messaging, record systems',BLUE,6),
           ('Clinical','More hospitals, Royal Colleges, midwife networks',BLUE,8),
           ('Data','Research groups and cohorts for evidence',SLATE,6),
           ('Distribution','Health Innovation Networks, NGOs, telecoms',SLATE,8),
           ('Big strategic','Diagnostics, pharma, insurers (later)',SLATE,10),
           ('Funders','Grants, angels, funds',GREEN,6)]
    y0=80; mw=520
    for i,(t,d,c,n) in enumerate(tiers):
        yy=y0+i*33; ww=mw-(i*38); xx=(760-ww)/2
        b+=f'<rect x="{xx}" y="{yy}" width="{ww}" height="27" rx="5" fill="{c}" opacity="{0.20 if i else 0.30}"/>'
        b+=T(xx+12,yy+18,t,11.5,c if i<2 or i==6 else INK,weight='700')
        b+=T(xx+ww-12,yy+18,d,10,SLATE,'end')
    b+=T(380,y0+7*33+30,'74 named organisations with the job title to ask for are in the Partner War Room spreadsheet.',11.5,SLATE,'middle')
    write('partner-tiers.svg',svg(w,h,b,'Partner tiers'))

# 13 — market scores
def markets():
    w,h=760,320; b=head(w,'Which countries to enter, and when','Scored on size, need, rules, competition and how easily you can sell there.')
    rows=[('United Kingdom',82,'Now',GREEN),('Nigeria',68,'Now, through an NGO',GREEN),('Kenya',61,'Year 2',BLUE),
          ('Ghana',57,'Year 2',BLUE),('Rwanda',55,'Year 3',SLATE),('South Africa',52,'Year 3',SLATE),
          ('Ireland / Netherlands',49,'Year 3',SLATE),('United States',44,'Only with a partner',SLATE),('India / Bangladesh',40,'Not yet',SLATE)]
    x0,y0=180,80; bw=380
    for i,(n,v,when,c) in enumerate(rows):
        yy=y0+i*25
        b+=T(x0-12,yy+13,n,11.5,INK,'end')
        b+=f'<rect x="{x0}" y="{yy+3}" width="{bw}" height="15" rx="3" fill="{MIST}"/>'
        b+=f'<rect x="{x0}" y="{yy+3}" width="{bw*v/100}" height="15" rx="3" fill="{c}" opacity="0.85"/>'
        b+=T(x0+bw*v/100+8,yy+15,v,10.5,SLATE,weight='600')
        b+=T(x0+bw+40,yy+15,when,10.5,c,weight='600')
    write('market-scores.svg',svg(w,h,b,'Market scores'))

# 14 — readiness
def readiness():
    w,h=760,340; b=head(w,'Are you ready to talk to investors?','Five of these must be green before your first meeting. Today, none are.')
    items=[('Company registered',0),('Ownership of MaternaLink agreed in writing',0),('Old AI claims withdrawn',0),('Name and trademark checked',0),
           ('First paying client',0),('A hospital agrees to a trial',0),('Two advisers signed up',0),('Product audited and documented',0),
           ('Financial model with real numbers',1),('Data room built',0),('Investor list ready',1),('Insurance and data registration',0),
           ('Your own time commitment written down',0),('15 interviews done',0),('One grant applied for',0)]
    x0,y0=50,80
    for i,(t,done) in enumerate(items):
        col=i//8; row=i%8; xx=x0+col*360; yy=y0+row*30
        c=GREEN if done else '#C3CBDA'
        b+=f'<rect x="{xx}" y="{yy}" width="18" height="18" rx="4" fill="{c}" opacity="{1 if done else 0.35}"/>'
        if done: b+=f'<path d="M {xx+4} {yy+9} l 4 4 l 7 -8" stroke="#fff" stroke-width="2.5" fill="none"/>'
        b+=T(xx+28,yy+14,t,11.5,INK if done else SLATE,weight='600' if done else '400')
    b+=f'<rect x="{x0}" y="{y0+250}" width="660" height="34" rx="6" fill="#FBF0F3"/>'
    b+=T(x0+14,y0+272,'Rule: no investor meeting until the first four are done and two of the next three. Score today: 1.3 out of 10.',11.5,'#8A2B47',weight='600')
    write('readiness.svg',svg(w,h,b,'Investor readiness'))

# 15 — have / building / next
def traction():
    w,h=760,270; b=head(w,'What you have, what you are building, what comes next','Say it in this order to investors. Never inflate the first column.')
    cols=[('What you have',['A full company plan','A prototype (needs an audit)','A past government conversation','A logo and two websites'],SLATE),
          ('Building now',['The company itself','Ownership agreement','First advisory clients','A hospital trial'],BLUE),
          ('Next',['First paying customer','A signed pilot','Advisers on board','Pre-seed round'],GREEN)]
    for i,(t,items,c) in enumerate(cols):
        x=40+i*240
        b+=f'<rect x="{x}" y="70" width="220" height="170" rx="9" fill="{MIST}" stroke="{LINE}"/>'
        b+=f'<rect x="{x}" y="70" width="220" height="4" rx="2" fill="{c}"/>'
        b+=T(x+16,98,t,13,c,weight='700')
        for j,it in enumerate(items):
            b+=f'<circle cx="{x+22}" cy="{119+j*28}" r="3" fill="{c}"/>'
            b+=T(x+34,123+j*28,it,11,INK)
    write('traction.svg',svg(w,h,b,'Have, building, next'))

# 16 — first £1m
def firstmillion():
    w,h=760,290; b=head(w,'Where your first £1,000,000 comes from','Services first. The product later. Grants alongside.')
    rows=[('Advisory and consulting',325,BLUE),('Hospital pilots and licences',200,'#3E5FB0'),('One African programme',225,'#7E93CE'),('Grants',175,GREEN),('Sponsorship and training',75,ROSE)]
    x0,y0=60,100; bw=640; tot=1000; cx=x0
    for n,v,c in rows:
        seg=bw*v/tot
        b+=f'<rect x="{cx}" y="{y0}" width="{seg}" height="50" fill="{c}"/>'
        b+=T(cx+seg/2,y0+31,f'£{v}k',13,'#fff','middle',weight='700')
        cx+=seg
    for i,(n,v,c) in enumerate(rows):
        col=i%3; row=i//3; xx=x0+col*215; yy=y0+95+row*26
        b+=f'<rect x="{xx}" y="{yy-11}" width="13" height="13" rx="3" fill="{c}"/>'+T(xx+20,yy,n,11,SLATE)
    b+=T(x0,y0+175,'Mid-points of the ranges. Roughly the first 12 to 18 months.',11,SLATE)
    write('first-million.svg',svg(w,h,b,'First million'))

# 17 — cuff vs watch
def device():
    w,h=760,270; b=head(w,'Cuff now, watch later','Why the wrist device is not the first thing to build.')
    opts=[('Arm cuff (now)',['Already approved for medical use','£40–£100 each','Doctors trust the readings','You can start in months'],GREEN),
          ('Rented certified watch (later)',['Someone else carries the safety risk','£4–£7 per month to rent','Only after the software works','Adds convenience, not accuracy'],AMBER),
          ('Build your own watch',['Two years and £1m+ before a sale','You become a device manufacturer','Wrist blood pressure is not accurate enough','Doctors will not act on it'],RED)]
    for i,(t,pts,c) in enumerate(opts):
        x=30+i*240
        b+=f'<rect x="{x}" y="70" width="220" height="175" rx="9" fill="#fff" stroke="{c}" stroke-width="1.5" opacity="1"/>'
        b+=f'<rect x="{x}" y="70" width="220" height="26" rx="9" fill="{c}" opacity="0.14"/>'
        b+=T(x+14,88,t,12,c,weight='700')
        for j,p in enumerate(pts):
            ws=p.split(); ln=[]; cur=''
            for wd in ws:
                if len(cur+' '+wd)>28: ln.append(cur); cur=wd
                else: cur=(cur+' '+wd).strip()
            ln.append(cur)
            yy=112+j*33
            b+=T(x+14,yy,('✓ ' if i==0 else ('• ' if i==1 else '✗ '))+ln[0],10.5,INK)
            for k,l in enumerate(ln[1:]): b+=T(x+24,yy+13*(k+1),l,10.5,INK)
    write('cuff-vs-watch.svg',svg(w,h,b,'Cuff versus watch'))

# 18 — document map
def docmap():
    w,h=760,330; b=head(w,'What to read, and when','Fourteen documents. You do not need to read them all at once.')
    groups=[('Read this week',['00 Start here','01 Where you stand','02 What we are building','06 The plan'],ROSE),
            ('Read before selling',['03 Who buys it','04 How we make money','07 Getting customers'],BLUE),
            ('Read before investors',['05 The money','10 Partners','13 The investor list'],GREEN),
            ('Look up when needed',['08 Running the company','09 Legal and safety','11 Brand','12 Structure and markets'],SLATE)]
    x0=30
    for i,(t,items,c) in enumerate(groups):
        x=x0+i*180
        b+=f'<rect x="{x}" y="72" width="168" height="30" rx="6" fill="{c}" opacity="0.14"/>'
        b+=T(x+14,92,t,11.5,c,weight='700')
        for j,it in enumerate(items):
            b+=f'<rect x="{x}" y="{112+j*38}" width="168" height="32" rx="5" fill="{MIST}" stroke="{LINE}"/>'
            b+=T(x+12,{0:132}.get(0,132)+j*38,it,10.5,INK)
    b+=T(x0,300,'Everything else is reference: the spreadsheets, the developer documents and the investor and partner lists.',11.5,SLATE)
    write('doc-map.svg',svg(w,h,b,'Document map'))

for f in (business_score,pillars,revenue,mix,cash,plan90,journey,how,pricing,funding,investors,partners,markets,readiness,traction,firstmillion,device,docmap):
    f()
print('all diagrams written to diagrams/')
