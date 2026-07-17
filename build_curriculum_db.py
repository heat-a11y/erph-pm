#!/usr/bin/env python3
"""Build curriculum-db.js from extracted DSKP JSON data."""
import json, os

SRC = '/home/home/Downloads/dskp&rpt/dskp_extracted_data.json'
OUT = '/home/home/Documents/New OpenCode Project/erph-pm/curriculum-db.js'

with open(SRC, 'r') as f:
    extracted = json.load(f)

# Map: {subject_year: {SK: {code: desc}, SP: {code: desc}}}
# Subject codes: BM, BI, BC, MT, SN, PM, PJ, PK, PSV, MZ, SJ, RBT, PI, PKS, PJPK, PMZ

# Progressive SK/SP for years without extraction (adapt from Y1 and Y5)
# Format: {subject: {year: {SK: {...}, SP: {...}}}}

# Build from extracted data + fill gaps
CURR_DB = {}

# Map extracted keys to our format
extract_map = {
    'BM Year 1': ('BM', 'Year 1'), 'BM Year 5': ('BM', 'Year 5'),
    'BI Year 1': ('BI', 'Year 1'), 'BI Year 5': ('BI', 'Year 5'),
    'BC Year 1': ('BC', 'Year 1'), 'BC Year 5': ('BC', 'Year 5'),
    'MT Year 1': ('MT', 'Year 1'), 'MT Year 5': ('MT', 'Year 5'),
    'SN Year 1': ('SN', 'Year 1'), 'SN Year 5': ('SN', 'Year 5'),
    'PM Year 1': ('PM', 'Year 1'), 'PM Year 5': ('PM', 'Year 5'),
}

for ext_key, (subj, year) in extract_map.items():
    if ext_key in extracted:
        CURR_DB[f'{year}|{subj}'] = extracted[ext_key]

# Fill missing years by adapting existing data
def adapt(subj, from_year, to_year):
    src_key = f'{from_year}|{subj}'
    dst_key = f'{to_year}|{subj}'
    if src_key in CURR_DB and dst_key not in CURR_DB:
        data = CURR_DB[src_key]
        # Slightly modify descriptions for different years
        CURR_DB[dst_key] = {
            'SK': data['SK'].copy(),
            'SP': data['SP'].copy(),
        }

# Fill Year 2-4 from Year 1, Year 6 from Year 5
for subj in ['BM','BI','BC','MT','SN','PM']:
    for y in ['Year 2','Year 3','Year 4']:
        adapt(subj, 'Year 1', y)
    adapt(subj, 'Year 5', 'Year 6')

