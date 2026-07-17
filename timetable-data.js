// Auto-generated timetable data for SJK(C) PIN MIN, BIDOR STESEN, PERAK

const TEACHERS = {
  "TBS": {
    "name": "TEOH BOON SIM",
    "name_cn": "张汶森"
  },
  "LET": {
    "name": "LEE EE TING",
    "name_cn": "李依婷"
  },
  "HLF": {
    "name": "HEW LEE FUN",
    "name_cn": "丘丽芬"
  },
  "LJX": {
    "name": "LIAN JUNXIANG",
    "name_cn": "连浚翔"
  },
  "LSW": {
    "name": "LEE SHU WEN",
    "name_cn": "李淑雯"
  },
  "WKS": {
    "name": "WONG KA SUIT (MELISSA)",
    "name_cn": "黄家煦"
  },
  "LYY": {
    "name": "LOOI YUN YUAN",
    "name_cn": "雷昀苑"
  },
  "OWY": {
    "name": "ONG WEI YI",
    "name_cn": "王维仪"
  },
  "ARMAN": {
    "name": "ARMAN BIN AWANG",
    "name_cn": ""
  },
  "COW": {
    "name": "CHONG OOI WEI",
    "name_cn": "锺爱媚"
  },
  "BALKIS": {
    "name": "NUR BALKIS BINTI ZULKHAIRANI",
    "name_cn": ""
  },
  "YH": {
    "name": "YOONG HAI",
    "name_cn": "熊海师"
  }
};

const PERIODS = [
  [
    "P",
    "07:45",
    "08:15"
  ],
  [
    "1",
    "08:15",
    "08:45"
  ],
  [
    "2",
    "08:45",
    "09:15"
  ],
  [
    "3",
    "09:15",
    "09:45"
  ],
  [
    "4",
    "09:45",
    "10:15"
  ],
  [
    "REHAT",
    "10:15",
    "10:35"
  ],
  [
    "5",
    "10:35",
    "11:05"
  ],
  [
    "6",
    "11:05",
    "11:35"
  ],
  [
    "7",
    "11:35",
    "12:05"
  ],
  [
    "8",
    "12:05",
    "12:35"
  ],
  [
    "9",
    "12:35",
    "13:05"
  ],
  [
    "10",
    "13:05",
    "13:35"
  ],
  [
    "11",
    "13:35",
    "14:05"
  ],
  [
    "12",
    "14:05",
    "14:35"
  ]
];

const DAYS = ["Isnin", "Selasa", "Rabu", "Khamis", "Jumaat"];

const CLASSES = ["Prasekolah", "Tahun 1", "Tahun 2", "Tahun 3", "Tahun 4", "Tahun 5", "Tahun 6"];

