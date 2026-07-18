#!/usr/bin/env python3
"""Rebuild complete eRPH-PM with all databases (activities, reflections, remedial)."""
import json, re, os

IN = '/home/home/Documents/New OpenCode Project/erph-pm/index.html'
OUT = '/tmp/rph_rebuilt.html'

# ─── 50+ REFLEKSI per language ───
REF = {
'bm':['Seramai 12 orang murid dapat menguasai objektif pembelajaran pada hari ini. Tiga orang murid masih memerlukan bimbingan tambahan. Aktiviti set induksi berjaya menarik minat murid. Langkah pengajaran perlu dipercepatkan pada sesi akan datang.','Objektif PdP tercapai. Murid dapat menyelesaikan tugasan yang diberikan dengan baik. Aktiviti berkumpulan berjalan lancar. Masa perlu diurus dengan lebih efisien.','15 daripada 18 orang murid mencapai objektif pembelajaran. Tiga orang murid perlu menjalani aktiviti pemulihan. Aktiviti hands-on sangat berkesan dan menarik minat murid.','Penguasaan murid pada hari ini adalah memuaskan. PdP berjalan seperti yang dirancang. Murid memberi kerjasama yang baik sepanjang sesi PdP.','Majoriti murid dapat menguasai standard pembelajaran. Beberapa orang murid masih perlukan latihan tambahan. Aktiviti kumpulan meningkatkan kemahiran kolaboratif murid.','Objektif PdP tercapai sepenuhnya. Murid aktif dalam perbincangan dan memberikan idea yang bernas. Pentaksiran formatif menunjukkan perkembangan positif.','PdP berjalan lancar. Murid dapat mengaitkan pembelajaran dengan kehidupan harian. Aktiviti gallery walk didapati sangat efektif untuk meningkatkan penglibatan murid.','Semua murid mencapai objektif minimum yang ditetapkan. Pembelajaran abad ke-21 telah diaplikasikan dalam aktiviti. Refleksi murid menunjukkan kefahaman yang baik.','Objektif PdP tercapai. Murid berjaya menyelesaikan tugasan berkumpulan dengan cemerlang. Kemahiran berfikir aras tinggi (KBAT) telah diterapkan dalam aktiviti.','Penguasaan murid sangat memuaskan. PdP berjalan mengikut perancangan dan masa diperuntukkan dengan baik. Murid bersedia untuk sesi pembelajaran akan datang.','Objektif tercapai. Murid dapat mengaplikasikan pengetahuan dalam situasi baru. Latihan pengukuhan diberikan sebagai kerja rumah untuk mengukuhkan kefahaman.','Seramai 10 orang murid mencapai tahap penguasaan 4 dan ke atas. Lima orang murid masih pada tahap 3. Aktiviti pemulihan akan dijalankan pada sesi akan datang.','PdP berjalan dengan lancar. Murid seronok dengan aktiviti yang disediakan. Bahan bantu mengajar yang pelbagai membantu meningkatkan kefahaman murid.','Murid dapat bekerjasama dalam kumpulan dan menyelesaikan tugasan yang diberikan. Pentaksiran rakan sebaya berjalan dengan baik.','Murid menunjukkan minat yang tinggi terhadap topik yang diajar. Mereka aktif bertanya dan memberi pendapat. PdP perlu diteruskan dengan aktiviti yang lebih mencabar.','PdP hari ini berjalan lancar. 80% murid mencapai objektif. Bimbingan tambahan diberikan kepada murid yang lemah. Aktiviti pengayaan diberikan kepada murid cemerlang.','Aktiviti pembelajaran yang pelbagai membantu mengekalkan minat murid. PdP berjalan lancar mengikut perancangan. Murid memberi kerjasama yang baik.','Objektif PdP tercapai. Murid dapat menguasai kemahiran yang diajar. Aktiviti berkumpulan meningkatkan semangat kerjasama. Masa pengajaran perlu ditambah.','PdP berjalan dengan baik. Murid memberi tumpuan sepanjang sesi. Soalan lisan dijawab dengan betul. Latihan bertulis menunjukkan peningkatan.','Seramai 14 orang murid mencapai objektif. Empat orang murid masih dalam proses pemulihan. Aktiviti differentiated learning membantu memenuhi keperluan murid.','Objektif PdP tercapai keseluruhannya. Murid dapat menyelesaikan tugasan dalam masa yang ditetapkan. Penggunaan BBM yang pelbagai meningkatkan kefahaman.','Murid sangat bersemangat semasa aktiviti kumpulan. Mereka dapat menyelesaikan tugasan dengan baik. Pembentangan hasil kerja menunjukkan usaha yang gigih.','PdP berjalan seperti yang dirancang. Murid memahami konsep yang diajar. Latihan pengukuhan diberikan untuk memantapkan kefahaman.','Majoriti murid mencapai objektif. Beberapa murid masih lemah dalam kemahiran membaca dan menulis. Intervensi khas akan dijalankan untuk murid-murid ini.','PdP berjalan lancar. Murid dapat mengenal pasti dan memahami konsep utama. Aktiviti hands-on sangat membantu murid yang lemah untuk memahami topik.','Objektif PdP tercapai dengan baik. Murid menunjukkan sikap positif terhadap pembelajaran. Mereka bekerjasama dalam kumpulan dan saling membantu.','Murid dapat menguasai standard pembelajaran yang ditetapkan. PdP berjalan lancar. Aktiviti pengayaan dan pemulihan telah dijalankan mengikut keperluan murid.','PdP hari ini sangat menyeronokkan. Murid belajar sambil bermain melalui aktiviti yang menarik. Mereka dapat mengingati konsep dengan lebih mudah.','Objektif PdP tercapai. Murid menunjukkan peningkatan dari segi kefahaman. Bimbingan berterusan diperlukan untuk murid pemulihan.','Keseluruhan PdP berjalan dengan jayanya. Murid mencapai objektif yang ditetapkan. Aktiviti yang pelbagai membantu memenuhi keperluan pembelajaran murid yang berbeza.','PdP hari ini berjaya menarik minat murid melalui aktiviti yang interaktif. Murid dapat berkolaborasi dengan baik dalam kumpulan masing-masing.','Objektif pembelajaran tercapai. Penggunaan teknologi dalam PdP meningkatkan penglibatan murid. Murid seronok belajar dengan cara yang menyeronokkan.','Murid dapat menguasai kemahiran yang diajar dengan bimbingan guru. Latihan pengukuhan akan diberikan untuk memantapkan lagi kefahaman mereka.','PdP berjalan lancar. Murid aktif bertanya dan memberi respons. Pendekatan belajar sambil bermain sangat sesuai untuk topik ini.','Objektif PdP tercapai sepenuhnya. Pembentangan hasil kerja murid menunjukkan usaha yang baik. Pentaksiran formatif dijalankan secara berterusan.','Seramai 16 orang murid mencapai objektif. Dua orang murid memerlukan perhatian khusus. Aktiviti pemulihan akan dijalankan secara individu.','Murid dapat mengaplikasikan pengetahuan dalam situasi baru. Pendekatan kontekstual membantu murid memahami topik dengan lebih mendalam.','PdP hari ini berjaya meningkatkan kemahiran berfikir kritis murid. Mereka dapat menyelesaikan masalah dengan kreatif.','Objektif PdP tercapai. Penggunaan BBM yang kreatif menarik minat murid. Mereka lebih mudah memahami konsep abstrak melalui visual.','Majoriti murid dapat menyelesaikan tugasan yang diberikan. Beberapa murid memerlukan bimbingan tambahan dalam kemahiran menulis.','PdP berjalan lancar dengan penglibatan aktif daripada murid. Aktiviti berkumpulan menggalakkan kerjasama dan komunikasi sesama murid.','Objektif PdP tercapai. Murid dapat menguasai kemahiran bertutur dengan yakin. Aktiviti main peranan sangat membantu.','Murid menunjukkan sikap positif dan minat yang tinggi. PdP berjalan lancar. Pentaksiran formatif menunjukkan perkembangan positif.','PdP hari ini berjaya mencapai objektif yang ditetapkan. Murid dapat bekerja secara berkumpulan dan individu dengan baik.','Objektif PdP tercapai. Murid dapat mengenal pasti dan memahami konsep yang diajar. Latihan pengukuhan diberikan untuk memantapkan kefahaman.','Murid seronok dengan aktiviti yang disediakan. Mereka dapat belajar dalam suasana yang menyeronokkan. PdP berjalan lancar.','PdP berjalan lancar mengikut perancangan. Murid dapat menguasai kemahiran yang diajar. Refleksi murid menunjukkan kefahaman yang baik.','Objektif PdP tercapai. Murid dapat menjawab soalan dengan betul. Aktiviti pengayaan dan pemulihan dijalankan mengikut keperluan.','Majoriti murid menunjukkan perkembangan positif. Beberapa murid masih perlu bimbingan. PdP akan datang akan memberi fokus kepada pemulihan.','PdP hari ini sangat memberangsangkan. Murid dapat menguasai objektif pembelajaran dengan cemerlang. Aktiviti yang pelbagai membantu proses pembelajaran.'],
'en':['12 pupils achieved the learning objectives today. 3 pupils need additional guidance. The set induction activity successfully engaged pupils. Teaching pace needs to be adjusted next session.','Learning objectives achieved. Pupils completed the given tasks well. Group activities ran smoothly. Time management needs improvement.','15 out of 18 pupils achieved the learning objectives. 3 pupils need remedial activities. Hands-on activities were very effective and engaging.','Pupil mastery today was satisfactory. The lesson proceeded as planned. Pupils cooperated well throughout the session.','The majority of pupils mastered the learning standards. A few pupils still need additional practice. Group activities improved collaborative skills.','Learning objectives fully achieved. Pupils were active in discussions. Formative assessment shows positive progress.','The lesson went well. Pupils could relate learning to daily life. The gallery walk activity was very effective for increasing engagement.','All pupils achieved the minimum objectives. 21st century learning was applied in activities. Pupil reflections show good understanding.','Learning objectives achieved. Pupils completed group tasks excellently. Higher order thinking skills were incorporated into activities.','Pupil mastery was very satisfactory. The lesson followed the plan well. Pupils are ready for the next learning session.','Objectives achieved. Pupils could apply knowledge in new situations. Reinforcement exercises given as homework.','10 pupils achieved mastery level 4 and above. 5 pupils are still at level 3. Remedial activities will be conducted next session.','The lesson went smoothly. Pupils enjoyed the activities provided. Various teaching aids helped improve understanding.','Learning objectives achieved. Pupils cooperated in groups and completed given tasks. Peer assessment went well.','Pupils showed high interest in the topic taught. They actively asked questions and gave opinions. Future lessons need more challenging activities.','80% of pupils achieved the objectives. Additional guidance given to weak pupils. Enrichment activities given to excellent pupils.','Varied learning activities maintained pupil interest throughout. The lesson proceeded as planned with good pupil cooperation.','Objectives achieved. Pupils mastered the skills taught. Group activities fostered cooperation. Teaching time needs to be extended.','The lesson went well. Pupils paid attention throughout the session. Oral questions were answered correctly. Written exercises showed improvement.','14 pupils achieved the objectives. 4 pupils are still in the remedial process. Differentiated learning activities helped meet pupil needs.','Learning objectives largely achieved. Pupils completed tasks within the given time. Use of various teaching aids improved understanding.','Pupils were very enthusiastic during group activities. They completed tasks well. Presentations showed great effort.','The lesson proceeded as planned. Pupils understood the concepts taught. Reinforcement exercises given to consolidate understanding.','Objectives achieved. Pupils answered questions correctly. Varied learning activities maintained pupil interest throughout the session.','Majority of pupils achieved objectives. A few pupils still weak in reading and writing skills. Special intervention will be conducted.','The lesson went well. Pupils could identify and understand key concepts. Hands-on activities greatly helped weak pupils understand the topic.','Learning objectives achieved well. Pupils showed positive attitudes towards learning. They cooperated in groups and helped each other.','Pupils mastered the prescribed learning standards. The lesson went smoothly. Enrichment and remedial activities were conducted according to pupil needs.','Today\'s lesson was very enjoyable. Pupils learned through play. They could remember concepts more easily through interesting activities.','Objectives achieved. Pupils showed improvement in understanding. Continuous guidance needed for remedial pupils.','The overall lesson was successful. Pupils achieved the set objectives. Varied activities helped meet the different learning needs of pupils.','Today\'s lesson successfully engaged pupils through interactive activities. They collaborated well in their respective groups.','Learning objectives achieved. Technology integration in T&L increased pupil engagement. Pupils enjoyed learning in a fun way.','Pupils mastered the skills taught with teacher guidance. Reinforcement exercises will be given to strengthen understanding.','The lesson went smoothly. Pupils actively asked questions and gave responses. The learn-through-play approach was very suitable.','Learning objectives fully achieved. Pupil presentations showed great effort. Formative assessment was conducted continuously.','16 pupils achieved the objectives. 2 pupils need special attention. Individual remedial activities will be conducted.','Pupils could apply knowledge in new situations. A contextual approach helped pupils understand the topic more deeply.','Today\'s lesson successfully improved pupils\' critical thinking skills. They could solve problems creatively.','Objectives achieved. Creative use of teaching aids attracted pupil interest. They understood abstract concepts more easily through visuals.','Majority of pupils completed the given tasks. A few pupils need additional guidance in writing skills.','The lesson proceeded with active pupil participation. Group activities encouraged cooperation and communication among pupils.','Objectives achieved. Pupils mastered speaking skills confidently. Role-play activities were very helpful.','Pupils showed positive attitudes and high interest. The lesson went smoothly. Formative assessment shows positive development.','Today\'s lesson successfully achieved the set objectives. Pupils could work well both in groups and individually.','Pupils enjoyed the activities provided. They could learn in a fun and engaging atmosphere. The lesson went well.','The lesson proceeded according to plan. Pupils mastered the skills taught. Pupil reflections show good understanding.','Objectives achieved. Pupils answered questions correctly. Enrichment and remedial activities were conducted according to needs.','Majority of pupils showed positive development. A few still need guidance. Next lesson will focus on remedial work.','Today\'s lesson was very encouraging. Pupils mastered the learning objectives excellently. Varied activities helped the learning process.'],
'zh':['今天有12名学生达到了学习目标。3名学生需要额外指导。导入活动成功吸引了学生的兴趣。下次授课需要调整教学节奏。','教学目标达成。学生能够很好地完成分配的任务。小组活动顺利进行。时间管理需要改善。','15名/18名学生达到了学习目标。3名学生需要进行补救活动。动手操作活动非常有效并吸引学生。','今天学生的掌握程度令人满意。教学按计划进行。学生在整个过程中给予了良好的配合。','大多数学生掌握了学习标准。少数学生还需要额外的练习。小组活动提高了协作能力。','教学目标完全达成。学生在讨论中很活跃。形成性评估显示出积极的进展。','教学顺利。学生能够将学习与日常生活联系起来。画廊漫步活动有效地提高了参与度。','所有学生都达到了最低目标。活动中应用了21世纪学习技能。学生的反思显示出良好的理解。','教学目标达成。学生出色地完成了小组任务。活动中融入了高层次思维技能。','学生的掌握程度非常令人满意。教学按计划顺利进行。学生已准备好接受下一堂课。','目标达成。学生能够在新情况下应用知识。布置了巩固练习作为家庭作业。','10名学生达到掌握水平4及以上。5名学生仍在水平3。下次课将进行补救活动。','教学顺利。学生喜欢所提供的活动。多样化的教具有助于提高理解。','教学目标达成。学生在小组中合作并完成了分配的任务。同伴评估进行得很好。','学生对所教主题表现出很高的兴趣。他们积极提问和发表意见。下次课需要更具挑战性的活动。','80%的学生达到了目标。对弱生给予了额外指导。对优生给予了充实活动。','多样化的学习活动保持了学生的兴趣。教学按计划进行，学生配合良好。','目标达成。学生掌握了所教的技能。小组活动培养了合作精神。需要增加教学时间。','教学顺利。学生全程专心听讲。口头问题回答正确。书面练习显示出进步。','14名学生达到了目标。4名学生仍在补救过程中。分层学习活动满足了学生的需求。','教学目标大体达成。学生在规定时间内完成了任务。多样化教具的使用提高了理解力。','学生在小组活动中非常积极。他们很好地完成了任务。呈现展示出很大的努力。','教学按计划进行。学生理解了所教的概念。进行了巩固练习以加强理解。','目标达成。学生正确回答了问题。多样化的学习活动保持了学生的兴趣。','大多数学生达到了目标。少数学生在阅读和写作方面仍然薄弱。将进行特别干预。','教学顺利。学生能够识别和理解关键概念。动手活动大大帮助了弱生理解主题。','教学目标很好地达成。学生对学习表现出积极的态度。他们在小组中合作并互相帮助。','学生掌握了规定的学习标准。教学顺利。根据学生的需要进行了充实和补救活动。','今天的课非常有趣。学生在玩中学。通过有趣的活动，他们更容易记住所教的概念。','目标达成。学生在理解方面显示出进步。补救学生需要持续的指导。','整体教学成功。学生达到了设定的目标。多样化的活动满足了学生不同的学习需求。','今天的课通过互动活动成功吸引了学生。他们在各自的小组中合作良好。','教学目标达成。科技融入教学提高了学生的参与度。学生喜欢有趣的学习方式。','学生在教师指导下掌握了所教的技能。将进行巩固练习以加强理解。','教学顺利。学生积极提问并做出回应。通过游戏学习的方法非常合适。','教学目标完全达成。学生的呈现展示出很大的努力。持续进行形成性评估。','16名学生达到了目标。2名学生需要特别关注。将进行个别补救活动。','学生能够在新情况下应用知识。情境教学法帮助学生更深入地理解主题。','今天的课成功提高了学生的批判性思维能力。他们能创造性地解决问题。','目标达成。教具的创造性使用吸引了学生的兴趣。他们通过视觉更容易理解抽象概念。','大多数学生完成了分配的任务。少数学生在写作技能方面需要额外指导。','教学顺利进行，学生积极参与。小组活动鼓励了学生之间的合作与沟通。','目标达成。学生自信地掌握了口语技能。角色扮演活动非常有帮助。','学生表现出积极的态度和高度的兴趣。教学顺利。形成性评估显示出积极的发展。','今天的课成功达到了设定的目标。学生能够在小组和个别工作中都表现良好。','学生喜欢所提供的活动。他们能在有趣和吸引人的氛围中学习。教学顺利。','教学按计划进行。学生掌握了所教的技能。学生的反思显示出良好的理解。','目标达成。学生正确回答了问题。根据需要进行充实和补救活动。','大多数学生显示出积极的发展。少数仍需要指导。下节课将重点进行补救工作。','今天的课非常令人鼓舞。学生出色地掌握了学习目标。多样化的活动帮助了学习过程。'],
}

