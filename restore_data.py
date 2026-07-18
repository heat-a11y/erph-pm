#!/usr/bin/env python3
"""Replace TEACHERS and SLOTS in index.html with full data from timetable-data.js."""
import re, json

IN = '/home/home/Documents/New OpenCode Project/erph-pm/index.html'
TT = '/home/home/Documents/New OpenCode Project/erph-pm/timetable-data.js'

with open(TT, 'r') as f:
    tt = f.read()

# Extract TEACHERS
m = re.search(r'const TEACHERS = ({.*?});', tt, re.DOTALL)
teachers = json.loads(m.group(1)) if m else {}
teachers_js = json.dumps(teachers, ensure_ascii=False)

# Extract SLOTS - fix unquoted keys
slots = {}
for code in ['TBS','LET','HLF','LJX','LSW','WKS','LYY','OWY','ARMAN','COW','BALKIS','YH']:
    pattern = rf'TEACHER_SLOTS_P1\["{code}"\]\s*=\s*(\[.*?\]);'
    m = re.search(pattern, tt, re.DOTALL)
    if m:
        arr_str = m.group(1)
        # Fix unquoted keys: {class: -> {"class":
        arr_str = re.sub(r'(\{)\s*(\w+)(\s*:)', r'\1"\2"\3', arr_str)
        arr_str = re.sub(r'(,\s*)(\w+)(\s*:)', r'\1"\2"\3', arr_str)
        try:
            slots[code] = json.loads(arr_str)
        except:
            print(f'Parse failed for {code}')
            slots[code] = []
slots_js = json.dumps(slots, ensure_ascii=False)

with open(IN, 'r') as f:
    html = f.read()

# Find and replace TEACHERS and SLOTS in the script
# The script tag spans multiple lines, so we need to find the right section
script_start = html.find('TEACHERS: {')
script_end = html.find('DAYS:', script_start)

if script_start > 0:
    # Replace from TEACHERS: to just before DAYS:
    old = html[script_start:script_end]
    new = f'TEACHERS: {teachers_js}'
    html = html[:script_start] + new + html[script_end:]
    print(f'TEACHERS replaced: {len(teachers)} teachers')

if 'SLOTS:' in html:
    s_start = html.find('SLOTS: {')
    s_end = html.find(',\n  DAYS:', s_start)
    if s_end < 0:
        s_end = html.find(',\n  PERIODS:', s_start)
    if s_start > 0 and s_end > s_start:
        old = html[s_start:s_end]
        new = f'SLOTS: {slots_js}'
        html = html[:s_start] + new + html[s_end:]
        total = sum(len(v) for v in slots.values())
        print(f'SLOTS replaced: {total} entries')

with open(IN, 'w') as f:
    f.write(html)

print('Done')
