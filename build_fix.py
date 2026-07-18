#!/usr/bin/env python3
"""Fix PDF export, add back-to-top, add day dividers."""
import re

with open('/home/home/Documents/New OpenCode Project/erph-pm/index.html', 'r') as f:
    html = f.read()

# ════════════════════════════════════════════════════════
# FIX 1: PDF Export - make robust with retry + print fallback
# ════════════════════════════════════════════════════════

# Replace pdf1 function with more robust version
old_pdf1 = """  pdf1(p){
    if(typeof html2pdf!=='undefined'){
      const el=document.createElement('div');el.innerHTML=this.ht(p);
      html2pdf().set({margin:[0.4,0.4,0.4,0.4],filename:'RPH_'+p.s+'_'+p.c.replace(' ','')+'_'+p.d+'.pdf',image:{type:'jpeg',quality:0.98},html2canvas:{scale:2,useCORS:true},jsPDF:{unit:'in',format:'a4',orientation:'portrait'}}).from(el).save();
    }else{const w=window.open('','_blank');if(!w)return;w.document.write('<html><head><title>RPH</title></head><body>'+this.ht(p)+'<script>window.print()<'+'/script></body></html>');w.document.close();}
  },"""

new_pdf1 = """  pdf1(p){
    const html = this.ht(p);
    const doPrint = () => {
      const w = window.open('','_blank');
      if(!w){alert('Sila benarkan popup untuk PDF.');return;}
      w.document.write('<!DOCTYPE html><html><head><meta charset="UTF-8"><title>RPH - '+p.sn+'</title><style>body{font-family:sans-serif;padding:1.5cm;color:#3A2A1A;line-height:1.6}table{border-collapse:collapse;width:100%}td,th{padding:4px 6px;border:1px solid #ddd}@media print{body{padding:0}}h2{color:#1E3A5F;font-size:1rem;margin-top:.8rem}.act-box{border:1.5px solid #C4956A;border-radius:8px;padding:8px;margin-bottom:6px;background:#FFF8F0}.act-box p{margin:2px 0}.tp-badge{display:inline-block;width:1.5rem;height:1.5rem;line-height:1.5rem;text-align:center;border-radius:50%;font-size:.65rem;font-weight:700}</style></head><body>'+html+'<script>setTimeout(function(){window.print();window.close()},500)<'+'/script></body></html>');
      w.document.close();
    };
    if(typeof html2pdf !== 'undefined'){
      const el=document.createElement('div');el.innerHTML=html;
      html2pdf().set({margin:[0.4,0.4,0.4,0.4],filename:'RPH_'+p.s+'_'+p.c.replace(' ','')+'_'+p.d+'.pdf',image:{type:'jpeg',quality:0.98},html2canvas:{scale:2,useCORS:true,logging:false},jsPDF:{unit:'in',format:'a4',orientation:'portrait'}}).from(el).save().catch(function(){doPrint();});
    }else{doPrint();}
  },"""

html = html.replace(old_pdf1, new_pdf1)
print('pdf1 fixed')

# Replace pAll function
old_pall = """  pAll(){
    if(!this.rph.length)return;
    const ps=this.rph.map((p,i)=>'<div style="'+(i<this.rph.length-1?'page-break-after:always;':'')+'page-break-inside:avoid">'+this.ht(p)+'</div>').join('');
    if(typeof html2pdf!=='undefined'){
      const el=document.createElement('div');el.innerHTML=ps;
      html2pdf().set({margin:[0.4,0.4,0.4,0.4],filename:'eRPH_PM_All.pdf',image:{type:'jpeg',quality:0.98},html2canvas:{scale:2,useCORS:true},jsPDF:{unit:'in',format:'a4',orientation:'portrait'}}).from(el).save();
    }else{const w=window.open('','_blank');if(!w)return;w.document.write('<html><head><title>RPH All</title></head><body>'+ps+'<script>window.print()<'+'/script></body></html>');w.document.close();}
  },"""

new_pall = """  pAll(){
    if(!this.rph.length)return;
    const ps=this.rph.map((p,i)=>'<div style="'+(i<this.rph.length-1?'page-break-after:always;':'')+'page-break-inside:avoid">'+this.ht(p)+'</div>').join('');
    const doPrint = () => {
      const w = window.open('','_blank');
      if(!w){alert('Sila benarkan popup untuk PDF Semua.');return;}
      w.document.write('<!DOCTYPE html><html><head><meta charset="UTF-8"><title>eRPH-PM All</title><style>body{font-family:sans-serif;padding:1.5cm;color:#3A2A1A;line-height:1.6}table{border-collapse:collapse;width:100%}td,th{padding:4px 6px;border:1px solid #ddd}.act-box{border:1.5px solid #C4956A;border-radius:8px;padding:8px;margin-bottom:6px;background:#FFF8F0}h2{color:#1E3A5F;font-size:1rem;margin-top:.8rem}.tp-badge{display:inline-block;width:1.5rem;height:1.5rem;line-height:1.5rem;text-align:center;border-radius:50%;font-size:.65rem;font-weight:700}@media print{body{padding:0}div[style*="page-break-after:always"]{page-break-after:always}}</style></head><body>'+ps+'<script>setTimeout(function(){window.print();window.close()},500)<'+'/script></body></html>');
      w.document.close();
    };
    if(typeof html2pdf !== 'undefined'){
      const el=document.createElement('div');el.innerHTML=ps;
      html2pdf().set({margin:[0.4,0.4,0.4,0.4],filename:'eRPH_PM_All.pdf',image:{type:'jpeg',quality:0.98},html2canvas:{scale:2,useCORS:true,logging:false},jsPDF:{unit:'in',format:'a4',orientation:'portrait'}}).from(el).save().catch(function(){doPrint();});
    }else{doPrint();}
  },"""