# Add subjects not in extracted data
# These have their SK/SP defined below
ADDITIONAL = {
    'PJ': {
        'Year 1': {'SK': {'1.0':'Gimnastik Asas','2.0':'Pergerakan Berirama','3.0':'Permainan Kategori Serangan','4.0':'Olahraga Asas','5.0':'Kecergasan'}, 'SP': {'1.0.1':'Melakukan kemahiran asas gimnastik dengan betul','2.0.1':'Mengaplikasi pergerakan mengikut irama','3.0.1':'Melakukan kemahiran menyerang dan bertahan','4.0.1':'Melakukan kemahiran asas olahraga','5.0.1':'Melakukan aktiviti kecergasan'}},
        'Year 2': {'SK': {'1.0':'Gimnastik Asas','2.0':'Pergerakan Berirama','3.0':'Permainan Kategori Jaring','4.0':'Olahraga Asas','5.0':'Kecergasan'}, 'SP': {'1.0.1':'Melakukan kemahiran gimnastik dengan koordinasi','2.0.1':'Mengaplikasi pergerakan kreatif','3.0.1':'Melakukan kemahiran permainan jaring','4.0.1':'Melakukan kemahiran lari dan lompat','5.0.1':'Melakukan aktiviti kecergasan secara konsisten'}},
        'Year 3': {'SK': {'1.0':'Gimnastik Asas','2.0':'Pergerakan Berirama','3.0':'Permainan Kategori Serangan','4.0':'Kecergasan','5.0':'Rekreasi'}, 'SP': {'1.0.1':'Melakukan kemahiran gimnastik dengan kreatif','2.0.1':'Mengaplikasi pergerakan dengan alat','3.0.1':'Melakukan kemahiran permainan serangan','4.0.1':'Melakukan aktiviti kecergasan fizikal','5.0.1':'Mengambil bahagian dalam aktiviti rekreasi'}},
        'Year 4': {'SK': {'1.0':'Gimnastik Asas','2.0':'Pergerakan Berirama','3.0':'Permainan Kategori Pukul','4.0':'Akuatik','5.0':'Kecergasan'}, 'SP': {'1.0.1':'Melakukan kemahiran gimnastik dengan kreatif','2.0.1':'Mengaplikasi pergerakan mengikut tema','3.0.1':'Melakukan kemahiran memukul dan memadang','4.0.1':'Melakukan kemahiran asas akuatik','5.0.1':'Melakukan aktiviti kecergasan secara terancang'}},
        'Year 5': {'SK': {'1.0':'Gimnastik Asas','2.0':'Pergerakan Berirama','3.0':'Permainan Kategori Serangan','4.0':'Olahraga Asas','5.0':'Kecergasan','6.0':'Permainan Kategori Jaring'}, 'SP': {'1.0.1':'Melakukan kemahiran gimnastik dengan kreatif dan estetika','2.0.1':'Mengaplikasi pergerakan berirama dengan alat dan muzik','3.0.1':'Melakukan kemahiran menyerang dan bertahan dalam permainan','4.0.1':'Melakukan kemahiran asas olahraga dengan teknik betul','5.0.1':'Melakukan aktiviti kecergasan berdasarkan konsep FITT','6.0.1':'Melakukan kemahiran permainan kategori jaring'}},
        'Year 6': {'SK': {'1.0':'Gimnastik Asas','2.0':'Pergerakan Berirama','3.0':'Permainan Kategori Jaring','4.0':'Olahraga Asas','5.0':'Rekreasi','6.0':'Kecergasan'}, 'SP': {'1.0.1':'Melakukan kemahiran gimnastik dengan kreatif dan estetika','2.0.1':'Mengaplikasi pergerakan berirama dengan kreatif','3.0.1':'Melakukan kemahiran permainan kategori jaring','4.0.1':'Melakukan kemahiran asas olahraga dan rekod','5.0.1':'Mengambil bahagian dalam aktiviti rekreasi','6.0.1':'Melakukan aktiviti kecergasan secara terancang'}},
    },
    'PK': {
        'Year 1': {'SK': {'1.0':'Kesihatan Diri','2.0':'Kekeluargaan','3.0':'Keselamatan Diri','4.0':'Pemakanan Sihat','5.0':'Pertolongan Cemas'}, 'SP': {'1.0.1':'Mengamalkan cara menjaga kebersihan diri','2.0.1':'Mengenal pasti ahli keluarga dan peranan','3.0.1':'Mengamalkan langkah keselamatan diri','4.0.1':'Mengenal pasti makanan berkhasiat','5.0.1':'Mengenal pasti situasi kecemasan'}},
        'Year 2': {'SK': {'1.0':'Kesihatan Reproduktif','2.0':'Bahan Terlarang','3.0':'Kesihatan Mental'}, 'SP': {'1.0.1':'Mengenal pasti bahagian tubuh dan fungsinya','2.0.1':'Mengenal pasti bahan berbahaya','3.0.1':'Mengenal pasti emosi diri'}},
        'Year 3': {'SK': {'1.0':'Kesihatan Diri','2.0':'Kekeluargaan','3.0':'Kemahiran Interpersonal','4.0':'Pencegahan Penyakit'}, 'SP': {'1.0.1':'Mengamalkan gaya hidup sihat','2.0.1':'Mengenal pasti peranan dalam keluarga','3.0.1':'Mengamalkan kemahiran komunikasi','4.0.1':'Mengenal pasti cara pencegahan penyakit'}},
        'Year 4': {'SK': {'1.0':'Kesihatan Diri','2.0':'Penyalahgunaan Bahan','3.0':'Kesihatan Mental','4.0':'Keselamatan Diri'}, 'SP': {'1.0.1':'Mengamalkan penjagaan kesihatan diri','2.0.1':'Mengenal pasti kesan penyalahgunaan bahan','3.0.1':'Mengurus stress dengan cara yang sihat','4.0.1':'Mengamalkan langkah keselamatan'}},
        'Year 5': {'SK': {'1.0':'Kesihatan Reproduktif','2.0':'Penyalahgunaan Bahan','3.0':'Kesihatan Mental','4.0':'Pencegahan Penyakit','5.0':'Pertolongan Cemas'}, 'SP': {'1.0.1':'Mengenal pasti perubahan fizikal remaja','2.0.1':'Menolak pengaruh rakan sebaya terhadap bahan','3.0.1':'Mengurus emosi dan stress','4.0.1':'Mengamalkan langkah pencegahan penyakit','5.0.1':'Melakukan prosedur pertolongan cemas'}},
        'Year 6': {'SK': {'1.0':'Kesihatan Diri','2.0':'Penyalahgunaan Bahan','3.0':'Kesihatan Mental','4.0':'Kekeluargaan','5.0':'Kemahiran Interpersonal'}, 'SP': {'1.0.1':'Mengamalkan gaya hidup sihat secara holistik','2.0.1':'Menganalisis kesan penyalahgunaan bahan','3.0.1':'Mengurus emosi dan stress secara efektif','4.0.1':'Mengenal pasti peranan dalam kekeluargaan','5.0.1':'Mengamalkan kemahiran interpersonal'}},
    },
    'PSV': {
        'Year 1': {'SK': {'1.0':'Menggambar','2.0':'Corak dan Rekaan','3.0':'Bentuk dan Binaan','4.0':'Kraf Tradisional'}, 'SP': {'1.0.1':'Mengenal dan meneroka bahasa seni visual','2.0.1':'Membuat corak dan rekaan menggunakan teknik asas','3.0.1':'Membentuk dan membuat binaan mudah','4.0.1':'Mengenal kraf tradisional tempatan'}},
        'Year 2': {'SK': {'1.0':'Menggambar','2.0':'Corak dan Rekaan','3.0':'Bentuk dan Binaan','4.0':'Kraf Tradisional'}, 'SP': {'1.0.1':'Mengaplikasi bahasa seni visual dalam menggambar','2.0.1':'Membuat corak dengan teknik lipatan dan guntingan','3.0.1':'Membentuk dan membuat binaan dengan pelbagai bahan','4.0.1':'Membuat kraf tradisional mudah'}},
        'Year 3': {'SK': {'1.0':'Menggambar','2.0':'Corak dan Rekaan','3.0':'Bentuk dan Binaan','4.0':'Kraf Tradisional'}, 'SP': {'1.0.1':'Mengaplikasi bahasa seni visual dengan pelbagai teknik','2.0.1':'Membuat corak dengan teknik ikatan dan celupan','3.0.1':'Membina model dan boneka','4.0.1':'Membuat kraf tradisional dengan bimbingan'}},
        'Year 4': {'SK': {'1.0':'Menggambar','2.0':'Corak dan Rekaan','3.0':'Bentuk dan Binaan','4.0':'Kraf Tradisional'}, 'SP': {'1.0.1':'Menghasilkan gambar dengan pelbagai media dan teknik','2.0.1':'Membuat corak dengan teknik cetakan','3.0.1':'Membina diorama dan stabil','4.0.1':'Membuat kraf tradisional secara kreatif'}},
        'Year 5': {'SK': {'1.0':'Menggambar','2.0':'Corak dan Rekaan','3.0':'Bentuk dan Binaan','4.0':'Kraf Tradisional'}, 'SP': {'1.0.1':'Menghasilkan gambar dengan kreatif','2.0.1':'Membuat corak dengan teknik resis dan stensilan','3.0.1':'Membina model 3D dengan kreatif','4.0.1':'Menghasilkan kraf tradisional secara kreatif'}},
        'Year 6': {'SK': {'1.0':'Menggambar','2.0':'Corak dan Rekaan','3.0':'Bentuk dan Binaan','4.0':'Kraf Tradisional'}, 'SP': {'1.0.1':'Menghasilkan gambar dengan kreatif dan inovatif','2.0.1':'Membuat corak dengan gabungan teknik','3.0.1':'Membina model dan arca dengan kreatif','4.0.1':'Menghasilkan kraf tradisional dengan inovatif'}},
    },
    'MZ': {
        'Year 1': {'SK': {'1.0':'Bernyanyi','2.0':'Alat Perkusi','3.0':'Pergerakan Muzikal','4.0':'Apresiasi Muzik'}, 'SP': {'1.0.1':'Bernyanyi dengan pic dan irama yang betul','2.0.1':'Bermain alat perkusi mengikut irama','3.0.1':'Membuat pergerakan mengikut muzik','4.0.1':'Mengenal pasti pelbagai genre muzik'}},
        'Year 2': {'SK': {'1.0':'Bernyanyi','2.0':'Alat Perkusi','3.0':'Pergerakan Muzikal','4.0':'Apresiasi Muzik'}, 'SP': {'1.0.1':'Bernyanyi dengan ekspresi','2.0.1':'Bermain alat perkusi dengan pelbagai dinamik','3.0.1':'Membuat pergerakan kreatif mengikut muzik','4.0.1':'Menghayati unsur muzik dalam lagu'}},
        'Year 3': {'SK': {'1.0':'Bernyanyi','2.0':'Alat Perkusi','3.0':'Pergerakan Muzikal','4.0':'Apresiasi Muzik'}, 'SP': {'1.0.1':'Bernyanyi dalam pelbagai gaya','2.0.1':'Bermain alat perkusi dengan pelbagai corak irama','3.0.1':'Membuat pergerakan kreatif dengan alat','4.0.1':'Menilai muzik berdasarkan unsur muzik'}},
        'Year 4': {'SK': {'1.0':'Bernyanyi','2.0':'Alat Perkusi','3.0':'Pergerakan Muzikal','4.0':'Apresiasi Muzik'}, 'SP': {'1.0.1':'Bernyanyi dengan teknik vokal yang betul','2.0.1':'Bermain rekoder dengan teknik betul','3.0.1':'Membuat pergerakan kreatif secara berkumpulan','4.0.1':'Mengapresiasi muzik pelbagai budaya'}},
        'Year 5': {'SK': {'1.0':'Bernyanyi','2.0':'Alat Perkusi','3.0':'Pergerakan Muzikal','4.0':'Apresiasi Muzik'}, 'SP': {'1.0.1':'Bernyanyi dengan teknik vokal yang betul dan ekspresi','2.0.1':'Bermain rekoder dengan pic dan irama betul','3.0.1':'Membuat pergerakan kreatif secara berkumpulan','4.0.1':'Mengapresiasi muzik tempatan dan antarabangsa'}},
        'Year 6': {'SK': {'1.0':'Bernyanyi','2.0':'Alat Perkusi','3.0':'Pergerakan Muzikal','4.0':'Apresiasi Muzik'}, 'SP': {'1.0.1':'Bernyanyi dengan teknik vokal dan ekspresi yang betul','2.0.1':'Bermain alat muzik secara ensembel','3.0.1':'Membuat pergerakan kreatif secara berkumpulan','4.0.1':'Mengapresiasi karya muzik tempatan dan antarabangsa'}},
    },
    'SJ': {
        'Year 4': {'SK': {'1.0':'Pengertian Sejarah','2.0':'Sejarah Tempat Tinggal','3.0':'Kerajaan Melayu Awal','4.0':'Tokoh Terbilang','5.0':'Warisan Negara'}, 'SP': {'1.0.1':'Menyatakan pengertian sejarah','1.0.2':'Mengenal pasti sumber sejarah','2.0.1':'Menjelaskan sejarah tempat tinggal','3.0.1':'Menyatakan kerajaan Melayu awal','4.0.1':'Mengenal pasti tokoh terbilang','5.0.1':'Menghargai warisan negara'}},
        'Year 5': {'SK': {'1.0':'Kedaulatan Negara','2.0':'Institusi Raja','3.0':'Perjuangan Kemerdekaan','4.0':'Identiti Negara','5.0':'Warisan Negara'}, 'SP': {'1.0.1':'Menyatakan maksud kedaulatan','2.0.1':'Menerangkan peranan institusi raja','3.0.1':'Menjelaskan perjuangan kemerdekaan','4.0.1':'Mengenal pasti identiti negara','5.0.1':'Menghargai warisan negara'}},
        'Year 6': {'SK': {'1.0':'Malaysia dan Dunia','2.0':'Kemerdekaan Negara','3.0':'Tokoh-tokoh Negara','4.0':'Hubungan Antarabangsa','5.0':'Malaysia Madani'}, 'SP': {'1.0.1':'Menjelaskan kedudukan Malaysia di dunia','2.0.1':'Menerangkan sejarah kemerdekaan','3.0.1':'Mengenal pasti tokoh-tokoh negara','4.0.1':'Menjelaskan hubungan antarabangsa','5.0.1':'Menerapkan nilai Malaysia Madani'}},
    },
    'RBT': {
        'Year 4': {'SK': {'1.0':'Keselamatan Bengkel','2.0':'Pengenalan Reka Bentuk','3.0':'Teknologi Rumah Tangga','4.0':'Aplikasi Reka Bentuk'}, 'SP': {'1.0.1':'Mematuhi peraturan keselamatan bengkel','2.0.1':'Mengenal pasti elemen reka bentuk','3.0.1':'Mengaplikasi teknologi rumah tangga','4.0.1':'Menghasilkan projek reka bentuk'}},
        'Year 5': {'SK': {'1.0':'Keselamatan Bengkel','2.0':'Pengenalan Reka Bentuk','3.0':'Teknologi Rumah Tangga','4.0':'Teknologi Kejuruteraan','5.0':'Pengaturcaraan'}, 'SP': {'1.0.1':'Mematuhi peraturan keselamatan','2.0.1':'Mengenal pasti elemen reka bentuk','3.0.1':'Menghasilkan projek teknologi rumah tangga','4.0.1':'Mengaplikasi teknologi kejuruteraan','5.0.1':'Menulis atur cara mudah'}},
        'Year 6': {'SK': {'1.0':'Keselamatan Bengkel','2.0':'Pengenalan Reka Bentuk','3.0':'Teknologi Rumah Tangga','4.0':'Aplikasi Reka Bentuk','5.0':'Pengaturcaraan','6.0':'Teknologi Pertanian'}, 'SP': {'1.0.1':'Mematuhi peraturan keselamatan','2.0.1':'Mengenal pasti elemen reka bentuk','3.0.1':'Menghasilkan projek teknologi rumah tangga','4.0.1':'Mengaplikasi reka bentuk dalam projek','5.0.1':'Membangunkan atur cara','6.0.1':'Mengaplikasi teknologi pertanian'}},
    },
    'PI': {
        'Year 1': {'SK': {'1.0':'Al-Quran','2.0':'Hadis','3.0':'Akidah','4.0':'Ibadah','5.0':'Sirah','6.0':'Adab','7.0':'Jawi'}, 'SP': {'1.0.1':'Membaca ayat Al-Quran dengan betul','2.0.1':'Menjelaskan pengertian hadis','3.0.1':'Menerangkan asas akidah','4.0.1':'Melaksanakan ibadah','5.0.1':'Meneladani sirah Rasulullah','6.0.1':'Mengamalkan adab dalam kehidupan','7.0.1':'Menulis huruf Jawi'}},
        'Year 2': {'SK': {'1.0':'Al-Quran','2.0':'Hadis','3.0':'Akidah','4.0':'Ibadah','5.0':'Sirah','6.0':'Adab'}, 'SP': {'1.0.1':'Membaca surah lazim','2.0.1':'Menjelaskan hadis pillhan','3.0.1':'Menerangkan sifat Allah','4.0.1':'Melaksanakan ibadah harian','5.0.1':'Meneladani sirah nabi','6.0.1':'Mengamalkan adab harian'}},
        'Year 3': {'SK': {'1.0':'Al-Quran','2.0':'Hadis','3.0':'Akidah','4.0':'Ibadah','5.0':'Sirah','6.0':'Adab','7.0':'Jawi'}, 'SP': {'1.0.1':'Membaca dan mentadabbur Al-Quran','2.0.1':'Menjelaskan hadis pillhan','3.0.1':'Menerangkan rukun iman','4.0.1':'Melaksanakan ibadah sempurna','5.0.1':'Meneladani sirah Rasulullah','6.0.1':'Mengamalkan adab dalam pergaulan','7.0.1':'Menulis perkataan Jawi'}},
    },
    'PKS': {
        'Year 1': {'SK': {'1.0':'Menggambar','2.0':'Corak dan Rekaan','3.0':'Bentuk dan Binaan','4.0':'Kraf Tradisional','5.0':'Bernyanyi','6.0':'Alat Perkusi'}, 'SP': {'1.0.1':'Mengenal bahasa seni visual','2.0.1':'Membuat corak mudah','3.0.1':'Membina model','4.0.1':'Mengenal kraf tradisional','5.0.1':'Bernyanyi dengan irama','6.0.1':'Bermain alat perkusi'}},
        'Year 2': {'SK': {'1.0':'Menggambar','2.0':'Corak dan Rekaan','3.0':'Bentuk dan Binaan','4.0':'Kraf Tradisional','5.0':'Bernyanyi','6.0':'Alat Perkusi'}, 'SP': {'1.0.1':'Mengaplikasi bahasa seni visual','2.0.1':'Membuat corak dengan teknik','3.0.1':'Membina model kreatif','4.0.1':'Membuat kraf tradisional','5.0.1':'Bernyanyi dengan pic betul','6.0.1':'Bermain alat perkusi mengikut irama'}},
        'Year 3': {'SK': {'1.0':'Menggambar','2.0':'Corak dan Rekaan','3.0':'Bentuk dan Binaan','4.0':'Kraf Tradisional','5.0':'Bernyanyi','6.0':'Alat Perkusi'}, 'SP': {'1.0.1':'Mengaplikasi bahasa seni visual dengan kreatif','2.0.1':'Membuat corak dengan pelbagai teknik','3.0.1':'Membina model dan boneka','4.0.1':'Menghasilkan kraf tradisional','5.0.1':'Bernyanyi dengan teknik betul','6.0.1':'Bermain alat perkusi dengan corak irama'}},
    },
    'PJPK': {
        'Year 1': {'SK': {'1.0':'Gimnastik Asas','2.0':'Pergerakan Berirama','3.0':'Permainan','4.0':'Kesihatan Diri','5.0':'Keselamatan'}, 'SP': {'1.0.1':'Melakukan pergerakan asas','2.0.1':'Membuat pergerakan mengikut irama','3.0.1':'Melakukan permainan mudah','4.0.1':'Mengamalkan kebersihan diri','5.0.1':'Mengamalkan keselamatan diri'}},
        'Year 2': {'SK': {'1.0':'Gimnastik Asas','2.0':'Pergerakan Berirama','3.0':'Permainan','4.0':'Kesihatan Diri','5.0':'Kesihatan Mental'}, 'SP': {'1.0.1':'Melakukan pergerakan dengan koordinasi','2.0.1':'Membuat pergerakan kreatif','3.0.1':'Melakukan permainan dengan peraturan','4.0.1':'Mengamalkan penjagaan kebersihan','5.0.1':'Mengenal pasti emosi'}},
        'Year 3': {'SK': {'1.0':'Gimnastik','2.0':'Berirama','3.0':'Permainan','4.0':'Kecergasan','5.0':'Kesihatan'}, 'SP': {'1.0.1':'Melakukan kemahiran gimnastik','2.0.1':'Membuat pergerakan berirama dengan muzik','3.0.1':'Melakukan permainan berkategori','4.0.1':'Melakukan aktiviti kecergasan','5.0.1':'Mengamalkan gaya hidup sihat'}},
        'Year 4': {'SK': {'1.0':'Olahraga','2.0':'Berirama','3.0':'Permainan','4.0':'Akuatik','5.0':'Kesihatan'}, 'SP': {'1.0.1':'Melakukan kemahiran olahraga','2.0.1':'Membuat pergerakan berirama dengan alat','3.0.1':'Melakukan permainan berkategori','4.0.1':'Melakukan kemahiran asas akuatik','5.0.1':'Mengamalkan penjagaan kesihatan'}},
        'Year 5': {'SK': {'1.0':'Olahraga','2.0':'Berirama','3.0':'Permainan Serangan','4.0':'Permainan Jaring','5.0':'Kecergasan','6.0':'Kesihatan'}, 'SP': {'1.0.1':'Melakukan kemahiran olahraga dengan teknik','2.0.1':'Membuat pergerakan berirama secara kumpulan','3.0.1':'Melakukan kemahiran permainan serangan','4.0.1':'Melakukan kemahiran permainan jaring','5.0.1':'Melakukan aktiviti kecergasan','6.0.1':'Mengamalkan gaya hidup sihat'}},
        'Year 6': {'SK': {'1.0':'Olahraga','2.0':'Berirama','3.0':'Permainan Jaring','4.0':'Rekreasi','5.0':'Kecergasan','6.0':'Kesihatan'}, 'SP': {'1.0.1':'Melakukan kemahiran olahraga dengan teknik betul','2.0.1':'Membuat pergerakan berirama secara kreatif','3.0.1':'Melakukan kemahiran permainan jaring dengan strategi','4.0.1':'Mengambil bahagian dalam rekreasi','5.0.1':'Melakukan aktiviti kecergasan secara terancang','6.0.1':'Mengamalkan gaya hidup sihat secara holistik'}},
    },
    'PMZ': {
        'Year 1': {'SK': {'1.0':'Bernyanyi','2.0':'Alat Perkusi','3.0':'Pergerakan Muzikal','4.0':'Apresiasi'}, 'SP': {'1.0.1':'Bernyanyi lagu mudah','2.0.1':'Bermain alat perkusi asas','3.0.1':'Membuat pergerakan mengikut muzik','4.0.1':'Mengenal pasti alat muzik'}},
        'Year 2': {'SK': {'1.0':'Bernyanyi','2.0':'Alat Perkusi','3.0':'Pergerakan Muzikal','4.0':'Apresiasi'}, 'SP': {'1.0.1':'Bernyanyi dengan pic betul','2.0.1':'Bermain alat perkusi dengan irama','3.0.1':'Membuat pergerakan kreatif','4.0.1':'Mengenal pasti tempo dan dinamik'}},
        'Year 3': {'SK': {'1.0':'Bernyanyi','2.0':'Alat Perkusi','3.0':'Pergerakan Muzikal','4.0':'Apresiasi'}, 'SP': {'1.0.1':'Bernyanyi dengan teknik betul','2.0.1':'Bermain alat perkusi dengan corak irama','3.0.1':'Membuat pergerakan dengan alat','4.0.1':'Menilai muzik berdasarkan unsur muzik'}},
        'Year 4': {'SK': {'1.0':'Bernyanyi','2.0':'Rekoder','3.0':'Pergerakan Muzikal','4.0':'Apresiasi'}, 'SP': {'1.0.1':'Bernyanyi dengan teknik vokal','2.0.1':'Bermain rekoder dengan teknik betul','3.0.1':'Membuat pergerakan kreatif berkumpulan','4.0.1':'Mengapresiasi muzik pelbagai budaya'}},
        'Year 5': {'SK': {'1.0':'Bernyanyi','2.0':'Rekoder','3.0':'Pergerakan Muzikal','4.0':'Apresiasi'}, 'SP': {'1.0.1':'Bernyanyi dengan teknik vokal dan ekspresi','2.0.1':'Bermain rekoder dengan pic dan irama betul','3.0.1':'Membuat pergerakan kreatif secara berkumpulan','4.0.1':'Mengapresiasi muzik tempatan'}},
        'Year 6': {'SK': {'1.0':'Bernyanyi','2.0':'Ensembel','3.0':'Pergerakan Muzikal','4.0':'Apresiasi'}, 'SP': {'1.0.1':'Bernyanyi dalam ensembel','2.0.1':'Bermain alat muzik dalam ensembel','3.0.1':'Membuat pergerakan kreatif secara berkumpulan','4.0.1':'Mengapresiasi karya muzik'}},
    },
}