# ─── 50+ REMEDIAL ───
REM = [
    {'t':'🧑‍🏫 Bimbingan Individu','d':'Bimbingan individu langkah-demi-langkah dengan soalan bimbingan dan pengukuhan positif. Murid dibimbing secara one-to-one.', 'st':['Bimbingan','Pengulangan','Soalan lisan']},
    {'t':'📝 Latihan Berstruktur','d':'Lembaran kerja dipermudah dengan arahan langkah-demi-langkah dan contoh jawapan.','st':['Latihan berpandu','Contoh','Struktur']},
    {'t':'👀 Tunjuk Cara Ulangan','d':'Guru mendemonstrasi semula kemahiran dengan penerangan yang lebih perlahan dan jelas.','st':['Demonstrasi','Pengulangan','Visual']},
    {'t':'📊 Bahan Bantu Visual','d':'Menggunakan gambar rajah, carta, peta konsep dan video untuk menjelaskan konsep secara visual.','st':['Visual','Peta konsep','Infografik']},
    {'t':'✏️ Latihan Pengukuhan','d':'Latihan tambahan yang lebih mudah untuk membina keyakinan murid sebelum beralih ke aras sederhana.','st':['Latihan','Pengukuhan','Keyakinan']},
    {'t':'🤝 Pembelajaran Berpasangan','d':'Murid cemerlang dipasangkan dengan murid pemulihan untuk saling membantu dan belajar bersama.','st':['Bimbingan rakan','Kolaboratif','Sosial']},
    {'t':'🎲 Permainan Pendidikan','d':'Gunakan permainan papan, kad atau digital untuk mengukuhkan kemahiran secara menyeronokkan.','st':['Permainan','Motivasi','Interaktif']},
    {'t':'🃏 Kad Imbasan','d':'Kad imbasan berwarna untuk mengukuhkan ingatan jangka pendek murid secara konsisten.','st':['Kad imbasan','Pengulangan','Visual']},
    {'t':'🎵 Nyanyian dan Gerakan','d':'Gunakan lagu, irama dan gerakan untuk mengukuhkan konsep. Sesuai untuk murid kinestetik.','st':['Muzik','Gerakan','Kinestetik']},
    {'t':'🗺️ Peta Konsep Bergambar','d':'Murid melengkapkan peta konsep bergambar yang mengandungi gambar dan kata kunci.','st':['Visual','Organisasi','Kreatif']},
    {'t':'📖 Bacaan Bergilir','d':'Guru dan murid membaca bersama. Guru berhenti pada perkataan sukar dan membimbing sebutan.','st':['Bacaan berpandu','Sebutan','Kefahaman']},
    {'t':'🔤 Dialog Strip Sequencing','d':'Dialog dipotong menjadi jalur. Murid menyusun dialog mengikut urutan yang betul.','st':['Susunan','Urutan','Bertutur']},
    {'t':'📄 Cloze Passage Bergambar','d':'Teks cloze di mana perkataan yang hilang ditunjukkan sebagai gambar di atas ruang kosong.','st':['Cloze','Visual','Kefahaman']},
    {'t':'🔍 Error Hunt','d':'Tunjukkan 3 ayat bergambar - 1 betul, 2 dengan kesalahan. Murid membulatkan kesalahan.','st':['Pengenalpastian','Pembetulan','Visual']},
    {'t':'📝 Mini Whiteboard','d':'Guru menunjukkan gambar dan menyebut perkataan/ayat. Murid menulis pada papan putih mini.','st':['Penulisan','Maklum balas','Cepat']},
    {'t':'🏃 Phonics Hopscotch','d':'Lukis grid hopscotch dengan huruf. Murid melompat ke huruf dan menyebut bunyi.','st':['Kinestetik','Fonik','Permainan']},
    {'t':'📑 Word Family Sorting','d':'Gunakan poket carta dengan kepala keluarga perkataan (-at, -an, -op).','st':['Pengelasan','Rakan sebaya','Visual']},
    {'t':'📦 Realia Show & Tell','d':'Bawa objek sebenar. Guru menyebut nama, murid ulang dan ambil objek yang betul.','st':['Objek sebenar','Visual','Verbal']},
    {'t':'⚽ Question Pass','d':'Berdiri dalam bulatan. Hantar bola; penerima jawab soalan dan tanya seterusnya.','st':['Bertutur','Sosial','Permainan']},
    {'t':'🖼️ Talk-the-Picture','d':'Beri pasangan gambar besar. Murid tunjuk dan sebut menggunakan rangka ayat.','st':['Visual','Berpasangan','Bertutur']},
    {'t':'✏️ Latihan Menulis','d':'Murid menulis huruf/perkataan dalam buku latihan dengan titik panduan dan garis bantu.','st':['Penulisan','Mekanis','Latih tubi']},
    {'t':'🧮 Pengiraan Maujud','d':'Gunakan blok, biji benih untuk mengira, menambah dan menolak secara konkrit.','st':['Konkrit','Maujud','Matematik']},
    {'t':'📏 Garis Nombor','d':'Garis nombor di lantai atau meja untuk membantu murid memahami tambah dan tolak.','st':['Visual','Konkrit','Operasi']},
    {'t':'🧠 Permainan Memori','d':'Kad diletakkan terbalik. Murid membuka dua kad untuk padanan gambar-perkataan.','st':['Memori','Padanan','Permainan']},
    {'t':'📒 Buku Skrap Pemulihan','d':'Murid mengumpul hasil kerja pemulihan dalam buku skrap untuk melihat perkembangan.','st':['Dokumentasi','Motivasi','Kendiri']},
    {'t':'✂️ Potong dan Tampal','d':'Murid memotong gambar/perkataan dan menampal pada tempat betul dalam lembaran kerja.','st':['Psikomotor','Pengelasan','Kreatif']},
    {'t':'💬 Soalan Lisan','d':'Guru mengemukakan soalan secara lisan dengan bimbingan rapat tanpa tekanan.','st':['Lisan','Bimbingan','Keyakinan']},
    {'t':'💻 Pembelajaran Digital','d':'Gunakan platform Quizizz, Google Forms atau YouTube untuk aktiviti interaktif.','st':['Digital','Interaktif','Kendiri']},
    {'t':'📓 Jurnal Pembelajaran','d':'Murid menulis jurnal ringkas tentang apa yang dipelajari dan apa yang masih sukar.','st':['Refleksi','Penulisan','Kendiri']},
    {'t':'🎪 Stesen Pemulihan','d':'Sediakan stesen khas dengan aktiviti pemulihan untuk murid yang belum menguasai.','st':['Kumpulan kecil','Bimbingan','Stesen']},
    {'t':'🎯 Sasaran Kata','d':'Murid membaling bola ke sasaran dan menyebut perkataan berdasarkan sasaran.','st':['Permainan','Sebutan','Fizikal']},
    {'t':'🧩 Puzzle Pendidikan','d':'Gunakan puzzle gambar atau perkataan untuk mengukuhkan kemahiran membaca.','st':['Puzzle','Visual','Kognitif']},
    {'t':'🎤 Karaoke','d':'Murid menyanyikan lagu pembelajaran dengan lirik dipaparkan di skrin.','st':['Muzik','Pengulangan','Menyanyi']},
    {'t':'📋 Checklist Kendiri','d':'Murid menyemak sendiri pemahaman menggunakan senarai semak mudah.','st':['Kendiri','Refleksi','Penilaian']},
    {'t':'🎭 Main Peranan','d':'Murid melakonkan situasi harian dengan bimbingan guru untuk tingkatkan keyakinan.','st':['Lakonan','Sosial','Kreatif']},
    {'t':'🔢 Kad Nombor','d':'Kad nombor berwarna untuk konsep matematik asas seperti nilai tempat.','st':['Visual','Matematik','Warna']},
    {'t':'📖 Bacaan Bergambar','d':'Buku cerita bergambar besar dengan teks mudah. Murid membaca dengan bimbingan.','st':['Bacaan','Visual','Bimbingan']},
    {'t':'🎲 Dadu Perkataan','d':'Murid melambung dadu dan menyebut perkataan berdasarkan nombor pada dadu.','st':['Permainan','Sebutan','Interaktif']},
    {'t':'📝 Lembaran Imbuhan','d':'Latihan khusus untuk imbuhan awalan, akhiran atau apitan.','st':['Tatabahasa','Latih tubi','Struktur']},
    {'t':'🧑‍🤝‍🧑 Kumpulan Fokus','d':'Kumpulan kecil 3-4 murid pemulihan dibimbing secara intensif oleh guru.','st':['Kumpulan kecil','Intensif','Bimbingan']},
    {'t':'🎯 Papan Ejaan','d':'Papan permainan ejaan khas untuk mengukuhkan kemahiran mengeja.','st':['Ejaan','Permainan','Visual']},
    {'t':'📸 Fotografi','d':'Murid mengambil gambar objek dan melabelkannya dengan perkataan yang betul.','st':['Kreatif','Visual','Teknologi']},
    {'t':'🎬 Video Pendek','d':'Murid menonton video pendek pembelajaran dan menjawab soalan mudah.','st':['Visual','Digital','Kefahaman']},
    {'t':'🧩 Teka Silang Kata','d':'Silang kata mudah dengan gambar sebagai petunjuk.','st':['Kosa kata','Pengukuhan','Puzzle']},
    {'t':'📑 Kad Tugasan','d':'Kad tugasan harian dengan arahan jelas untuk murid pemulihan.','st':['Rutin','Bimbingan','Struktur']},
    {'t':'🎤 Bacaan Berirama','d':'Murid membaca teks mengikut irama atau rap untuk tingkatkan kelancaran.','st':['Bacaan','Irama','Seronok']},
    {'t':'🎨 Mewarna','d':'Lembaran mewarna dengan perkataan atau konsep yang perlu dipelajari.','st':['Mewarna','Visual','Santai']},
    {'t':'📋 Panduan Mini','d':'Murid mencipta buku panduan mini tentang topik yang sukar difahami.','st':['Kreatif','Dokumentasi','Rujukan']},
    {'t':'🤖 Gamifikasi','d':'Gunakan elemen permainan seperti lencana, mata, tahap untuk motivasi.','st':['Gamifikasi','Motivasi','Digital']},
    {'t':'📞 Telefon Bual','d':'Telefon daripada cawan kertas. Murid bercakap untuk tingkatkan kemahiran lisan.','st':['Bertutur','Mendengar','Kreatif']},
]

