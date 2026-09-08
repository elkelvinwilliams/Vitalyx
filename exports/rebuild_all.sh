#!/bin/bash
# Rebuild every export from the Markdown sources. Run from the repository root.
set -e
cd "$(dirname "$0")/.."
echo "1/6 diagrams";   python3 exports/build_diagrams.py > /dev/null
echo "2/6 PDFs";       python3 exports/build_pdfs.py | tail -1
echo "3/6 deck PDFs";  python3 exports/build_deck_pdfs.py | tail -1
echo "4/6 workbooks";  python3 exports/build_xlsx.py | tail -1
echo "5/6 Word+PPT";   python3 exports/build_exports.py | tail -1
echo "6/6 executive pack + zips"
python3 - <<'PY'
import pymupdf, os
order=['00_START_HERE','01_WHERE_YOU_STAND','02_WHAT_WE_ARE_BUILDING','04_HOW_WE_MAKE_MONEY','05_THE_MONEY','06_THE_PLAN']
out=pymupdf.open()
for n in order:
    p=f'exports/pdf/{n}.pdf'
    if os.path.exists(p): out.insert_pdf(pymupdf.open(p))
out.save('exports/pdf/Vytalix_Executive_Pack.pdf'); print('executive pack:',len(out),'pages')
PY
rm -f exports/*.zip
zip -qr exports/Vytalix_Pack_1_Documents.zip exports/pdf exports/xlsx exports/pptx FACTS_BASE.md README.md docs product assets diagrams brand
zip -qr exports/Vytalix_Pack_2_Sites_Data_Source.zip exports/docx exports/live website maternalink-site investors finance operations -x "*/__pycache__/*"
du -h exports/*.zip
