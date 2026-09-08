#!/usr/bin/env python3
"""Branded Excel workbooks: adds a cover sheet with logo to existing workbooks and builds new working tools.
Run: python3 exports/build_xlsx.py   Outputs: exports/xlsx/*.xlsx"""
import os,csv,glob,shutil
from openpyxl import Workbook,load_workbook
from openpyxl.styles import Font,PatternFill,Alignment,Border,Side
from openpyxl.drawing.image import Image as XImage
from openpyxl.utils import get_column_letter
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(ROOT,'exports','xlsx'); os.makedirs(OUT,exist_ok=True)
LOGO=os.path.join(ROOT,'website','assets','img','vytalix-logo.png')
BLUE='153892'; ROSE='C93D63'; TINT='E9EDF8'
HF=Font(bold=True,color='FFFFFF'); HFILL=PatternFill('solid',fgColor=BLUE); INPUT=PatternFill('solid',fgColor='FFF7DD'); thin=Side(style='thin',color='D9DEE9')
def header(ws,row=1):
    for c in ws[row]:
        if c.value is not None: c.font=HF; c.fill=HFILL; c.alignment=Alignment(wrap_text=True,vertical='top')
def widths(ws,default=16,maxw=48):
    for col in ws.columns:
        L=max((len(str(c.value)) for c in col if c.value is not None),default=8)
        ws.column_dimensions[get_column_letter(col[0].column)].width=max(10,min(maxw,L+2))
def cover(wb,title,desc,contents):
    ws=wb.create_sheet('Cover',0)
    ws.sheet_view.showGridLines=False
    try:
        img=XImage(LOGO); img.width,img.height=300,118; ws.add_image(img,'B2')
    except Exception as e: print('logo skipped',e)
    ws['B10']=title; ws['B10'].font=Font(size=24,bold=True,color=BLUE)
    ws['B12']=desc; ws['B12'].font=Font(size=11,color='4B5568'); ws['B12'].alignment=Alignment(wrap_text=True,vertical='top'); ws.merge_cells('B12:H14')
    ws['B16']='Prepared for'; ws['C16']='The Founder, Vytalix'; ws['B17']='Date'; ws['C17']='8 September 2026'; ws['B18']='Version'; ws['C18']='1.0 · Confidential draft'
    for r in (16,17,18): ws[f'B{r}'].font=Font(bold=True,color=BLUE)
    ws['B20']='Contents'; ws['B20'].font=Font(bold=True,size=12,color=BLUE)
    for i,(s,d) in enumerate(contents): ws[f'B{21+i}']=s; ws[f'C{21+i}']=d; ws[f'B{21+i}'].font=Font(bold=True)
    ws[f'B{23+len(contents)}']='Colour code: yellow cells are inputs you can change; blue headers are fixed; every figure is an ESTIMATE unless labelled VERIFIED (see FACTS_BASE).'; ws[f'B{23+len(contents)}'].font=Font(italic=True,color='4B5568')
    ws.column_dimensions['B'].width=18; ws.column_dimensions['C'].width=70
    return ws
def brand_existing(src,dst,title,desc):
    wb=load_workbook(src)
    contents=[(s.title,'') for s in wb.worksheets]
    if 'Cover' in wb.sheetnames: del wb['Cover']
    cover(wb,title,desc,contents)
    for ws in wb.worksheets[1:]:
        if ws.max_row>=1 and any(c.value for c in ws[1]): header(ws)
    wb.save(dst); print('branded',os.path.basename(dst))

# 1) Brand existing workbooks
brand_existing(os.path.join(ROOT,'investors','VYTALIX_INVESTOR_CRM.xlsx'),os.path.join(OUT,'Vytalix_Investor_CRM.xlsx'),'Investor CRM','316 investors scored for fit and contactability, with Top 25, four call lists, pipeline stages and dashboard. Phone numbers only where traced to an official public source.')
brand_existing(os.path.join(ROOT,'finance','Vytalix_Financial_Model_3yr.xlsx'),os.path.join(OUT,'Vytalix_Financial_Model_3yr.xlsx'),'Financial Model (36 months)','Three scenarios (Conservative, Base, High-growth) driven from one assumptions sheet. Change the scenario selector on the Assumptions sheet. Nothing here is an actual; all figures are scenario outputs.')
brand_existing(os.path.join(ROOT,'investors','partners','PARTNER_WAR_ROOM.xlsx'),os.path.join(OUT,'Partner_War_Room.xlsx'),'Partner War Room','74 target organisations with the job title to approach, a CRM with the eleven-stage partner pipeline, stage rules and monthly KPIs.')