# ─── 50+ LEARNING ACTIVITIES per phase per language group ───
ACTS = {
'bm':{
'induction':[
'🎵 Murid menyanyikan lagu bertema dengan iringan muzik. Guru memimpin nyanyian dan murid membuat gerakan kreatif. [Dif: A - Nyanyi dengan gerakan kreatif, B - Nyanyi dengan bimbingan lirik, C - Dengar dan tepuk irama]',
'🎬 Tayangan video pendek sebagai rangsangan. Murid meneka tajuk pembelajaran berdasarkan video. [Dif: A - Teka dengan ayat lengkap, B - Teka satu perkataan, C - Padankan gambar]',
'🧩 Permainan teka-teki atau \"Cari Pasangan\" - murid mencari rakan dengan kad berpasangan. [Dif: A - Padan perkataan dengan ayat, B - Padan gambar dengan perkataan, C - Padan gambar dengan gambar]',
'🎭 Bercerita menggunakan boneka jari atau puppets. Murid meneka watak dan jalan cerita. [Dif: A - Bercerita ayat sendiri, B - Ulang dialog watak, C - Namakan watak]',
'🖼️ Tunjuk gambar bersiri. Murid menyusun mengikut urutan dan meneka cerita. [Dif: A - Susun dan cerita, B - Susun dan baca ayat, C - Susun gambar]',
'❓ Soal jawab lisan berdasarkan objek maujud atau gambar yang dibawa oleh guru. [Dif: A - Jawab ayat penuh, B - Jawab frasa, C - Tunjuk dan angguk]',
'🔄 Permainan \"Cari Perbezaan\" - murid membandingkan dua gambar. [Dif: A - Terangkan perbezaan, B - Cari dan tunjuk, C - Padankan]',
'👂 Dengar dan teka: Guru memainkan bunyi atau audio, murid meneka benda. [Dif: A - Teka dan huraikan, B - Teka benda, C - Pilih gambar]',
'🎈 Permainan \"Bola Berbual\" - murid menangkap bola dan menjawab soalan guru. [Dif: A - Jawab soalan KBAT, B - Jawab soalan mudah, C - Bantu rakan]',
'📦 Kotak Misteri: Murid memegang objek dalam kotak dan teka apa objek tersebut. [Dif: A - Terangkan ciri objek, B - Teka objek, C - Rasa dan tunjuk]',
],
'pre':[
'📇 Perkenal kosa kata baru menggunakan kad imbasan (flashcards). Murid menyebut dan mengeja. [Dif: A - Bina ayat, B - Sebut dan eja, C - Ulang sebutan]',
'👥 Perbincangan kumpulan kecil (Think-Pair-Share) tentang topik pembelajaran. [Dif: A - Kongsi ayat lengkap, B - Kongsi frasa, C - Dengar dan ulang]',
'🔗 Aktiviti padanan: Murid memadankan gambar dengan perkataan pada papan putih. [Dif: A - Padan dan tulis ayat, B - Padan dan sebut, C - Padan gambar]',
'🗣️ Mendengar dan mengulang sebutan frasa penting dengan teknik ulang dengar. [Dif: A - Sebut dengan intonasi, B - Sebut frasa, C - Sebut perkataan]',
'📋 Permainan \"Kad Kategori\" - murid mengelaskan kad ke dalam kumpulan betul. [Dif: A - Kelas dan beri alasan, B - Kelas dengan bimbingan, C - Padan contoh]',
'📝 Latihan lisan: Guru tunjuk gambar, murid jawab secara serentak. [Dif: A - Ayat penuh, B - Satu perkataan, C - Angkat tangan]',
'🎯 Aktiviti \"Minggu, Bulan, Tahun\" - menyusun kad mengikut kategori. [Dif: A - Susun dan bina ayat, B - Susun, C - Padan gambar]',
'🎲 Permainan papan soalan: Murid baling dadu dan jawab soalan. [Dif: A - Soalan KBAT, B - Soalan mudah, C - Bantu kumpulan]',
'🃏 Kad Teka: Murid pilih kad dan terangkan tanpa menyebut perkataan. [Dif: A - Terangkan dengan ayat, B - Guna bahasa badan, C - Tunjuk gambar]',
'✏️ Melukis peta minda ringkas tentang pengetahuan sedia ada. [Dif: A - Peta minda lengkap, B - Peta separa, C - Warnakan]',
],
'dev':[
'📖 Membaca petikan secara berpasangan dan menjawab soalan kefahaman beraras. [Dif: A - Soalan KBAT, B - Soalan literal, C - Lukis jawapan]',
'✍️ Menulis karangan/ayat berpandu menggunakan peta pemikiran i-Think. [Dif: A - Karangan lengkap, B - Ayat berpandu, C - Susun dan tiru]',
'🎭 Aktiviti lakonan (Role Play) - murid melakonkan dialog dalam situasi harian. [Dif: A - Dialog sendiri, B - Dialog diberi, C - Bimbingan guru]',
'🖼️ Gallery Walk - murid berjalan melihat hasil kerja rakan dan memberi komen. [Dif: A - Komen bernas, B - Komen ringkas, C - Tampal stiker]',
'📘 Mencipta buku mini (foldable booklet) berdasarkan topik. [Dif: A - Isi lengkap, B - Isi berpandu, C - Warnakan gambar]',
'🏫 Aktiviti \"Stesen Pembelajaran\" - murid bergerak ke 4-5 stesen berbeza. [Dif: A - Stesen KBAT, B - Stesen sederhana, C - Stesen bimbingan]',
'🧩 Permainan Bahasa - Scrabble, Boggle atau Silang Kata. [Dif: A - Bina ayat, B - Cari perkataan, C - Padan huruf]',
'🗺️ Mencipta peta minda atau peta bulatan secara berkumpulan. [Dif: A - Peta lengkap sub-topik, B - Peta bulatan, C - Bergambar]',
'💻 Penggunaan aplikasi pendidikan seperti Quizizz, Kahoot atau Google Classroom. [Dif: A - Soalan KBAT, B - Soalan sederhana, C - Soalan bergambar]',
'🎨 Aktiviti kraftangan: Poster, model atau diorama berkaitan topik. [Dif: A - Kreatif sendiri, B - Guna template, C - Bantu mewarna]',
'🔬 Eksperimen atau penyiasatan secara berkumpulan. [Dif: A - Reka eksperimen, B - Ikut langkah, C - Bantu rekod]',
'📊 Projek berkumpulan: Siapkan dan bentang projek. [Dif: A - Projek kompleks, B - Projek sederhana, C - Bantu kumpulan]',
'🎪 Karnival pembelajaran: Gerai interaktif untuk topik. [Dif: A - Urus gerai, B - Bantu gerai, C - Lawat gerai]',
'📝 Pembelajaran berasaskan projek: Folio atau buku skrap. [Dif: A - Folio lengkap, B - Buku skrap, C - Koleksi gambar]',
'🎯 Aktiviti \"Hot Seat\" - seorang murid duduk di kerusi panas. [Dif: A - Beri soalan, B - Jawab soalan, C - Catat jawapan]',
],
'post':[
'👨‍🏫 Pembentangan hasil kerja kumpulan terpilih di hadapan kelas. [Dif: A - Bentang yakin, B - Bentang bimbingan, C - Tunjuk hasil]',
'📝 Kuiz Kahoot atau Quizizz secara berkumpulan atau individu. [Dif: A - Soalan KBAT, B - Soalan sederhana, C - Soalan bergambar]',
'💬 Sesi refleksi: Murid berkongsi satu perkara yang dipelajari hari ini. [Dif: A - Kongsi ayat lengkap, B - Kongsi frasa, C - Tunjuk gambar]',
'✏️ Aktiviti \"3-2-1\" - 3 perkara belajar, 2 perkara menarik, 1 soalan. [Dif: A - Tulis lengkap, B - Tulis berpandu, C - Lukis]',
'🗣️ Sumbangsaran secara kelas untuk merumus isi pelajaran. [Dif: A - Idea bernas, B - Setuju/tidak setuju, C - Ulang idea]',
'⭐ Penilaian rakan sebaya menggunakan rubrik mudah. [Dif: A - Guna rubrik, B - Beri bintang, C - Tampal stiker]',
'📊 Pameran hasil kerja (Mini Exhibition). [Dif: A - Susun pameran, B - Bentang, C - Lawat]',
'🎯 Kuiz lisan pantas: Soalan spontan untuk uji kefahaman. [Dif: A - Jawab KBAT, B - Jawab mudah, C - Bantu jawab]',
'🔄 Aktiviti \"Round Table\" - setiap murid menulis idea secara bergilir. [Dif: A - Tulis lengkap, B - Tulis kata kunci, C - Lukis]',
'💭 Refleksi bertulis dalam jurnal pembelajaran. [Dif: A - Perenggan penuh, B - Beberapa ayat, C - Lukis dan label]',
],
'closure':[
'📋 Rumusan isi penting dengan bimbingan murid. Murid melengkapkan peta konsep. [Dif: A - Lengkap peta, B - Separuh, C - Warnakan]',
'🎫 Exit Ticket - murid tulis jawapan pada kertas kecil sebelum keluar. [Dif: A - Ayat lengkap, B - Perkataan, C - Lukis]',
'✅ Permainan \"Betul atau Salah\" untuk menguji kefahaman. [Dif: A - Beri alasan, B - Jawab betul/salah, C - Tiru jawapan]',
'🙏 Doa dan nyanyian lagu penutup. Refleksi lisan oleh 2-3 orang murid. [Dif: A - Pimpin doa, B - Kongsi refleksi, C - Dengar]',
'📚 Guru beri latihan pengukuhan sebagai kerja rumah. [Dif: A - KBAT, B - Sederhana, C - Asas]',
'🔮 Preview pembelajaran seterusnya dengan gambar/soalan teaser. [Dif: A - Ramal ayat, B - Ramal kata, C - Lihat gambar]',
'🎯 Murid lengkap \"What Stuck With You Today?\" pada sticky note. [Dif: A - Tulis lengkap, B - Tulis frasa, C - Lukis]',
'🔄 Sesi soal jawab pantas menggunakan papan putih mini. [Dif: A - Jawab KBAT, B - Jawab mudah, C - Tunjuk jawapan]',
'⭐ Murid letak magnet pada carta \"Tahap Kefahaman\". [Dif: A - Terangkan pilihan, B - Letak magnet, C - Bantu rakan]',
'✏️ Jurnal refleksi: Satu perenggan tentang pembelajaran hari ini. [Dif: A - Perenggan penuh, B - 3 ayat, C - Lukis]',
],
},
'en':{
'induction':[
'🎵 Sing a themed song with actions. Teacher uses guitar or audio. [Diff: A - Create new verses, B - Sing with actions, C - Clap along]',
'🎬 Show a short video clip. Pupils guess the topic of the lesson. [Diff: A - Full sentence guess, B - One word guess, C - Point to picture]',
'🧩 Play "What\'s Missing?" - 4-5 flashcards, close eyes, teacher removes one. [Diff: A - Say in sentence, B - Say the word, C - Point]',
'🎭 Guessing game: Teacher describes something, pupils guess. [Diff: A - Give own clues, B - Guess from clues, C - Point to picture]',
'📦 Mystery bag: Pupils feel objects and guess before seeing. [Diff: A - Describe feeling, B - Guess object, C - Touch and point]',
'🎯 Quick quiz: Show pictures rapidly, pupils name them. [Diff: A - Full sentence, B - Single word, C - Point]',
'👂 Listen and guess: Play sounds, pupils identify the source. [Diff: A - Describe sound, B - Name source, C - Point to image]',
'🎈 Balloon Buzz: Pass a ball; when music stops, the holder answers. [Diff: A - Answer HOTS, B - Answer basic, C - Help teammate]',
'🖼️ Show picture split into parts. Reveal one at a time. [Diff: A - Predict story, B - Guess picture, C - Name objects]',
'🔍 Spot the Difference: Compare two pictures and find differences. [Diff: A - Describe differences, B - Point to them, C - Count]',
],
'pre':[
'📇 Introduce key vocabulary using flashcards. [Diff: A - Make sentence, B - Say and spell, C - Repeat]',
'👥 Match pictures to words on whiteboard in a relay race. [Diff: A - Match and write, B - Match and say, C - Match pictures]',
'💭 Think-Pair-Share: Discuss a question with a partner. [Diff: A - Share full sentence, B - Share keyword, C - Listen]',
'🗣️ Drill key sentence structures using substitution tables. [Diff: A - Create own, B - Complete, C - Repeat]',
'📋 Categorisation game: Sort word cards into groups. [Diff: A - Sort and justify, B - Sort with help, C - Match example]',
'📝 Oral practice: Teacher shows pictures, pupils respond chorally. [Diff: A - Full answer, B - Keyword, C - Gesture]',
'🎲 Board game: Roll a die and answer questions. [Diff: A - HOTS question, B - Basic question, C - Help team]',
'🃏 Taboo word game: Describe a word without using certain words. [Diff: A - Describe well, B - Use gestures, C - Show picture]',
'✏️ Draw a mind map of prior knowledge about the topic. [Diff: A - Full mind map, B - Partial, C - Colour]',
'🔗 Matching activity: Connect words to definitions on the board. [Diff: A - Match and explain, B - Match, C - Copy]',
],
'dev':[
'📖 Read a short passage in pairs. Answer comprehension questions at different levels. [Diff: A - Inferential Qs, B - Literal Qs, C - Draw answer]',
'✍️ Write a short paragraph using a writing frame at 3 levels. [Diff: A - Write independently, B - Complete cloze, C - Trace]',
'🎭 Role-play a dialogue in pairs based on a scenario. [Diff: A - Create dialogue, B - Use given, C - Repeat]',
'🖼️ Gallery Walk: Display work. Pupils walk, read, and give feedback. [Diff: A - Write feedback, B - One comment, C - Draw star]',
'📘 Create a foldable mini-booklet summarising vocabulary. [Diff: A - Full content, B - Guided content, C - Colour]',
'🏫 Station-based learning: 4-5 stations with different tasks. [Diff: A - HOTS station, B - Standard station, C - Guided station]',
'🧩 Information Gap Activity: Pairs have different information. [Diff: A - Ask full Qs, B - Ask keywords, C - Show and copy]',
'🗺️ Create a mind map or graphic organiser in groups. [Diff: A - Full sub-topics, B - Main ideas, C - Pictures]',
'💻 Use educational apps like Quizizz, Kahoot or Padlet. [Diff: A - HOTS Qs, B - Standard Qs, C - Picture Qs]',
'🎨 Craft: Create posters, models or dioramas. [Diff: A - Independent, B - Template, C - Help colour]',
'🔬 Experiment or investigation in groups. [Diff: A - Design experiment, B - Follow steps, C - Record data]',
'📊 Group project: Complete and present. [Diff: A - Complex project, B - Standard project, C - Assist group]',
'🎪 Learning carnival: Set up interactive booths. [Diff: A - Manage booth, B - Help booth, C - Visit booths]',
'📝 Project-based learning: Create a folio or scrapbook. [Diff: A - Full folio, B - Scrapbook, C - Picture collection]',
'🎯 Hot Seat: One pupil sits in the hot seat, others ask questions. [Diff: A - Ask Qs, B - Answer Qs, C - Record answers]',
],
'post':[
'👨‍🏫 Selected groups present their work to the class. [Diff: A - Present confidently, B - Present with support, C - Display work]',
'📝 Quick quiz using Kahoot, Quizizz, or mini-whiteboards. [Diff: A - Explain answer, B - Choose answer, C - Copy answer]',
'💬 Reflection circle: Each pupil shares one thing they learned. [Diff: A - Full sentence, B - One word, C - Gesture]',
'✏️ Exit ticket: Write one sentence about what you learned. [Diff: A - Write sentence, B - Complete sentence, C - Draw and label]',
'🗣️ Class brainstorming to summarise the lesson. [Diff: A - Give ideas, B - Agree/disagree, C - Repeat]',
'⭐ Peer assessment using a simple rubric. [Diff: A - Use rubric, B - Give star, C - Place sticker]',
'📊 Mini Exhibition: Display all work. [Diff: A - Set up, B - Present, C - Visit]',
'🎯 Quick oral quiz: Spontaneous questions. [Diff: A - HOTS, B - Basic, C - Help answer]',
'🔄 Round Table: Each pupil writes an idea in turn. [Diff: A - Write full, B - Keyword, C - Draw]',
'💭 Written reflection in learning journal. [Diff: A - Full paragraph, B - Few sentences, C - Draw]',
],
'closure':[
'📋 Teacher summarises with pupil input using a mind map. [Diff: A - Add details, B - Add keywords, C - Colour]',
'🎫 Exit ticket: Answer a question on small paper before leaving. [Diff: A - Write sentence, B - Write word, C - Draw]',
'✅ Quick review game like "Hot Seat" or "Back to the Board". [Diff: A - Give clues, B - Guess, C - Cheer]',
'🙏 Closing prayer or song. 2-3 pupils share reflection. [Diff: A - Lead prayer, B - Share reflection, C - Listen]',
'📚 Teacher assigns homework. [Diff: A - HOTS, B - Standard, C - Basic]',
'🔮 Preview next lesson with a teaser. [Diff: A - Predict sentences, B - Predict word, C - Look]',
'🎯 Pupils complete "What Stuck With You Today?" on sticky note. [Diff: A - Write full, B - Write phrase, C - Draw]',
'🔄 Quick Q&A using mini-whiteboards. [Diff: A - HOTS, B - Basic, C - Show]',
'⭐ Pupils place magnet on "Understanding Level" chart. [Diff: A - Explain, B - Place, C - Help peer]',
'✏️ Reflection journal: Write about today\'s learning. [Diff: A - Full, B - 3 sentences, C - Draw]',
],
},
'zh':{
'induction':[
'🎵 学生唱主题歌曲并做动作。教师用吉他或录音带领。[分层：A - 自创新歌词，B - 唱并做动作，C - 拍手跟节奏]',
'🎬 播放短视频或展示图片，学生猜测本节课主题。[分层：A - 完整句子猜，B - 关键词猜，C - 指认图片]',
'🧩 猜谜语：教师描述，学生猜答案。[分层：A - 自己出谜语，B - 猜谜语，C - 选图片答案]',
'🎭 展示实物或模型，学生观察和触摸引出主题。[分层：A - 描述特征，B - 说出名称，C - 触摸指认]',
'📦 神秘袋：学生触摸袋中物品并猜测。[分层：A - 描述感觉，B - 猜物品，C - 触摸指认]',
'🎯 快速闪卡：教师快速展示图片，学生快速回答。[分层：A - 完整句子，B - 关键词，C - 指认]',
'👂 听声音猜事物。[分层：A - 描述声音，B - 猜事物，C - 指认图片]',
'🔍 找不同：比较两幅图找出不同。[分层：A - 描述不同，B - 指出不同，C - 数数量]',
'🖼️ 图片拼图：展示部分图片，学生猜测完整图片。[分层：A - 预测故事，B - 猜图片，C - 指出物品]',
'❓ 快速问答游戏。[分层：A - 回答高思考问题，B - 回答简单问题，C - 帮助组员]',
],
'pre':[
'📇 使用字卡介绍关键概念词汇，学生跟读。[分层：A - 造句，B - 读词，C - 跟读]',
'👥 小组讨论 (Think-Pair-Share)。[分层：A - 完整表达，B - 表达关键词，C - 听取意见]',
'🔗 图文配对活动。[分层：A - 配对并造句，B - 配对并读词，C - 配图片]',
'🗣️ 教师示范关键概念，学生观察模仿。[分层：A - 复述步骤，B - 做简单操作，C - 观察模仿]',
'📋 分类游戏：将物品/概念卡分类。[分层：A - 分类并说明，B - 分类，C - 参考示例]',
'📝 全班口头练习：教师展示图片，学生齐声回答。[分层：A - 完整答，B - 关键词，C - 举手]',
'🎲 棋盘游戏：掷骰子回答问题。[分层：A - 高思考，B - 简单，C - 帮组员]',
'🃏 禁忌词游戏：描述词汇但不准用某些词。[分层：A - 很好描述，B - 用肢体，C - 展示图片]',
'✏️ 学生绘制主题先备知识的思维导图。[分层：A - 完整导图，B - 部分，C - 涂色]',
'🔗 连线：将词汇与定义连接。[分层：A - 连并说明，B - 连，C - 抄写]',
],
'dev':[
'📖 小组阅读短文并回答不同层次的理解问题。[分层：A - 高思考，B - 直接回答，C - 画答案]',
'✍️ 使用写作框架写段落（三层）。[分层：A - 独立写，B - 填空，C - 描写]',
'🎭 角色扮演：学生扮演不同角色模拟情境。[分层：A - 自编对话，B - 使用给定，C - 跟读]',
'🖼️ 画廊漫步：参观同伴作品并留言反馈。[分层：A - 写反馈，B - 写评语，C - 贴贴纸]',
'📘 制作折叠小书总结关键词汇句子。[分层：A - 完整内容，B - 引导内容，C - 涂色]',
'🏫 学习站：轮流到4-5个站完成任务。[分层：A - 挑战站，B - 标准站，C - 辅导站]',
'🧩 信息差活动：成对学生信息不同，互相询问。[分层：A - 问完整问题，B - 问关键词，C - 展示抄写]',
'🗺️ 小组创作思维导图或图形组织器。[分层：A - 完整子主题，B - 主要想法，C - 图片]',
'💻 使用教育应用：Quizizz、Kahoot、Padlet。[分层：A - 高思考，B - 标准，C - 图片题]',
'🎨 手工艺：制作海报、模型或立体模型。[分层：A - 独立创造，B - 用模板，C - 帮助涂色]',
'🔬 小组实验或调查。[分层：A - 设计实验，B - 跟步骤，C - 记录数据]',
'📊 小组项目：完成并呈现。[分层：A - 复杂项目，B - 标准项目，C - 帮助小组]',
'🎪 学习嘉年华：设置互动展位。[分层：A - 管理展位，B - 帮忙，C - 参观]',
'📝 项目式学习：创建文件夹或剪贴簿。[分层：A - 完整文件夹，B - 剪贴簿，C - 收集图片]',
'🎯 热座活动：一名学生坐热座，其他学生提问。[分层：A - 提问，B - 回答，C - 记录]',
],
'post':[
'👨‍🏫 选定小组在班前呈现工作成果。[分层：A - 自信呈现，B - 辅助呈现，C - 展示作品]',
'📝 使用 Kahoot 或 Quizizz 进行快速测验。[分层：A - 解释答案，B - 选答案，C - 抄答案]',
'💬 反射圈：每位学生分享今天学到一个知识点。[分层：A - 完整句子，B - 关键词，C - 手势]',
'✏️ Exit ticket：写一句话关于今天所学。[分层：A - 写句子，B - 完成句子，C - 画图标]',
'🗣️ 全班集体讨论总结课程内容。[分层：A - 给想法，B - 同意/不同意，C - 复述]',
'⭐ 同伴互评使用简单量规。[分层：A - 用量规，B - 给星星，C - 贴贴纸]',
'📊 迷你展览：展示所有作品。[分层：A - 布置，B - 呈现，C - 参观]',
'🎯 快速口头测验。[分层：A - 高思考，B - 简单，C - 帮助回答]',
'🔄 圆桌活动：学生轮流写一个想法。[分层：A - 写完整，B - 关键词，C - 画]',
'💭 书面反思在学习日志中。[分层：A - 完整段落，B - 几句话，C - 画]',
],
'closure':[
'📋 教师引导学生总结重点，完成概念图。[分层：A - 添加细节，B - 添关键词，C - 涂色]',
'🎫 Exit ticket：离开前在小纸上回答问题。[分层：A - 写句子，B - 写词，C - 画]',
'✅ 快速复习游戏如对或错。[分层：A - 给理由，B - 判断，C - 挥旗]',
'🙏 祈祷或闭幕歌曲。2-3名学生口头分享。[分层：A - 领祷告，B - 分享反思，C - 听]',
'📚 教师布置分层作业。[分层：A - 挑战题，B - 标准题，C - 基础题]',
'🔮 用问题或图片预告下节课。[分层：A - 预测句子，B - 预测词，C - 看图]',
'🎯 学生在便签上完成今天学到了什么。[分层：A - 写完整，B - 写短语，C - 画]',
'🔄 快速问答用小白板。[分层：A - 高思考，B - 简单，C - 展示]',
'⭐ 学生在理解程度表上放置磁铁。[分层：A - 解释，B - 放置，C - 帮助同学]',
'✏️ 反思日志：写一段今天学习内容。[分层：A - 完整段，B - 三句，C - 画]',
],
},
}

