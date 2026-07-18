#!/usr/bin/env python3
"""Full update: SK/SP from curriculum-db + elaborated activities + language fix."""
import json, re

IN = '/home/home/Documents/New OpenCode Project/erph-pm/index.html'

with open(IN, 'r') as f:
    html = f.read()

# ══════════════════════════════════════════════════════════
# 1. Update gen() to use real SK/SP from curriculum-db.js
# ══════════════════════════════════════════════════════════

# Find the gen() function's SK/SP assignment
# Current: sk:['Standard Kandungan mengikut DSKP'],sp:['Standard Pembelajaran mengikut DSKP'],
old_sk_sp = """sk:['Standard Kandungan mengikut DSKP'],sp:['Standard Pembelajaran mengikut DSKP'],
        obj:['🎯 Pada akhir PdP, murid dapat memahami dan mengaplikasikan konsep.','✅ Murid dapat menjawab soalan dan menunjukkan kefahaman.'],
        kj:['✅ Saya boleh memahami konsep.','✅ Saya boleh menyelesaikan tugasan.'],
        bbm:['📖 Buku teks','📝 Lembaran kerja'],nilai:['🤝 Kerjasama','🙏 Hormat'],emk:['🗣️ Bahasa','🎨 Kreativiti'],"""

# The obj/kj/bbm/nilai/emk should also be language-aware
new_sk_sp = """sk:(function(){try{const c=getCurriculum(('Year '+s.c.match(/\\d+/)),s.s);if(c)return Object.values(c.SK).slice(0,3);}catch(e){}return['Standard Kandungan'];})(),
        sp:(function(){try{const c=getCurriculum(('Year '+s.c.match(/\\d+/)),s.s);if(c)return Object.values(c.SP).slice(0,3);}catch(e){}return['Standard Pembelajaran'];})(),
        obj:l==='bm'?['🎯 Pada akhir PdP, murid dapat memahami dan mengaplikasikan konsep dalam topik ini.','✅ Murid dapat menjawab soalan dan menunjukkan kefahaman dengan bimbingan.','✅ Murid dapat menyelesaikan tugasan yang diberikan dengan betul.']:l==='en'?['🎯 By the end of the lesson, pupils will be able to understand and apply the concepts in this topic.','✅ Pupils will be able to answer questions and demonstrate understanding with guidance.','✅ Pupils will be able to complete the assigned tasks correctly.']:['🎯 在课堂结束时，学生能够理解和应用本课题的概念。','✅ 学生能够在教师的引导下回答问题并展示理解。','✅ 学生能够正确完成所分配的任务。'],
        kj:l==='bm'?['✅ Saya boleh memahami konsep yang diajar.','✅ Saya boleh menyelesaikan tugasan yang diberikan.','✅ Saya boleh menerangkan kepada rakan tentang apa yang saya belajar.']:l==='en'?['✅ I can understand the concept taught.','✅ I can complete the given tasks.','✅ I can explain what I learned to a friend.']:['✅ 我能理解所教的概念。','✅ 我能完成分配的任务。','✅ 我能向同学解释我学到的东西。'],
        bbm:l==='en'?['📖 Textbook','📝 Worksheets','🃏 Flashcards','✏️ Stationery','📋 Whiteboard']:l==='bm'?['📖 Buku teks','📝 Lembaran kerja','🃏 Kad imbasan','✏️ Alat tulis','📋 Papan putih']:['📖 课本','📝 工作纸','🃏 字卡','✏️ 文具','📋 白板'],
        nilai:l==='en'?['🤝 Cooperation','🙏 Respect','💪 Responsibility','🌟 Diligence']:l==='bm'?['🤝 Kerjasama','🙏 Hormat-menghormati','💪 Tanggungjawab','🌟 Kesungguhan']:['🤝 合作','🙏 尊重','💪 责任','🌟 勤奋'],
        emk:l==='en'?['🗣️ Language','💻 ICT','🎨 Creativity and Innovation','🌟 Values']:l==='bm'?['🗣️ Bahasa','💻 TMK','🎨 Kreativiti dan Inovasi','🌟 Nilai Murni']:['🗣️ 语言','💻 资讯科技','🎨 创造与创新','🌟 价值观'],"""

if old_sk_sp in html:
    html = html.replace(old_sk_sp, new_sk_sp)
    print('SK/SP gen() updated')
else:
    print('WARNING: SK/SP pattern not found')

# ══════════════════════════════════════════════════════════
# 2. Elaborated ACTS database (50 per language, full descriptions)
# ══════════════════════════════════════════════════════════

# Build elaborated ACTS
ACTS = {}