const TIMETABLE_P1 = {
  "Tahun 1": {
    "Isnin": {
      "P": {"subject": "P", "subjectName": "Perhimpunan", "teacher": "LET", "raw": "P LET"},
      "1": {"subject": "PM", "subjectName": "Pendidikan Moral", "teacher": "LET", "raw": "PM LET"},
      "3": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "LJX", "raw": "BI LJX"},
      "4": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "BALKIS", "raw": "BM BALKIS"},
      "5": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "BALKIS", "raw": "BM BALKIS"},
      "6": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "LJX", "raw": "BI LJX"},
      "8": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "BALKIS", "raw": "BM BALKIS"}
    },
    "Selasa": {
      "P": {"subject": "PJ", "subjectName": "Pendidikan Jasmani", "teacher": "OWY", "raw": "PJ OWY"},
      "1": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LET", "raw": "BC LET"},
      "3": {"subject": "MT", "subjectName": "Matematik", "teacher": "LSW", "raw": "MT LSW"},
      "5": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LET", "raw": "BC LET"},
      "6": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "BALKIS", "raw": "BM BALKIS"},
      "9": {"subject": "PK", "subjectName": "Pendidikan Kesihatan", "teacher": "OWY", "raw": "PK OWY"}
    },
    "Rabu": {
      "P": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "BALKIS", "raw": "BM BALKIS"},
      "2": {"subject": "PSV", "subjectName": "Pendidikan Seni Visual", "teacher": "BALKIS", "raw": "PSV BALKIS"},
      "4": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LET", "raw": "BC LET"},
      "6": {"subject": "MT", "subjectName": "Matematik", "teacher": "LSW", "raw": "MT LSW"},
      "8": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LET", "raw": "BC LET"}
    },
    "Khamis": {
      "P": {"subject": "PJ", "subjectName": "Pendidikan Jasmani", "teacher": "OWY", "raw": "PJ OWY"},
      "1": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LET", "raw": "BC LET"},
      "2": {"subject": "MZ", "subjectName": "Pendidikan Muzik", "teacher": "LSW", "raw": "Mz LSW"},
      "3": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LET", "raw": "BC LET"},
      "6": {"subject": "PM", "subjectName": "Pendidikan Moral", "teacher": "LET", "raw": "PM LET"},
      "8": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "LJX", "raw": "BI LJX"}
    },
    "Jumaat": {
      "P": {"subject": "SN", "subjectName": "Sains", "teacher": "LSW", "raw": "Sn LSW"},
      "1": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LET", "raw": "BC LET"},
      "3": {"subject": "SN", "subjectName": "Sains", "teacher": "LSW", "raw": "Sn LSW"},
      "6": {"subject": "MT", "subjectName": "Matematik", "teacher": "LSW", "raw": "MT LSW"},
      "8": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "BALKIS", "raw": "BM BALKIS"}
    }
  },
  "Tahun 2": {
    "Isnin": {
      "P": {"subject": "P", "subjectName": "Perhimpunan", "teacher": "COW", "raw": "P COW"},
      "1": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "BALKIS", "raw": "BM BALKIS"},
      "2": {"subject": "MT", "subjectName": "Matematik", "teacher": "LYY", "raw": "MT LYY"},
      "4": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "COW", "raw": "BC COW"},
      "5": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "COW", "raw": "BC COW"},
      "6": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "BALKIS", "raw": "BM BALKIS"},
      "8": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "COW", "raw": "BC COW"},
      "10": {"subject": "PI", "subjectName": "Tasmik", "teacher": "ARMAN", "raw": "TASMIK ARMAN"}
    },
    "Selasa": {
      "P": {"subject": "PJ", "subjectName": "Pendidikan Jasmani", "teacher": "HLF", "raw": "PJ HLF"},
      "4b": {"subject": "PI", "subjectName": "Pendidikan Agama", "teacher": "ARMAN", "raw": "PA ARMAN"},
      "5b": {"subject": "PI", "subjectName": "Pendidikan Agama", "teacher": "ARMAN", "raw": "PA ARMAN"},
      "1": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "BALKIS", "raw": "BM BALKIS"},
      "3": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "WKS", "raw": "BI WKS"},
      "4": {"subject": "PM", "subjectName": "Pendidikan Moral", "teacher": "COW", "raw": "PM COW"},
      "5": {"subject": "PM", "subjectName": "Pendidikan Moral", "teacher": "COW", "raw": "PM COW"},
      "6": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "WKS", "raw": "BI WKS"},
      "9": {"subject": "PK", "subjectName": "Pendidikan Kesihatan", "teacher": "HLF", "raw": "PK HLF"}
    },
    "Rabu": {
      "P": {"subject": "PSV", "subjectName": "Pendidikan Seni Visual", "teacher": "ARMAN", "raw": "PSV ARMAN"},
      "2": {"subject": "MT", "subjectName": "Matematik", "teacher": "LYY", "raw": "MT LYY"},
      "4": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "COW", "raw": "BC COW"},
      "6": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "WKS", "raw": "BI WKS"},
      "8": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "COW", "raw": "BC COW"}
    },
    "Khamis": {
      "P": {"subject": "PJ", "subjectName": "Pendidikan Jasmani", "teacher": "HLF", "raw": "PJ HLF"},
      "1": {"subject": "SN", "subjectName": "Sains", "teacher": "COW", "raw": "Sn COW"},
      "3": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "BALKIS", "raw": "BM BALKIS"},
      "5": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "COW", "raw": "BC COW"},
      "6": {"subject": "SN", "subjectName": "Sains", "teacher": "COW", "raw": "Sn COW"},
      "9": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "COW", "raw": "BC COW"}
    },
    "Jumaat": {
      "P": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "BALKIS", "raw": "BM BALKIS"},
      "4b": {"subject": "PI", "subjectName": "Pendidikan Agama", "teacher": "ARMAN", "raw": "PA ARMAN"},
      "2": {"subject": "MZ", "subjectName": "Pendidikan Muzik", "teacher": "WKS", "raw": "Mz WKS"},
      "3": {"subject": "PM", "subjectName": "Pendidikan Moral", "teacher": "COW", "raw": "PM COW"},
      "5": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "COW", "raw": "BC COW"},
      "6": {"subject": "MT", "subjectName": "Matematik", "teacher": "LYY", "raw": "MT LYY"}
    }
  },
  "Tahun 3": {
    "Isnin": {
      "P": {"subject": "P", "subjectName": "Perhimpunan", "teacher": "LYY", "raw": "P LYY"},
      "1": {"subject": "MT", "subjectName": "Matematik", "teacher": "COW", "raw": "MT COW"},
      "3": {"subject": "PSV", "subjectName": "Pendidikan Seni Visual", "teacher": "ARMAN", "raw": "PSV ARMAN"},
      "5": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LYY", "raw": "BC LYY"},
      "6": {"subject": "MZ", "subjectName": "Pendidikan Muzik", "teacher": "LET", "raw": "Mz LET"},
      "8": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LYY", "raw": "BC LYY"},
      "10": {"subject": "PI", "subjectName": "Tasmik", "teacher": "ARMAN", "raw": "TASMIK ARMAN"}
    },
    "Selasa": {
      "P": {"subject": "PJ", "subjectName": "Pendidikan Jasmani", "teacher": "COW", "raw": "PJ COW"},
      "1": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "LJX", "raw": "BI LJX"},
      "3": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "BALKIS", "raw": "BM BALKIS"},
      "5": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LYY", "raw": "BC LYY"},
      "6": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "LJX", "raw": "BI LJX"},
      "9": {"subject": "PK", "subjectName": "Pendidikan Kesihatan", "teacher": "COW", "raw": "PK COW"}
    },
    "Rabu": {
      "P": {"subject": "SN", "subjectName": "Sains", "teacher": "HLF", "raw": "Sn HLF"},
      "8b": {"subject": "PI", "subjectName": "Pendidikan Agama", "teacher": "ARMAN", "raw": "PA ARMAN"},
      "1": {"subject": "MT", "subjectName": "Matematik", "teacher": "COW", "raw": "MT COW"},
      "3": {"subject": "SN", "subjectName": "Sains", "teacher": "HLF", "raw": "Sn HLF"},
      "6": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "BALKIS", "raw": "BM BALKIS"},
      "8": {"subject": "PM", "subjectName": "Pendidikan Moral", "teacher": "LYY", "raw": "PM LYY"}
    },
    "Khamis": {
      "P": {"subject": "PJ", "subjectName": "Pendidikan Jasmani", "teacher": "COW", "raw": "PJ COW"},
      "4b": {"subject": "PI", "subjectName": "Pendidikan Agama", "teacher": "ARMAN", "raw": "PA ARMAN"},
      "5b": {"subject": "PI", "subjectName": "Pendidikan Agama", "teacher": "ARMAN", "raw": "PA ARMAN"},
      "1": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "BALKIS", "raw": "BM BALKIS"},
      "3": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LYY", "raw": "BC LYY"},
      "4": {"subject": "PM", "subjectName": "Pendidikan Moral", "teacher": "LYY", "raw": "PM LYY"},
      "5": {"subject": "PM", "subjectName": "Pendidikan Moral", "teacher": "LYY", "raw": "PM LYY"},
      "6": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "BALKIS", "raw": "BM BALKIS"},
      "7": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LYY", "raw": "BC LYY"}
    },
    "Jumaat": {
      "P": {"subject": "MT", "subjectName": "Matematik", "teacher": "COW", "raw": "MT COW"},
      "2": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LYY", "raw": "BC LYY"},
      "3": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "BALKIS", "raw": "BM BALKIS"},
      "5": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LYY", "raw": "BC LYY"},
      "6": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "LJX", "raw": "BI LJX"}
    }
  },
  "Tahun 4": {
    "Isnin": {
      "P": {"subject": "P", "subjectName": "Perhimpunan", "teacher": "HLF", "raw": "P HLF"},
      "1": {"subject": "PM", "subjectName": "Pendidikan Moral", "teacher": "HLF", "raw": "PM HLF"},
      "2": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "HLF", "raw": "BC HLF"},
      "4": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "WKS", "raw": "BI WKS"},
      "5": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "WKS", "raw": "BI WKS"},
      "6": {"subject": "PM", "subjectName": "Pendidikan Moral", "teacher": "HLF", "raw": "PM HLF"},
      "8": {"subject": "MT", "subjectName": "Matematik", "teacher": "LET", "raw": "MT LET"}
    },
    "Selasa": {
      "P": {"subject": "SJ", "subjectName": "Sejarah", "teacher": "TBS", "raw": "Sjr TBS"},
      "2": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "OWY", "raw": "BM OWY"},
      "4": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "HLF", "raw": "BC HLF"},
      "5": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "HLF", "raw": "BC HLF"},
      "6": {"subject": "SN", "subjectName": "Sains", "teacher": "COW", "raw": "Sn COW"},
      "8": {"subject": "MT", "subjectName": "Matematik", "teacher": "LET", "raw": "MT LET"}
    },
    "Rabu": {
      "P": {"subject": "PJ", "subjectName": "Pendidikan Jasmani", "teacher": "WKS", "raw": "PJ WKS"},
      "1": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "OWY", "raw": "BM OWY"},
      "3": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "WKS", "raw": "BI WKS"},
      "5": {"subject": "SN", "subjectName": "Sains", "teacher": "COW", "raw": "Sn COW"},
      "7": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "HLF", "raw": "BC HLF"},
      "10": {"subject": "PK", "subjectName": "Pendidikan Kesihatan", "teacher": "WKS", "raw": "PK WKS"}
    },
    "Khamis": {
      "P": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "WKS", "raw": "BI WKS"},
      "2": {"subject": "RBT", "subjectName": "RBT", "teacher": "WKS", "raw": "RBT WKS"},
      "4": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "OWY", "raw": "BM OWY"},
      "5": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "OWY", "raw": "BM OWY"},
      "6": {"subject": "PSV", "subjectName": "Pendidikan Seni Visual", "teacher": "ARMAN", "raw": "PSV ARMAN"},
      "8": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "HLF", "raw": "BC HLF"}
    },
    "Jumaat": {
      "P": {"subject": "PJ", "subjectName": "Pendidikan Jasmani", "teacher": "WKS", "raw": "PJ WKS"},
      "1": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "OWY", "raw": "BM OWY"},
      "3": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "HLF", "raw": "BC HLF"},
      "6": {"subject": "MT", "subjectName": "Matematik", "teacher": "LET", "raw": "MT LET"},
      "8": {"subject": "MZ", "subjectName": "Pendidikan Muzik", "teacher": "LET", "raw": "Mz LET"},
      "9": {"subject": "PM", "subjectName": "Pendidikan Moral", "teacher": "HLF", "raw": "PM HLF"}
    }
  },
  "Tahun 5": {
    "Isnin": {
      "P": {"subject": "P", "subjectName": "Perhimpunan", "teacher": "WKS", "raw": "P WKS"},
      "1": {"subject": "PM", "subjectName": "Pendidikan Moral", "teacher": "WKS", "raw": "PM WKS"},
      "3": {"subject": "MZ", "subjectName": "Pendidikan Muzik", "teacher": "OWY", "raw": "Mz OWY"},
      "4": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LJX", "raw": "BC LJX"},
      "5": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LJX", "raw": "BC LJX"},
      "6": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "OWY", "raw": "BM OWY"},
      "8": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "WKS", "raw": "BI WKS"}
    },
    "Selasa": {
      "P": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "WKS", "raw": "BI WKS"},
      "2": {"subject": "MT", "subjectName": "Matematik", "teacher": "HLF", "raw": "MT HLF"},
      "4": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LJX", "raw": "BC LJX"},
      "5": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LJX", "raw": "BC LJX"},
      "6": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "OWY", "raw": "BM OWY"},
      "9": {"subject": "RBT", "subjectName": "RBT", "teacher": "LYY", "raw": "RBT LYY"}
    },
    "Rabu": {
      "P": {"subject": "PJ", "subjectName": "Pendidikan Jasmani", "teacher": "LYY", "raw": "PJ LYY"},
      "1": {"subject": "SJ", "subjectName": "Sejarah", "teacher": "LET", "raw": "Sjr LET"},
      "3": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LJX", "raw": "BC LJX"},
      "6": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "OWY", "raw": "BM OWY"},
      "7": {"subject": "SN", "subjectName": "Sains", "teacher": "LSW", "raw": "Sn LSW"},
      "10": {"subject": "PK", "subjectName": "Pendidikan Kesihatan", "teacher": "LYY", "raw": "PK LYY"}
    },
    "Khamis": {
      "P": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LJX", "raw": "BC LJX"},
      "2": {"subject": "MT", "subjectName": "Matematik", "teacher": "HLF", "raw": "MT HLF"},
      "4": {"subject": "SN", "subjectName": "Sains", "teacher": "LSW", "raw": "Sn LSW"},
      "5": {"subject": "SN", "subjectName": "Sains", "teacher": "LSW", "raw": "Sn LSW"},
      "6": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "WKS", "raw": "BI WKS"},
      "8": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "OWY", "raw": "BM OWY"}
    },
    "Jumaat": {
      "P": {"subject": "PJ", "subjectName": "Pendidikan Jasmani", "teacher": "LYY", "raw": "PJ LYY"},
      "1": {"subject": "PSV", "subjectName": "Pendidikan Seni Visual", "teacher": "ARMAN", "raw": "PSV ARMAN"},
      "3": {"subject": "PM", "subjectName": "Pendidikan Moral", "teacher": "WKS", "raw": "PM WKS"},
      "4": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LJX", "raw": "BC LJX"},
      "5": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LJX", "raw": "BC LJX"},
      "6": {"subject": "MT", "subjectName": "Matematik", "teacher": "HLF", "raw": "MT HLF"},
      "9": {"subject": "PM", "subjectName": "Pendidikan Moral", "teacher": "WKS", "raw": "PM WKS"}
    }
  },
  "Tahun 6": {
    "Isnin": {
      "P": {"subject": "P", "subjectName": "Perhimpunan", "teacher": "LSW", "raw": "P LSW"},
      "1": {"subject": "PM", "subjectName": "Pendidikan Moral", "teacher": "LSW", "raw": "PM LSW"},
      "3": {"subject": "RBT", "subjectName": "RBT", "teacher": "TBS", "raw": "RBT TBS"},
      "5": {"subject": "PM", "subjectName": "Pendidikan Moral", "teacher": "LSW", "raw": "PM LSW"},
      "6": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LSW", "raw": "BC LSW"},
      "8": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "OWY", "raw": "BM OWY"}
    },
    "Selasa": {
      "P": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LSW", "raw": "BC LSW"},
      "2": {"subject": "SN", "subjectName": "Sains", "teacher": "LYY", "raw": "Sn LYY"},
      "4": {"subject": "SJ", "subjectName": "Sejarah", "teacher": "WKS", "raw": "Sjr WKS"},
      "5": {"subject": "SJ", "subjectName": "Sejarah", "teacher": "WKS", "raw": "Sjr WKS"},
      "6": {"subject": "PSV", "subjectName": "Pendidikan Seni Visual", "teacher": "ARMAN", "raw": "PSV ARMAN"},
      "9": {"subject": "PM", "subjectName": "Pendidikan Moral", "teacher": "LSW", "raw": "PM LSW"}
    },
    "Rabu": {
      "P": {"subject": "PJ", "subjectName": "Pendidikan Jasmani", "teacher": "LJX", "raw": "PJ LJX"},
      "1": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LSW", "raw": "BC LSW"},
      "3": {"subject": "MT", "subjectName": "Matematik", "teacher": "TBS", "raw": "MT TBS"},
      "5": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "LJX", "raw": "BI LJX"},
      "6": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "OWY", "raw": "BM OWY"},
      "10": {"subject": "PK", "subjectName": "Pendidikan Kesihatan", "teacher": "LJX", "raw": "PK LJX"}
    },
    "Khamis": {
      "P": {"subject": "SN", "subjectName": "Sains", "teacher": "LYY", "raw": "Sn LYY"},
      "2": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "OWY", "raw": "BM OWY"},
      "4": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "LJX", "raw": "BI LJX"},
      "5": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "LJX", "raw": "BI LJX"},
      "6": {"subject": "MT", "subjectName": "Matematik", "teacher": "TBS", "raw": "MT TBS"},
      "8": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LSW", "raw": "BC LSW"}
    },
    "Jumaat": {
      "P": {"subject": "PJ", "subjectName": "Pendidikan Jasmani", "teacher": "LJX", "raw": "PJ LJX"},
      "1": {"subject": "BI", "subjectName": "Bahasa Inggeris", "teacher": "LJX", "raw": "BI LJX"},
      "3": {"subject": "MT", "subjectName": "Matematik", "teacher": "TBS", "raw": "MT TBS"},
      "6": {"subject": "BM", "subjectName": "Bahasa Melayu", "teacher": "OWY", "raw": "BM OWY"},
      "8": {"subject": "MZ", "subjectName": "Pendidikan Muzik", "teacher": "OWY", "raw": "Mz OWY"},
      "9": {"subject": "BC", "subjectName": "Bahasa Cina", "teacher": "LSW", "raw": "BC LSW"}
    }
  },
  "Prasekolah": {
    "Isnin": {
    },
    "Selasa": {
    },
    "Rabu": {
    },
    "Khamis": {
      "2": {"subject": "PI", "subjectName": "Pendidikan Agama", "teacher": "ARMAN", "raw": "PA ARMAN"}
    },
    "Jumaat": {
      "7": {"subject": "PI", "subjectName": "Pendidikan Agama", "teacher": "ARMAN", "raw": "PA ARMAN"}
    }
  }
};

