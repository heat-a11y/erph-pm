#!/usr/bin/env python3
"""Add students DB, TP tracking, fix PDF export."""
import json, re

with open('/home/home/Documents/New OpenCode Project/erph-pm/index.html', 'r') as f:
    html = f.read()

# 1. STUDENTS database
students = {
    'Year 1': ['BERNICE KONG ZHI YING','KOK CHEE HANG','KOK HAO YUEN','LAI JING TING','LAI PEI SHEN','LAKSHAIYAN A/L JAMES','LEE IYNNA','LIM JING TONG','MATHI SELVAM A/L RAVICHANDRAN','PANG YUNXIN','SHAVINA SREE A/P MOGAN RAJ','SIN CHEE CHUNG'],
    'Year 2': ['ARSHDEEP SINGH','CHEAH MING XUAN','FOO YI TING','HENDRIKUS PADA','KOK SIN LING','LAI SHU NI','LIEW ZI QIAN','LIM ZING HENG','MACSON YOONG','NOVIAN','RUVISHA A/P DILIP KUMAR','SARANIYA SREE','TANALECHIMI','YAATHISH'],
    'Year 3': ['AIDEN CHIN PARK YIN','AURELIUS SOSISEKO MISA','KOK ZI YING','LAI JING ROU','LAM YU NA','LIEW HENG KAI','LIM YI SHENG','NIHAHARIKA','PRITISHAA SREE'],
    'Year 4': ['CHEAH YAN YEE','FOO GUO JUN','LEE EYNENE','LEM JIA QI','LING HOCK JUN','LOO ZI HAO','LOW XUAN XUAN','NG HUI QI'],
    'Year 5': ['DARRSHAN','HOR YI HUI','KHONG MEI SEE','LIM JING XUAN','MAXIME YOONG','TEW WEN YONG'],
    'Year 6': ['ALICIA CHIN','CHAI CAROL','CHOO JANNA','GOH HUA YI','KOH QUAN JUN','LEE PUI YING','LEE YIHANN','LIEW WEI YANG','LIEW ZI SHUN','YONG HAN PENG'],
}
sj = json.dumps(students, ensure_ascii=False)
html = html.replace("document.addEventListener('alpine:init'", f"const STUDENTS = {sj};\n\ndocument.addEventListener('alpine:init'")

# 2. Add TP section after reflection
tp_block = '''
            <div class="border-t border-[#C4956A]/10 pt-2 mt-2">
              <div class="flex items-center justify-between mb-1">
                <p class="font-semibold text-indigo-700 text-[10px] uppercase tracking-wider">📊 Rekod Transit</p>
                <button @click.stop="genTP(p)" class="rounded border border-indigo-300 bg-indigo-50 px-2 py-0.5 text-[9px] font-medium text-indigo-700 hover:bg-indigo-100">🎲 Jana TP</button>
              </div>
              <div x-show="p._tpOpen" x-collapse class="overflow-x-auto rounded-lg border border-indigo-200 bg-white text-xs">
                <table class="w-full min-w-[350px]">
                  <thead><tr class="border-b bg-indigo-50">
                    <th class="px-2 py-1 text-left font-semibold text-indigo-600 w-8">#</th>
                    <th class="px-2 py-1 text-left font-semibold text-indigo-600">Nama</th>
                    <th class="px-2 py-1 text-center font-semibold text-indigo-600 w-12">TP</th>
                    <th class="px-2 py-1 text-left font-semibold text-indigo-600">Catatan</th>
                  </tr></thead>
                  <tbody><template x-for="(s,si) in p._students" :key="si">
                    <tr class="border-b last:border-0 hover:bg-indigo-50/50">
                      <td class="px-2 py-1 text-center text-indigo-400 text-[10px]" x-text="si+1"></td>
                      <td class="px-2 py-1"><input type="text" x-model="s.n" class="w-full min-w-[90px] rounded border-0 bg-transparent p-0 text-xs font-medium text-slate-700 focus:outline-none"></td>
                      <td class="px-2 py-1 text-center">
                        <select x-model="s.tp" class="w-9 rounded border border-indigo-200 bg-white px-0 py-0.5 text-center text-xs font-bold focus:border-indigo-400">
                          <template x-for="tp in 6" :key="tp"><option :value="tp" x-text="tp"></option></template>
                        </select>
                      </td>
                      <td class="px-2 py-1"><input type="text" x-model="s.c" class="w-full min-w-[80px] rounded border-0 bg-transparent p-0 text-[10px] text-amber-700 placeholder-slate-300 focus:outline-none" placeholder="Intervensi..."></td>
                    </tr>
                  </template></tbody>
                </table>
              </div>
              <button @click.stop="p._tpOpen=!p._tpOpen;if(p._tpOpen&&!p._tpInit){p._tpInit=true;const y=p.c.replace('Tahun ','Year ');const ns=STUDENTS[y]||[];p._students=ns.map(n=>({n,tp:Math.floor(Math.random()*6)+1,c:''}));}" class="mt-1 inline-flex items-center gap-1 rounded border border-indigo-300 bg-indigo-50 px-2.5 py-1 text-[10px] font-medium text-indigo-700 hover:bg-indigo-100">📊 Buka Rekod Transit</button>
            </div>'''