# ─── LANGUAGE MAP ───
# BM -> 'bm', BI -> 'en', everything else -> 'zh'
LANG_MAP = {'BM':'bm','BI':'en'}

ref_json = json.dumps(REF, ensure_ascii=False)
rem_json = json.dumps(REM, ensure_ascii=False)
acts_json = json.dumps(ACTS, ensure_ascii=False)

with open(IN, 'r') as f:
    html = f.read()

# Inject REF, REM, ACTS as const variables before the Alpine init
# Find the last script tag
last_script = html.rfind('</script>')
injection = f'''
const REF = {ref_json};
const REM = {rem_json};
const ACTS = {acts_json};
'''
html = html[:last_script] + injection + html[last_script:]

# Add REF, REM, ACTS to Alpine data
html = html.replace('  REF: {}', '  REF: REF,\n  REM: REM,\n  ACTS: ACTS,')

# Update gen() function to use ACTS and include differentiation + remedial
# The gen function should pick random activities and remedial
old_gen = '''      const rem=REM.sort(()=>Math.random()-0.5).slice(0,3);
      const phases=['🎯 Set Induksi','📚 Pra-PdP','📖 Perkembangan PdP','💡 Pasca-PdP','🎯 Penutup'];
      const duDef=[8,7,22,5,5];const tr=['👩‍🏫 Membimbing','👨‍🏫 Menerangkan','👩‍🏫 Memudahcara','👨‍🏫 Menilai','👩‍🏫 Merumus'];
      const sr=['🙋 Melibatkan diri','👂 Mendengar','✍️ Melaksanakan','🗣️ Membentang','💭 Mereflek'];
      const acts=this.D?.ACTS?.bm||{induction:[],pre:[],dev:[],post:[],closure:[]};
      const pk=['induction','pre','dev','post','closure'];'''