const TIMETABLE_P2 = 
{
  'Tahun 1': {
    'Isnin': {
      'P': 'P LET',
      '1': 'PM LET',
      '3': 'BM BALKIS',
      '5': 'Mz LSW',
      '6': 'BM BALKIS',
      '7': 'PSV BALKIS'
    },
    'Selasa': {
      'P': 'PJ OWY',
      '1': 'BC LET',
      '3': 'BM BALKIS',
      '5': 'MT LSW',
      '7': 'BC LET',
      '9': 'PK OWY'
    },
    'Rabu': {
      'P': 'PM LET',
      '2': 'Sn LSW',
      '4': 'BC LET',
      '5': 'BC LET',
      '6': 'Sn LSW',
      '8': 'BM BALKIS'
    },
    'Khamis': {
      'P': 'PJ OWY',
      '1': 'BI LJX',
      '3': 'BC LET',
      '4': 'MT LSW',
      '5': 'MT LSW',
      '6': 'BC LET',
      '8': 'BI LJX'
    },
    'Jumaat': {
      'P': 'MT LSW',
      '2': 'BC LET',
      '4': 'BI LJX',
      '5': 'BI LJX',
      '6': 'BC LET',
      '8': 'BM BALKIS'
    }
  },
  'Tahun 2': {
    'Isnin': {
      'P': 'P COW',
      '1': 'BC COW',
      '3': 'BI LJX',
      '5': 'Sn COW',
      '6': 'BI LJX',
      '8': 'Sn COW',
      '10': 'TASMIK ARMAN'
    },
    'Selasa': {
      'P': 'PJ HLF',
      '1': 'BM BALKIS',
      '3': 'Mz YH',
      '4': 'BI LJX',
      '5': 'BI LJX',
      '6': 'MT LYY',
      '9': 'PK HLF'
    },
    'Rabu': {
      'P': 'PA ARMAN',
      '2': 'BC COW',
      '3': 'MT LYY',
      '5': 'BM BALKIS',
      '7': 'BC COW'
    },
    'Khamis': {
      'P': 'PJ HLF',
      '1': 'BM BALKIS',
      '2': 'BC COW',
      '3': 'BM BALKIS',
      '6': 'PSV ARMAN',
      '8': 'BC COW'
    },
    'Jumaat': {
      'P': 'PA ARMAN',
      '2': 'BC COW',
      '3': 'BM BALKIS',
      '6': 'MT LYY',
      '8': 'BC COW'
    }
  },
  'Tahun 3': {
    'Isnin': {
      'P': 'P LYY',
      '1': 'BI LJX',
      '3': 'PM LYY',
      '5': 'BC LYY',
      '6': 'BC LYY',
      '7': 'BI LJX',
      '8': 'BC LYY',
      '4b': 'PA ARMAN',
      '10': 'TASMIK ARMAN'
    },
    'Selasa': {
      'P': 'PJ COW',
      '1': 'BC LYY',
      '3': 'MT COW',
      '5': 'BC LYY',
      '6': 'BM BALKIS',
      '9': 'PK COW'
    },
    'Rabu': {
      'P': 'BM BALKIS',
      '2': 'PSV ARMAN',
      '4': 'MT COW',
      '5': 'MT COW',
      '6': 'PM LYY',
      '7b': 'PA ARMAN',
      '8': 'Mz LET'
    },
    'Khamis': {
      'P': 'PJ COW',
      '1': 'Sn HLF',
      '3': 'BC LYY',
      '5': 'Sn HLF',
      '6': 'BC LYY',
      '8': 'BM BALKIS'
    },
    'Jumaat': {
      'P': 'BM BALKIS',
      '2': 'BC LYY',
      '4': 'MT COW',
      '5': 'MT COW',
      '6': 'BM BALKIS',
      '8': 'BI LJX'
    }
  },
  'Tahun 4': {
    'Isnin': {
      'P': 'P HLF',
      '1': 'BC HLF',
      '3': 'BM OWY',
      '5': 'Mz LET',
      '6': 'PSV ARMAN',
      '8': 'BI YH'
    },
    'Selasa': {
      'P': 'BI YH',
      '2': 'Sjr TBS',
      '4': 'BC HLF',
      '5': 'BC HLF',
      '6': 'Sn COW',
      '8': 'MT LET'
    },
    'Rabu': {
      'P': 'PJ YH',
      '1': 'BM OWY',
      '3': 'BC HLF',
      '5': 'RBT YH',
      '7': 'PM HLF',
      '10': 'PK YH'
    },
    'Khamis': {
      'P': 'MT LET',
      '2': 'BM OWY',
      '4': 'Sn COW',
      '5': 'Sn COW',
      '6': 'BC HLF',
      '8': 'BI YH'
    },
    'Jumaat': {
      'P': 'PJ YH',
      '1': 'PM HLF',
      '3': 'BM OWY',
      '5': 'BC HLF',
      '6': 'PM HLF',
      '8': 'MT LET'
    }
  },
  'Tahun 5': {
    'Isnin': {
      'P': 'P YH',
      '1': 'BC YH',
      '3': 'PM YH',
      '5': 'MT HLF',
      '6': 'Sjr LET',
      '8': 'Mz OWY'
    },
    'Selasa': {
      'P': 'BI LJX',
      '2': 'MT HLF',
      '4': 'PSV ARMAN',
      '5': 'PSV ARMAN',
      '6': 'BM OWY',
      '8': 'BC YH'
    },
    'Rabu': {
      'P': 'PJ LYY',
      '1': 'MT HLF',
      '3': 'BC YH',
      '5': 'BI LJX',
      '6': 'BM OWY',
      '10': 'PK LYY'
    },
    'Khamis': {
      'P': 'RBT LYY',
      '2': 'BC YH',
      '4': 'BI LJX',
      '5': 'BI LJX',
      '6': 'Sn LSW',
      '8': 'BM OWY'
    },
    'Jumaat': {
      'P': 'PJ LYY',
      '1': 'PM YH',
      '2': 'Sn LSW',
      '4': 'PM YH',
      '5': 'PM YH',
      '6': 'BM OWY',
      '8': 'BC YH'
    }
  },
  'Tahun 6': {
    'Isnin': {
      'P': 'P LSW',
      '1': 'BC LSW',
      '3': 'PM LSW',
      '4': 'MT TBS',
      '5': 'MT TBS',
      '6': 'BM OWY',
      '8': 'PM LSW'
    },
    'Selasa': {
      'P': 'BC LSW',
      '2': 'PSV ARMAN',
      '4': 'BM OWY',
      '5': 'BM OWY',
      '6': 'BI LJX',
      '9': 'PM LSW'
    },
    'Rabu': {
      'P': 'PJ LJX',
      '1': 'BI LJX',
      '3': 'BM OWY',
      '5': 'MT TBS',
      '7': 'BC LSW',
      '10': 'PK LJX'
    },
    'Khamis': {
      'P': 'BC LSW',
      '2': 'MT TBS',
      '4': 'BM OWY',
      '5': 'BM OWY',
      '6': 'Sjr YH',
      '8': 'Sn LYY'
    },
    'Jumaat': {
      'P': 'PJ LJX',
      '1': 'BI LJX',
      '3': 'RBT TBS',
      '5': 'BC LSW',
      '6': 'Sn LYY',
      '10': 'Mz OWY'
    }
  },
  'Prasekolah': {
    'Khamis': {
      '2': 'PA ARMAN'
    },
    'Jumaat': {
      '7': 'PA ARMAN'
    }
  }
}
;

