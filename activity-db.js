/**
 * ActivityDB — Comprehensive learning activity & remedial instruction database
 * Organized by subject group, year band, and phase.
 * Each activity includes: description, differentiation strategy, teacher/student roles, duration.
 */
const ActivityDB = {
  // ──────────────────────────────────────────
  // LEARNING ACTIVITIES by SUBJECT GROUP
  // ──────────────────────────────────────────

  // --- BAHASA MELAYU (BM) ---
  BM: {
    induction: [
      { d: 'Murid mendengar dan menyanyikan lagu bertema yang berkaitan dengan topik. Guru menggunakan gitar atau rakaman audio.', dif: 'A: Nyanyi dengan gerakan kreatif. B: Nyanyi dengan bimbingan lirik. C: Dengar dan tepuk irama.', t: 'Memimpin nyanyian dengan iringan muzik', s: 'Menyanyi dan membuat gerakan kreatif', dur: 8 },
      { d: 'Guru menunjukkan video pendek atau tayangan slaid bergambar. Murid diminta meneka tajuk pembelajaran.', dif: 'A: Teka dengan ayat lengkap. B: Teka dengan satu perkataan. C: Padankan gambar.', t: 'Menayangkan video dan membimbing perbincangan', s: 'Menonton dan meneka tajuk pembelajaran', dur: 7 },
      { d: 'Permainan \"Cari Pasangan\" - murid mencari rakan yang memegang kad berpasangan (gambar-perkataan).', dif: 'A: Padan perkataan dengan ayat. B: Padan gambar dengan perkataan. C: Padan gambar dengan gambar.', t: 'Menyediakan kad dan menerangkan peraturan permainan', s: 'Mencari pasangan kad yang betul', dur: 10 },
      { d: 'Bercerita menggunakan boneka jari atau puppets. Murid meneka watak dan jalan cerita.', dif: 'A: Bercerita menggunakan ayat sendiri. B: Mengulang dialog watak. C: Menamakan watak.', t: 'Menggerakkan boneka dan bercerita dengan intonasi', s: 'Mendengar dan meneka jalan cerita', dur: 8 },
      { d: 'Soal jawab lisan berdasarkan objek maujud atau gambar yang dibawa oleh guru.', dif: 'A: Menjawab dalam ayat penuh. B: Menjawab dalam frasa. C: Menunjuk dan mengangguk.', t: 'Menunjukkan objek dan mengemukakan soalan', s: 'Menjawab soalan secara lisan', dur: 5 },
      { d: 'Murid berdiri dalam bulatan. Guru menyebut satu perkataan, murid menyebut perkataan berkaitan secara bergilir.', dif: 'A: Sebut perkataan + ayat. B: Sebut perkataan berkaitan. C: Ulang perkataan guru.', t: 'Memulakan permainan kata dan membimbing giliran', s: 'Menyebut perkataan berkaitan secara bergilir', dur: 7 },
      { d: 'Tayang gambar bersiri. Murid menyusun gambar mengikut urutan dan meneka cerita.', dif: 'A: Susun dan cerita. B: Susun dan baca ayat. C: Susun gambar.', t: 'Menyediakan gambar bersiri dan membimbing susunan', s: 'Menyusun gambar dan meneka cerita', dur: 8 },
    ],
    pre: [
      { d: 'Perkenalkan kosa kata baru menggunakan kad imbasan (flashcards). Murid menyebut dan mengeja.', dif: 'A: Sebut, eja, bina ayat. B: Sebut dan eja. C: Sebut dan tiru.', t: 'Menunjukkan kad imbasan dan menyebut perkataan', s: 'Menyebut dan mengeja perkataan', dur: 7 },
      { d: 'Aktiviti \"Minggu, Bulan, Tahun\" - murid menyusun kad perkataan mengikut kategori.', dif: 'A: Susun dan bina ayat. B: Susun mengikut kategori. C: Padan dengan gambar.', t: 'Menyediakan kad dan membimbing pengelasan', s: 'Menyusun kad mengikut kategori', dur: 8 },
      { d: 'Perbincangan kumpulan kecil (Think-Pair-Share) tentang topik pembelajaran.', dif: 'A: Kongsi idea dengan ayat lengkap. B: Kongsi dengan frasa. C: Dengar dan ulang.', t: 'Menerangkan tugas dan memantau perbincangan', s: 'Berbincang dalam pasangan dan berkongsi idea', dur: 10 },
      { d: 'Mendengar dan mengulang sebutan frasa penting menggunakan teknik ulang dengar.', dif: 'A: Sebut dengan intonasi betul. B: Sebut frasa mudah. C: Sebut perkataan.', t: 'Menyebut frasa dengan intonasi yang betul', s: 'Mengulang sebutan frasa penting', dur: 5 },
      { d: 'Aktiviti padanan: Murid memadankan gambar dengan perkataan pada papan putih.', dif: 'A: Padan dan tulis ayat. B: Padan dan sebut. C: Padan gambar.', t: 'Menyediakan bahan dan membimbing aktiviti', s: 'Memadankan gambar dengan perkataan', dur: 7 },
      { d: 'Latihan lisan secara kelas: Guru menunjukkan gambar, murid menjawab secara serentak.', dif: 'A: Jawab ayat penuh. B: Jawab satu perkataan. C: Angkat tangan.', t: 'Menunjukkan gambar dan mengemukakan soalan', s: 'Menjawab soalan secara lisan', dur: 5 },
      { d: 'Permainan \"Kad Kategori\" - murid mengelaskan kad perkataan ke dalam kumpulan yang betul.', dif: 'A: Kelas dan beri alasan. B: Kelas dengan bimbingan. C: Padan contoh.', t: 'Menyediakan kad kategori dan membimbing', s: 'Mengelaskan kad mengikut kategori', dur: 8 },
    ],
    dev: [
      { d: 'Murid membaca petikan secara berpasangan dan menjawab soalan kefahaman. Soalan beraras untuk kumpulan berbeza.', dif: 'A: Baca dan jawab soalan KBAT. B: Baca dan jawab soalan literal. C: Baca bergilir dan lukis jawapan.', t: 'Menyediakan petikan beraras dan membimbing bacaan', s: 'Membaca dan menjawab soalan kefahaman', dur: 20 },
      { d: 'Menulis karangan/ayat berpandu dengan menggunakan peta pemikiran i-Think.', dif: 'A: Tulis karangan lengkap. B: Tulis ayat berpandu. C: Susun ayat dan tiru.', t: 'Menerangkan penggunaan peta i-Think dan membimbing', s: 'Menulis karangan menggunakan peta pemikiran', dur: 22 },
      { d: 'Aktiviti lakonan (Role Play) - murid melakonkan dialog dalam situasi harian.', dif: 'A: Lakon dengan dialog sendiri. B: Lakon dengan dialog diberi. C: Lakon dengan bimbingan guru.', t: 'Menyediakan skrip dan membimbing lakonan', s: 'Melakonkan dialog dalam kumpulan', dur: 20 },
      { d: 'Gallery Walk - murid berjalan melihat hasil kerja rakan dan memberi komen pada post-it.', dif: 'A: Tulis komen bernas. B: Tulis komen ringkas. C: Tampal stiker.', t: 'Mengatur stesen dan membimbing aktiviti', s: 'Berjalan dan memberi maklum balas', dur: 18 },
      { d: 'Mencipta buku mini (foldable booklet) berdasarkan topik yang dipelajari.', dif: 'A: Tulis isi lengkap. B: Tulis isi berpandu. C: Warnakan gambar.', t: 'Menyediakan template buku mini dan bahan', s: 'Mencipta buku mini secara kreatif', dur: 25 },
      { d: 'Aktiviti \"Stesen Pembelajaran\" - murid bergerak ke 4-5 stesen berbeza untuk menyelesaikan tugasan.', dif: 'A: Stesen KBAT. B: Stesen sederhana. C: Stesen bimbingan guru.', t: 'Menyediakan bahan setiap stesen dan memantau', s: 'Bergerak dan menyelesaikan tugasan stesen', dur: 25 },
      { d: 'Permainan Bahasa - Scrabble, Boggle atau Silang Kata berkaitan topik.', dif: 'A: Bina ayat dari perkataan. B: Cari perkataan tersembunyi. C: Padan huruf.', t: 'Menyediakan permainan dan membimbing', s: 'Bermain sambil belajar perkataan baru', dur: 20 },
      { d: 'Mencipta peta minda atau peta bulatan tentang topik secara berkumpulan.', dif: 'A: Peta minda lengkap dengan sub-topik. B: Peta bulatan dengan idea. C: Peta bulatan bergambar.', t: 'Menerangkan teknik peta minda dan membimbing', s: 'Mencipta peta minda secara berkumpulan', dur: 20 },
    ],
    post: [
      { d: 'Pembentangan hasil kerja kumpulan terpilih di hadapan kelas.', dif: 'A: Bentang dengan yakin. B: Bentang dengan bimbingan. C: Bantu tunjuk hasil kerja.', t: 'Memilih wakil dan membimbing pembentangan', s: 'Membentang hasil kerja kumpulan', dur: 10 },
      { d: 'Kuiz Kahoot atau Quizizz secara berkumpulan atau individu.', dif: 'A: Soalan KBAT. B: Soalan sederhana. C: Soalan bergambar.', t: 'Menyediakan kuiz dan memantau jawapan', s: 'Menjawab kuiz secara individu/kumpulan', dur: 8 },
      { d: 'Sesi refleksi: Murid berkongsi satu perkara yang mereka pelajari hari ini.', dif: 'A: Kongsi dalam ayat lengkap. B: Kongsi dalam frasa. C: Tunjuk pada gambar.', t: 'Memimpin sesi refleksi dan memberi giliran', s: 'Berkongsi refleksi pembelajaran', dur: 5 },
      { d: 'Aktiviti \"3-2-1\" - 3 perkara belajar, 2 perkara menarik, 1 soalan.', dif: 'A: Tulis lengkap. B: Tulis berpandu. C: Lukis dan label.', t: 'Mengedarkan borang 3-2-1 dan membimbing', s: 'Melengkapkan refleksi 3-2-1', dur: 7 },
      { d: 'Sumbangsaran secara kelas untuk merumuskan isi pelajaran.', dif: 'A: Beri idea bernas. B: Bersetuju/tidak setuju. C: Ulang idea rakan.', t: 'Mencatat idea di papan putih dan merumus', s: 'Memberi sumbangsaran secara lisan', dur: 5 },
    ],
    closure: [
      { d: 'Rumusan isi penting oleh guru dengan bimbingan murid. Murid melengkapkan peta konsep.', dif: 'A: Lengkap peta konsep sendiri. B: Lengkap separa. C: Warnakan peta.', t: 'Merumus isi penting dengan bimbingan murid', s: 'Melengkapkan peta konsep', dur: 5 },
      { d: 'Exit Ticket - murid menulis jawapan pada kertas kecil sebelum keluar kelas.', dif: 'A: Tulis ayat lengkap. B: Tulis perkataan. C: Lukis dan label.', t: 'Mengedarkan exit ticket dan mengumpul', s: 'Menulis jawapan pada exit ticket', dur: 5 },
      { d: 'Permainan ringkas seperti \"Betul atau Salah\" atau \"Ya atau Tidak\" untuk menguji kefahaman.', dif: 'A: Beri alasan. B: Jawab betul/salah. C: Tiru jawapan rakan.', t: 'Membaca kenyataan dan memimpin permainan', s: 'Menjawab betul atau salah', dur: 5 },
      { d: 'Doa dan nyanyian lagu penutup. Refleksi secara lisan oleh 2-3 orang murid.', dif: 'A: Pimpin doa. B: Kongsi refleksi. C: Dengar dan aminkan.', t: 'Memimpin doa dan memilih murid untuk refleksi', s: 'Berdoa dan mendengar refleksi', dur: 3 },
      { d: 'Guru memberikan latihan pengukuhan sebagai kerja rumah dan menerangkan arahan.', dif: 'A: Latihan KBAT. B: Latihan sederhana. C: Latihan asas.', t: 'Menerangkan latihan dan memberi arahan', s: 'Mendengar dan menyimpan latihan', dur: 5 },
    ],
  },

  // --- ENGLISH (BI) ---
  BI: {
    induction: [
      { d: 'Sing a themed song or chant with actions. Teacher uses guitar or audio recording.', dif: 'A: Create new verses. B: Sing with actions. C: Clap along.', t: 'Leads the song with guitar/audio and actions', s: 'Sings and does actions', dur: 8 },
      { d: 'Show a short video clip or picture. Pupils guess the topic of the lesson.', dif: 'A: Guess in full sentences. B: Guess one word. C: Point to the picture.', t: 'Plays video and elicits responses', s: 'Watches and guesses the topic', dur: 7 },
      { d: 'Play "What\'s Missing?" - place 4-5 flashcards, pupils close eyes, teacher removes one.', dif: 'A: Say missing word in sentence. B: Say missing word. C: Point to missing.', t: 'Places cards and leads the game', s: 'Recalls and names the missing item', dur: 5 },
      { d: 'Guessing game: Teacher describes something, pupils guess what it is.', dif: 'A: Give own clues. B: Guess from 2 clues. C: Point to picture.', t: 'Gives clues and confirms guesses', s: 'Listens and guesses correctly', dur: 7 },
      { d: 'Show real objects from a mystery bag. Pupils feel and guess before seeing.', dif: 'A: Describe the feel. B: Guess the object. C: Touch and point.', t: 'Brings mystery bag and elicits vocabulary', s: 'Feels and guesses the objects', dur: 8 },
    ],
    pre: [
      { d: 'Introduce key vocabulary using flashcards with words and pictures.', dif: 'A: Say word in sentence. B: Say and spell word. C: Repeat after teacher.', t: 'Shows flashcards and models pronunciation', s: 'Repeats and practises vocabulary', dur: 7 },
      { d: 'Match pictures to words on the whiteboard in a relay race.', dif: 'A: Match and write sentence. B: Match and say word. C: Match pictures.', t: 'Sets up relay game and monitors', s: 'Runs and matches pictures to words', dur: 8 },
      { d: 'Think-Pair-Share: Pupils discuss a question about the topic with a partner.', dif: 'A: Share in full sentences. B: Share key word. C: Listen and nod.', t: 'Poses question and monitors pairs', s: 'Discusses and shares ideas', dur: 7 },
      { d: 'Drill key sentence structures using substitution tables.', dif: 'A: Create own sentences. B: Complete sentences. C: Repeat sentences.', t: 'Models sentence structures and drills', s: 'Practises sentence structures', dur: 8 },
      { d: 'Categorisation game: Sort word cards into groups (e.g. food/animals/colours).', dif: 'A: Sort and justify. B: Sort with help. C: Match to example.', t: 'Provides word cards and guides sorting', s: 'Sorts words into correct categories', dur: 7 },
    ],
    dev: [
      { d: 'Read a short passage in pairs and answer comprehension questions at different levels.', dif: 'A: Answer inferential questions. B: Answer literal questions. C: Draw the answer.', t: 'Provides graded passages and guides reading', s: 'Reads and answers comprehension questions', dur: 20 },
      { d: 'Write a short paragraph using a writing frame or template.', dif: 'A: Write independently. B: Complete cloze passage. C: Trace sentences.', t: 'Provides writing frames at 3 levels', s: 'Writes using the template', dur: 22 },
      { d: 'Role-play a dialogue in pairs or small groups based on a scenario.', dif: 'A: Create own dialogue. B: Use given dialogue. C: Repeat after teacher.', t: 'Provides scenarios and guides practice', s: 'Performs role-play dialogue', dur: 18 },
      { d: 'Gallery Walk: Display work on desks. Pupils walk, read, and leave sticky note feedback.', dif: 'A: Write constructive feedback. B: Write one positive comment. C: Draw a star.', t: 'Organises gallery walk and models feedback', s: 'Walks and gives peer feedback', dur: 15 },
      { d: 'Create a foldable mini-booklet summarising key vocabulary and sentences.', dif: 'A: Write full sentences. B: Write key words. C: Colour pictures.', t: 'Provides booklet template and materials', s: 'Creates a mini-booklet', dur: 20 },
      { d: 'Station-based learning: 4-5 stations with different tasks (reading, writing, speaking, listening).', dif: 'A: Higher-order station. B: Standard station. C: Guided station.', t: 'Sets up stations and rotates groups', s: 'Rotates and completes station tasks', dur: 25 },
      { d: 'Information Gap Activity: Pairs have different information, ask each other to complete.', dif: 'A: Ask full questions. B: Ask key words. C: Show and copy.', t: 'Prepares different information cards', s: 'Asks and shares information', dur: 18 },
    ],
    post: [
      { d: 'Selected groups present their work to the class.', dif: 'A: Present confidently. B: Present with support. C: Display work.', t: 'Selects presenters and guides presentation', s: 'Presents group work', dur: 10 },
      { d: 'Quick quiz using Kahoot, Quizizz, or mini-whiteboards.', dif: 'A: Explain answers. B: Choose answer. C: Copy answer.', t: 'Runs the quiz and checks answers', s: 'Answers quiz questions', dur: 8 },
      { d: 'Reflection circle: Each pupil shares one thing they learned.', dif: 'A: Share full sentence. B: Share one word. C: Nod or gesture.', t: 'Facilitates reflection circle', s: 'Shares reflection', dur: 5 },
      { d: 'Exit ticket: Write one sentence about what you learned today.', dif: 'A: Write sentence. B: Complete sentence. C: Draw and label.', t: 'Distributes and collects exit tickets', s: 'Completes exit ticket', dur: 5 },
    ],
    closure: [
      { d: 'Teacher summarises key points with pupil input using a mind map.', dif: 'A: Suggest connections. B: Identify key words. C: Point to pictures.', t: 'Draws mind map with pupil input', s: 'Contributes to the mind map', dur: 5 },
      { d: 'Play a quick review game like "Hot Seat" or "Back to the Board".', dif: 'A: Give clues. B: Guess the word. C: Cheer for team.', t: 'Organises the game and keeps score', s: 'Guesses words from clues', dur: 7 },
      { d: '"I learned, I enjoyed, I wonder" - pupils complete three sentence starters.', dif: 'A: Write all three. B: Complete two. C: Draw one.', t: 'Provides sentence starters', s: 'Completes reflection sentences', dur: 5 },
      { d: 'Preview next lesson with a teaser question or picture.', dif: 'A: Predict in sentences. B: Predict one word. C: Look at picture.', t: 'Shows teaser and elicits predictions', s: 'Predicts next topic', dur: 3 },
    ],
  },

  // --- CHINESE (BC) + MATHS (MT) + SCIENCE (SN) + OTHERS (zh language) ---
  ZH: {
    induction: [
      { d: '播放短视频或展示图片，学生猜测本节课的学习主题。', dif: '高组：用完整句子猜测。中组：用关键词猜测。低组：指认图片。', t: '播放视频并引导学生讨论', s: '观看视频并猜测主题', dur: 8 },
      { d: '谜语或脑筋急转弯：老师说谜语，学生猜答案。', dif: '高组：自己出谜语。中组：猜谜语。低组：从图片中选答案。', t: '说出谜语并提示答案', s: '猜谜语并说出答案', dur: 7 },
      { d: '展示实物或模型，学生通过观察和触摸引出主题。', dif: '高组：描述实物特征。中组：说出实物名称。低组：触摸和指认。', t: '展示实物并提问引导', s: '观察和触摸实物', dur: 8 },
      { d: '听声音猜事物：播放声音片段（动物叫、交通工具等），学生猜测。', dif: '高组：猜并描述声音。中组：猜出事物。低组：指认图片。', t: '播放声音并引导学生猜测', s: '听声音并猜测事物', dur: 5 },
      { d: '快速问答游戏：教师快速展示闪卡，学生快速回答。', dif: '高组：快速回答完整句子。中组：回答关键词。低组：重复答案。', t: '快速展示闪卡并提问', s: '快速回答教师提问', dur: 7 },
      { d: '故事导入：教师讲述与主题相关的短故事，学生预测内容。', dif: '高组：预测故事发展。中组：回答故事问题。低组：指认故事角色。', t: '讲述故事并引导学生预测', s: '听故事并参与预测', dur: 8 },
      { d: '游戏导入：\"找不同\"或\"What\'s Missing\"，展示图片后隐藏一个。', dif: '高组：描述缺少的物品。中组：说出缺少的物品。低组：指认缺少的物品。', t: '展示图片并引导游戏', s: '观察并找出缺少的物品', dur: 5 },
    ],
    pre: [
      { d: '使用字卡或图片卡介绍关键概念和词汇，学生跟读。', dif: '高组：造句。中组：读词卡。低组：跟读。', t: '展示字卡并示范发音', s: '跟读字卡并记忆词汇', dur: 7 },
      { d: '小组讨论 (Think-Pair-Share)：学生与同伴讨论与主题相关的问题。', dif: '高组：完整表达观点。中组：简单表达。低组：听取同伴意见。', t: '提出讨论问题并巡视指导', s: '与同伴讨论和分享意见', dur: 8 },
      { d: '图文配对活动：将图片与词语或句子配对。', dif: '高组：配并对造句。中组：配对并读词。低组：配图片。', t: '准备配对材料并示范活动', s: '将图片与文字配对', dur: 7 },
      { d: '快速问答预热：教师提问已学知识，学生回顾旧知。', dif: '高组：详细回答。中组：简单回答。低组：点头或摇头。', t: '提问已学知识并引导回顾', s: '回顾并回答旧知识', dur: 5 },
      { d: '示范操作：教师示范关键步骤或概念，学生观察。', dif: '高组：示范后复述步骤。中组：示范后做简单操作。低组：观察并模仿。', t: '示范关键步骤并讲解', s: '观察示范并理解概念', dur: 8 },
      { d: '分类游戏：将物品/概念卡分类到正确的组别。', dif: '高组：分类并说明理由。中组：分类。低组：参考示例分类。', t: '准备分类材料和引导', s: '将物品分类到正确组别', dur: 7 },
      { d: '听指令做动作：教师发出指令，学生根据指令做动作。', dif: '高组：发出指令。中组：听指令做动作。低组：观察同伴做动作。', t: '发出指令并示范动作', s: '听指令并做相应动作', dur: 6 },
    ],
    dev: [
      { d: '小组合作完成任务：学生分组合作解决一个问题或完成一个项目。', dif: '高组：完成挑战性任务。中组：完成标准任务。低组：在教师指导下完成任务。', t: '准备任务材料并分组指导', s: '小组合作完成任务', dur: 22 },
      { d: '分层工作纸：学生根据能力完成不同难度的工作纸（3个层次）。', dif: '高组：高阶思考题。中组：标准练习题。低组：基础巩固题。', t: '准备三层工作纸并分发', s: '根据能力完成工作纸', dur: 20 },
      { d: '实验/实践活动：学生动手进行实验或实践操作。', dif: '高组：设计实验步骤。中组：按步骤实验。低组：观察和记录。', t: '准备实验材料和指导步骤', s: '动手进行实验并记录结果', dur: 25 },
      { d: '画廊漫步 (Gallery Walk)：学生参观同伴的作品并留下反馈。', dif: '高组：写详细反馈。中组：写一句反馈。低组：贴贴纸。', t: '组织画廊漫步并示范反馈', s: '参观作品并写反馈', dur: 15 },
      { d: '角色扮演：学生扮演不同角色模拟真实情境。', dif: '高组：自编对话。中组：使用给定对话。低组：跟读台词。', t: '提供情境和角色卡', s: '扮演角色进行对话', dur: 20 },
      { d: '学习站 (Station Learning)：学生轮流到4-5个站完成任务。', dif: '高组：挑战站。中组：标准站。低组：辅导站。', t: '设置学习站并指导轮换', s: '轮流到各站完成任务', dur: 25 },
      { d: '创作活动：学生创作海报、模型、小书或展示板。', dif: '高组：独立创作。中组：参考模板创作。低组：填色和剪贴。', t: '提供创作材料和模板', s: '进行创作活动', dur: 22 },
      { d: '解决问题活动：学生应用所学知识解决实际问题。', dif: '高组：多步骤复杂问题。中组：简单应用问题。低组：引导式问题。', t: '设计问题并引导学生解决', s: '应用知识解决问题', dur: 20 },
      { d: '拼图式学习 (Jigsaw)：每组专攻一部分内容，然后互相教学。', dif: '高组：专家教学。中组：学习并分享。低组：在小组中学习。', t: '分配内容和组织教学', s: '学习并互相教学', dur: 22 },
    ],
    post: [
      { d: '小组呈现：选定的组呈现他们的工作成果。', dif: '高组：自信呈现。中组：辅助呈现。低组：展示作品。', t: '选择呈现组别并指导', s: '呈现在组内完成的工作', dur: 10 },
      { d: '快速测验：口头问答或小测验检查理解。', dif: '高组：解释答案原因。中组：选择正确答案。低组：指认答案。', t: '进行快速测验和核对答案', s: '回答问题并检查理解', dur: 8 },
      { d: '反射圈：学生分享今天学到的一个知识点。', dif: '高组：用完整句子分享。中组：用关键词分享。低组：指认学习内容。', t: '引导学生分享和反思', s: '分享今天的学习收获', dur: 5 },
      { d: '3-2-1活动：3个学到的知识，2个有趣的事，1个问题。', dif: '高组：书写完整。中组：填空式。低组：画图。', t: '分发3-2-1表格', s: '完成3-2-1反思活动', dur: 7 },
      { d: '作品互评：学生互相评价同伴的作品（使用评价量规）。', dif: '高组：用量规评价。中组：简单评语。低组：选最佳作品。', t: '提供简单评价量规', s: '互相评价同伴作品', dur: 8 },
    ],
    closure: [
      { d: '教师总结要点，学生补充，形成思维导图。', dif: '高组：补充细节。中组：补充关键词。低组：指认图片。', t: '绘制思维导图并引导学生总结', s: '参与总结和补充', dur: 5 },
      { d: 'Exit ticket：学生在下课前写下今天学到的一个知识点。', dif: '高组：写完整句子。中组：写关键词。低组：画图并标注。', t: '分发Exit ticket并收集', s: '书写Exit ticket', dur: 5 },
      { d: '快速游戏：\"对或错\"教师说陈述，学生判断对错。', dif: '高组：说明理由。中组：判断对错。低组：举牌表示。', t: '说出陈述并引导学生判断', s: '判断对错并说明理由', dur: 5 },
      { d: '预告下节课：展示下节课相关图片或问题，激发兴趣。', dif: '高组：预测下节课内容。中组：回答相关问题。低组：看图片。', t: '展示预告图片或问题', s: '预测下节课内容', dur: 3 },
      { d: '巩固练习：教师布置分层作业（必做/选做/挑战题）。', dif: '高组：挑战题。中组：标准题。低组：基础题。', t: '布置分层作业并说明要求', s: '记录作业要求', dur: 5 },
    ],
  },
};