# 2) KPI dashboard and pipeline trackers from CSVs
def from_csv(path,title,desc,sheetname):
    wb=Workbook(); ws=wb.active; ws.title=sheetname
    for r in csv.reader(open(path,encoding='utf-8')): ws.append(r)
    header(ws); widths(ws); ws.freeze_panes='A2'; ws.auto_filter.ref=ws.dimensions
    return wb,ws
wb,ws=from_csv(os.path.join(ROOT,'operations','KPI_DASHBOARD.csv'),'KPI Dashboard','Commercial, investment, product, marketing and finance KPIs with formulas and month 1–3 targets. Replace EXAMPLE rows with actuals each Friday.','KPIs')
cover(wb,'KPI Dashboard','Commercial, investment, product, marketing and finance KPIs with targets for months 1–3. Replace EXAMPLE rows with actuals every Friday.',[('KPIs','Definitions, formulas, targets, actuals')]); wb.save(os.path.join(OUT,'KPI_Dashboard.xlsx'))
wb,ws=from_csv(os.path.join(ROOT,'operations','PIPELINE_TRACKERS.csv'),'Pipeline Trackers','Investor, partnership, product, revenue and strategic-project pipelines in one sheet.','Pipelines')
cover(wb,'Pipeline Trackers','Investor, partnership, product, revenue and strategic-project pipelines. Filter by the Pipeline column.',[('Pipelines','All five pipelines; filter by type')]); wb.save(os.path.join(OUT,'Pipeline_Trackers.xlsx'))
wb,ws=from_csv(os.path.join(ROOT,'assets','CONTENT_CALENDAR.csv'),'Content Calendar','Twelve weeks of dated content across LinkedIn, website, email, video and events.','Calendar')
cover(wb,'Content Calendar','Twelve weeks from Monday 14 September 2026 across LinkedIn, website, email, video and events; consistent with the marketing engine.',[('Calendar','Dated items with pillar, format, CTA, owner and status')]); wb.save(os.path.join(OUT,'Content_Calendar.xlsx'))

