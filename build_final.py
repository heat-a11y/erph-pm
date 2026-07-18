#!/usr/bin/env python3
"""Build final eRPH-PM with all features + databases."""
import json, re

BASE = '/tmp/v4_base.html'
OUT = '/home/home/Documents/New OpenCode Project/erph-pm/index.html'

with open(BASE, 'r') as f:
    html = f.read()

# Remove any existing REF/REM const declarations
html = re.sub(r'\nconst REF\s*=\s*\{.*?\};', '\n', html, flags=re.DOTALL)
html = re.sub(r'\nconst REM\s*=\s*\[.*?\];', '\n', html, flags=re.DOTALL)

# Build databases
REF = {'bm':['Seramai 12 orang murid dapat menguasai objektif pembelajaran pada hari ini.','Objektif PdP tercapai. Murid dapat menyelesaikan tugasan yang diberikan dengan baik.','15 daripada 18 orang murid mencapai objektif pembelajaran.','Penguasaan murid pada hari ini adalah memuaskan.','Majoriti murid dapat menguasai standard pembelajaran.','Objektif PdP tercapai sepenuhnya.','PdP berjalan lancar. Murid dapat mengaitkan pembelajaran dengan kehidupan harian.','Semua murid mencapai objektif minimum yang ditetapkan.','Objektif PdP tercapai. Murid berjaya menyelesaikan tugasan berkumpulan.','Penguasaan murid sangat memuaskan.','Objektif tercapai. Murid dapat mengaplikasikan pengetahuan dalam situasi baru.','Seramai 10 orang murid mencapai tahap penguasaan 4 dan ke atas.','PdP berjalan dengan lancar.','Murid dapat bekerjasama dalam kumpulan.','Murid menunjukkan minat yang tinggi.','PdP hari ini berjalan lancar. 80% murid mencapai objektif.','Aktiviti pembelajaran yang pelbagai membantu mengekalkan minat murid.','Objektif PdP tercapai.','PdP berjalan dengan baik.','Seramai 14 orang murid mencapai objektif.','Objektif PdP tercapai keseluruhannya.','Murid sangat bersemangat semasa aktiviti kumpulan.','PdP berjalan seperti yang dirancang.','Majoriti murid mencapai objektif.','PdP berjalan lancar. Murid dapat mengenal pasti konsep utama.','Objektif PdP tercapai dengan baik.','Murid dapat menguasai standard pembelajaran yang ditetapkan.','PdP hari ini sangat menyeronokkan.','Objektif PdP tercapai. Murid menunjukkan peningkatan.','Keseluruhan PdP berjalan dengan jayanya.','PdP hari ini berjaya menarik minat murid.','Objektif pembelajaran tercapai.','Murid dapat menguasai kemahiran yang diajar.','PdP berjalan lancar. Murid aktif bertanya.','Objektif PdP tercapai sepenuhnya.','Seramai 16 orang murid mencapai objektif.','Murid dapat mengaplikasikan pengetahuan.','PdP hari ini berjaya meningkatkan kemahiran berfikir kritis.','Objektif PdP tercapai. Penggunaan BBM yang kreatif.','Majoriti murid dapat menyelesaikan tugasan.','PdP berjalan lancar dengan penglibatan aktif.','Murid dapat menguasai kemahiran bertutur dengan yakin.','Murid menunjukkan sikap positif.','PdP hari ini berjaya mencapai objektif.','Objektif PdP tercapai. Murid dapat mengenal pasti konsep.','Murid seronok dengan aktiviti yang disediakan.','PdP berjalan lancar mengikut perancangan.','Objektif PdP tercapai. Murid dapat menjawab soalan.','Majoriti murid menunjukkan perkembangan positif.','PdP hari ini sangat memberangsangkan.'],
'en':['12 pupils achieved the objectives today. 3 need additional guidance.','Learning objectives achieved. Pupils completed tasks well.','15 out of 18 pupils achieved the learning objectives.','Pupil mastery today was satisfactory.','The majority of pupils mastered the learning standards.','Learning objectives fully achieved.','The lesson went well. Pupils related learning to daily life.','All pupils achieved the minimum objectives.','Learning objectives achieved. Pupils completed group tasks excellently.','Pupil mastery was very satisfactory.','Objectives achieved. Pupils applied knowledge in new situations.','10 pupils achieved mastery level 4 and above.','The lesson went smoothly.','Learning objectives achieved. Pupils cooperated in groups.','Pupils showed high interest in the topic.','80% of pupils achieved the objectives.','Varied learning activities maintained pupil interest.','Objectives achieved. Pupils mastered the skills taught.','The lesson went well. Pupils paid attention.','14 pupils achieved the objectives.','Learning objectives largely achieved.','Pupils were very enthusiastic during group activities.','The lesson proceeded as planned.','Objectives achieved. Pupils answered questions correctly.','Majority of pupils achieved objectives.','The lesson went well. Pupils identified key concepts.','Learning objectives achieved well.','Pupils mastered the prescribed learning standards.','Today\'s lesson was very enjoyable.','Objectives achieved. Pupils showed improvement.','The overall lesson was successful.','Today\'s lesson engaged pupils through interactive activities.','Learning objectives achieved through technology integration.','Pupils mastered the skills taught with guidance.','The lesson went smoothly. Pupils asked questions.','Learning objectives fully achieved. Pupil presentations showed effort.','16 pupils achieved the objectives. 2 need attention.','Pupils applied knowledge in new situations.','Today\'s lesson improved critical thinking skills.','Objectives achieved. Creative use of teaching aids.','Majority of pupils completed the given tasks.','The lesson proceeded with active participation.','Pupils mastered speaking skills confidently.','Pupils showed positive attitudes.','Today\'s lesson achieved the set objectives.','Pupils enjoyed the activities provided.','The lesson proceeded according to plan.','Objectives achieved. Pupils answered correctly.','Majority of pupils showed positive development.','Today\'s lesson was very encouraging.'],
'zh':['今天有12名学生达到了学习目标。3名学生需要额外指导。','教学目标达成。学生能够很好地完成分配的任务。','15名/18名学生达到了学习目标。','今天学生的掌握程度令人满意。','大多数学生掌握了学习标准。','教学目标完全达成。','教学顺利。学生能够将学习与日常生活联系起来。','所有学生都达到了最低目标。','教学目标达成。学生出色地完成了小组任务。','学生的掌握程度非常令人满意。','目标达成。学生能够在新情况下应用知识。','10名学生达到掌握水平4及以上。','教学顺利。','教学目标达成。学生在小组中合作并完成了任务。','学生对所教主题表现出很高的兴趣。','80%的学生达到了目标。','多样化的学习活动保持了学生的兴趣。','目标达成。学生掌握了所教的技能。','教学顺利。学生全程专心听讲。','14名学生达到了目标。','教学目标大体达成。','学生在小组活动中非常积极。','教学按计划进行。','目标达成。学生正确回答了问题。','大多数学生达到了目标。','教学顺利。学生能够识别和理解关键概念。','教学目标很好地达成。','学生掌握了规定的学习标准。','今天的课非常有趣。学生在玩中学。','目标达成。学生显示出进步。','整体教学成功。','今天的课通过互动活动成功吸引了学生。','教学目标达成。科技融入教学提高了参与度。','学生在教师指导下掌握了所教的技能。','教学顺利。学生积极提问。','教学目标完全达成。学生的呈现展示出努力。','16名学生达到了目标。2名学生需要特别关注。','学生能够在新情况下应用知识。','今天的课成功提高了批判性思维能力。','目标达成。教具的创造性使用吸引了兴趣。','大多数学生完成了分配的任务。','教学顺利进行，学生积极参与。','目标达成。学生自信地掌握了口语技能。','学生表现出积极的态度和兴趣。','今天的课成功达到了设定的目标。','学生喜欢所提供的活动。','教学按计划进行。','目标达成。学生正确回答了问题。','大多数学生显示出积极的发展。','今天的课非常令人鼓舞。']}
REM = [{'t':'🧑‍🏫 Bimbingan Individu','d':'Bimbingan langkah-demi-langkah.','st':['Bimbingan','Ulang']},{'t':'📝 Latihan Berstruktur','d':'Lembaran dipermudah.','st':['Latihan','Contoh']},{'t':'👀 Tunjuk Cara','d':'Demonstrasi perlahan.','st':['Demo','Ulang']},{'t':'📊 Bahan Visual','d':'Gambar rajah, carta.','st':['Visual','Peta']},{'t':'✏️ Pengukuhan','d':'Latihan mudah.','st':['Latih','Yakin']},{'t':'🤝 Berpasangan','d':'Cemerlang + pemulihan.','st':['Rakan','Bantu']},{'t':'🎲 Permainan','d':'Papan/digital.','st':['Main','Motivasi']},{'t':'🃏 Kad Imbasan','d':'Kad ingatan.','st':['Ulang','Visual']},{'t':'🎵 Nyanyian','d':'Lagu gerakan.','st':['Muzik','Gerak']},{'t':'🗺️ Peta Konsep','d':'Peta bergambar.','st':['Visual','Peta']},{'t':'📖 Bacaan Bergilir','d':'Baca bersama.','st':['Baca','Bimbing']},{'t':'🔤 Dialog Strip','d':'Susun dialog.','st':['Susun','Urut']},{'t':'📄 Cloze Gambar','d':'Teks cloze gambar.','st':['Cloze','Visual']},{'t':'🔍 Error Hunt','d':'Cari kesalahan.','st':['Cari','Betul']},{'t':'📝 Mini Whiteboard','d':'Papan mini tulis.','st':['Tulis','Cepat']},{'t':'🏃 Hopscotch','d':'Grid lompat sebut.','st':['Gerak','Sebut']},{'t':'📑 Word Family','d':'Keluarga kata.','st':['Kelaskan','Rakan']},{'t':'📦 Realia','d':'Objek sebenar.','st':['Objek','Sebut']},{'t':'⚽ Question Pass','d':'Bola jawab.','st':['Bual','Main']},{'t':'🖼️ Talk Picture','d':'Gambar ayat.','st':['Visual','Pasang']},{'t':'✏️ Menulis','d':'Titik panduan.','st':['Tulis','Pandu']},{'t':'🧮 Pengiraan','d':'Blok kira.','st':['Kira','Konkrit']},{'t':'📏 Garis Nombor','d':'Garis tambah.','st':['Visual','Nombor']},{'t':'🧠 Memori','d':'Kad padan.','st':['Ingat','Padan']},{'t':'📒 Buku Skrap','d':'Kumpul kerja.','st':['Kumpul','Motivasi']},{'t':'✂️ Potong Tampal','d':'Potong gam.','st':['Kreatif','Tampal']},{'t':'💬 Soalan Lisan','d':'Soalan tanpa tekanan.','st':['Lisan','Bimbing']},{'t':'💻 Digital','d':'Quizizz/Forms.','st':['Digital','Klik']},{'t':'📓 Jurnal','d':'Tulis belajar.','st':['Tulis','Refleksi']},{'t':'🎪 Stesen','d':'Stesen khas.','st':['Kecil','Bimbing']},{'t':'🎯 Sasaran Kata','d':'Bola sasaran.','st':['Main','Sebut']},{'t':'🧩 Puzzle','d':'Puzzle gambar.','st':['Puzzle','Fikir']},{'t':'🎤 Karaoke','d':'Nyanyi lirik.','st':['Muzik','Ulang']},{'t':'📋 Checklist','d':'Semak sendiri.','st':['Semak','Diri']},{'t':'🎭 Main Peranan','d':'Lakonan situasi.','st':['Lakon','Sosial']},{'t':'🔢 Kad Nombor','d':'Kad nilai.','st':['Visual','Nombor']},{'t':'📖 Baca Bergambar','d':'Buku cerita.','st':['Baca','Visual']},{'t':'🎲 Dadu Kata','d':'Dadu sebut.','st':['Main','Sebut']},{'t':'📝 Imbuhan','d':'Latihan imbuhan.','st':['Tatabahasa','Tulis']},{'t':'🧑‍🤝‍🧑 Fokus','d':'Kumpulan intensif.','st':['Kecil','Fokus']},{'t':'🎯 Papan Ejaan','d':'Permainan eja.','st':['Eja','Main']},{'t':'📸 Fotografi','d':'Gambar label.','st':['Kreatif','Visual']},{'t':'🎬 Video','d':'Tonton jawab.','st':['Visual','Dengar']},{'t':'🧩 Silang Kata','d':'Silang gambar.','st':['Fikir','Kosa']},{'t':'📑 Kad Tugasan','d':'Arahan hari.','st':['Rutin','Bimbing']},{'t':'🎤 Bacaan Berirama','d':'Baca irama.','st':['Baca','Irama']},{'t':'🎨 Mewarna','d':'Mewarna konsep.','st':['Warna','Visual']},{'t':'📋 Panduan Mini','d':'Buku panduan.','st':['Buat','Rujuk']},{'t':'🤖 Gamifikasi','d':'Lencana motivasi.','st':['Main','Motivasi']},{'t':'📞 Telefon Bual','d':'Cawan kertas.','st':['Bual','Dengar']}]

