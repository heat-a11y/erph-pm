#!/usr/bin/env python3
"""Final rebuild: take working HTML, inject full databases + SLOTS."""
import json, re

SRC = '/home/home/Documents/New OpenCode Project/erph-pm/index.html'
OUT = '/home/home/Documents/New OpenCode Project/erph-pm/index.html'

with open(SRC, 'r') as f:
    html = f.read()

# ─── FULL SLOTS DATA (186 entries from original timetable-data.js) ───
with open('/home/home/Documents/New OpenCode Project/erph-pm/timetable-data.js', 'r') as f:
    tt = f.read()

# Extract TEACHER_SLOTS_P1 data  
slots = {}
for code in ['TBS','LET','HLF','LJX','LSW','WKS','LYY','OWY','ARMAN','COW','BALKIS','YH']:
    pattern = rf'TEACHER_SLOTS_P1\["{code}"\]\s*=\s*(\[.*?\]);'
    m = re.search(pattern, tt, re.DOTALL)
    if m:
        arr_str = m.group(1)
        # Fix unquoted keys for JSON parsing
        arr_str = re.sub(r'(\{)\s*(\w+)(\s*:)', r'\1"\2"\3', arr_str)
        arr_str = re.sub(r'(,\s*)(\w+)(\s*:)', r'\1"\2"\3', arr_str)
        arr = json.loads(arr_str)
        # Convert {class:...,day:...,period:...,subject:...,subjectName:...} -> {c:...,d:...,p:...,s:...,n:...}
        converted = []
        for item in arr:
            # Map subject names
            sn = item.get('subjectName','')
            converted.append({
                'c': item.get('class',''),
                'd': item.get('day',''),
                'p': item.get('period',''),
                's': item.get('subject',''),
                'n': sn
            })
        slots[code] = converted

total_slots = sum(len(v) for v in slots.values())
print(f'SLOTS: {len(slots)} teachers, {total_slots} entries')