# Insert after reflection textarea
ref_tag = '<textarea x-model="p.ref" class="w-full rounded-lg border-2 border-amber-200 bg-amber-50 p-3 text-xs text-[#78350f] focus:border-amber-400 focus:outline-none" rows="3" placeholder="💬 Taip refleksi..."></textarea></div>'
html = html.replace(ref_tag, ref_tag + tp_block)

# 3. Add genTP helper to init
html = html.replace(
    'init(){',
    'genTP(p){if(!p._students||!p._students.length)return;p._students.forEach(s=>{s.tp=Math.floor(Math.random()*6)+1;});},\n  init(){'
)

# 4. Fix PDF: add activity descriptions + TP table  
# Add a.d description after the phase/duration line in PDF
pdf_act = 'page-break-inside:avoid;background:#FFF8F0;word-break:break-word;overflow-wrap:break-word"><p style="font-size:.75rem;font-weight:600;color:#8B5A2B;margin:0 0 4px 0">'
idx = html.find(pdf_act, html.find('ht(p){'))
if idx > 0:
    p_end = html.find('</p>', idx)
    desc_tag = '</p><p style="font-size:.7rem;color:#3A2A1A;margin:4px 0 0 0;line-height:1.6;word-break:break-word;overflow-wrap:break-word;white-space:pre-wrap">\' +e(a.d||"")+ \'</p>'
    html = html[:p_end+4] + desc_tag + html[p_end+4:]
    print('PDF activity descriptions fixed')

# Add TP table in PDF (before footer)
pdf_footer = "'+e(p.ref)+'</p></div>'+chr(39)+':'+chr(39)+')+chr(39)+chr(39)"
# Find the PDF closing and add TP
pdf_end = html.find("🇲🇾 Dijana oleh eRPH-PM")
if pdf_end > 0:
    before_footer = html.rfind("';", 0, pdf_end)
    tp_table_code = "'+(p._students&&p._students.length?'<div style=\"margin-top:.5rem;border-top:2px solid #C4956A;padding-top:.4rem\"><h2 style=\"font-size:.8rem;font-weight:700;color:#6366f1;margin-bottom:.3rem\">📊 Rekod Transit</h2><table style=\"width:100%;border-collapse:collapse;font-size:.7rem\"><thead><tr style=\"background:#eef2ff;border-bottom:2px solid #c7d2fe\"><th style=\"padding:3px 6px;text-align:left;color:#4338ca\">#</th><th style=\"padding:3px 6px;text-align:left;color:#4338ca\">Nama</th><th style=\"padding:3px 6px;text-align:center;color:#4338ca\">TP</th><th style=\"padding:3px 6px;text-align:left;color:#4338ca\">Catatan</th></tr></thead><tbody>'+p._students.map((s,i)=>'<tr style=\"border-bottom:1px solid #e2e8f0\"><td style=\"padding:2px 6px;color:#94a3b8\">'+(i+1)+'</td><td style=\"padding:2px 6px;font-weight:500;color:#334155\">'+e(s.n)+'</td><td style=\"padding:2px 6px;text-align:center\"><span style=\"display:inline-block;width:1.5rem;height:1.5rem;line-height:1.5rem;text-align:center;border-radius:9999px;font-size:.65rem;font-weight:700;background:'+(s.tp>=5?'#dcfce7':s.tp>=3?'#fef3c7':'#fee2e2')+';color:'+(s.tp>=5?'#166534':s.tp>=3?'#92400e':'#991b1b')+'\">'+s.tp+'</span></td><td style=\"padding:2px 6px;color:#78350f;font-size:.65rem\">'+e(s.c||'')+'</td></tr>').join('')+'</tbody></table></div>':'')+'"
    html = html[:before_footer] + tp_table_code + html[before_footer:]
    print('PDF TP table added')

with open('/home/home/Documents/New OpenCode Project/erph-pm/index.html', 'w') as f:
    f.write(html)

m = re.search(r'<script>([\s\S]*?)</script>', html)
if m:
    with open('/tmp/check.js', 'w') as f:
        f.write(m.group(1))
    import subprocess
    r = subprocess.run(['node', '--check', '/tmp/check.js'], capture_output=True, text=True)
    print('JS:', 'OK' if r.returncode == 0 else r.stderr[:200])

total = sum(len(v) for v in students.values())
print(f'Students: {total}')