# 3) MaternaLink pricing calculator (formulas)
wb=Workbook(); ws=wb.active; ws.title='UK Calculator'
rows=[['MATERNALINK PRICING CALCULATOR — UK (all inputs are ESTIMATES to validate)',''],[],
['Inputs','Value','Notes'],
['Annual births at the service',5000,'Drives site-licence band'],
['Women enrolled per year',5000,'Usually equals births for Core'],
['Core price per woman (£)',22,'Range 18–36'],
['Site licence (£)',20000,'12k–30k by births band'],
['Engagement module: enrolled women',5000,''],['Engagement price per woman (£)',10,'Range 8–14'],
['Triage module sites',1,''],['Triage price per site (£)',25000,'15k–35k'],
['Glucose module: women with condition',350,'Typically 5–10% of cohort'],['Glucose price per woman (£)',25,'20–30'],
['Watch devices leased',0,''],['Watch lease per device per month (£)',5.5,'4–7'],
['Analytics (£ per site)',8000,'6k–12k'],
['Integration interfaces (count)',1,''],['Integration setup per interface (£)',25000,'15k–40k'],['Integration annual per interface (£)',6000,'4k–8k'],
['Implementation one-off (£)',45000,'25k–75k'],
['Service plan % (Standard 0.20 / Enhanced 0.26 / Premium 0.32)',0.26,''],
[],['Outputs','£',''],
['Core software','=B4*0+B5*B6+B7',''],['Engagement','=B8*B9',''],['Triage','=B10*B11',''],['Glucose','=B12*B13',''],['Analytics','=B16',''],
['Software subtotal (annual)','=SUM(B24:B28)',''],
['Annual service plan','=B29*B21',''],
['Watch lease (annual)','=B14*B15*12',''],
['Integration annual','=B17*B19',''],
['Recurring annual total','=B29+B30+B31+B32',''],
['One-off: integration setup + implementation','=B17*B18+B20',''],
['YEAR 1 TOTAL','=B33+B34',''],['YEAR 2+ RUN-RATE','=B33',''],['Recurring cost per enrolled woman (£)','=IF(B5>0,B33/B5,0)','']]
for r in rows: ws.append(r)
ws['A1'].font=Font(bold=True,size=13,color=BLUE); header(ws,3); header(ws,23)
for r in range(4,22): ws[f'B{r}'].fill=INPUT
for r in (35,36,37): ws[f'A{r}'].font=Font(bold=True,color=BLUE); ws[f'B{r}'].font=Font(bold=True)
for r in range(24,38): ws[f'B{r}'].number_format='£#,##0'
ws['B37'].number_format='£#,##0.00'; ws['B21'].number_format='0%'
ws.column_dimensions['A'].width=52; ws.column_dimensions['B'].width=16; ws.column_dimensions['C'].width=40
ws2=wb.create_sheet('Programme Calculator')
rows2=[['MATERNALINK PRICING CALCULATOR — PROGRAMME (Africa / donor-funded)',''],[],['Inputs','Value','Notes'],
['Women enrolled',15000,''],['Core price per woman (£) — tiered: 10 / 7 / 5 / 4','=IF(B4<=5000,10,IF(B4<=25000,7,IF(B4<=100000,5,4)))','Formula applies the published tiers'],
['Engagement price per woman (£)',4,'3–5'],['Facilities with triage',20,''],['Triage per facility (£)',2500,'1.5k–4k'],
['Training cohorts',10,''],['Training per cohort (£)',1800,'1.2k–2.5k'],['Implementation one-off (£)',80000,'40k–120k'],
['Service plan % (0.20 / 0.28 / 0.35)',0.28,''],
[],['Outputs','£',''],['Core','=B4*B5',''],['Engagement','=B4*B6',''],['Triage','=B7*B8',''],['Software subtotal','=SUM(B15:B17)',''],
['Service plan','=MAX(B18*B12,12000)','Minimum £12,000'],['Training','=B9*B10',''],['YEAR 1 TOTAL','=B18+B19+B20+B11',''],['YEAR 2+ RUN-RATE','=B18+B19',''],
['Year-1 cost per woman (£)','=IF(B4>0,B21/B4,0)',''],['Run-rate cost per woman (£)','=IF(B4>0,B22/B4,0)','']]
for r in rows2: ws2.append(r)
ws2['A1'].font=Font(bold=True,size=13,color=BLUE); header(ws2,3); header(ws2,14)
for r in range(4,13): ws2[f'B{r}'].fill=INPUT
ws2['B5'].fill=PatternFill('solid',fgColor=TINT)
for r in range(15,25): ws2[f'B{r}'].number_format='£#,##0'
ws2['B23'].number_format='£#,##0.00'; ws2['B24'].number_format='£#,##0.00'; ws2['B12'].number_format='0%'
for r in (21,22): ws2[f'A{r}'].font=Font(bold=True,color=BLUE); ws2[f'B{r}'].font=Font(bold=True)
ws2.column_dimensions['A'].width=52; ws2.column_dimensions['B'].width=16; ws2.column_dimensions['C'].width=40
ws3=wb.create_sheet('Price Book')
for r in [['Product','UK model','UK indicative','Programme model','Programme indicative'],
['Core platform','Site licence + per woman/yr','£12k–£30k + £18–£36','Per woman/yr tiered','£10 / £7 / £5 / £4'],
['Engagement module','Per woman/yr','£8–£14','Per woman/yr','£3–£5'],['Maternity triage','Per site/yr','£15k–£35k','Per facility/yr','£1.5k–£4k'],
['Diabetes glucose diary','Per woman with condition/yr','£20–£30','Per woman','£6–£10'],['Voice diaries','Per woman/yr','£3–£5','Per woman','£1–£2'],
['Maternity Watch (certified third-party device)','Lease per device/month','£4–£7 (or £120–£220 + £30/yr)','Lease per device/month','£2–£4 (or £90–£160 + £15/yr)'],
['Integration pack','Setup + annual per interface','£15k–£40k + £4k–£8k','Setup + annual','£8k–£25k + £3k'],['Analytics','Per site/yr','£6k–£12k','Included in programme','—'],
['Training','Per cohort of 25','£2.5k–£4.5k','Per cohort of 30','£1.2k–£2.5k'],['Implementation','One-off per site','£25k–£75k','One-off per programme','£40k–£120k'],
['Pilot (12 weeks)','Fixed','£40k–£90k','Scoped','On scope'],['Service plans','% of licence','Std 18–22% · Enh 25–28% · Prem 30–35% (min £8k)','% of software','20% · 28% · 35% (min £12k)']]: ws3.append(r)
header(ws3); widths(ws3,maxw=44)
cover(wb,'MaternaLink Pricing Calculator','Working calculators for UK services and programme deployments, plus the published price book. Yellow cells are inputs. Every price is an ESTIMATE until validated with three buyers per segment.',[('UK Calculator','Trust or hospital pricing by module and service plan'),('Programme Calculator','Per-woman tiered pricing for state and NGO programmes'),('Price Book','Published ranges per product')])
wb.save(os.path.join(OUT,'MaternaLink_Pricing_Calculator.xlsx')); print('pricing calculator ok')