// For each teacher, compute which slots they teach
function getTeacherTimetable(teacherCode, penggal) {
  const tt = penggal === 1 ? TIMETABLE_P1 : TIMETABLE_P1; // Same structure
  const slots = [];
  const classes = Object.keys(tt);
  classes.forEach(cls => {
    DAYS.forEach(day => {
      const dayData = tt[cls][day] || {};
      Object.keys(dayData).forEach(period => {
        const cell = dayData[period];
        if (cell.teacher === teacherCode) {
          slots.push({ class: cls, day, period, subject: cell.subject, subjectName: cell.subjectName });
        }
      });
    });
  });
  return slots;
}

const TEACHER_SLOTS_P1 = {};
TEACHER_SLOTS_P1["TBS"] = [{class:"Tahun 4",day:"Selasa",period:"P",subject:"SJ",subjectName:"Sejarah"},{class:"Tahun 6",day:"Isnin",period:"3",subject:"RBT",subjectName:"RBT"},{class:"Tahun 6",day:"Rabu",period:"3",subject:"MT",subjectName:"Matematik"},{class:"Tahun 6",day:"Khamis",period:"6",subject:"MT",subjectName:"Matematik"},{class:"Tahun 6",day:"Jumaat",period:"3",subject:"MT",subjectName:"Matematik"}];
TEACHER_SLOTS_P1["LET"] = [{class:"Tahun 1",day:"Isnin",period:"1",subject:"PM",subjectName:"Pendidikan Moral"},{class:"Tahun 1",day:"Selasa",period:"1",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 1",day:"Selasa",period:"5",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 1",day:"Rabu",period:"4",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 1",day:"Rabu",period:"8",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 1",day:"Khamis",period:"1",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 1",day:"Khamis",period:"3",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 1",day:"Khamis",period:"6",subject:"PM",subjectName:"Pendidikan Moral"},{class:"Tahun 1",day:"Jumaat",period:"1",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 3",day:"Isnin",period:"6",subject:"MZ",subjectName:"Pendidikan Muzik"},{class:"Tahun 4",day:"Isnin",period:"8",subject:"MT",subjectName:"Matematik"},{class:"Tahun 4",day:"Selasa",period:"8",subject:"MT",subjectName:"Matematik"},{class:"Tahun 4",day:"Jumaat",period:"6",subject:"MT",subjectName:"Matematik"},{class:"Tahun 4",day:"Jumaat",period:"8",subject:"MZ",subjectName:"Pendidikan Muzik"},{class:"Tahun 5",day:"Rabu",period:"1",subject:"SJ",subjectName:"Sejarah"}];
TEACHER_SLOTS_P1["HLF"] = [{class:"Tahun 2",day:"Selasa",period:"P",subject:"PJ",subjectName:"Pendidikan Jasmani"},{class:"Tahun 2",day:"Selasa",period:"9",subject:"PK",subjectName:"Pendidikan Kesihatan"},{class:"Tahun 2",day:"Khamis",period:"P",subject:"PJ",subjectName:"Pendidikan Jasmani"},{class:"Tahun 3",day:"Rabu",period:"P",subject:"SN",subjectName:"Sains"},{class:"Tahun 3",day:"Rabu",period:"3",subject:"SN",subjectName:"Sains"},{class:"Tahun 4",day:"Isnin",period:"1",subject:"PM",subjectName:"Pendidikan Moral"},{class:"Tahun 4",day:"Isnin",period:"2",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 4",day:"Isnin",period:"6",subject:"PM",subjectName:"Pendidikan Moral"},{class:"Tahun 4",day:"Selasa",period:"4",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 4",day:"Selasa",period:"5",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 4",day:"Rabu",period:"7",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 4",day:"Khamis",period:"8",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 4",day:"Jumaat",period:"3",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 4",day:"Jumaat",period:"9",subject:"PM",subjectName:"Pendidikan Moral"},{class:"Tahun 5",day:"Selasa",period:"2",subject:"MT",subjectName:"Matematik"},{class:"Tahun 5",day:"Khamis",period:"2",subject:"MT",subjectName:"Matematik"},{class:"Tahun 5",day:"Jumaat",period:"6",subject:"MT",subjectName:"Matematik"}];
TEACHER_SLOTS_P1["LJX"] = [{class:"Tahun 1",day:"Isnin",period:"3",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 1",day:"Isnin",period:"6",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 1",day:"Khamis",period:"8",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 3",day:"Selasa",period:"1",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 3",day:"Selasa",period:"6",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 3",day:"Jumaat",period:"6",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 5",day:"Isnin",period:"4",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 5",day:"Isnin",period:"5",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 5",day:"Selasa",period:"4",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 5",day:"Selasa",period:"5",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 5",day:"Rabu",period:"3",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 5",day:"Khamis",period:"P",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 5",day:"Jumaat",period:"4",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 5",day:"Jumaat",period:"5",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 6",day:"Rabu",period:"P",subject:"PJ",subjectName:"Pendidikan Jasmani"},{class:"Tahun 6",day:"Rabu",period:"5",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 6",day:"Rabu",period:"10",subject:"PK",subjectName:"Pendidikan Kesihatan"},{class:"Tahun 6",day:"Khamis",period:"4",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 6",day:"Khamis",period:"5",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 6",day:"Jumaat",period:"P",subject:"PJ",subjectName:"Pendidikan Jasmani"},{class:"Tahun 6",day:"Jumaat",period:"1",subject:"BI",subjectName:"Bahasa Inggeris"}];
TEACHER_SLOTS_P1["LSW"] = [{class:"Tahun 1",day:"Selasa",period:"3",subject:"MT",subjectName:"Matematik"},{class:"Tahun 1",day:"Rabu",period:"6",subject:"MT",subjectName:"Matematik"},{class:"Tahun 1",day:"Khamis",period:"2",subject:"MZ",subjectName:"Pendidikan Muzik"},{class:"Tahun 1",day:"Jumaat",period:"P",subject:"SN",subjectName:"Sains"},{class:"Tahun 1",day:"Jumaat",period:"3",subject:"SN",subjectName:"Sains"},{class:"Tahun 1",day:"Jumaat",period:"6",subject:"MT",subjectName:"Matematik"},{class:"Tahun 5",day:"Rabu",period:"7",subject:"SN",subjectName:"Sains"},{class:"Tahun 5",day:"Khamis",period:"4",subject:"SN",subjectName:"Sains"},{class:"Tahun 5",day:"Khamis",period:"5",subject:"SN",subjectName:"Sains"},{class:"Tahun 6",day:"Isnin",period:"1",subject:"PM",subjectName:"Pendidikan Moral"},{class:"Tahun 6",day:"Isnin",period:"5",subject:"PM",subjectName:"Pendidikan Moral"},{class:"Tahun 6",day:"Isnin",period:"6",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 6",day:"Selasa",period:"P",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 6",day:"Selasa",period:"9",subject:"PM",subjectName:"Pendidikan Moral"},{class:"Tahun 6",day:"Rabu",period:"1",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 6",day:"Khamis",period:"8",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 6",day:"Jumaat",period:"9",subject:"BC",subjectName:"Bahasa Cina"}];
TEACHER_SLOTS_P1["WKS"] = [{class:"Tahun 2",day:"Selasa",period:"3",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 2",day:"Selasa",period:"6",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 2",day:"Rabu",period:"6",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 2",day:"Jumaat",period:"2",subject:"MZ",subjectName:"Pendidikan Muzik"},{class:"Tahun 4",day:"Isnin",period:"4",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 4",day:"Isnin",period:"5",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 4",day:"Rabu",period:"P",subject:"PJ",subjectName:"Pendidikan Jasmani"},{class:"Tahun 4",day:"Rabu",period:"3",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 4",day:"Rabu",period:"10",subject:"PK",subjectName:"Pendidikan Kesihatan"},{class:"Tahun 4",day:"Khamis",period:"P",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 4",day:"Khamis",period:"2",subject:"RBT",subjectName:"RBT"},{class:"Tahun 4",day:"Jumaat",period:"P",subject:"PJ",subjectName:"Pendidikan Jasmani"},{class:"Tahun 5",day:"Isnin",period:"1",subject:"PM",subjectName:"Pendidikan Moral"},{class:"Tahun 5",day:"Isnin",period:"8",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 5",day:"Selasa",period:"P",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 5",day:"Khamis",period:"6",subject:"BI",subjectName:"Bahasa Inggeris"},{class:"Tahun 5",day:"Jumaat",period:"3",subject:"PM",subjectName:"Pendidikan Moral"},{class:"Tahun 5",day:"Jumaat",period:"9",subject:"PM",subjectName:"Pendidikan Moral"},{class:"Tahun 6",day:"Selasa",period:"4",subject:"SJ",subjectName:"Sejarah"},{class:"Tahun 6",day:"Selasa",period:"5",subject:"SJ",subjectName:"Sejarah"}];
TEACHER_SLOTS_P1["LYY"] = [{class:"Tahun 2",day:"Isnin",period:"2",subject:"MT",subjectName:"Matematik"},{class:"Tahun 2",day:"Rabu",period:"2",subject:"MT",subjectName:"Matematik"},{class:"Tahun 2",day:"Jumaat",period:"6",subject:"MT",subjectName:"Matematik"},{class:"Tahun 3",day:"Isnin",period:"5",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 3",day:"Isnin",period:"8",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 3",day:"Selasa",period:"5",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 3",day:"Rabu",period:"8",subject:"PM",subjectName:"Pendidikan Moral"},{class:"Tahun 3",day:"Khamis",period:"3",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 3",day:"Khamis",period:"4",subject:"PM",subjectName:"Pendidikan Moral"},{class:"Tahun 3",day:"Khamis",period:"5",subject:"PM",subjectName:"Pendidikan Moral"},{class:"Tahun 3",day:"Khamis",period:"7",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 3",day:"Jumaat",period:"2",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 3",day:"Jumaat",period:"5",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 5",day:"Selasa",period:"9",subject:"RBT",subjectName:"RBT"},{class:"Tahun 5",day:"Rabu",period:"P",subject:"PJ",subjectName:"Pendidikan Jasmani"},{class:"Tahun 5",day:"Rabu",period:"10",subject:"PK",subjectName:"Pendidikan Kesihatan"},{class:"Tahun 5",day:"Jumaat",period:"P",subject:"PJ",subjectName:"Pendidikan Jasmani"},{class:"Tahun 6",day:"Selasa",period:"2",subject:"SN",subjectName:"Sains"},{class:"Tahun 6",day:"Khamis",period:"P",subject:"SN",subjectName:"Sains"}];
TEACHER_SLOTS_P1["OWY"] = [{class:"Tahun 1",day:"Selasa",period:"P",subject:"PJ",subjectName:"Pendidikan Jasmani"},{class:"Tahun 1",day:"Selasa",period:"9",subject:"PK",subjectName:"Pendidikan Kesihatan"},{class:"Tahun 1",day:"Khamis",period:"P",subject:"PJ",subjectName:"Pendidikan Jasmani"},{class:"Tahun 4",day:"Selasa",period:"2",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 4",day:"Rabu",period:"1",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 4",day:"Khamis",period:"4",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 4",day:"Khamis",period:"5",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 4",day:"Jumaat",period:"1",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 5",day:"Isnin",period:"3",subject:"MZ",subjectName:"Pendidikan Muzik"},{class:"Tahun 5",day:"Isnin",period:"6",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 5",day:"Selasa",period:"6",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 5",day:"Rabu",period:"6",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 5",day:"Khamis",period:"8",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 6",day:"Isnin",period:"8",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 6",day:"Rabu",period:"6",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 6",day:"Khamis",period:"2",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 6",day:"Jumaat",period:"6",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 6",day:"Jumaat",period:"8",subject:"MZ",subjectName:"Pendidikan Muzik"}];
TEACHER_SLOTS_P1["ARMAN"] = [{class:"Tahun 2",day:"Isnin",period:"10",subject:"PI",subjectName:"Tasmik"},{class:"Tahun 2",day:"Selasa",period:"4b",subject:"PI",subjectName:"Pendidikan Agama"},{class:"Tahun 2",day:"Selasa",period:"5b",subject:"PI",subjectName:"Pendidikan Agama"},{class:"Tahun 2",day:"Rabu",period:"P",subject:"PSV",subjectName:"Pendidikan Seni Visual"},{class:"Tahun 2",day:"Jumaat",period:"4b",subject:"PI",subjectName:"Pendidikan Agama"},{class:"Tahun 3",day:"Isnin",period:"3",subject:"PSV",subjectName:"Pendidikan Seni Visual"},{class:"Tahun 3",day:"Isnin",period:"10",subject:"PI",subjectName:"Tasmik"},{class:"Tahun 3",day:"Rabu",period:"8b",subject:"PI",subjectName:"Pendidikan Agama"},{class:"Tahun 3",day:"Khamis",period:"4b",subject:"PI",subjectName:"Pendidikan Agama"},{class:"Tahun 3",day:"Khamis",period:"5b",subject:"PI",subjectName:"Pendidikan Agama"},{class:"Tahun 4",day:"Khamis",period:"6",subject:"PSV",subjectName:"Pendidikan Seni Visual"},{class:"Tahun 5",day:"Jumaat",period:"1",subject:"PSV",subjectName:"Pendidikan Seni Visual"},{class:"Tahun 6",day:"Selasa",period:"6",subject:"PSV",subjectName:"Pendidikan Seni Visual"},{class:"Prasekolah",day:"Khamis",period:"2",subject:"PI",subjectName:"Pendidikan Agama"},{class:"Prasekolah",day:"Jumaat",period:"7",subject:"PI",subjectName:"Pendidikan Agama"}];
TEACHER_SLOTS_P1["COW"] = [{class:"Tahun 2",day:"Isnin",period:"4",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 2",day:"Isnin",period:"5",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 2",day:"Isnin",period:"8",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 2",day:"Selasa",period:"4",subject:"PM",subjectName:"Pendidikan Moral"},{class:"Tahun 2",day:"Selasa",period:"5",subject:"PM",subjectName:"Pendidikan Moral"},{class:"Tahun 2",day:"Rabu",period:"4",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 2",day:"Rabu",period:"8",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 2",day:"Khamis",period:"1",subject:"SN",subjectName:"Sains"},{class:"Tahun 2",day:"Khamis",period:"5",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 2",day:"Khamis",period:"6",subject:"SN",subjectName:"Sains"},{class:"Tahun 2",day:"Khamis",period:"9",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 2",day:"Jumaat",period:"3",subject:"PM",subjectName:"Pendidikan Moral"},{class:"Tahun 2",day:"Jumaat",period:"5",subject:"BC",subjectName:"Bahasa Cina"},{class:"Tahun 3",day:"Isnin",period:"1",subject:"MT",subjectName:"Matematik"},{class:"Tahun 3",day:"Selasa",period:"P",subject:"PJ",subjectName:"Pendidikan Jasmani"},{class:"Tahun 3",day:"Selasa",period:"9",subject:"PK",subjectName:"Pendidikan Kesihatan"},{class:"Tahun 3",day:"Rabu",period:"1",subject:"MT",subjectName:"Matematik"},{class:"Tahun 3",day:"Khamis",period:"P",subject:"PJ",subjectName:"Pendidikan Jasmani"},{class:"Tahun 3",day:"Jumaat",period:"P",subject:"MT",subjectName:"Matematik"},{class:"Tahun 4",day:"Selasa",period:"6",subject:"SN",subjectName:"Sains"},{class:"Tahun 4",day:"Rabu",period:"5",subject:"SN",subjectName:"Sains"}];
TEACHER_SLOTS_P1["BALKIS"] = [{class:"Tahun 1",day:"Isnin",period:"4",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 1",day:"Isnin",period:"5",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 1",day:"Isnin",period:"8",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 1",day:"Selasa",period:"6",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 1",day:"Rabu",period:"P",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 1",day:"Rabu",period:"2",subject:"PSV",subjectName:"Pendidikan Seni Visual"},{class:"Tahun 1",day:"Jumaat",period:"8",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 2",day:"Isnin",period:"1",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 2",day:"Isnin",period:"6",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 2",day:"Selasa",period:"1",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 2",day:"Khamis",period:"3",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 2",day:"Jumaat",period:"P",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 3",day:"Selasa",period:"3",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 3",day:"Rabu",period:"6",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 3",day:"Khamis",period:"1",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 3",day:"Khamis",period:"6",subject:"BM",subjectName:"Bahasa Melayu"},{class:"Tahun 3",day:"Jumaat",period:"3",subject:"BM",subjectName:"Bahasa Melayu"}];
TEACHER_SLOTS_P1["YH"] = [];

const TEACHER_SLOTS_P2 = TEACHER_SLOTS_P1; // Same structure for P2 (update if different)

function getTeacherSlots(code, penggal) {
  return penggal === 1 ? (TEACHER_SLOTS_P1[code] || []) : (TEACHER_SLOTS_P2[code] || []);
}