# ─── FULL REF DATA (50 per language) ───
REF = {'bm':[f"Refleksi BM {i}: Murid dapat menguasai objektif pembelajaran." for i in range(50)],'en':[f"Reflection EN {i}: Pupils achieved the learning objectives." for i in range(50)],'zh':[f"反思 ZH {i}: 学生达到了学习目标。" for i in range(50)]}
# Actually use real reflections
REF = json.loads(open('/dev/stdin').read()) if False else json.loads('{}')
# Build proper reflections
bm_refs = ['Seramai 12 orang murid dapat menguasai objektif pembelajaran pada hari ini.','Objektif PdP tercapai. Murid dapat menyelesaikan tugasan yang diberikan dengan baik.','15 daripada 18 orang murid mencapai objektif pembelajaran.','Penguasaan murid pada hari ini adalah memuaskan. PdP berjalan seperti yang dirancang.','Majoriti murid dapat menguasai standard pembelajaran. Beberapa orang murid masih perlukan latihan tambahan.','Objektif PdP tercapai sepenuhnya. Murid aktif dalam perbincangan dan memberikan idea yang bernas.','PdP berjalan lancar. Murid dapat mengaitkan pembelajaran dengan kehidupan harian.','Semua murid mencapai objektif minimum yang ditetapkan.','Objektif PdP tercapai. Murid berjaya menyelesaikan tugasan berkumpulan dengan cemerlang.','Penguasaan murid sangat memuaskan. PdP berjalan mengikut perancangan.','Objektif tercapai. Murid dapat mengaplikasikan pengetahuan dalam situasi baru.','Seramai 10 orang murid mencapai tahap penguasaan 4 dan ke atas.','PdP berjalan dengan lancar. Murid seronok dengan aktiviti yang disediakan.','Murid dapat bekerjasama dalam kumpulan dan menyelesaikan tugasan yang diberikan.','Murid menunjukkan minat yang tinggi terhadap topik yang diajar.','PdP hari ini berjalan lancar. 80% murid mencapai objektif.','Aktiviti pembelajaran yang pelbagai membantu mengekalkan minat murid.','Objektif PdP tercapai. Murid dapat menguasai kemahiran yang diajar.','PdP berjalan dengan baik. Murid memberi tumpuan sepanjang sesi.','Seramai 14 orang murid mencapai objektif. Empat orang murid masih dalam proses pemulihan.','Objektif PdP tercapai keseluruhannya. Penggunaan BBM yang pelbagai meningkatkan kefahaman.','Murid sangat bersemangat semasa aktiviti kumpulan.','PdP berjalan seperti yang dirancang. Murid memahami konsep yang diajar.','Majoriti murid mencapai objektif. Beberapa murid masih lemah dalam kemahiran membaca.','PdP berjalan lancar. Murid dapat mengenal pasti dan memahami konsep utama.','Objektif PdP tercapai dengan baik. Murid menunjukkan sikap positif terhadap pembelajaran.','Murid dapat menguasai standard pembelajaran yang ditetapkan.','PdP hari ini sangat menyeronokkan. Murid belajar sambil bermain melalui aktiviti yang menarik.','Objektif PdP tercapai. Murid menunjukkan peningkatan dari segi kefahaman.','Keseluruhan PdP berjalan dengan jayanya. Murid mencapai objektif yang ditetapkan.','PdP hari ini berjaya menarik minat murid melalui aktiviti yang interaktif.','Objektif pembelajaran tercapai. Penggunaan teknologi dalam PdP meningkatkan penglibatan murid.','Murid dapat menguasai kemahiran yang diajar dengan bimbingan guru.','PdP berjalan lancar. Murid aktif bertanya dan memberi respons.','Objektif PdP tercapai sepenuhnya. Pembentangan hasil kerja murid menunjukkan usaha yang baik.','Seramai 16 orang murid mencapai objektif. Dua orang murid memerlukan perhatian khusus.','Murid dapat mengaplikasikan pengetahuan dalam situasi baru.','PdP hari ini berjaya meningkatkan kemahiran berfikir kritis murid.','Objektif PdP tercapai. Penggunaan BBM yang kreatif menarik minat murid.','Majoriti murid dapat menyelesaikan tugasan yang diberikan.','PdP berjalan lancar dengan penglibatan aktif daripada murid.','Objektif PdP tercapai. Murid dapat menguasai kemahiran bertutur dengan yakin.','Murid menunjukkan sikap positif dan minat yang tinggi.','PdP hari ini berjaya mencapai objektif yang ditetapkan.','Objektif PdP tercapai. Murid dapat mengenal pasti dan memahami konsep yang diajar.','Murid seronok dengan aktiviti yang disediakan.','PdP berjalan lancar mengikut perancangan. Murid dapat menguasai kemahiran yang diajar.','Objektif PdP tercapai. Murid dapat menjawab soalan dengan betul.','Majoriti murid menunjukkan perkembangan positif. Beberapa murid masih perlu bimbingan.','PdP hari ini sangat memberangsangkan. Murid dapat menguasai objektif pembelajaran dengan cemerlang.']
en_refs = ['12 pupils achieved the learning objectives today. 3 pupils need additional guidance.','Learning objectives achieved. Pupils completed the given tasks well.','15 out of 18 pupils achieved the learning objectives.','Pupil mastery today was satisfactory. The lesson proceeded as planned.','The majority of pupils mastered the learning standards. A few pupils still need additional practice.','Learning objectives fully achieved. Pupils were active in discussions.','The lesson went well. Pupils could relate learning to daily life.','All pupils achieved the minimum objectives. 21st century learning was applied in activities.','Learning objectives achieved. Pupils completed group tasks excellently.','Pupil mastery was very satisfactory. The lesson followed the plan well.','Objectives achieved. Pupils could apply knowledge in new situations.','10 pupils achieved mastery level 4 and above. 5 pupils are still at level 3.','The lesson went smoothly. Pupils enjoyed the activities provided.','Learning objectives achieved. Pupils cooperated in groups and completed given tasks.','Pupils showed high interest in the topic taught. They actively asked questions.','80% of pupils achieved the objectives. Additional guidance given to weak pupils.','Varied learning activities maintained pupil interest throughout the lesson.','Objectives achieved. Pupils mastered the skills taught. Group activities fostered cooperation.','The lesson went well. Pupils paid attention throughout the session.','14 pupils achieved the objectives. 4 pupils are still in the remedial process.','Learning objectives largely achieved. Pupils completed tasks within the given time.','Pupils were very enthusiastic during group activities.','The lesson proceeded as planned. Pupils understood the concepts taught.','Objectives achieved. Pupils answered questions correctly. Varied learning activities maintained interest.','Majority of pupils achieved objectives. A few pupils still weak in reading and writing skills.','The lesson went well. Pupils could identify and understand key concepts.','Learning objectives achieved well. Pupils showed positive attitudes towards learning.','Pupils mastered the prescribed learning standards. The lesson went smoothly.','Today\'s lesson was very enjoyable. Pupils learned through play.','Objectives achieved. Pupils showed improvement in understanding. Continuous guidance needed.','The overall lesson was successful. Pupils achieved the set objectives.','Today\'s lesson successfully engaged pupils through interactive activities.','Learning objectives achieved. Technology integration in T&L increased pupil engagement.','Pupils mastered the skills taught with teacher guidance. Reinforcement exercises given.','The lesson went smoothly. Pupils actively asked questions and gave responses.','Learning objectives fully achieved. Pupil presentations showed great effort.','16 pupils achieved the objectives. 2 pupils need special attention.','Pupils could apply knowledge in new situations. A contextual approach helped.','Today\'s lesson successfully improved pupils\' critical thinking skills.','Objectives achieved. Creative use of teaching aids attracted pupil interest.','Majority of pupils completed the given tasks. A few need additional guidance.','The lesson proceeded with active pupil participation. Group activities encouraged cooperation.','Objectives achieved. Pupils mastered speaking skills confidently. Role-play activities helped.','Pupils showed positive attitudes and high interest. Formative assessment shows positive development.','Today\'s lesson successfully achieved the set objectives.','Pupils enjoyed the activities provided. They could learn in a fun atmosphere.','The lesson proceeded according to plan. Pupils mastered the skills taught.','Objectives achieved. Pupils answered questions correctly. Enrichment activities were provided.','Majority of pupils showed positive development. A few still need guidance.','Today\'s lesson was very encouraging. Pupils mastered learning objectives excellently.']
zh_refs = ['今天有12名学生达到了学习目标。3名学生需要额外指导。','教学目标达成。学生能够很好地完成分配的任务。','15名/18名学生达到了学习目标。3名学生需要进行补救活动。','今天学生的掌握程度令人满意。教学按计划进行。','大多数学生掌握了学习标准。少数学生还需要额外的练习。','教学目标完全达成。学生在讨论中很活跃。形成性评估显示出积极进展。','教学顺利。学生能够将学习与日常生活联系起来。','所有学生都达到了最低目标。活动中应用了21世纪学习技能。','教学目标达成。学生出色地完成了小组任务。活动中融入了高层次思维技能。','学生的掌握程度非常令人满意。教学按计划顺利进行。','目标达成。学生能够在新情况下应用知识。布置了巩固练习作为家庭作业。','10名学生达到掌握水平4及以上。5名学生仍在水平3。下次课将进行补救活动。','教学顺利。学生喜欢所提供的活动。多样化的教具有助于提高理解。','教学目标达成。学生在小组中合作并完成了分配的任务。同伴评估进行得很好。','学生对所教主题表现出很高的兴趣。他们积极提问和发表意见。','80%的学生达到了目标。对弱生给予了额外指导。对优生给予了充实活动。','多样化的学习活动保持了学生的兴趣。教学按计划进行，学生配合良好。','目标达成。学生掌握了所教的技能。小组活动培养了合作精神。','教学顺利。学生全程专心听讲。口头问题回答正确。书面练习显示出进步。','14名学生达到了目标。4名学生仍在补救过程中。分层学习活动满足了学生的需求。','教学目标大体达成。学生在规定时间内完成了任务。多样化教具的使用提高了理解力。','学生在小组活动中非常积极。他们很好地完成了任务。呈现展示出很大的努力。','教学按计划进行。学生理解了所教的概念。进行了巩固练习以加强理解。','目标达成。学生正确回答了问题。多样化的学习活动保持了学生的兴趣。','大多数学生达到了目标。少数学生在阅读和写作方面仍然薄弱。将进行特别干预。','教学顺利。学生能够识别和理解关键概念。动手活动大大帮助了弱生理解主题。','教学目标很好地达成。学生对学习表现出积极的态度。他们在小组中合作并互相帮助。','学生掌握了规定的学习标准。教学顺利。根据学生的需要进行了充实和补救活动。','今天的课非常有趣。学生在玩中学。通过有趣的活动，他们更容易记住所教的概念。','目标达成。学生在理解方面显示出进步。补救学生需要持续的指导。','整体教学成功。学生达到了设定的目标。多样化的活动满足了学生不同的学习需求。','今天的课通过互动活动成功吸引了学生。他们在各自的小组中合作良好。','教学目标达成。科技融入教学提高了学生的参与度。学生喜欢有趣的学习方式。','学生在教师指导下掌握了所教的技能。将进行巩固练习以加强理解。','教学顺利。学生积极提问并做出回应。通过游戏学习的方法非常合适。','教学目标完全达成。学生的呈现展示出很大的努力。持续进行形成性评估。','16名学生达到了目标。2名学生需要特别关注。将进行个别补救活动。','学生能够在新情况下应用知识。情境教学法帮助学生更深入地理解主题。','今天的课成功提高了学生的批判性思维能力。他们能创造性地解决问题。','目标达成。教具的创造性使用吸引了学生的兴趣。他们通过视觉更容易理解抽象概念。','大多数学生完成了分配的任务。少数学生在写作技能方面需要额外指导。','教学顺利进行，学生积极参与。小组活动鼓励了学生之间的合作与沟通。','目标达成。学生自信地掌握了口语技能。角色扮演活动非常有帮助。','学生表现出积极的态度和高度的兴趣。教学顺利。形成性评估显示出积极的发展。','今天的课成功达到了设定的目标。学生能够在小组和个别工作中都表现良好。','学生喜欢所提供的活动。他们能在有趣和吸引人的氛围中学习。','教学按计划进行。学生掌握了所教的技能。学生的反思显示出良好的理解。','目标达成。学生正确回答了问题。根据需要进行充实和补救活动。','大多数学生显示出积极的发展。少数仍需要指导。下节课将重点进行补救工作。','今天的课非常令人鼓舞。学生出色地掌握了学习目标。多样化的活动帮助了学习过程。']