# 4) Investor readiness scorecard
wb=Workbook(); ws=wb.active; ws.title='Scorecard'
ws.append(['#','Readiness item','Today (0/1)','Target','How to close','Owner','Due','Status','Notes'])
items=[('Legal entity, bank, accountant',0,1,'Name clearance, incorporate, bank, accountant, SEIS/EIS advance assurance','Founder','Day 10'),('MaternaLink IP owned or licensed in writing',0,1,'Heads of terms then IP deed with collaborator; contributor assignments','Founder + solicitor','Day 30'),('No unvalidated clinical claims public',0,1,'Retire 2025 deck; relabel prototype rules; auth; remove photos','Founder','Day 14'),('Name and trademark clearance',0,1,'Knock-out searches; file UK TM classes 9, 41, 42, 44','Founder + attorney','Day 20'),('First revenue',0,1,'Advisory packages; 40 conversations; first SOW','Founder','Day 45'),('Pilot partner LOI',0,1,'15 discovery interviews; pilot proposal','Founder','Day 60'),('Advisory board (2 confirmed)',0,1,'Named asks; advisory agreements','Founder','Day 60'),('Product evidence (audit, PRD, intended use, hazard log)',0,1,'Code audit; clinician sign-off','CTO/CPO','Day 30'),('Financial model with actuals',1,1,'Update with months 1–3 actuals','CFO role','Day 60'),('Data room',0,1,'Index in doc 23 §2','Founder','Day 45'),('Investor list and outreach system',1,1,'Verify Call List 1 phones','Founder','Day 55'),('Compliance basics (ICO, Cyber Essentials, insurance)',0,1,'See doc 15','Founder','Day 30'),('Founder commitment statement and time split',0,1,'Written statement','Founder','Day 7'),('Proof of demand (15 interviews)',0,1,'Discovery interviews','Founder','Day 60'),('Non-dilutive application submitted',0,1,'Innovate UK Smart / SBRI Healthcare','Founder','Day 75')]
for i,(a,t,g,h,o,d) in enumerate(items,1): ws.append([i,a,t,g,h,o,d,'Not started',''])
n=len(items)+1
ws.append([]); ws.append(['','READINESS SCORE /10',f'=ROUND(SUM(C2:C{n})/COUNT(C2:C{n})*10,1)','', 'Rule: no first investor meeting until items 1–4 are done and two of 5–7 are done'])
ws[f'B{n+2}'].font=Font(bold=True,color=BLUE); ws[f'C{n+2}'].font=Font(bold=True,size=12)
header(ws); widths(ws,maxw=60); ws.freeze_panes='A2'
for r in range(2,n+1): ws[f'C{r}'].fill=INPUT; ws[f'H{r}'].fill=INPUT
cover(wb,'Investor Readiness Scorecard','Fifteen readiness items with owners and due dates. Update the Today column (0 or 1) weekly; the score recalculates. Rule: no first investor meeting until items 1–4 are done and two of 5–7 are done.',[('Scorecard','Items, targets, owners, due dates, live score')])
wb.save(os.path.join(OUT,'Investor_Readiness_Scorecard.xlsx')); print('scorecard ok')
print('xlsx done')