# --- BM ACTIVITIES (elaborated with multi-sentence descriptions) ---
ACTS['bm'] = {
'i': [
'🎵 Murid menyanyikan lagu bertema yang berkaitan dengan topik pembelajaran yang akan diajar. Guru memimpin nyanyian dengan iringan gitar atau rakaman audio sambil menayangkan lirik lagu di papan putih. Murid diminta membuat gerakan kreatif yang sesuai dengan lirik lagu secara berkumpulan. Selepas nyanyian, guru bersoal jawab dengan murid tentang isi lagu untuk merangsang pemikiran dan mengaitkan dengan topik pembelajaran. [Dif: A - Nyanyi dengan gerakan kreatif dan ubah suai lirik lagu, B - Nyanyi dengan bimbingan lirik dan tunjuk cara guru, C - Dengar lagu sambil menepuk irama mengikut rentak]',
'🎬 Guru menayangkan video pendek (2-3 minit) yang berkaitan dengan topik pembelajaran seperti fenomena alam, situasi harian atau kisah menarik. Sebelum tayangan, guru mengemukakan 2-3 soalan rangsangan untuk membina skema sedia ada murid. Semasa tayangan, murid diminta mengambil nota ringkas atau mengingati maklumat penting. Selepas tayangan, murid dibimbing untuk meneka tajuk pembelajaran berdasarkan isi video dan perkaitan dengan pengalaman sedia ada. [Dif: A - Mengaitkan isi video dengan tajuk pembelajaran dalam ayat lengkap dan memberi contoh, B - Meneka tajuk pembelajaran dalam satu perkataan atau frasa, C - Memadankan gambar dari video dengan tajuk pembelajaran]',
'🧩 Permainan Cari Pasangan dijalankan dengan menyediakan kad bergambar dan kad berperkataan. Setiap murid memegang sekeping kad secara rawak. Apabila guru memberi isyarat, murid bergerak mencari rakan yang memegang kad padanan (gambar dengan perkataan). Pasangan yang lengkap duduk bersama dan membaca kad masing-masing. Aktiviti ini membantu murid menguasai kosa kata baru secara menyeronokkan. [Dif: A - Padan perkataan dengan ayat penerangan yang lengkap, B - Padan gambar dengan perkataan yang betul, C - Padan gambar dengan gambar yang sama]',
'🎭 Guru membawa masuk boneka jari atau puppets dan bercerita dengan intonasi yang menarik dan ekspresi muka yang pelbagai. Boneka dijadikan sebagai alat perantara untuk menyampaikan isi cerita yang berkaitan dengan topik. Semasa bercerita, guru berhenti di bahagian-bahagian tertentu untuk bertanya soalan ramalan. Murid dibimbing meneka watak, jalan cerita, konflik dan pengajaran yang boleh diambil daripada cerita tersebut. [Dif: A - Bercerita semula menggunakan ayat sendiri dengan kreatif, B - Mengulang dialog watak utama dengan intonasi, C - Menamakan watak-watak dalam cerita]',
'🖼️ Guru menyediakan 4-6 keping gambar bersiri yang tidak tersusun. Murid secara berkumpulan diminta menyusun gambar mengikut urutan yang betul berdasarkan pemahaman mereka tentang tema. Selepas selesai menyusun, setiap kumpulan menerangkan jalan cerita yang terbentuk. Guru membimbing murid mengenal pasti urutan yang paling logik dan munasabah. [Dif: A - Menyusun gambar dan menghasilkan cerita lengkap dengan ayat sendiri, B - Menyusun gambar dan membaca ayat penerangan yang disediakan, C - Menyusun gambar mengikut urutan dengan bimbingan]',
'❓ Guru membawa objek maujud atau gambar yang menarik dan berkaitan dengan topik. Objek diletakkan di hadapan kelas atau diedarkan kepada kumpulan. Guru mengemukakan soalan rangsangan seperti "Apa yang kamu nampak?", "Apa yang kamu rasa?" atau "Apakah yang ingin kamu tahu tentang objek ini?" untuk membangkitkan rasa ingin tahu murid. Murid menjawab secara lisan berdasarkan pemerhatian mereka. [Dif: A - Jawab dalam ayat lengkap dengan sebab dan contoh, B - Jawab dalam frasa yang sesuai, C - Menunjuk dan mengangguk atau geleng kepala]',
'🔄 Permainan Cari Perbezaan dijalankan dengan menayangkan dua gambar yang hampir serupa tetapi mempunyai beberapa perbezaan. Murid secara berkumpulan atau individu diminta membandingkan dan mencari sebanyak mungkin perbezaan. Aktiviti ini melatih kemahiran pemerhatian dan tumpuan murid. [Dif: A - Menerangkan perbezaan dalam ayat lengkap, B - Mencari dan menunjuk perbezaan yang ditemui, C - Memadankan objek yang sama dalam kedua-dua gambar]',
'👂 Guru memainkan bunyi atau audio pendek yang berkaitan dengan topik seperti bunyi haiwan, bunyi kenderaan, bunyi alam atau bunyi persekitaran. Murid mendengar dengan teliti dan meneka sumber bunyi tersebut. Aktiviti ini merangsang pendengaran dan meningkatkan kemahiran mendengar aktif dalam kalangan murid. [Dif: A - Meneka dan menghuraikan ciri-ciri bunyi dengan lengkap, B - Meneka sumber bunyi dengan tepat, C - Memilih gambar yang sesuai dengan bunyi yang didengar]',
'🎈 Permainan Bola Berbual: Murid duduk dalam bulatan. Guru memulakan permainan dengan mengemukakan satu soalan sambil memegang bola. Bola dihantar secara rawak kepada murid. Penerima bola perlu menjawab soalan dengan yakin sebelum menghantar bola kepada rakan yang lain. Aktiviti ini membina keyakinan murid untuk bercakap di hadapan kumpulan. [Dif: A - Menjawab soalan KBAT dengan ayat lengkap dan alasan, B - Menjawab soalan mudah dengan frasa, C - Membantu rakan menjawab dengan memberi petunjuk]',
'📦 Kotak Misteri: Guru menyediakan sebuah kotak tertutup yang mengandungi objek berkaitan topik. Murid secara bergilir memasukkan tangan ke dalam kotak dan meraba objek tanpa melihat. Mereka perlu meneka objek berdasarkan deria sentuhan. Selepas meneka, objek dikeluarkan untuk disahkan. Aktiviti ini merangsang rasa ingin tahu dan melatih kemahiran membuat inferens. [Dif: A - Menerangkan ciri-ciri objek yang diraba dengan lengkap, B - Meneka objek dengan tepat, C - Merasa dan menunjuk gambar objek yang sama]',
],
'p': [
'📇 Guru memperkenalkan kosa kata baru menggunakan kad imbasan (flashcards) berwarna dan bersaiz besar. Setiap kad mengandungi gambar yang menarik dan perkataan yang jelas. Guru menunjukkan kad sambil menyebut perkataan dengan sebutan yang betul dan intonasi yang sesuai. Murid mengecam, mengeja dan menyebut perkataan secara kelas, kumpulan dan individu. Kaitkan gambar dengan perkataan untuk memudahkan kefahaman. [Dif: A - Membina ayat menggunakan perkataan baru, B - Menyebut dan mengeja perkataan, C - Mengulang sebutan selepas guru]',
'👥 Perbincangan kumpulan kecil menggunakan teknik Think-Pair-Share (Fikir-Pasang-Kongsi). Guru mengemukakan soalan atau isu berkaitan topik. Murid diberi masa 1-2 minit untuk berfikir secara individu (Think). Kemudian mereka berbincang dengan pasangan (Pair) untuk berkongsi idea. Akhirnya, beberapa pasangan dipilih untuk berkongsi dengan seluruh kelas (Share). [Dif: A - Kongsi idea dalam ayat lengkap dengan alasan, B - Kongsi pandangan dalam frasa ringkas, C - Mendengar dan mengulang idea rakan]',
'🔗 Guru menyediakan kad bergambar dan kad berperkataan. Murid diminta memadankan gambar dengan perkataan yang betul. Aktiviti dilakukan secara individu atau berpasangan di atas meja atau papan putih. Guru membimbing dan memberi maklum balas. Sebut perkataan dengan kuat selepas padanan dibuat. [Dif: A - Padankan dan menulis ayat mudah, B - Padankan dan menyebut perkataan, C - Padankan gambar yang sama]',
'🗣️ Latihan mendengar dan mengulang sebutan frasa penting. Guru menyebut frasa dengan intonasi dan tekanan yang betul. Murid mendengar dengan teliti dan mengulang sebutan secara kelas (choral repetition), kumpulan kecil dan individu. Beri penekanan pada sebutan perkataan sukar dan intonasi ayat. [Dif: A - Menyebut frasa dengan intonasi dan ekspresi yang betul, B - Menyebut frasa mudah dengan bantuan, C - Menyebut perkataan utama]',
'📋 Permainan Kad Kategori: Murid diberikan kad perkataan dan diminta mengelaskannya ke dalam kumpulan yang betul seperti haiwan, tumbuhan, warna atau bentuk. Guru menyediakan kategori di papan tulis atau atas meja. Murid menampal kad di bawah kategori yang betul sambil menyebut perkataan tersebut. [Dif: A - Mengelaskan dan memberi alasan pengelasan, B - Mengelaskan dengan bimbingan rakan, C - Memadankan dengan contoh yang diberi]',
'📝 Latihan lisan secara kelas: Guru menunjukkan gambar atau objek. Murid menjawab secara serentak (choral response) untuk membina keyakinan. Kemudian secara individu untuk penilaian. Guru memberi maklum balas segera. [Dif: A - Jawab dalam ayat lengkap, B - Jawab dalam satu perkataan, C - Angkat tangan atau tunjuk jawapan]',
'🎯 Aktiviti menyusun kad perkataan mengikut kategori masa seperti Minggu, Bulan dan Tahun. Murid diberikan kad-kad perkataan yang bercampur aduk dan diminta menyusun mengikut urutan yang betul secara berkumpulan. [Dif: A - Menyusun dan membina ayat tentang masa, B - Menyusun kad mengikut urutan, C - Memadankan kad dengan gambar]',
'🎲 Permainan papan pendidikan: Murid membaling dadu dan bergerak mengikut bilangan petak. Setiap petak mengandungi soalan berkaitan topik seperti teka perkataan, jawab soalan atau buat ayat. Murid perlu menjawab soalan dengan betul untuk terus bergerak. [Dif: A - Soalan aras KBAT, B - Soalan aras sederhana, C - Membantu rakan menjawab soalan]',
'🃏 Kad Teka: Murid memilih kad dan perlu menerangkan perkataan kepada rakan tanpa menyebut perkataan tersebut. Rakan lain meneka perkataan yang diterangkan. Aktiviti ini melatih kemahiran berfikir dan berkomunikasi. [Dif: A - Menerangkan menggunakan ayat lengkap, B - Menggunakan bahasa badan dan isyarat, C - Menunjukkan gambar kepada rakan]',
'✏️ Murid melukis peta minda ringkas tentang pengetahuan sedia ada berkaitan topik. Guru membimbing murid mengenal pasti idea utama dan idea sampingan. Murid melukis peta minda masing-masing di atas kertas atau menggunakan aplikasi digital. [Dif: A - Peta minda lengkap dengan sub-topik dan cabang, B - Peta minda separa dengan bimbingan, C - Mewarna dan menampal gambar pada peta]',
],
'd': [
'📖 Aktiviti membaca petikan secara berpasangan. Guru menyediakan petikan pada 3 aras kesukaran (mudah, sederhana, mencabar). Murid membaca bergilir dengan pasangan dan membincangkan isi petikan. Guru menyediakan soalan kefahaman beraras yang merangkumi soalan literal, inferensi dan KBAT. Murid menjawab soalan secara lisan atau bertulis. [Dif: A - Membaca petikan aras tinggi dan menjawab soalan KBAT, B - Membaca petikan aras sederhana dan menjawab soalan literal, C - Membaca petikan bergambar dan melukis jawapan]',
'✍️ Menulis karangan atau ayat berpandu dengan menggunakan peta pemikiran i-Think. Murid merancang penulisan menggunakan peta bulatan, peta buih atau peta pokok sebelum menulis. Karangan dihasilkan secara individu atau berpasangan. Guru menyediakan rangka karangan dan senarai semak untuk membimbing murid. [Dif: A - Menulis karangan lengkap dengan isi tersusun dan ayat gramatis, B - Menulis ayat berpandu menggunakan rangka dan frasa, C - Menyusun ayat yang diberikan dan menyalin tulisan]',
'🎭 Aktiviti lakonan (Role Play): Murid melakonkan dialog dalam situasi harian berkaitan topik. Guru menyediakan kad situasi yang pelbagai. Murid merancang dialog secara berkumpulan dan berlatih sebelum melakonkan di hadapan kelas. Guru menilai intonasi, sebutan dan ekspresi. [Dif: A - Mencipta dialog sendiri berdasarkan situasi dengan kreatif, B - Menggunakan dialog yang diberi dengan olahan, C - Melakonkan dialog dengan bimbingan guru]',
'🖼️ Gallery Walk: Hasil kerja murid dipamerkan di atas meja atau dilekat di dinding kelas. Murid berjalan dalam kumpulan melihat hasil kerja rakan sambil mencatat maklumat penting. Mereka meninggalkan komen pada sticky note atau kad feedback. Setiap kumpulan berhenti di setiap stesen selama 2-3 minit. [Dif: A - Menulis komen yang bernas, membina dan spesifik, B - Menulis komen ringkas yang positif, C - Menampal stiker atau tanda pada hasil kerja]',
'📘 Mencipta buku mini (foldable booklet) berdasarkan topik. Guru menyediakan template buku mini daripada sehelai kertas A4. Murid mengisi kandungan buku mengikut kreativiti masing-masing seperti definisi, gambar, contoh dan rumusan. Buku mini mengandungi ringkasan isi pelajaran. [Dif: A - Mengisi kandungan lengkap dengan ayat sendiri dan ilustrasi, B - Mengisi kandungan berpandu soalan dan gambar, C - Mewarna gambar dan menampal label yang diberi]',
'🏫 Aktiviti Stesen Pembelajaran: Murid bergerak dalam kumpulan ke 4-5 stesen yang menyediakan tugasan berbeza. Setiap stesen mengambil masa 5-7 minit. Stesen termasuk stesen membaca, menulis, mewarna, permainan dan kreativiti. Guru memantau dan membimbing di stesen yang memerlukan bantuan. [Dif: A - Stesen cabaran KBAT dengan tugasan kompleks, B - Stesen tugasan sederhana dengan arahan jelas, C - Stesen bimbingan guru dengan bantuan rapat]',
'🧩 Permainan Bahasa: Scrabble, Boggle, Permainan Kad Perkataan atau Silang Kata. Murid bermain dalam kumpulan kecil untuk mengukuhkan kosa kata, ejaan dan struktur ayat. Permainan dijalankan secara pusingan dalam tempoh masa yang ditetapkan. [Dif: A - Membina ayat daripada perkataan yang ditemui, B - Mencari perkataan tersembunyi dalam grid, C - Memadankan huruf untuk membentuk perkataan]',
'🗺️ Mencipta peta minda atau peta pemikiran secara berkumpulan. Gunakan kertas mahjong dan pen marker berwarna. Murid melukis peta minda yang kreatif dengan gambar dan warna. Setiap kumpulan membentangkan peta minda mereka. Hasil kerja dipamerkan di sudut kelas. [Dif: A - Peta minda lengkap dengan sub-topik dan cabang terperinci, B - Peta bulatan dengan idea utama berkaitan, C - Peta bergambar dengan bantuan rakan]',
'💻 Penggunaan aplikasi pendidikan seperti Quizizz, Kahoot!, Google Classroom atau Wordwall. Murid menjawab kuiz interaktif secara individu atau berkumpulan menggunakan telefon bimbit, tablet atau komputer. Soalan merangkumi pelbagai aras kesukaran. Markah dipaparkan secara langsung. [Dif: A - Soalan aras KBAT dengan penaakulan, B - Soalan aras sederhana dengan pilihan, C - Soalan bergambar dengan pilihan jawapan]',
'🎨 Aktiviti kraftangan: Menghasilkan poster, buku skrap, model 3D atau diorama berkaitan topik. Murid menggunakan bahan seperti kertas warna, kotak terbuang, gam, gunting, pensel warna dan bahan kitar semula. Hasil kerja dipamerkan dan dibentangkan. [Dif: A - Menghasilkan kraftangan secara kreatif tanpa contoh, B - Menggunakan template dan contoh yang diberi, C - Membantu mewarna dan menghias]',
'🔬 Eksperimen atau penyiasatan secara berkumpulan. Murid menjalankan aktiviti saintifik untuk menguji hipotesis. Mereka merekod pemerhatian, menganalisis data dan membuat kesimpulan secara berkumpulan. Guru membimbing langkah demi langkah. [Dif: A - Mereka bentuk eksperimen sendiri dengan kawalan pembolehubah, B - Mengikut langkah eksperimen yang disediakan, C - Membantu rakan merekod data dan pemerhatian]',
'📊 Projek berkumpulan: Murid menyiapkan projek secara berkumpulan dan membentangkan hasil kerja. Projek merangkumi penyelidikan, pengumpulan maklumat, analisis dan persembahan kreatif. Tempoh projek 1-2 minggu. [Dif: A - Projek kompleks dengan penyelidikan mendalam dan analisis, B - Projek sederhana dengan bimbingan dan panduan, C - Membantu kumpulan dalam tugasan mudah]',
'🎪 Karnival pembelajaran: Murid menyediakan gerai interaktif berkaitan topik. Setiap kumpulan menguruskan satu gerai dengan aktiviti seperti kuiz, permainan atau pameran. Kelas lain atau guru pelawat melawat gerai-gerai tersebut. [Dif: A - Mengurus dan mengendalikan gerai sepenuhnya, B - Membantu menguruskan gerai dengan bimbingan, C - Melawat dan menyertai aktiviti gerai]',
'📝 Pembelajaran berasaskan projek (PBL): Murid menyiapkan folio atau buku skrap secara berkumpulan. Projek merangkumi tajuk, objektif, kandungan, ilustrasi dan rumusan. Sumber rujukan termasuk buku, internet dan temu bual. [Dif: A - Folio lengkap dengan kandungan terperinci dan kreatif, B - Buku skrap dengan isi berpandu dan contoh, C - Koleksi gambar dan bahan dengan label]',
'🎯 Aktiviti Hot Seat: Seorang murid duduk di kerusi panas di hadapan kelas. Rakan sekelas bertanya soalan berkaitan topik secara bergilir. Murid di kerusi panas perlu menjawab soalan dengan yakin dan jelas. Aktiviti ini melatih keyakinan dan kefasihan. [Dif: A - Memberi soalan yang mencabar dan mendalam, B - Menjawab soalan dengan yakin dan tepat, C - Mencatat jawapan dan membantu rakan]',
],
'ps': [
'👨‍🏫 Pembentangan hasil kerja kumpulan terpilih di hadapan kelas. Wakil kumpulan membentang dengan menggunakan alat bantu seperti poster, slaid atau model. Penerangan merangkumi objektif, proses dan hasil kerja. Kumpulan lain memberi maklum balas dan bertanya soalan. [Dif: A - Membentang dengan yakin, jelas dan kreatif, B - Membentang dengan bimbingan guru dan nota, C - Menunjukkan hasil kerja sambil guru menerangkan]',
'📝 Kuiz Kahoot! atau Quizizz secara berkumpulan atau individu. Soalan kuiz merangkumi pelbagai aras kesukaran daripada aras rendah hingga KBAT. Murid menjawab dalam masa yang ditetapkan. Markah dan kedudukan dipaparkan secara langsung untuk meningkatkan motivasi. [Dif: A - Soalan aras KBAT dengan penaakulan, B - Soalan aras sederhana dengan pilihan, C - Soalan bergambar dengan pilihan jawapan]',
'💬 Sesi refleksi: Murid berkongsi satu perkara yang mereka pelajari pada hari ini secara lisan. Guru meminta beberapa orang murid secara rawak untuk berkongsi. Refleksi boleh juga dilakukan secara bertulis dalam jurnal pembelajaran ringkas. [Dif: A - Berkongsi dalam ayat lengkap dengan contoh dan kaitan, B - Berkongsi dalam frasa ringkas, C - Menunjuk pada gambar atau bahan belajar]',
'✏️ Aktiviti 3-2-1: Murid menulis 3 perkara yang dipelajari, 2 perkara yang menarik dan 1 soalan yang masih tertanya-tanya. Tulis di atas kertas atau sticky note. Kemudian lekatkan pada papan refleksi di sudut kelas. [Dif: A - Menulis lengkap dalam ayat gramatis, B - Menulis isi berpandu soalan bimbingan, C - Melukis gambar dan menulis label]',
'🗣️ Sumbangsaran secara kelas untuk merumuskan isi pelajaran. Guru menulis idea-idea murid di papan putih dalam bentuk peta minda. Murid membincangkan perkaitan antara idea dan membuat rumusan bersama. [Dif: A - Memberi idea bernas yang berhubung kait, B - Setuju atau tidak setuju dengan alasan yang sesuai, C - Mengulang idea yang disebut rakan]',
'⭐ Penilaian rakan sebaya: Murid menilai hasil kerja rakan menggunakan rubrik mudah seperti bintang atau smiley face. Murid memberi komen lisan atau bertulis tentang kekuatan dan cadangan penambahbaikan. [Dif: A - Menggunakan rubrik penilaian dengan tepat dan objektif, B - Memberi bintang dan komen ringkas, C - Menampal stiker pada hasil kerja]',
'📊 Pameran hasil kerja (Mini Exhibition): Semua hasil kerja dipamerkan di sudut kelas atau meja. Murid berjalan melihat pameran secara berkumpulan. Beberapa orang murid dipilih untuk menerangkan hasil kerja mereka kepada pengunjung. [Dif: A - Mengatur dan menyusun pameran dengan kreatif, B - Menerangkan hasil kerja dengan jelas, C - Melawat dan melihat pameran]',
'🎯 Kuiz lisan pantas: Guru mengemukakan soalan spontan secara rawak untuk menguji kefahaman murid. Murid menjawab secara lisan. Soalan merangkumi pelbagai aras daripada soalan mudah hingga KBAT. [Dif: A - Soalan KBAT yang mencabar pemikiran, B - Soalan aras sederhana, C - Soalan mudah dengan bantuan dan petunjuk]',
'🔄 Aktiviti Round Table: Setiap murid dalam kumpulan menulis satu idea secara bergilir pada sehelai kertas. Kertas dipusingkan mengikut arah jam sehingga semua ahli kumpulan memberi sumbangan. Hasil dikongsi dengan kelas. [Dif: A - Menulis idea lengkap dalam ayat gramatis, B - Menulis kata kunci berkaitan topik, C - Melukis gambar berkaitan idea]',
'💭 Refleksi bertulis dalam jurnal pembelajaran ringkas. Murid menulis apa yang dipelajari, apa yang menarik dan apa yang masih kurang jelas. Guru membaca dan memberi komen dan galakan. [Dif: A - Menulis perenggan penuh dengan refleksi mendalam, B - Menulis beberapa ayat mudah, C - Melukis gambar dan menulis label]',
],
'c': [
'📋 Rumusan isi penting: Guru membimbing murid melengkapkan peta konsep atau peta i-Think. Murid mengisi tempat kosong dengan maklumat yang betul berdasarkan pembelajaran hari ini. Rumusan dibuat secara kolaboratif oleh seluruh kelas. [Dif: A - Melengkapkan peta konsep sendiri tanpa bantuan, B - Mengisi separuh daripada peta dengan bimbingan, C - Mewarnakan dan menampal label pada peta]',
'🎫 Exit Ticket: Murid menulis jawapan pada kertas kecil atau sticky note sebelum keluar kelas. Soalan mudah seperti Satu perkara yang saya belajar hari ini... atau Saya masih kabur tentang... Guru mengumpul dan menyemak exit ticket untuk menilai kefahaman. [Dif: A - Menulis jawapan dalam ayat lengkap, B - Menulis perkataan atau frasa, C - Melukis gambar dan menulis label]',
'✅ Permainan Betul atau Salah: Guru menyatakan beberapa kenyataan berkaitan topik. Murid berdiri jika betul dan duduk jika salah. Atau menggunakan kad hijau (betul) dan kad merah (salah). Aktiviti ini menyeronokkan dan menguji kefahaman dengan cepat. [Dif: A - Memberi alasan kenapa betul atau salah, B - Menjawab betul atau salah dengan yakin, C - Meniru tindakan rakan]',
'🙏 Doa dan nyanyian lagu penutup. Refleksi secara lisan oleh 2-3 orang murid terpilih. Guru memimpin doa dan murid mengaminkan. Suasana pembelajaran ditutup dengan positif. [Dif: A - Memimpin doa dan memberi refleksi, B - Berkongsi refleksi ringkas, C - Mendengar dan mengaminkan doa]',
'📚 Guru memberikan latihan pengukuhan sebagai kerja rumah. Latihan berasaskan topik yang dipelajari. Guru menerangkan arahan dengan jelas dan memberi contoh. Murid menyimpan latihan dalam beg untuk dibuat di rumah. [Dif: A - Latihan KBAT dan penyelesaian masalah, B - Latihan aras sederhana, C - Latihan asas pengukuhan]',
'🔮 Preview pembelajaran seterusnya: Guru menunjukkan gambar atau mengemukakan soalan teaser tentang topik akan datang. Murid meramal apa yang akan dipelajari untuk membangkitkan minat dan rasa ingin tahu. [Dif: A - Meramal dalam ayat lengkap, B - Meramal dalam satu perkataan, C - Melihat gambar dengan bimbingan]',
'🎯 Murid melengkapkan What Stuck With You Today? pada sticky note. Mereka menulis konsep atau kemahiran yang paling diingati daripada pembelajaran hari ini. Sticky note dilekatkan pada papan khas di sudut kelas. [Dif: A - Menulis dalam ayat lengkap dan jelas, B - Menulis frasa pendek, C - Melukis gambar]',
'🔄 Sesi soal jawab pantas menggunakan papan putih mini. Guru bertanya soalan berkaitan topik. Murid menulis jawapan pada papan dan menunjukkan serentak. Guru memberi maklum balas segera. Aktiviti ini membolehkan guru menilai kefahaman semua murid dengan cepat. [Dif: A - Soalan KBAT yang mencabar, B - Soalan aras sederhana, C - Menunjukkan jawapan yang ditulis]',
'⭐ Murid meletakkan magnet atau penanda pada carta Tahap Kefahaman yang mengandungi tiga bahagian: Faham, Ragu-ragu dan Tidak Faham. Guru dapat melihat secara visual tahap kefahaman kelas dan merancang tindakan susulan. [Dif: A - Menerangkan pilihan tahap kefahaman, B - Meletakkan magnet pada tahap sendiri, C - Membantu rakan meletakkan magnet]',
'✏️ Jurnal refleksi harian: Murid menulis satu perenggan pendek tentang pembelajaran hari ini. Fokus pada apa yang dipelajari, apa yang dirasai dan apa yang akan dilakukan. Guru membaca dan memberi komen motivasi. [Dif: A - Menulis perenggan lengkap dengan refleksi, B - Menulis 3 ayat mudah, C - Melukis gambar berserta label]',
],
}

