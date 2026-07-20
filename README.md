# eRPH-PM — eRancangan Pengajaran Harian (Malaysia)

A fully client-side, multi-subject lesson plan (RPH) generator for Malaysian SJKC primary school teachers. All data stays in your browser — no server, no login required.

**Live demo:** [https://heat-a11y.github.io/erph-pm](https://heat-a11y.github.io/erph-pm)

---

## Features

- **16 KSSR Subjects** — BM, BC, BI, MT, SN, SJ, RBT, PJ, PK, PJPK, PSV, MZ, PMZ, PKS, PM, PI
- **Years 1–6** — Complete DSKP curriculum data for all primary levels
- **Interactive Timetable** — Visual timetable grid; click cells to add/edit class slots
- **RPH Generator** — Generate daily lesson plans from your timetable with DSKP-aligned content
- **Curriculum Browser** — Browse Content Standards (SK) and Learning Standards (SP) per subject/year
- **Student Tracking** — Auto-populated student names with TP (Tahap Penguasaan) levels 1–6
- **Smart Reflections** — TP-aware reflections with student names and activity references
- **PDF Export** — Export individual or bulk lesson plans as A4 PDF
- **Local Storage** — All data persists in your browser automatically

---

## Quick Start

1. Open `index.html` in Chrome, Firefox, or Edge
2. **Select a teacher** from the sidebar dropdown
3. The **Timetable** tab shows the teacher's weekly schedule
4. Click **Jana RPH** to generate lesson plans for the week
5. Click **PDF Semua** to export all plans, or **PDF** on individual plans

---

## Detailed Tutorial

### 1. Teacher Selection

Open the app — the **sidebar** on the left lists all 11 teachers at SJK(C) PIN MIN. Select a teacher to load their timetable.

- **Language rules**: BM subjects → BM content, BI subjects → English, all others → Chinese
- **Exception**: Teachers ARMAN BIN AWANG and NUR BALKIS BINTI ZULKHAIRANI always get BM content regardless of subject

### 2. Timetable Tab

The timetable shows the teacher's weekly schedule in a grid (Period × Day). Each cell shows the subject and class.

- **Empty cells** — Click any empty cell to add a new slot (enter subject code and class)
- **Slots with data** — Shows subject name and class (Year abbreviation)
- **Periods** — Timings follow the school's period schedule (P = Prep, 1–12 = periods, REHAT = break)

### 3. Generating RPH (Lesson Plans)

1. Select a **week** from the "Pilih Minggu" dropdown (shows school calendar dates)
2. Click the **⚡ Jana RPH** button
3. The RPH tab opens with all generated lesson plans, one per timetable slot

Each lesson plan includes:
- **Subject** and **Class** (with date, period, duration)
- **Unit** — Auto-generated from subject + class
- **Standard Kandungan (SK)** — 3 content standards pulled from the DSKP database
- **Standard Pembelajaran (SP)** — 3 learning standards pulled from the DSKP database
- **Objektif** — Learning objectives in the appropriate language
- **Kriteria Kejayaan** — Success criteria
- **Aktiviti** — 5 activities (Set Induction, Pre-lesson, Development, Post-lesson, Closure)
- **BBM / Nilai / EMK** — Teaching aids, moral values, cross-curricular elements
- **Pemulihan** — 3 remedial activities for weaker students
- **Rekod Transit** — Student TP tracking table
- **Refleksi** — TP-aware reflection text

### 4. Editing Lesson Plans

Each generated plan is fully editable:

- **Click the plan header** to expand/collapse
- **SK/SP dropdowns** — Select from available curriculum standards instead of typing
- **Click + Tambah** to add custom SK/SP entries
- **Activity textareas** — Edit activity descriptions directly
- **Guru/Murid fields** — Edit teacher and student role descriptions
- **Bold red Pemulihan section** — Edit remedial activity descriptions
- **Any change is saved automatically** to your browser's localStorage

### 5. SK & SP Selection

SK (Standard Kandungan) and SP (Standard Pembelajaran) now use **dropdown menus** populated from the official DSKP curriculum database. Each dropdown shows the standard code + description, e.g.:

```
1.1 Mendengar dan memberikan respons semasa berkomunikasi dalam pelbagai situasi
```

- Select any standard from the dropdown
- Use **+ Tambah** to add more rows
- Click the **✕** button to remove a row

### 6. Student TP Tracking

Each plan auto-loads students for that class from the school's student database.

- **TP (Tahap Penguasaan)** levels 1–6 are randomly assigned on generation
- Click **🎲 Jana TP** to re-randomize all TP values for a plan
- **Intervention notes** auto-update based on TP:
  - TP 1–2: "Bimbingan tambahan dalam kemahiran asas."
  - TP 3–4: "Bimbingan sederhana untuk meningkatkan kefahaman."
  - TP 5–6: "Aktiviti pengayaan untuk mencabar pemikiran."
- The TP table is also included in the PDF export

### 7. Reflections

Reflections are **automatically generated** for every lesson plan.

The smart reflection system:
- Counts students at each TP level (rendah 1–2, sederhana 3–4, cemerlang 5–6)
- **Names** high achievers and students needing guidance
- References the **main learning activity** from the plan
- References any **remedial activities** assigned
- Uses the correct language (BM/EN/ZH) based on subject and teacher

To manually regenerate a reflection:
- Click **💬 Jana Refleksi** on any plan
- Or click **💬 Sisip Refleksi** to generate reflections for all empty plans at once

### 8. Curriculum Browser Tab

The **Kurikulum** tab lets you explore the official DSKP standards:

1. Select a **subject** (e.g., Bahasa Melayu)
2. Select a **year** (e.g., Year 1)
3. **SK section** — Lists all Content Standards with codes and descriptions
4. **SP section** — Lists all Learning Standards with codes and descriptions

This is the same data used by the RPH generator.

### 9. PDF Export

Two export options:

- **📄 PDF** (on each plan) — Opens a new window with print-optimized HTML for that single plan
- **📄 PDF Semua** — Opens a new window with all plans, separated by page breaks, with day dividers

The PDF output includes:
- RPH header with school name and teacher info
- SK, SP, Objectives, Activities, BBM/Nilai/EMK
- Reflections
- Rekod Transit TP table with colour-coded TP badges
- Remedial activities section
- Footer with "Dijana oleh eRPH-PM"

> **Note**: PDF export uses `window.print()` with a popup window. Allow popups when prompted. If html2pdf.js is loaded, it attempts a smoother PDF download first, falling back to print.

### 10. Data Persistence

All data is stored in your browser's **localStorage**:

| Data | Key | Description |
|------|-----|-------------|
| Teacher | `eptg` | Currently selected teacher |
| Plans | `eprph` | All generated lesson plans |
| Week | `epwk` | Currently selected week |
| Slots | `erphp_slots` | Custom timetable slots |

**Nothing is sent to any server.** Your data persists across sessions until you clear your browser data.

To delete all plans, click the **🗑️ Padam** button.

### 11. Teacher-Specific Behavior

| Teacher Code | Name | Language Behavior |
|:---:|---|---|
| TBS | TEOH BOON SIM | BM→BM, BI→EN, others→ZH |
| LET | LEE EE TING | BM→BM, BI→EN, others→ZH |
| HLF | HEW LEE FUN | BM→BM, BI→EN, others→ZH |
| LJX | LIAN JUNXIANG | BM→BM, BI→EN, others→ZH |
| LSW | LEE SHU WEN | BM→BM, BI→EN, others→ZH |
| LYY | LOOI YUN YUAN | BM→BM, BI→EN, others→ZH |
| OWY | ONG WEI YI | BM→BM, BI→EN, others→ZH |
| **ARMAN** | ARMAN BIN AWANG | Always BM |
| COW | CHONG OOI WEI | BM→BM, BI→EN, others→ZH |
| **BALKIS** | NUR BALKIS BINTI ZULKHAIRANI | Always BM |
| YH | YOONG HAI | BM→BM, BI→EN, others→ZH |

---

## Subjects Covered

| Code | Subject | Years |
|:---:|---|---|
| BM | Bahasa Melayu | 1–6 |
| BC | Bahasa Cina | 1–6 |
| BI | English | 1–6 |
| MT | Matematik | 1–6 |
| SN | Sains | 1–6 |
| SJ | Sejarah | 4–6 |
| RBT | Reka Bentuk dan Teknologi | 4–6 |
| PJ | Pendidikan Jasmani | 1–6 |
| PK | Pendidikan Kesihatan | 1–6 |
| PJPK | Pendidikan Jasmani & Kesihatan | 1–6 |
| PSV | Pendidikan Seni Visual | 1–6 |
| MZ | Pendidikan Muzik | 1–6 |
| PMZ | Pendidikan Muzik (alternate) | 1–6 |
| PKS | Pendidikan Kesenian | 1–6 |
| PM | Pendidikan Moral | 1–6 |
| PI | Pendidikan Islam | 1–6 |

---

## Tech Stack

- **HTML** — Single-page application
- **Tailwind CSS** — Utility-first styling (loaded via CDN)
- **Alpine.js** — Reactive JavaScript framework (loaded via CDN)
- **html2pdf.js** — Client-side PDF generation (loaded via CDN, fallback to `window.print()`)

## Data Source

Curriculum data is based on the official **KSSR Semakan 2017 DSKP (Dokumen Standard Kurikulum dan Pentaksiran)** documents for SJKC schools. Activity banks, remedial activities, and reflection templates are curated for the Malaysian primary classroom context.

## License

MIT