ref_data = {'bm': bm_refs, 'en': en_refs, 'zh': zh_refs}
ref_js = json.dumps(ref_data, ensure_ascii=False)

# ─── FULL REM DATA (50 entries) ───
rem_data = []
for i in range(50):
    rem_data.append({'t': f'Activity {i+1}', 'd': f'Description {i+1}', 'st': ['Strategy A', 'Strategy B']})

# Use actual REM from the original build
# The HTML already has the 50 REM entries from the previous build, so let's keep them

# ─── REPLACE SLOTS IN HTML ───
slots_js = json.dumps(slots, ensure_ascii=False)
# Find and replace SLOTS
old_slots_match = re.search(r'SLOTS:\s*\{.*?\},\s*DAYS:', html, re.DOTALL)
if old_slots_match:
    old = old_slots_match.group(0)
    new = f'SLOTS: {slots_js},\n  DAYS:'
    html = html.replace(old, new)
    print('SLOTS replaced')
else:
    print('SLOTS pattern not found')

# ─── REPLACE REF IN HTML ───
# Find REF: {...} or REF: REF line and replace with full data
html = re.sub(r'REF:\s*\{.*?\}', f'REF: {ref_js}', html)

print(f'REF: {len(bm_refs)} BM + {len(en_refs)} EN + {len(zh_refs)} ZH')

# Verify JS
m = re.search(r'<script>([\s\S]*?)</script>', html)
if m:
    with open('/tmp/check.js', 'w') as f:
        f.write(m.group(1))
    import subprocess
    r = subprocess.run(['node', '--check', '/tmp/check.js'], capture_output=True, text=True)
    print('JS:', 'OK' if r.returncode == 0 else r.stderr[:200])

with open(OUT, 'w') as f:
    f.write(html)
print(f'Size: {len(html)} bytes')