ref_js = json.dumps(REF, ensure_ascii=False)
rem_js = json.dumps(REM, ensure_ascii=False)

# Inject REF/REM as const before Alpine init  
html = html.replace("document.addEventListener('alpine:init", f"const REF = {ref_js};\nconst REM = {rem_js};\n\ndocument.addEventListener('alpine:init")

# Reference REF/REM in Alpine data
html = html.replace('REF: {},', 'REF: REF,\n  REM: REM,')

# Fix ref1 to use per-language REF
html = html.replace(
    "ref1(p){const refs=this.REF[p.s]||[];if(refs.length)p.ref=refs[Math.floor(Math.random()*refs.length)];}",
    "ref1(p){const l=this.lg(p.s);const refs=REF[l]||REF['bm']||[];if(refs.length)p.ref=refs[Math.floor(Math.random()*refs.length)];}"
)

# Add lg(s,t) with teacher check if missing
if 'lg(s){' not in html and 'lg(s,t){' not in html:
    html = html.replace(
        "tN(){const t=this.TEACHERS[this.tg];return t?t.n+' ('+this.tg+')':'';},",
        "tN(){const t=this.TEACHERS[this.tg];return t?t.n+' ('+this.tg+')':'';},\n  lg(s,t){if(t&&(t==='ARMAN'||t==='BALKIS'))return'bm';const m={BM:'bm',BI:'en'};return m[s]||'zh';},"
    )