// ──────────────────────────────────────────
// REMEDIAL INSTRUCTION DATABASE (30 activities)
// ──────────────────────────────────────────
const RemedialDB = [
  {
    id: 'rm01', title: 'Bimbingan Individu Berstruktur',
    desc: 'Guru memberi bimbingan individu kepada murid yang belum menguasai kemahiran. Gunakan pendekatan langkah-demi-langkah dengan soalan bimbingan.',
    strategies: ['Bimbingan individu', 'Soalan lisan', 'Pengulangan'],
    materials: ['Lembaran kerja pemulihan', 'Alat tulis', 'Kad imbasan'],
    dur: 15, levels: [1,2,3,4,5,6],
    focus: 'Kemahiran asas yang belum dikuasai',
  },
  {
    id: 'rm02', title: 'Latihan Berstruktur Langkah-demi-Langkah',
    desc: 'Lembaran kerja dipermudah dengan arahan langkah-demi-langkah dan contoh. Murid menyelesaikan satu langkah pada satu masa.',
    strategies: ['Latihan berpandu', 'Contoh', 'Pengukuhan positif'],
    materials: ['Lembaran kerja berstruktur', 'Contoh jawapan'],
    dur: 12, levels: [1,2,3,4,5,6],
    focus: 'Pengukuhan kemahiran asas',
  },
  {
    id: 'rm03', title: 'Tunjuk Cara Ulangan (Re-demonstration)',
    desc: 'Guru mendemonstrasi semula kemahiran dengan penerangan yang lebih perlahan dan jelas. Murid mengulang selepas guru.',
    strategies: ['Demonstrasi', 'Pengulangan', 'Latihan terbimbing'],
    materials: ['Alat bantu mengajar', 'Bahan maujud'],
    dur: 10, levels: [1,2,3,4,5,6],
    focus: 'Kefahaman melalui demonstrasi ulangan',
  },
  {
    id: 'rm04', title: 'Bahan Bantu Visual (Visual Aids)',
    desc: 'Menggunakan gambar rajah, carta, peta konsep dan video untuk menjelaskan konsep secara visual. Sesuai untuk murid visual.',
    strategies: ['Visual', 'Konkrit', 'Peta konsep'],
    materials: ['Carta', 'Gambar rajah', 'Video', 'Peta minda'],
    dur: 10, levels: [1,2,3,4,5,6],
    focus: 'Kefahaman konsep melalui visual',
  },
  {
    id: 'rm05', title: 'Latihan Pengukuhan Bertulis',
    desc: 'Latihan tambahan yang lebih mudah untuk membina keyakinan murid sebelum beralih ke latihan aras sederhana.',
    strategies: ['Latihan', 'Pengukuhan', 'Keyakinan diri'],
    materials: ['Lembaran kerja pemulihan', 'Pensel', 'Pemadam'],
    dur: 12, levels: [1,2,3,4,5,6],
    focus: 'Membina keyakinan melalui latihan mudah',
  },
  {
    id: 'rm06', title: 'Pembelajaran Berpasangan (Peer Tutoring)',
    desc: 'Murid cemerlang dipasangkan dengan murid pemulihan. Mereka belajar bersama dan saling membantu.',
    strategies: ['Bimbingan rakan sebaya', 'Kolaboratif', 'Keyakinan'],
    materials: ['Bahan pembelajaran', 'Alat tulis'],
    dur: 15, levels: [1,2,3,4,5,6],
    focus: 'Pembelajaran melalui bimbingan rakan',
  },
  {
    id: 'rm07', title: 'Permainan Pendidikan (Educational Games)',
    desc: 'Gunakan permainan papan, kad atau digital untuk mengukuhkan kemahiran secara menyeronokkan.',
    strategies: ['Permainan', 'Pengukuhan', 'Motivasi'],
    materials: ['Permainan papan', 'Kad soalan', 'Dadu'],
    dur: 12, levels: [1,2,3,4],
    focus: 'Pengukuhan melalui permainan',
  },
  {
    id: 'rm08', title: 'Kad Imbasan (Flashcard Drilling)',
    desc: 'Gunakan kad imbasan berwarna untuk mengukuhkan ingatan jangka pendek murid. Ulang secara konsisten.',
    strategies: ['Kad imbasan', 'Pengulangan', 'Visual'],
    materials: ['Kad imbasan berwarna', 'Gambar'],
    dur: 8, levels: [1,2,3,4,5,6],
    focus: 'Pengukuhan ingatan',
  },
  {
    id: 'rm09', title: 'Nyanyian dan Gerakan (Songs & Movement)',
    desc: 'Gunakan lagu, irama dan gerakan untuk mengukuhkan konsep. Sesuai untuk murid kinestetik.',
    strategies: ['Muzik', 'Gerakan', 'Kinestetik'],
    materials: ['Rakaman audio', 'Alat perkusi', 'Kad lirik'],
    dur: 8, levels: [1,2,3,4],
    focus: 'Pembelajaran melalui muzik dan gerakan',
  },
  {
    id: 'rm10', title: 'Peta Konsep Bergambar',
    desc: 'Murid melengkapkan peta konsep bergambar yang mengandungi gambar dan kata kunci.',
    strategies: ['Visual', 'Peta konsep', 'Organisasi maklumat'],
    materials: ['Peta konsep kosong', 'Gambar', 'Gam'],
    dur: 10, levels: [1,2,3,4,5,6],
    focus: 'Organisasi dan pengukuhan konsep',
  },
  {
    id: 'rm11', title: 'Bacaan Bergilir (Guided Reading)',
    desc: 'Guru dan murid membaca bersama. Guru berhenti pada perkataan sukar dan membimbing sebutan.',
    strategies: ['Bacaan berpandu', 'Sebutan', 'Kefahaman'],
    materials: ['Buku bacaan', 'Kad perkataan'],
    dur: 12, levels: [1,2,3,4],
    focus: 'Kemahiran membaca dan menyebut',
  },
  {
    id: 'rm12', title: 'Dialog Strip Sequencing',
    desc: 'Berikan dialog yang dipotong menjadi jalur. Murid menyusun dialog mengikut urutan yang betul.',
    strategies: ['Susunan', 'Urutan', 'Bertutur'],
    materials: ['Jalur dialog', 'Gam', 'Kertas'],
    dur: 10, levels: [1,2,3,4,5,6],
    focus: 'Kefahaman urutan dialog',
  },
  {
    id: 'rm13', title: 'Cloze Passage dengan Gambar',
    desc: 'Teks cloze di mana perkataan yang hilang ditunjukkan sebagai gambar di atas ruang kosong.',
    strategies: ['Cloze', 'Visual', 'Kefahaman membaca'],
    materials: ['Teks cloze bergambar', 'Pensel'],
    dur: 12, levels: [1,2,3,4],
    focus: 'Kefahaman membaca dengan bantuan gambar',
  },
  {
    id: 'rm14', title: 'Error Hunt (Cari Kesalahan)',
    desc: 'Tunjukkan 3 ayat bergambar - 1 betul, 2 dengan kesalahan. Murid membulatkan kesalahan.',
    strategies: ['Pengenalpastian kesalahan', 'Pembetulan', 'Visual'],
    materials: ['Lembaran kerja', 'Pensel warna'],
    dur: 10, levels: [1,2,3,4,5,6],
    focus: 'Kemahiran mengenal pasti dan membetulkan kesalahan',
  },
  {
    id: 'rm15', title: 'Mini Whiteboard Quick-Write',
    desc: 'Guru menunjukkan gambar dan menyebut perkataan/ayat. Murid menulis pada papan putih mini dan tunjuk.',
    strategies: ['Penulisan cepat', 'Visual', 'Maklum balas segera'],
    materials: ['Papan putih mini', 'Pen marker'],
    dur: 8, levels: [1,2,3,4,5,6],
    focus: 'Penulisan perkataan dan ayat mudah',
  },
  {
    id: 'rm16', title: 'Alphabet / Phonics Hopscotch',
    desc: 'Lukis grid hopscotch dengan huruf. Murid melompat ke huruf dan menyebut bunyi atau perkataan.',
    strategies: ['Kinestetik', 'Fonik', 'Permainan'],
    materials: ['Kapur', 'Tape pelekat lantai'],
    dur: 10, levels: [1,2,3],
    focus: 'Pengukuhan huruf dan bunyi',
  },
  {
    id: 'rm17', title: 'Word Family Sorting',
    desc: 'Gunakan poket carta dengan kepala keluarga perkataan (-at, -an, -op). Murid menyusun kad ke keluarga betul.',
    strategies: ['Keluarga perkataan', 'Pengelasan', 'Rakan sebaya'],
    materials: ['Poket carta', 'Kad perkataan'],
    dur: 10, levels: [1,2,3],
    focus: 'Kemahiran membaca dan mengeja',
  },
  {
    id: 'rm18', title: 'Realia Show & Tell',
    desc: 'Bawa objek sebenar. Guru menyebut nama, murid ulang dan ambil objek yang betul apabila ditanya.',
    strategies: ['Objek sebenar', 'Visual', 'Verbal'],
    materials: ['Objek sebenar', 'Kad nama'],
    dur: 12, levels: [1,2,3,4],
    focus: 'Perbendaharaan kata melalui objek sebenar',
  },
  {
    id: 'rm19', title: 'Question-Question Pass',
    desc: 'Berdiri dalam bulatan. Guru model soalan mudah. Hantar bola; penerima jawab dan tanya seterusnya.',
    strategies: ['Bertutur', 'Sosial', 'Permainan'],
    materials: ['Bola lembut'],
    dur: 8, levels: [1,2,3,4],
    focus: 'Kemahiran bertutur dan mendengar',
  },
  {
    id: 'rm20', title: 'Talk-the-Picture Frame',
    desc: 'Beri setiap pasangan gambar besar. Murid tunjuk dan sebut apa yang mereka lihat menggunakan rangka ayat.',
    strategies: ['Visual', 'Bertutur', 'Berpasangan'],
    materials: ['Gambar besar', 'Rangka ayat'],
    dur: 10, levels: [1,2,3,4],
    focus: 'Kemahiran bertutur menggunakan rangka ayat',
  },
  {
    id: 'rm21', title: 'Latihan Menulis Huruf/Perkataan',
    desc: 'Murid menulis huruf atau perkataan dalam buku latihan khas dengan titik panduan dan garis bantu.',
    strategies: ['Penulisan', 'Mekanis', 'Latih tubi'],
    materials: ['Buku latihan menulis', 'Pensel'],
    dur: 10, levels: [1,2],
    focus: 'Kemahiran menulis huruf dan perkataan',
  },
  {
    id: 'rm22', title: 'Pengiraan Menggunakan Bahan Maujud',
    desc: 'Menggunakan blok, biji benih atau bahan lain untuk mengira, menambah dan menolak secara konkrit.',
    strategies: ['Konkrit', 'Maujud', 'Pengiraan'],
    materials: ['Blok pengiraan', 'Biji benih', 'Bekas'],
    dur: 12, levels: [1,2,3],
    focus: 'Kemahiran mengira secara konkrit',
  },
  {
    id: 'rm23', title: 'Garis Nombor (Number Line)',
    desc: 'Gunakan garis nombor di lantai atau atas meja untuk membantu murid memahami konsep tambah dan tolak.',
    strategies: ['Visual', 'Konkrit', 'Operasi'],
    materials: ['Garis nombor', 'Marker'],
    dur: 10, levels: [1,2,3],
    focus: 'Kefahaman operasi tambah dan tolak',
  },
  {
    id: 'rm24', title: 'Permainan Memori (Memory Game)',
    desc: 'Kad diletakkan terbalik. Murid membuka dua kad, padankan gambar-perkataan atau soalan-jawapan.',
    strategies: ['Memori', 'Padanan', 'Permainan'],
    materials: ['Kad memori', 'Meja'],
    dur: 10, levels: [1,2,3,4,5,6],
    focus: 'Pengukuhan ingatan dan padanan',
  },
  {
    id: 'rm25', title: 'Buku Skrap Pemulihan',
    desc: 'Murid mengumpul hasil kerja pemulihan dalam buku skrap khas untuk melihat perkembangan mereka.',
    strategies: ['Dokumentasi', 'Motivasi', 'Kendiri'],
    materials: ['Buku skrap', 'Gunting', 'Gam'],
    dur: 15, levels: [1,2,3,4,5,6],
    focus: 'Dokumentasi perkembangan pembelajaran',
  },
  {
    id: 'rm26', title: 'Aktiviti Potong dan Tampal',
    desc: 'Murid memotong gambar/perkataan dan menampal pada tempat yang betul dalam lembaran kerja.',
    strategies: ['Psikomotor halus', 'Visual', 'Pengelasan'],
    materials: ['Gunting', 'Gam', 'Lembaran kerja'],
    dur: 10, levels: [1,2,3],
    focus: 'Kemahiran psikomotor halus dan pengelasan',
  },
  {
    id: 'rm27', title: 'Soalan Lisan Berbimbing',
    desc: 'Guru mengemukakan soalan secara lisan dengan bimbingan rapat. Murid digalakkan menjawab tanpa tekanan.',
    strategies: ['Lisan', 'Bimbingan', 'Keyakinan'],
    materials: ['Kad soalan', 'Gambar'],
    dur: 8, levels: [1,2,3,4,5,6],
    focus: 'Kemahiran menjawab soalan lisan',
  },
  {
    id: 'rm28', title: 'Pembelajaran Atas Talian (Online Remedial)',
    desc: 'Gunakan platform seperti Quizizz, Google Forms atau YouTube untuk aktiviti pemulihan interaktif.',
    strategies: ['Digital', 'Interaktif', 'Kendiri'],
    materials: ['Komputer/tablet', 'Internet'],
    dur: 12, levels: [3,4,5,6],
    focus: 'Pembelajaran interaktif digital',
  },
  {
    id: 'rm29', title: 'Jurnal Pembelajaran (Learning Journal)',
    desc: 'Murid menulis jurnal ringkas tentang apa yang mereka pelajari dan apa yang masih sukar difahami.',
    strategies: ['Refleksi', 'Penulisan', 'Kendiri'],
    materials: ['Buku jurnal', 'Pensel'],
    dur: 10, levels: [3,4,5,6],
    focus: 'Refleksi kendiri pembelajaran',
  },
  {
    id: 'rm30', title: 'Stesen Pemulihan (Remedial Station)',
    desc: 'Sediakan stesen khas dengan aktiviti pemulihan untuk murid yang belum menguasai kemahiran.',
    strategies: ['Stesen', 'Kumpulan kecil', 'Bimbingan'],
    materials: ['Bahan stesen', 'Lembaran kerja', 'Alat tulis'],
    dur: 15, levels: [1,2,3,4,5,6],
    focus: 'Pemulihan dalam kumpulan kecil',
  },
];

// ActivityDB subject group mapping
// BM -> BM, BI -> BI, BC/MT/SN/PM/PI/PJ/PK/PSV/MZ/SJ/RBT/PKS/PJPK/PMZ -> ZH
ActivityDB.getGroup = function(subjectCode) {
  if (subjectCode === 'BM') return this.BM;
  if (subjectCode === 'BI') return this.BI;
  return this.ZH;
};

ActivityDB.getActivities = function(subjectCode, phase, count = 3) {
  const group = this.getGroup(subjectCode);
  const pool = group[phase] || group['induction'];
  const shuffled = [...pool].sort(() => Math.random() - 0.5);
  return shuffled.slice(0, Math.min(count, shuffled.length));
};

ActivityDB.getRemedial = function(count = 3) {
  const shuffled = [...RemedialDB].sort(() => Math.random() - 0.5);
  return shuffled.slice(0, Math.min(count, shuffled.length));
};