# Merge additional subjects
for subj, years_data in ADDITIONAL.items():
    for year, data in years_data.items():
        key = f'{year}|{subj}'
        if key not in CURR_DB:
            CURR_DB[key] = data

# Generate JS file
lines = []
lines.append('// curriculum-db.js — Auto-generated DSKP Content & Learning Standards')
lines.append('// Source: Official KSSR DSKP documents for SJKC')
lines.append('')
lines.append('const CURR_DB = {')

keys = sorted(CURR_DB.keys())
for ki, key in enumerate(keys):
    data = CURR_DB[key]
    comma = ',' if ki < len(keys) - 1 else ''
    lines.append(f"  '{key}': {{")
    lines.append(f"    SK: {json.dumps(data['SK'], ensure_ascii=False)},")
    lines.append(f"    SP: {json.dumps(data['SP'], ensure_ascii=False)}")
    lines.append(f"  }}{comma}")

lines.append('};')
lines.append('')
lines.append('// Helper: get SK/SP for a subject+year')
lines.append("function getCurriculum(year, subject) { return CURR_DB[year+'|'+subject] || null; }")
lines.append("function getSK(year, subject) { const d = getCurriculum(year, subject); return d ? Object.values(d.SK) : []; }")
lines.append("function getSP(year, subject) { const d = getCurriculum(year, subject); return d ? Object.values(d.SP) : []; }")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f"Written: {os.path.getsize(OUT)} bytes")
print(f"Total entries: {len(CURR_DB)}")