# Check what the gen function looks like now
import re
gen_match = re.search(r'const rem=REM.*?const pk=\[.*?\];', html, re.DOTALL)
if gen_match:
    old_gen_text = gen_match.group()
    new_gen_text = '''      const rem=REM.sort(()=>Math.random()-0.5).slice(0,3);
      const l=this.lg(s.s);
      const phases=l==='bm'?['🎯 Set Induksi','📚 Pra-PdP','📖 Perkembangan PdP','💡 Pasca-PdP','🎯 Penutup']:l==='en'?['🎯 Set Induction','📚 Pre-lesson','📖 Lesson Development','💡 Post-lesson','🎯 Closure']:['🎯 导入','📚 课前活动','📖 主要教学','💡 课后活动','🎯 总结'];
      const duDef=[8,7,22,5,5];const tr=l==='bm'?['👩‍🏫 Membimbing','👨‍🏫 Menerangkan','👩‍🏫 Memudahcara','👨‍🏫 Menilai','👩‍🏫 Merumus']:l==='en'?['👩‍🏫 Guide','👨‍🏫 Explain','👩‍🏫 Facilitate','👨‍🏫 Assess','👩‍🏫 Summarise']:['👩‍🏫 引导','👨‍🏫 讲解','👩‍🏫 引导活动','👨‍🏫 评估','👩‍🏫 总结'];
      const sr=l==='bm'?['🙋 Melibatkan diri','👂 Mendengar','✍️ Melaksanakan','🗣️ Membentang','💭 Mereflek']:l==='en'?['🙋 Participate','👂 Listen','✍️ Carry out','🗣️ Present','💭 Reflect']:['🙋 积极参与','👂 聆听','✍️ 执行','🗣️ 呈现','💭 反思'];
      const acts=ACTS[l]||ACTS['bm']||{};
      const pk=['induction','pre','dev','post','closure'];'''
    html = html.replace(old_gen_text, new_gen_text)
    print('Gen function updated')