# --- EN ACTIVITIES ---
ACTS['en'] = {'i': [
'🎵 Sing a themed song related to the learning topic. Teacher leads the singing with guitar accompaniment or audio recording while displaying lyrics on the whiteboard. Pupils create creative movements that match the lyrics in groups. After singing, the teacher asks questions about the song content to stimulate thinking and connect to the lesson topic. [Diff: A - Create new verses with creative movements, B - Sing with guided lyrics and teacher demonstration, C - Clap along to the rhythm]',
'🎬 Show a short video (2-3 minutes) related to the topic such as natural phenomena, daily situations or interesting stories. Before viewing, the teacher poses 2-3 stimulus questions to activate prior knowledge. During viewing, pupils take brief notes or remember important information. After viewing, pupils are guided to guess the lesson topic based on the video content. [Diff: A - Relate video content to topic in full sentences with examples, B - Guess topic in one word or phrase, C - Match pictures from video to topic]',
'🧩 Find Your Partner game: Prepare picture cards and word cards. Each pupil holds one card randomly. When the teacher signals, pupils move around to find their matching partner (picture with word). Complete pairs sit together and read their cards aloud. This activity helps pupils master new vocabulary in a fun way. [Diff: A - Match word with sentence description, B - Match picture with correct word, C - Match identical pictures]',
'🎭 The teacher uses finger puppets or hand puppets to tell a story with engaging intonation and varied facial expressions. Puppets serve as mediators to deliver story content related to the topic. During storytelling, the teacher pauses at certain parts to ask prediction questions. Pupils are guided to guess characters, plot and moral values. [Diff: A - Retell story using own words creatively, B - Repeat main character dialogues with intonation, C - Name the characters in the story]',
'🖼️ Prepare 4-6 jumbled picture series. Pupils work in groups to arrange the pictures in the correct sequence based on their understanding of the theme. After arranging, each group explains the story formed. The teacher guides pupils to identify the most logical sequence. [Diff: A - Arrange pictures and produce a complete story with own sentences, B - Arrange pictures and read provided sentences, C - Arrange pictures in order with guidance]',
'❓ Bring real objects or interesting pictures related to the topic. Objects are placed in front of the class or distributed to groups. The teacher poses stimulus questions like What do you see?, What do you feel? or What do you want to know? to arouse curiosity. Pupils answer orally based on their observations. [Diff: A - Answer in full sentences with reasons and examples, B - Answer in appropriate phrases, C - Point and nod or shake head]',
'🔄 Spot the Difference game: Show two similar pictures with several differences. Pupils in groups or individually compare and find as many differences as possible. This activity trains observational skills and concentration. [Diff: A - Explain differences in full sentences, B - Find and point to the differences, C - Match identical objects in both pictures]',
'👂 Play sounds or short audio related to the topic such as animal sounds, vehicle sounds, nature sounds or environmental sounds. Pupils listen carefully and identify the sound source. This activity stimulates listening skills and improves active listening. [Diff: A - Guess and describe sound characteristics in detail, B - Identify the sound source accurately, C - Choose the correct picture matching the sound]',
'🎈 Talking Ball game: Pupils sit in a circle. The teacher starts by posing a question while holding a ball. The ball is passed randomly. The receiver must answer confidently before passing to another friend. This activity builds pupils\' confidence to speak in front of a group. [Diff: A - Answer HOTS questions in full sentences with reasons, B - Answer simple questions in phrases, C - Help a friend answer by giving clues]',
'📦 Mystery Box: Prepare a closed box containing objects related to the topic. Pupils take turns putting their hand into the box and feeling the object without looking. They guess the object based on touch. After guessing, the object is revealed to confirm. This activity stimulates curiosity and trains inference skills. [Diff: A - Describe the characteristics of the object thoroughly, B - Guess the object accurately, C - Feel and point to the matching picture]',
],
'p': [
'📇 Introduce new vocabulary using colorful large-sized flashcards. Each card contains an attractive picture and clear text. The teacher shows the card while pronouncing the word correctly with proper intonation. Pupils recognize, spell and say the words in class, group and individually. Connect pictures with words for easier understanding. [Diff: A - Create sentences using the new words, B - Say and spell the words correctly, C - Repeat after the teacher]',
'👥 Small group discussion using the Think-Pair-Share technique. The teacher poses a question or issue related to the topic. Pupils are given 1-2 minutes to think individually (Think). Then they discuss with a partner (Pair) to share ideas. Finally, selected pairs share with the whole class (Share). [Diff: A - Share ideas in full sentences with reasons, B - Share opinions in short phrases, C - Listen and repeat a friend\'s idea]',
'🔗 Prepare picture cards and word cards. Pupils match pictures with the correct words. This is done individually or in pairs on a table or whiteboard. The teacher guides and gives feedback. Say the word aloud after matching. [Diff: A - Match and write a simple sentence, B - Match and say the word, C - Match identical pictures]',
'🗣️ Listen and repeat key phrases drill. The teacher says phrases with correct intonation and stress. Pupils listen carefully and repeat in class (choral repetition), small groups and individually. Emphasize difficult word pronunciation and sentence intonation. [Diff: A - Say phrases with correct intonation and expression, B - Say simple phrases with help, C - Say key words]',
'📋 Category Cards game: Pupils are given word cards and asked to sort them into correct groups such as animals, plants, colours or shapes. The teacher provides categories on the board or table. Pupils paste cards under the correct category while saying the word. [Diff: A - Sort and give reasons for the classification, B - Sort with a friend\'s guidance, C - Match with given examples]',
'📝 Choral oral practice: The teacher shows pictures or objects. Pupils respond in chorus to build confidence. Then individually for assessment. The teacher gives immediate feedback. [Diff: A - Answer in full sentences, B - Answer in one word, C - Raise hand or point to the answer]',
'🎯 Arrange word cards according to time categories (Days, Months, Years). Pupils are given mixed word cards and asked to arrange them in correct order in groups. [Diff: A - Arrange and create sentences about time, B - Arrange cards in correct order, C - Match cards with pictures]',
'🎲 Educational board game: Pupils roll a die and move according to the number. Each space contains a question about the topic such as guess the word, answer a question or make a sentence. Pupils must answer correctly to continue moving. [Diff: A - HOTS level questions, B - Standard level questions, C - Help a friend answer]',
'🃏 Taboo word game: Pupils pick a card and must describe the word to a friend without saying the word itself. Other friends guess the described word. This activity trains thinking and communication skills. [Diff: A - Describe using full sentences, B - Use body language and gestures, C - Show the picture to a friend]',
'✏️ Draw a simple mind map of prior knowledge about the topic. The teacher guides pupils to identify main ideas and supporting details. Pupils draw their own mind maps on paper or using digital apps. [Diff: A - Complete mind map with sub-topics and branches, B - Partial mind map with guidance, C - Colour and paste pictures on the map]',
],
'd': [
'📖 Read a short passage in pairs. The teacher prepares passages at 3 difficulty levels (easy, standard, challenging). Pupils take turns reading with partners and discuss the content. The teacher provides differentiated comprehension questions covering literal, inferential and HOTS levels. Pupils answer orally or in writing. [Diff: A - Read high-level passage and answer HOTS questions, B - Read standard passage and answer literal questions, C - Read picture passage and draw answers]',
'✍️ Write a paragraph using i-Think thinking maps (Circle Map, Bubble Map, Tree Map). Pupils plan their writing using the map before writing. Writing is done individually or in pairs. The teacher provides a writing frame and checklist to guide pupils. [Diff: A - Write complete paragraph with organized content and correct grammar, B - Write guided sentences using frames and phrases, C - Arrange given sentences and trace the writing]',
'🎭 Role-play activity: Pupils act out dialogues in daily situations related to the topic. The teacher provides various situation cards. Pupils plan dialogues in groups and practice before performing in front of the class. The teacher assesses intonation, pronunciation and expression. [Diff: A - Create own dialogue based on situation creatively, B - Use given dialogue with adaptation, C - Act out dialogue with teacher guidance]',
'🖼️ Gallery Walk: Pupils\' work is displayed on desks or walls. Pupils walk in groups to view friends\' work while noting important information. They leave comments on sticky notes or feedback cards. Each group stops at each station for 2-3 minutes. [Diff: A - Write constructive, specific and meaningful comments, B - Write short positive comments, C - Paste stickers or marks on work]',
'📘 Create a mini booklet (foldable) based on the topic. The teacher provides a booklet template from an A4 paper. Pupils fill in the content creatively including definitions, pictures, examples and summaries. The mini booklet contains a summary of the lesson. [Diff: A - Fill in complete content with own sentences and illustrations, B - Fill in guided content with questions and pictures, C - Colour pictures and paste given labels]',
'🏫 Station-Based Learning: Pupils move in groups to 4-5 stations with different tasks. Each station takes 5-7 minutes. Stations include reading, writing, colouring, games and creativity. The teacher monitors and guides at stations needing help. [Diff: A - HOTS challenge station with complex tasks, B - Standard task station with clear instructions, C - Teacher guided station with close support]',
'🧩 Language Games: Scrabble, Boggle, Word Card Games or Crosswords. Pupils play in small groups to reinforce vocabulary, spelling and sentence structure. Games rotate among groups within a set time period. [Diff: A - Create sentences from found words, B - Find hidden words in grids, C - Match letters to form words]',
'🗺️ Create a mind map or thinking map in groups. Use mahjong paper and coloured markers. Pupils draw creative mind maps with pictures and colours. Each group presents their mind map. Work is displayed in the class corner. [Diff: A - Complete mind map with sub-topics and detailed branches, B - Circle map with related main ideas, C - Picture map with a friend\'s help]',
'💻 Use educational apps like Quizizz, Kahoot!, Google Classroom or Wordwall. Pupils answer interactive quizzes individually or in groups using mobile phones, tablets or computers. Questions cover various difficulty levels. Scores are displayed live. [Diff: A - HOTS level questions with reasoning, B - Standard level questions with choices, C - Picture questions with answer choices]',
'🎨 Craft activity: Create posters, scrapbooks, 3D models or dioramas related to the topic. Pupils use materials like coloured paper, recycled boxes, glue, scissors, colour pencils and recycled materials. Work is displayed and presented. [Diff: A - Create craft creatively without example, B - Use given template and example, C - Help colour and decorate]',
'🔬 Experiment or investigation in groups. Pupils conduct scientific activities to test hypotheses. They record observations, analyse data and draw conclusions in groups. The teacher guides step by step. [Diff: A - Design own experiment with variable control, B - Follow provided experiment steps, C - Help friends record data and observations]',
'📊 Group project: Pupils complete a project in groups and present their work. The project includes research, information gathering, analysis and creative presentation. Project duration is 1-2 weeks. [Diff: A - Complex project with in-depth research and analysis, B - Standard project with guidance and guidelines, C - Help the group with simple tasks]',
'🎪 Learning Carnival: Pupils set up interactive booths related to the topic. Each group manages a booth with activities like quizzes, games or exhibitions. Other classes or visiting teachers visit the booths. [Diff: A - Fully manage and run a booth independently, B - Help manage the booth with guidance, C - Visit and participate in booth activities]',
'📝 Project-Based Learning (PBL): Pupils complete a folio or scrapbook in groups. The project includes title, objectives, content, illustrations and summary. Reference sources include books, internet and interviews. [Diff: A - Complete folio with detailed and creative content, B - Scrapbook with guided content and examples, C - Collection of pictures and materials with labels]',
'🎯 Hot Seat activity: One pupil sits in the hot seat in front of the class. Classmates take turns asking questions about the topic. The pupil in the hot seat must answer confidently and clearly. This activity builds confidence and fluency. [Diff: A - Ask challenging and in-depth questions, B - Answer questions confidently and accurately, C - Record answers and help a friend]',
],
'ps': [
'👨‍🏫 Selected groups present their work in front of the class. Group representatives present using aids like posters, slides or models. The explanation covers objectives, process and outcomes. Other groups give feedback and ask questions. [Diff: A - Present confidently, clearly and creatively, B - Present with teacher guidance and notes, C - Display work while teacher explains]',
'📝 Quick quiz using Kahoot! or Quizizz individually or in groups. Questions cover various difficulty levels from basic to HOTS. Pupils answer within the time limit. Scores and rankings are displayed live to increase motivation. [Diff: A - HOTS level questions with reasoning, B - Standard level questions with choices, C - Picture questions with answer choices]',
'💬 Reflection circle: Each pupil shares one thing they learned today orally. The teacher randomly selects a few pupils to share. Reflection can also be done in writing in a short learning journal. [Diff: A - Share in full sentences with examples and connections, B - Share in short phrases, C - Point to pictures or learning materials]',
'✏️ 3-2-1 activity: Pupils write 3 things learned, 2 interesting things and 1 question still wondering about. Write on paper or sticky note. Then post on the reflection board in the class corner. [Diff: A - Write completely in correct sentences, B - Write guided content with prompt questions, C - Draw pictures and write labels]',
'🗣️ Class brainstorming to summarise the lesson. The teacher writes pupils\' ideas on the whiteboard in a mind map format. Pupils discuss connections between ideas and make conclusions together. [Diff: A - Give insightful and connected ideas, B - Agree or disagree with appropriate reasons, C - Repeat friends\' ideas]',
'⭐ Peer assessment: Pupils assess friends\' work using a simple rubric like stars or smiley faces. Pupils give oral or written comments about strengths and suggestions for improvement. [Diff: A - Use assessment rubric accurately and objectively, B - Give stars and short comments, C - Paste stickers on work]',
'📊 Mini Exhibition: All work is displayed in the class corner or on tables. Pupils walk around viewing the exhibition in groups. A few pupils are selected to explain their work to visitors. [Diff: A - Set up and organise the exhibition creatively, B - Explain the work clearly, C - Visit and view the exhibition]',
'🎯 Quick oral quiz: The teacher poses spontaneous questions randomly to test understanding. Pupils answer orally. Questions cover various levels from simple to HOTS. [Diff: A - Challenging HOTS questions that stimulate thinking, B - Standard level questions, C - Simple questions with help and clues]',
'🔄 Round Table activity: Each pupil in a group writes one idea in turn on a piece of paper. The paper is rotated clockwise until all group members contribute. Results are shared with the class. [Diff: A - Write complete ideas in grammatically correct sentences, B - Write related keywords, C - Draw related pictures]',
'💭 Written reflection in a short learning journal. Pupils write what they learned, what was interesting and what is still unclear. The teacher reads and gives comments and encouragement. [Diff: A - Write a full paragraph with deep reflection, B - Write a few simple sentences, C - Draw pictures and write labels]',
],
'c': [
'📋 Summary using a mind map or i-Think map. The teacher guides pupils to complete the concept map. Pupils fill in blanks with correct information based on today\'s learning. The summary is done collaboratively by the whole class. [Diff: A - Complete the concept map independently, B - Fill in half of the map with guidance, C - Colour and paste labels on the map]',
'🎫 Exit Ticket: Pupils write answers on small paper or sticky note before leaving class. Simple questions like One thing I learned today... or I\'m still confused about... The teacher collects and checks exit tickets to assess understanding. [Diff: A - Write answer in full sentences, B - Write words or phrases, C - Draw picture and write labels]',
'✅ True or False game: The teacher states several statements related to the topic. Pupils stand if true and sit if false. Or use green cards (true) and red cards (false). This fun activity quickly tests understanding. [Diff: A - Give reasons for true or false, B - Answer true or false confidently, C - Follow friends\' actions]',
'🙏 Closing prayer or song. Oral reflection by 2-3 selected pupils. The teacher leads the prayer and pupils respond. The learning session ends on a positive note. [Diff: A - Lead the prayer and give a reflection, B - Share a short reflection, C - Listen and respond to the prayer]',
'📚 The teacher assigns homework for reinforcement. Homework is based on the topic learned. The teacher explains instructions clearly and gives examples. Pupils keep homework in their bags. [Diff: A - HOTS and problem-solving homework, B - Standard level homework, C - Basic reinforcement homework]',
'🔮 Preview the next lesson: The teacher shows a picture or poses a teaser question about the next topic. Pupils predict what they will learn to arouse interest and curiosity. [Diff: A - Predict in full sentences, B - Predict in one word, C - Look at the picture with guidance]',
'🎯 Pupils complete What Stuck With You Today? on a sticky note. They write the concept or skill they remember most from today\'s learning. Sticky notes are posted on a special board in the class corner. [Diff: A - Write in clear full sentences, B - Write short phrases, C - Draw a picture]',
'🔄 Quick Q&A session using mini whiteboards. The teacher asks questions related to the topic. Pupils write answers on whiteboards and show simultaneously. The teacher gives immediate feedback. This activity allows the teacher to quickly assess all pupils\' understanding. [Diff: A - Challenging HOTS questions, B - Standard level questions, C - Show the written answer]',
'⭐ Pupils place a magnet or marker on the Understanding Level chart which has three sections: Understand, Unsure and Don\'t Understand. The teacher can visually see the class understanding level and plan follow-up actions. [Diff: A - Explain the understanding level choice, B - Place the magnet on own level, C - Help a friend place the magnet]',
'✏️ Daily reflection journal: Pupils write a short paragraph about today\'s learning. Focus on what was learned, how it felt and what will be done. The teacher reads and gives motivating comments. [Diff: A - Write a complete paragraph with reflection, B - Write 3 simple sentences, C - Draw a picture with labels]',
],
}

