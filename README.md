# eRPH-PM — eRancangan Pengajaran Harian (Malaysia)

A fully client-side, multi-subject lesson plan generator for Malaysian primary school teachers (SK & SJKC).

**Live demo:** [https://heat-a11y.github.io/erph-pm](https://heat-a11y.github.io/erph-pm)

## Features

- **Multi-subject** — All KSSR subjects: BM, BI, BC, MT, SN, PM, PI, PJ, PK, PSV, MZ, SJ, RBT
- **Years 1–6** — Complete curriculum coverage for all primary levels
- **RPT-aligned** — Curriculum data extracted from official 2026 RPT documents
- **Interactive Timetable** — Click any cell to add/edit class slots by subject and year
- **RPH Generator** — Generate daily lesson plans from your timetable with DSKP-aligned content
- **Curriculum Browser** — Browse units, content standards, and learning standards per subject/year
- **PDF Export** — Download individual or bulk lesson plans as PDF (A4 format)
- **Local Storage** — All data stays in your browser — no server, no login

## Quick Start

1. Open `index.html` in any modern browser
2. Select your **Subject** and **Year** from the top bar
3. Browse the curriculum in the **Curriculum** tab
4. Switch to **Timetable** to add your teaching slots
5. Go to **Generate RPH**, select a week, and click **Generate RPH**
6. Edit, reflect, and export to PDF

## Tech Stack

HTML · Tailwind CSS · Alpine.js · html2pdf.js

## Data Source

Curriculum data extracted from official 2026 KSSR RPT (Rancangan Pengajaran Tahunan) documents for SJKC.

## License

MIT