else:
    print('Gen function not found')

# Update the act generation to use ACTS database
old_act_gen = '''acts:phases.map((ph,i)=>({ph,d:'Aktiviti '+ph,dr:duDef[i],t:tr[i]||'',s:sr[i]||''})),'''
new_act_gen = '''acts:phases.map((ph,i)=>{const pool=acts[pk[i]]||[];const pick=pool.length?pool[Math.floor(Math.random()*pool.length)]:('Aktiviti '+ph);return{ph,d:pick,dr:duDef[i],t:tr[i]||'',s:sr[i]||''};}),'''
html = html.replace(old_act_gen, new_act_gen)

# Update ref1 to use per-language REF
old_ref1 = '''ref1(p){const refs=this.REF[p.s]||[];if(refs.length)p.ref=refs[Math.floor(Math.random()*refs.length)];},'''
new_ref1 = '''ref1(p){const l=this.lg(p.s);const refs=REF[l]||REF['bm']||[];if(refs.length)p.ref=refs[Math.floor(Math.random()*refs.length)];},'''
html = html.replace(old_ref1, new_ref1)

# Also need to add lg() function if not present
if 'lg(s){' not in html:
    # Add language getter
    old_tn = "tN(){const t=this.TEACHERS[this.tg];return t?t.n+' ('+this.tg+')':'';},"
    new_tn = old_tn + '''
  lg(s){const m={BM:'bm',BI:'en'};return m[s]||'zh';},'''
    html = html.replace(old_tn, new_tn)

with open(OUT, 'w') as f:
    f.write(html)

# Verify JS
import subprocess
m = re.search(r'<script>([\s\S]*?)</script>', html)
if m:
    with open('/tmp/check.js', 'w') as f:
        f.write(m.group(1))
    r = subprocess.run(['node', '--check', '/tmp/check.js'], capture_output=True, text=True)
    print('JS:', 'OK' if r.returncode == 0 else r.stderr[:300])

print('Done')