# --- ZH ACTIVITIES ---
ACTS['zh'] = {'i': [
'🎵 学生唱与主题相关的歌曲。教师用吉他或录音带领，同时在白板上显示歌词。学生分组创作与歌词匹配的创意动作。唱完后，教师就歌曲内容提问以激发思维并联系课程主题。[分层: A - 自创新歌词和创意动作, B - 在指导下唱歌并跟随示范, C - 拍手跟节奏]',
'🎬 播放与主题相关的短视频（2-3分钟），如自然现象、日常情境或有趣故事。观看前教师提出2-3个引导性问题以激活先备知识。观看时学生做简要笔记或记住重要信息。观看后学生根据视频内容猜测课程主题。[分层: A - 用完整句子联系视频内容和主题并举例, B - 用一个词或短语猜主题, C - 将视频中的图片与主题匹配]',
'🧩 找朋友游戏：准备图片卡和词语卡。每个学生随机拿一张卡。教师发出信号后，学生走动找到配对的伙伴（图片配词语）。配对的伙伴坐在一起读卡。这个活动帮助学生以有趣的方式掌握新词汇。[分层: A - 将词语与句子描述配对, B - 将图片与正确词语配对, C - 将相同图片配对]',
'🎭 教师使用手指玩偶或手偶以吸引人的语调和多变的面部表情讲故事。玩偶作为媒介来传递与主题相关的内容。讲故事时教师在特定部分停下来问预测性问题。学生猜测角色、情节和可吸取的道德价值观。[分层: A - 用自己的话创造性地复述故事, B - 用语调重复主要角色的对话, C - 说出故事中角色的名字]',
'🖼️ 准备4-6张顺序打乱的图片。学生分组根据对主题的理解将图片按正确顺序排列。排列后每组解释形成的故事情节。教师引导学生识别最逻辑的顺序。[分层: A - 排列图片并用自己句子创作完整故事, B - 排列图片并读提供的句子, C - 在指导下排列顺序]',
'❓ 带与主题相关的实物或有趣图片。物品放在班前或分发给小组。教师提出引导性问题如你看到了什么？你感觉到了什么？或你想知道什么？以激发好奇心。学生根据观察口头回答。[分层: A - 用完整句子回答并给原因和例子, B - 用适当短语回答, C - 指认并点头或摇头]',
'🔄 找不同游戏：展示两幅相似的图片，有几处不同。学生分组或个人比较并找出尽可能多的不同。这个活动训练观察能力和注意力。[分层: A - 用完整句子解释不同之处, B - 找出并指出不同, C - 匹配两幅图中的相同物体]',
'👂 播放与主题相关的声音或简短音频，如动物叫声、车辆声、自然声或环境声。学生仔细听并辨认声音来源。这个活动刺激听觉技能并提高主动聆听能力。[分层: A - 猜测并详细描述声音特征, B - 准确辨认声音来源, C - 选择匹配声音的正确图片]',
'🎈 传话球游戏：学生坐成圆圈。教师拿着球开始提问。球被随机传递。接球者必须自信地回答再传给下一个。这个活动建立学生在小组前说话的自信心。[分层: A - 用完整句子回答高阶思维问题并给理由, B - 用短语回答简单问题, C - 用提示帮助朋友回答]',
'📦 神秘箱：准备一个封闭的箱子，里面装有与主题相关的物品。学生轮流把手伸进箱子，不看不摸物品并凭触觉猜。猜完后拿出物品确认。这个活动激发好奇心并训练推理能力。[分层: A - 全面描述物品的特征, B - 准确猜出物品, C - 触摸并指向匹配的图片]',
],
'p': [
'📇 使用彩色大号字卡介绍新词汇。每张卡包含吸引人的图片和清晰的文字。教师展示卡片并正确发音。学生以全班、小组和个人形式认读、拼写和说出词语。将图片与词语联系起来以便理解。[分层: A - 用新词造句, B - 正确说出和拼写词语, C - 跟教师重复]',
'👥 使用Think-Pair-Share技巧进行小组讨论。教师提出与主题相关的问题或议题。学生有1-2分钟独立思考（Think）。然后与同伴讨论（Pair）分享想法。最后选定的几组与全班分享（Share）。[分层: A - 用完整句子分享想法并给理由, B - 用短语分享观点, C - 听并重复朋友的想法]',
'🔗 准备图片卡和词语卡。学生在桌子或白板上将图片与正确词语配对。教师指导并给反馈。配对后大声说词语。[分层: A - 配对并写简单句子, B - 配对并说出词语, C - 配相同的图片]',
'🗣️ 听和重复关键短语的练习。教师用正确语调和重音说短语。学生以全班、小组和个人形式仔细听和重复。强调难词的发音和句子语调。[分层: A - 用正确语调和表情说短语, B - 在帮助下说简单短语, C - 说关键的词]',
'📋 分类卡游戏：学生拿到词语卡需要分类到正确的组别如动物、植物、颜色或形状。教师在白板或桌子上提供类别。学生将卡贴在正确类别下同时说出词语。[分层: A - 分类并给出分类理由, B - 在朋友指导下分类, C - 匹配给的例子]',
'📝 全班口头练习：教师展示图片或物品。学生齐声回答以建立信心。然后个别回答以进行评估。教师即时反馈。[分层: A - 用完整句子回答, B - 用一个词回答, C - 举手或指向答案]',
'🎯 按时间类别（日、月、年）排列词语卡。学生拿到打乱的词语卡，分组按正确顺序排列。[分层: A - 排列并用时间造句, B - 按正确顺序排列卡, C - 将卡与图片匹配]',
'🎲 教育棋盘游戏：学生掷骰子并按数字移动。每个格子包含与主题相关的问题如猜词、回答问题或造句。学生必须正确回答才能继续移动。[分层: A - 高阶思维水平题, B - 标准水平题, C - 帮助朋友回答]',
'🃏 禁忌词游戏：学生选一张卡，必须向朋友描述这个词但不能说出这个词。其他朋友猜被描述的词。这个活动训练思维和沟通能力。[分层: A - 用完整句子描述, B - 用身体语言和手势, C - 向朋友展示图片]',
'✏️ 画一个关于主题先备知识的简单思维导图。教师引导学生识别主要思想和辅助细节。学生在纸上或用数字应用画自己的思维导图。[分层: A - 带子主题和分支的完整导图, B - 有引导的部分导图, C - 在导图上涂色和贴图片]',
],
'd': [
'📖 结对阅读短文。教师准备3个难度级别（容易、标准、挑战）的短文。学生与同伴轮流阅读并讨论内容。教师提供分层理解题涵盖字面、推理和高阶思维水平。学生口头或书面回答。[分层: A - 读高级短文回答高阶思维题, B - 读标准短文回答字面题, C - 读图画短文画答案]',
'✍️ 使用i-Think思维图（圆圈图、气泡图、树状图）写段落。学生写之前用思维图规划写作。个人或结对照写。教师提供写作框架和检查清单指导。[分层: A - 写内容组织良好语法正确的完整段落, B - 用框架和短语写引导句, C - 排列给的句子并描写]',
'🎭 角色扮演活动：学生表演与主题相关的日常情景对话。教师提供各种情景卡。学生分组设计对话并练习后在班前表演。教师评估语调、发音和表情。[分层: A - 根据情景创造性地创作自己的对话, B - 用给对话并改编, C - 在教师指导下表演对话]',
'🖼️ 画廊漫步：学生作品展示在桌子上或墙上。学生分组走动看朋友作品并记录重要信息。他们在便利贴或反馈卡上留言。每组在每站停2-3分钟。[分层: A - 写有建设性、具体和有意义的评论, B - 写简短积极评论, C - 在作品上贴贴纸或标记]',
'📘 基于主题制作折叠小书。教师用A4纸提供小书模板。学生创造性地填写内容包括定义、图片、例子和总结。小书包含课堂摘要。[分层: A - 用自己的话和插图填写完整内容, B - 用问题和图片填写引导内容, C - 涂色并贴给的标签]',
'🏫 站点式学习：学生分组轮流到4-5个不同任务的站点。每站5-7分钟。站点包括阅读、写作、涂色、游戏和创意。教师监测并在需要帮助的站点指导。[分层: A - 带复杂任务的高阶思维挑战站, B - 带明确指示的标准任务站, C - 带密切支持的教师辅导站]',
'🧩 语言游戏：Scrabble、Boggle、词语卡游戏或填字游戏。学生分组玩以加强词汇、拼写和句子结构。游戏在规定时间内轮换。[分层: A - 用找到的词造句, B - 在网格中找隐藏的词, C - 匹配字母组成词]',
'🗺️ 分组创建思维导图或思考图。用马尼拉纸和彩色马克笔。学生画带图片和颜色的创意思维导图。每组呈现自己的导图。作品展示在教室角落。[分层: A - 完整导图带子主题和详细分支, B - 带相关主要思想的圆圈图, C - 在朋友帮助下画图]',
'💻 使用Quizizz、Kahoot!、Google Classroom或Wordwall等教育应用。学生用手机、平板或电脑个人或分组回答互动测验。问题涵盖各种难度。分数实时显示。[分层: A - 带推理的高阶思维题, B - 带选项的标准题, C - 带答案选项的图片题]',
'🎨 手工艺活动：制作与主题相关的海报、剪贴簿、3D模型或立体模型。学生用彩纸、回收盒、胶水、剪刀、彩铅和回收材料。作品展示和呈现。[分层: A - 没有范例创造性地制作手工艺, B - 用给的模板和范例, C - 帮助涂色和装饰]',
'🔬 小组实验或调查。学生进行科学活动以验证假设。他们分组记录观察、分析数据并得出结论。教师逐步指导。[分层: A - 用变量控制设计自己的实验, B - 按提供的实验步骤操作, C - 帮助朋友记录数据和观察]',
'📊 小组项目：学生分组完成项目并呈现作品。项目包括研究、信息收集、分析和创意呈现。项目为期1-2周。[分层: A - 有深入研究和分析的复杂项目, B - 有指导的标准项目, C - 帮助小组完成简单任务]',
'🎪 学习嘉年华：学生设置与主题相关的互动展位。每组管理一个展位，活动包括测验、游戏或展览。其他班或教师参观展位。[分层: A - 独立完全管理和运营展位, B - 在指导下帮助管理展位, C - 参观和参与展位活动]',
'📝 项目式学习：学生分组完成文件夹或剪贴簿。项目包括标题、目标、内容、插图和总结。参考来源包括书籍、互联网和访谈。[分层: A - 内容和创意详细的完整文件夹, B - 有引导内容的剪贴簿, C - 带标签的图片和材料收集]',
'🎯 热座活动：一名学生坐在班前的热座上。同学轮流问与主题相关的问题。热座上的学生必须自信清晰地回答。这个活动建立自信心和流利度。[分层: A - 问有挑战性和深度的问题, B - 自信准确回答, C - 记录答案并帮助朋友]',
],
'ps': [
'👨‍🏫 选定小组在班前呈现作品。小组代表用海报、幻灯片或模型等辅助工具呈现。解释涵盖目标、过程和成果。其他组给反馈和提问。[分层: A - 自信、清晰、创造性地呈现, B - 在教师指导和不记帮助下呈现, C - 展示作品由教师解释]',
'📝 使用Kahoot!或Quizizz进行个人或小组快速测验。问题涵盖从基础到高阶思维的各种难度。学生在限定时间内作答。分数和排名实时显示以提高动力。[分层: A - 带推理的高阶思维题, B - 带选项的标准题, C - 带答案选项的图片题]',
'💬 反射圈：每位学生口头分享今天学到的一件事。教师随机选几位学生分享。反射也可以在学习日志中书面完成。[分层: A - 用完整句子分享并举例和联系, B - 用短语简短分享, C - 指向图片或学习材料]',
'✏️ 3-2-1活动：学生写3件学到的事、2件有趣的事和1个仍然想知道的问题。写在纸或便利贴上。然后贴在教室角落的反射板上。[分层: A - 用正确句子完整写, B - 用提示问题写引导内容, C - 画图并写标签]',
'🗣️ 全班集思广益总结课程。教师以思维导图格式把学生想法写在白板上。学生讨论想法之间的联系并一起做结论。[分层: A - 给有洞察力和联系的想法, B - 用适当理由同意或不同意, C - 复述朋友的想法]',
'⭐ 同伴互评：学生用简单量规如星星或笑脸评估朋友的作品。学生就给优势和改进建议给出口头或书面评论。[分层: A - 准确客观地使用评估量规, B - 给星星和短评, C - 在作品上贴贴纸]',
'📊 迷你展览：所有作品展示在教室角落或桌子上。学生分组走动看展览。选几位学生向参观者解释他们的作品。[分层: A - 创造性地布置和组织展览, B - 清晰解释作品, C - 参观和看展览]',
'🎯 快速口头测验：教师随机提出即兴问题以测试理解。学生口头回答。问题涵盖从简单到高阶思维的各种水平。[分层: A - 挑战思维的进阶题, B - 标准水平题, C - 有帮助和提示的简单题]',
'🔄 圆桌活动：小组中每位学生轮流在一张纸上写一个想法。纸按顺时针方向轮转直到所有组员都贡献。与全班分享结果。[分层: A - 用语法正确的句子写完整想法, B - 写相关的关键词, C - 画相关图片]',
'💭 在简短学习日志中写书面反思。学生写学到了什么、什么有趣以及什么还不清楚。教师阅读并给评论和鼓励。[分层: A - 写带深度反思的完整段落, B - 写几个简单句子, C - 画图并写标签]',
],
'c': [
'📋 用思维图或i-Think图总结。教师引导学生完成概念图。学生根据今天的学习用正确信息填空。全班合作完成总结。[分层: A - 独立完成概念图, B - 在指导下填一半图, C - 涂色并在图上贴标签]',
'🎫 Exit Ticket：学生离开前在小纸或便利贴上写答案。简单问题如今天我学到的一件事或我仍然困惑的是。教师收集并检查以评估理解。[分层: A - 用完整句子写答案, B - 写词语或短语, C - 画图并写标签]',
'✅ 对或错游戏：教师陈述与主题相关的说法。学生认为对就站，错就坐。或用绿卡（对）和红卡（错）。这个有趣的游戏快速测试理解。[分层: A - 给出对或错的理由, B - 自信答对或错, C - 跟朋友的动作]',
'🙏 结束祈祷或歌曲。选2-3名学生口头反思。教师领祷学生回应。学习在积极氛围中结束。[分层: A - 领祷并给反思, B - 分享简短反思, C - 听并对祈祷回应]',
'📚 教师布置巩固练习作为家庭作业。作业基于所学主题。教师清楚说明指示并给例子。学生把作业收进书包。[分层: A - 高阶思维和解决问题作业, B - 标准题, C - 基础巩固题]',
'🔮 预习下节课：教师展示图片或提出关于下节课的引导性问题。学生预测将要学的内容以激发兴趣和好奇心。[分层: A - 用完整句子预测, B - 用一个词预测, C - 在指导下看图]',
'🎯 学生在便利贴上完成今天学到的。他们写下今天学习中最记得的概念或技能。便利贴在教室角落的专设板上。[分层: A - 用清晰完整句子写, B - 写短短语, C - 画图]',
'🔄 用小白板进行快速问答。教师问与主题相关的问题。学生把答案写在小白板上并同时展示。教师即时反馈。这个活动让教师快速评估全班理解。[分层: A - 挑战性高阶思维题, B - 标准水平题, C - 展示写的答案]',
'⭐ 学生在理解程度表（理解/不确定/不理解三个部分）上放磁铁或标记。教师可以直观看到全班的理解水平并计划后续行动。[分层: A - 解释理解水平选择, B - 在自已的水平上放磁铁, C - 帮朋友放磁铁]',
'✏️ 每日反思日志：学生写关于今天学习的短段落。重点写学到了什么、感受如何以及将要做什么。教师阅读并给鼓励性评论。[分层: A - 写带反思的完整段落, B - 写3个简单句子, C - 画带标签的图]',
],
}

acts_js = json.dumps(ACTS, ensure_ascii=False)

# Replace ACTS data
old_acts = re.search(r'const ACTS = \{.*?\};', html, re.DOTALL)
if old_acts:
    html = html.replace(old_acts.group(0), f'const ACTS = {acts_js};')
    print('ACTS replaced')
else:
    print('WARNING: ACTS not found, adding new...')
    # Add after the lg() function
    html = html.replace("lg(s){const m={BM:'bm',BI:'en'};return m[s]||'zh'}",
                        f"lg(s){{const m={{BM:'bm',BI:'en'}};return m[s]||'zh'}};\nconst ACTS = {acts_js};")
    print('ACTS added')

# Verify
m = re.search(r'<script>([\s\S]*?)</script>', html)
if m:
    with open('/tmp/check.js', 'w') as f:
        f.write(m.group(1))
    import subprocess
    r = subprocess.run(['node', '--check', '/tmp/check.js'], capture_output=True, text=True)
    print('JS:', 'OK' if r.returncode == 0 else r.stderr[:200])

print(f'Size: {len(html)} bytes')

with open(IN, 'w') as f:
    f.write(html)