# Also update ref1 to pass teacher code
html = html.replace(
    "ref1(p){const l=this.lg(p.s);const refs=REF[l]||REF['bm']||[];if(refs.length)p.ref=refs[Math.floor(Math.random()*refs.length)];}",
    "ref1(p){const l=this.lg(p.s,this.tg);const refs=REF[l]||REF['bm']||[];if(refs.length)p.ref=refs[Math.floor(Math.random()*refs.length)];}"
)

# Add curriculum-db script
if 'curriculum-db.js' not in html:
    html = html.replace('</head>', '<script src="curriculum-db.js"></script>\n</head>')

# Add D getter
if 'get D(){return this}' not in html:
    html = html.replace("init(){", "get D(){return this;},\n  init(){")

# Add TAKWIM to data
if 'TAKWIM: TAKWIM' not in html:
    html = html.replace(
        "tabs:[{i:'📅',l:'Jadual',id:'tt'}",
        "TAKWIM: TAKWIM,\n  tabs:[{i:'📅',l:'Jadual',id:'tt'}"
    )

with open(OUT, 'w') as f:
    f.write(html)

m = re.search(r'<script>([\s\S]*?)</script>', html)
if m:
    with open('/tmp/check.js', 'w') as f:
        f.write(m.group(1))
    import subprocess
    r = subprocess.run(['node', '--check', '/tmp/check.js'], capture_output=True, text=True)
    print('JS:', 'OK' if r.returncode == 0 else r.stderr[:200])

print(f'Size: {len(html)} bytes')
print(f'Theme: {"C4956A" in html}')
print(f'Emojis: {"📅" in html}')
print(f'Blink: {"btn-jana" in html}')
print(f'REF: {len(json.dumps(REF))}b')
print(f'REM: {len(json.dumps(REM))}b')
print(f'lg(): {"lg(s)" in html}')
print(f'curriculum: {"curriculum-db.js" in html}')
print(f'D getter: {"get D()" in html}')