html = html.replace(old_pall, new_pall)
print('pAll fixed')

# ════════════════════════════════════════════════════════
# FIX 2: Back to top button
# ════════════════════════════════════════════════════════
# Add CSS for back-to-top
html = html.replace(
    '/* ── Standardized Theme ── */',
    '''/* ── Back to Top ── */
.back-to-top{position:fixed;bottom:1.5rem;right:1.5rem;z-index:9999;width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,#C4956A,#8B5A2B);color:#fff;border:none;font-size:1.2rem;cursor:pointer;box-shadow:0 2px 12px rgba(196,149,106,0.3);transition:all .2s;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none}
.back-to-top.show{opacity:1;pointer-events:auto}
.back-to-top:hover{transform:scale(1.1);box-shadow:0 4px 20px rgba(196,149,106,0.4)}
/* ── Standardized Theme ── */'''
)

# Add button HTML after body tag
html = html.replace(
    '<main class="flex-1 overflow-y-auto p-2 md:p-4">',
    '''<button onclick="window.scrollTo({top:0,behavior:'smooth'})" class="back-to-top" id="backToTop">↑</button>
  <script>
    window.addEventListener('scroll',function(){var b=document.getElementById('backToTop');if(b){if(window.scrollY>300)b.classList.add('show');else b.classList.remove('show');}});
  </script>
  <main class="flex-1 overflow-y-auto p-2 md:p-4">'''
)
print('Back-to-top added')

# ════════════════════════════════════════════════════════
# FIX 3: Day dividers in RPH list
# ════════════════════════════════════════════════════════
# Add CSS for day dividers
html = html.replace(
    '.cc-act-textarea{word-break:break-word;overflow-wrap:break-word;white-space:pre-wrap;hyphens:auto;width:100%;max-width:100%;line-height:1.6;font-size:.7rem}',
    '''.cc-act-textarea{word-break:break-word;overflow-wrap:break-word;white-space:pre-wrap;hyphens:auto;width:100%;max-width:100%;line-height:1.6;font-size:.7rem}
.day-divider{display:flex;align-items:center;gap:.5rem;padding:.5rem .75rem;border-radius:.75rem;font-size:.85rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin:1rem 0 .5rem;box-shadow:0 1px 3px rgba(0,0,0,0.06)}
.day-divider span:last-child{font-size:.65rem;font-weight:400;opacity:.7}'''
)

# Find the RPH list and add day divider logic before each plan
# The rph list renders: <template x-for="(p,i) in rph" :key="p.id">
# We need to add a divider when the day changes

# Add a computed property to get unique days and add dividers
# We'll modify the rendering to check for day changes
old_rph_list = '''<template x-if="rph.length"><div class="space-y-4"><template x-for="(p,i) in rph" :key="p.id"><div class="rounded-xl border border-[#C4956A]/20 bg-white shadow-sm">'''

# Inject day divider logic
day_emojis = {'Isnin':'🌙','Selasa':'🔥','Rabu':'💡','Khamis':'⭐','Jumaat':'🌙'}
day_colors = {'Isnin':'border-l-4 border-l-blue-400 bg-blue-50 text-blue-800','Selasa':'border-l-4 border-l-orange-400 bg-orange-50 text-orange-800','Rabu':'border-l-4 border-l-green-400 bg-green-50 text-green-800','Khamis':'border-l-4 border-l-purple-400 bg-purple-50 text-purple-800','Jumaat':'border-l-4 border-l-rose-400 bg-rose-50 text-rose-800'}
day_names = {'Isnin':'Isnin - Monday','Selasa':'Selasa - Tuesday','Rabu':'Rabu - Wednesday','Khamis':'Khamis - Thursday','Jumaat':'Jumaat - Friday'}

# Build the divider HTML
divider_html = '''<template x-if="rph.length"><div class="space-y-4"><template x-for="(p,i) in rph" :key="p.id">
<template x-if="i===0||rph[i-1].d!==p.d"><div class="day-divider ''' + 'border-l-4' + '''" 
  :style="'border-left-color:'+({Isnin:'#60a5fa',Selasa:'#fb923c',Rabu:'#4ade80',Khamis:'#a78bfa',Jumaat:'#fb7185'})[p.d]+';background:'+({Isnin:'#eff6ff',Selasa:'#fff7ed',Rabu:'#f0fdf4',Khamis:'#faf5ff',Jumaat:'#fff1f2'})[p.d]">
  <span x-text="({Isnin:'🌙',Selasa:'🔥',Rabu:'💡',Khamis:'⭐',Jumaat:'🌙'})[p.d]||'📅'"></span>
  <span x-text="({Isnin:'Isnin',Selasa:'Selasa',Rabu:'Rabu',Khamis:'Khamis',Jumaat:'Jumaat'})[p.d]||p.d"></span>
  <span class="text-[10px] opacity-60 ml-auto" x-text="p.d"></span>
</div></template>
'''

html = html.replace(old_rph_list, divider_html)
print('Day dividers added')

# Also fix the day name display in the divider - the x-text for day name
# Add the day name mapping inline

# Verify
import subprocess
m = re.search(r'<script>([\s\S]*?)</script>', html)
if m:
    with open('/tmp/check.js', 'w') as f:
        f.write(m.group(1))
    r = subprocess.run(['node', '--check', '/tmp/check.js'], capture_output=True, text=True)
    print('JS:', 'OK' if r.returncode == 0 else r.stderr[:200])

print(f'Size: {len(html)} bytes')
print(f'Back-to-top: {"backToTop" in html}')
print(f'Day dividers: {"day-divider" in html}')

with open('/home/home/Documents/New OpenCode Project/erph-pm/index.html', 'w') as f:
    f.write(html)
