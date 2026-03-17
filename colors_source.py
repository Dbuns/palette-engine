"""
Color palette database.

Sources:
- Palette Perfect – Lauren Wager
- Dictionary of Color Combinations, Vol. 1 (Seigensha, 2011)

This file is intentionally data-only.
"""

palettes = {
# -- 2-colors
  "PP001": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "Color_1", "rgb": (254,240,235), "cmyk": ( 0, 8, 7, 0)},
      "B": {"name": "Color_2", "rgb": ( 86, 81, 94), "cmyk": (68,63,47,29)}
    },
    "roles": {"dominant": "B", "accent": ["A"]}    
  },
  
  "PP002": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "Color_3", "rgb": (186,201,199), "cmyk": (32,14,22, 1)},
      "B": {"name": "Color_4", "rgb": (235,236,161), "cmyk": (12, 0,47, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}    
  },
  
  "PP006": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (211,156,111), "cmyk": (16,42,58,4)},
      "B": {"name": "color_2", "rgb": (246,215,192), "cmyk": (3,20,26,0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": []}
  },  
  
  "PP007": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (159,159,161), "cmyk": (40,31,30,9)},
      "B": {"name": "color_2", "rgb": (232,238,247), "cmyk": (11,4,2,0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": []}
  },
  
  "PP008": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (141,92,100), "cmyk": (36,62,41,28)},
      "B": {"name": "color_2", "rgb": (218,207,230), "cmyk": (16,21,1,0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": []}
  },
  
  "PP018": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (201,217,236), "cmyk": (25,10,3,0)},
      "B": {"name": "color_2", "rgb": (119,102,116), "cmyk": (57,58,41,15)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": []}
  },

  "PP019": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (232,230,202), "cmyk": (12,6,26,0)},
      "B": {"name": "color_2", "rgb": (186,185,178), "cmyk": (30,22,28,4)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": []}
  },

  "PP025": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (241,245,249), "cmyk": (7,2,2,0)},
      "B": {"name": "color_2", "rgb": (184,203,214), "cmyk": (32,14,13,0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": []}
  },
    
  "PP026": {
     "source": "palette_perfect",
     "colors": {
       "A": {"name": "color_1", "rgb": (165,163,166), "cmyk": (41,33,32,0)},
       "B": {"name": "color_2", "rgb": (252,220,207), "cmyk": (0,18,18,0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": []}
  },
  
  "DCC001": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "english_red", "rgb": (222, 69, 0), "cmyk": (13, 73, 100, 0)},
      "B": {"name": "cerulian_blue", "rgb": (41, 189, 173), "cmyk": (84, 26, 32, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC002": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dark_tyrian_blue", "rgb": (13, 43, 82), "cmyk": (90, 66, 36, 50)},
      "B": {"name": "yellow_orange", "rgb": (255, 140, 0), "cmyk": (0, 45, 100, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC003": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)},
      "B": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC004": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "red_violet", "rgb": (52, 0, 163), "cmyk": (76, 100, 25, 15)},
      "B": {"name": "isabella_color", "rgb": (195, 165, 92), "cmyk": (15, 28, 60, 10)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC005": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cossack_green", "rgb": (50, 142, 19), "cmyk": (76, 32, 91, 18)},
      "B": {"name": "vandar_poels_blue", "rgb": (0, 62, 131), "cmyk": (100, 73, 43, 10)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC006": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "deep_indigo", "rgb": (0, 8, 49), "cmyk": (100, 92, 52, 60)},
      "B": {"name": "grenadine_pink", "rgb": (255, 97, 107), "cmyk": (0, 62, 58, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC007": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "glaucous_green", "rgb": (178, 232, 194), "cmyk": (30, 9, 24, 0)},
      "B": {"name": "orange", "rgb": (255, 82, 0), "cmyk": (0, 68, 100, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC008": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cinnamon_rufous", "rgb": (194, 97, 44), "cmyk": (20, 60, 82, 5)},
      "B": {"name": "grayish_lavender", "rgb": (184, 184, 255), "cmyk": (28, 28, 0, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC009": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dull_blue_violet", "rgb": (110, 102, 212), "cmyk": (57, 60, 17, 0)},
      "B": {"name": "violet_red", "rgb": (61, 0, 121), "cmyk": (75, 100, 50, 5)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC010": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dark_citrine", "rgb": (126, 135, 67), "cmyk": (38, 34, 67, 20)},
      "B": {"name": "cinnamon_rufous", "rgb": (194, 97, 44), "cmyk": (20, 60, 82, 5)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC011": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "mineral_gray", "rgb": (159, 194, 178), "cmyk": (33, 18, 25, 7)},
      "B": {"name": "ivory_buff", "rgb": (235, 217, 153), "cmyk": (8, 15, 40, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC012": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "green_blue", "rgb": (45, 188, 148), "cmyk": (82, 24, 40, 3)},
      "B": {"name": "isabella_color", "rgb": (195, 165, 92), "cmyk": (15, 28, 60, 10)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC013": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)},
      "B": {"name": "vernonia_purple", "rgb": (126, 48, 117), "cmyk": (42, 78, 46, 15)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC014": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "naples_yellow", "rgb": (250, 237, 143), "cmyk": (2, 7, 44, 0)},
      "B": {"name": "spinel_red", "rgb": (255, 77, 201), "cmyk": (0, 70, 21, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC015": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "grayish_lavender", "rgb": (184, 184, 255), "cmyk": (28, 28, 0, 0)},
      "B": {"name": "benzol_green", "rgb": (0, 217, 115), "cmyk": (100, 15, 55, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC016": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_kings_blue", "rgb": (171, 245, 237), "cmyk": (33, 4, 7, 0)},
      "B": {"name": "vandyke_red", "rgb": (116, 9, 9), "cmyk": (32, 95, 95, 33)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC017": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "eugenia_red", "rgb": (237, 61, 102), "cmyk": (7, 76, 60, 0)},
      "B": {"name": "sea_green", "rgb": (51, 255, 125), "cmyk": (80, 0, 51, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC018": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dusky_madder_violet", "rgb": (45, 0, 96), "cmyk": (75, 100, 46, 30)},
      "B": {"name": "fawn", "rgb": (209, 176, 178), "cmyk": (18, 31, 30, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC019": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "night_green", "rgb": (122, 255, 0), "cmyk": (52, 0, 100, 0)},
      "B": {"name": "tobacco", "rgb": (82, 32, 0), "cmyk": (39, 76, 100, 47)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC020": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "laelia_pink", "rgb": (204, 133, 209), "cmyk": (20, 48, 18, 0)},
      "B": {"name": "calamine_blue", "rgb": (128, 255, 204), "cmyk": (50, 0, 20, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC021": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "grenadine_pink", "rgb": (255, 97, 107), "cmyk": (0, 62, 58, 0)},
      "B": {"name": "sea_green", "rgb": (51, 255, 125), "cmyk": (80, 0, 51, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC022": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "deep_lyons_blue", "rgb": (0, 36, 204), "cmyk": (100, 85, 15, 6)},
      "B": {"name": "yellow", "rgb": (255, 255, 0), "cmyk": (0, 0, 100, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC023": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "light_mauve", "rgb": (145, 97, 242), "cmyk": (43, 62, 5, 0)},
      "B": {"name": "cinnamon_buff", "rgb": (255, 191, 110), "cmyk": (0, 25, 57, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC024": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "vernonia_purple", "rgb": (126, 48, 117), "cmyk": (42, 78, 46, 15)},
      "B": {"name": "sepia", "rgb": (80, 61, 0), "cmyk": (48, 60, 100, 40)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC025": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "etruscan_red", "rgb": (201, 48, 62), "cmyk": (16, 80, 74, 6)},
      "B": {"name": "nile_blue", "rgb": (191, 255, 230), "cmyk": (25, 0, 10, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC026": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "green_blue", "rgb": (45, 188, 148), "cmyk": (82, 24, 40, 3)},
      "B": {"name": "isabella_color", "rgb": (195, 165, 92), "cmyk": (15, 28, 60, 10)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC027": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "corinthian_pink", "rgb": (255, 166, 217), "cmyk": (0, 35, 15, 0)},
      "B": {"name": "slate_color", "rgb": (27, 54, 68), "cmyk": (85, 70, 62, 30)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC028": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "deep_indigo", "rgb": (0, 8, 49), "cmyk": (100, 92, 52, 60)},
      "B": {"name": "madder_brown", "rgb": (101, 19, 0), "cmyk": (36, 88, 100, 38)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC029": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "salvia_blue", "rgb": (150, 191, 230), "cmyk": (41, 25, 10, 0)},
      "B": {"name": "kronbergs_green", "rgb": (117, 146, 67), "cmyk": (48, 35, 70, 12)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC030": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "mineral_gray", "rgb": (159, 194, 178), "cmyk": (33, 18, 25, 7)},
      "B": {"name": "pompeian_red", "rgb": (169, 6, 54), "cmyk": (18, 97, 74, 19)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC031": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)},
      "B": {"name": "red_orange", "rgb": (232, 25, 0), "cmyk": (9, 90, 100, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC032": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "night_green", "rgb": (122, 255, 0), "cmyk": (52, 0, 100, 0)},
      "B": {"name": "ochraceous_salmon", "rgb": (217, 158, 115), "cmyk": (15, 38, 55, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC033": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)},
      "B": {"name": "slate_color", "rgb": (27, 54, 68), "cmyk": (85, 70, 62, 30)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC034": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "eosine_pink", "rgb": (255, 94, 196), "cmyk": (0, 63, 23, 0)},
      "B": {"name": "neutral_gray", "rgb": (181, 209, 204), "cmyk": (29, 18, 20, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC035": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "carmine_red", "rgb": (161, 11, 43), "cmyk": (25, 95, 80, 16)},
      "B": {"name": "light_brown_drab", "rgb": (176, 134, 153), "cmyk": (8, 30, 20, 25)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC036": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "sulphine_yellow", "rgb": (186, 166, 0), "cmyk": (24, 32, 100, 4)},
      "B": {"name": "turquoise_green", "rgb": (181, 255, 194), "cmyk": (29, 0, 24, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC037": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "red_violet", "rgb": (52, 0, 163), "cmyk": (76, 100, 25, 15)},
      "B": {"name": "brick_red", "rgb": (163, 33, 0), "cmyk": (22, 84, 100, 18)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC038": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "diamine_green", "rgb": (30, 184, 0), "cmyk": (87, 20, 100, 10)},
      "B": {"name": "deep_lyons_blue", "rgb": (0, 36, 204), "cmyk": (100, 85, 15, 6)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC039": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "carmine", "rgb": (214, 0, 54), "cmyk": (0, 100, 75, 16)},
      "B": {"name": "helvetia_blue", "rgb": (0, 87, 186), "cmyk": (100, 62, 19, 10)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC040": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "vinaceous_tawny", "rgb": (199, 67, 0), "cmyk": (17, 72, 100, 6)},
      "B": {"name": "citron_yellow", "rgb": (166, 212, 13), "cmyk": (35, 17, 95, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC041": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dark_citrine", "rgb": (126, 135, 67), "cmyk": (38, 34, 67, 20)},
      "B": {"name": "calamine_blue", "rgb": (128, 255, 204), "cmyk": (50, 0, 20, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC042": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "violet", "rgb": (38, 25, 209), "cmyk": (85, 90, 18, 0)},
      "B": {"name": "yellow_ocher", "rgb": (224, 184, 31), "cmyk": (12, 28, 88, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC043": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "aconite_violet", "rgb": (156, 82, 242), "cmyk": (39, 68, 5, 0)},
      "B": {"name": "corinthian_pink", "rgb": (255, 166, 217), "cmyk": (0, 35, 15, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC044": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "olympic_blue", "rgb": (79, 143, 230), "cmyk": (69, 44, 10, 0)},
      "B": {"name": "light_porcelain_green", "rgb": (35, 193, 124), "cmyk": (86, 22, 50, 3)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC045": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "seashell_pink", "rgb": (255, 207, 196), "cmyk": (0, 19, 23, 0)},
      "B": {"name": "lemon_yellow", "rgb": (242, 255, 38), "cmyk": (5, 0, 85, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC046": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "orange", "rgb": (255, 82, 0), "cmyk": (0, 68, 100, 0)},
      "B": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC047": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "grayish_lavender", "rgb": (184, 184, 255), "cmyk": (28, 28, 0, 0)},
      "B": {"name": "etruscan_red", "rgb": (201, 48, 62), "cmyk": (16, 80, 74, 6)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC048": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "rosolanc_purple", "rgb": (178, 25, 171), "cmyk": (30, 90, 33, 0)},
      "B": {"name": "helvetia_blue", "rgb": (0, 87, 186), "cmyk": (100, 62, 19, 10)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC049": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_kings_blue", "rgb": (171, 245, 237), "cmyk": (33, 4, 7, 0)},
      "B": {"name": "blue", "rgb": (13, 117, 255), "cmyk": (95, 54, 0, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC050": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dusky_madder_violet", "rgb": (45, 0, 96), "cmyk": (75, 100, 46, 30)},
      "B": {"name": "ivory_buff", "rgb": (235, 217, 153), "cmyk": (8, 15, 40, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC051": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "blue", "rgb": (13, 117, 255), "cmyk": (95, 54, 0, 0)},
      "B": {"name": "carmine_red", "rgb": (161, 11, 43), "cmyk": (25, 95, 80, 16)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC052": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)},
      "B": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC053": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "yellow_orange", "rgb": (255, 140, 0), "cmyk": (0, 45, 100, 0)},
      "B": {"name": "dusky_madder_violet", "rgb": (45, 0, 96), "cmyk": (75, 100, 46, 30)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC054": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "benzol_green", "rgb": (0, 217, 115), "cmyk": (100, 15, 55, 0)},
      "B": {"name": "light_glaucous_blue", "rgb": (166, 230, 219), "cmyk": (35, 10, 14, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC055": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "old_rose", "rgb": (217, 77, 153), "cmyk": (15, 70, 40, 0)},
      "B": {"name": "white", "rgb": (255, 255, 255), "cmyk": (0, 0, 0, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC056": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "grayish_lavender", "rgb": (184, 184, 255), "cmyk": (28, 28, 0, 0)},
      "B": {"name": "violet", "rgb": (38, 25, 209), "cmyk": (85, 90, 18, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC057": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "taupe_brown", "rgb": (107, 46, 99), "cmyk": (30, 70, 35, 40)},
      "B": {"name": "slate_color", "rgb": (27, 54, 68), "cmyk": (85, 70, 62, 30)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC058": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "sea_green", "rgb": (51, 255, 125), "cmyk": (80, 0, 51, 0)},
      "B": {"name": "hays_russet", "rgb": (104, 25, 22), "cmyk": (37, 85, 87, 35)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC059": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "citrine", "rgb": (152, 161, 0), "cmyk": (36, 32, 100, 7)},
      "B": {"name": "eosine_pink", "rgb": (255, 94, 196), "cmyk": (0, 63, 23, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC060": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dark_tyrian_blue", "rgb": (13, 43, 82), "cmyk": (90, 66, 36, 50)},
      "B": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC061": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cotinga_purple", "rgb": (52, 0, 89), "cmyk": (66, 100, 42, 40)},
      "B": {"name": "light_green_yellow", "rgb": (189, 242, 38), "cmyk": (26, 5, 85, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC062": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)},
      "B": {"name": "yellow", "rgb": (255, 255, 0), "cmyk": (0, 0, 100, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC063": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "vistoris_lake", "rgb": (92, 44, 69), "cmyk": (40, 71, 55, 40)},
      "B": {"name": "cerulian_blue", "rgb": (41, 189, 173), "cmyk": (84, 26, 32, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC064": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "aconite_violet", "rgb": (156, 82, 242), "cmyk": (39, 68, 5, 0)},
      "B": {"name": "dark_soft_violet", "rgb": (77, 82, 222), "cmyk": (70, 68, 13, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC065": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)},
      "B": {"name": "calamine_blue", "rgb": (128, 255, 204), "cmyk": (50, 0, 20, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC066": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "olive_green", "rgb": (88, 119, 30), "cmyk": (56, 40, 85, 22)},
      "B": {"name": "olive_ocher", "rgb": (209, 189, 51), "cmyk": (18, 26, 80, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC067": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dark_tyrian_blue", "rgb": (13, 43, 82), "cmyk": (90, 66, 36, 50)},
      "B": {"name": "olympic_blue", "rgb": (79, 143, 230), "cmyk": (69, 44, 10, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC068": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "yellow", "rgb": (255, 255, 0), "cmyk": (0, 0, 100, 0)},
      "B": {"name": "light_brown_drab", "rgb": (176, 134, 153), "cmyk": (8, 30, 20, 25)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC069": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)},
      "B": {"name": "warm_gray", "rgb": (156, 178, 158), "cmyk": (37, 28, 36, 3)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC070": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "lincoln_green", "rgb": (64, 84, 22), "cmyk": (60, 48, 86, 37)},
      "B": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC071": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "ochraceous_salmon", "rgb": (217, 158, 115), "cmyk": (15, 38, 55, 0)},
      "B": {"name": "pompeian_red", "rgb": (169, 6, 54), "cmyk": (18, 97, 74, 19)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC072": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_kings_blue", "rgb": (171, 245, 237), "cmyk": (33, 4, 7, 0)},
      "B": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC073": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "rainette_green", "rgb": (106, 147, 70), "cmyk": (42, 20, 62, 28)},
      "B": {"name": "pale_raw_umber", "rgb": (94, 64, 23), "cmyk": (46, 63, 87, 32)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC074": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "green_blue", "rgb": (45, 188, 148), "cmyk": (82, 24, 40, 3)},
      "B": {"name": "turquoise_green", "rgb": (181, 255, 194), "cmyk": (29, 0, 24, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC075": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_kings_blue", "rgb": (171, 245, 237), "cmyk": (33, 4, 7, 0)},
      "B": {"name": "violet_blue", "rgb": (32, 45, 133), "cmyk": (85, 79, 38, 16)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC076": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)},
      "B": {"name": "warm_gray", "rgb": (156, 178, 158), "cmyk": (37, 28, 36, 3)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC077": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "eugenia_red_2", "rgb": (230, 46, 115), "cmyk": (0, 80, 50, 10)},
      "B": {"name": "vandar_poels_blue", "rgb": (0, 62, 131), "cmyk": (100, 73, 43, 10)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC078": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "venice_green", "rgb": (107, 255, 178), "cmyk": (58, 0, 30, 0)},
      "B": {"name": "pinkish_cinnamon", "rgb": (242, 173, 120), "cmyk": (5, 32, 53, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC079": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "green_blue", "rgb": (45, 188, 148), "cmyk": (82, 24, 40, 3)},
      "B": {"name": "madder_brown", "rgb": (101, 19, 0), "cmyk": (36, 88, 100, 38)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC080": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)},
      "B": {"name": "light_mauve", "rgb": (145, 97, 242), "cmyk": (43, 62, 5, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC081": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "golden_yellow", "rgb": (250, 148, 66), "cmyk": (2, 42, 74, 0)},
      "B": {"name": "warm_gray", "rgb": (156, 178, 158), "cmyk": (37, 28, 36, 3)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC082": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "hays_russet", "rgb": (104, 25, 22), "cmyk": (37, 85, 87, 35)},
      "B": {"name": "dusky_madder_violet", "rgb": (45, 0, 96), "cmyk": (75, 100, 46, 30)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC083": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "violet_blue", "rgb": (32, 45, 133), "cmyk": (85, 79, 38, 16)},
      "B": {"name": "olive_buff", "rgb": (188, 211, 130), "cmyk": (16, 6, 42, 12)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC084": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "seashell_pink", "rgb": (255, 207, 196), "cmyk": (0, 19, 23, 0)},
      "B": {"name": "deep_slate_green", "rgb": (15, 38, 31), "cmyk": (80, 50, 60, 70)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC085": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "antwarp_blue", "rgb": (0, 138, 161), "cmyk": (100, 40, 30, 10)},
      "B": {"name": "vinaceous_tawny", "rgb": (199, 67, 0), "cmyk": (17, 72, 100, 6)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC086": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)},
      "B": {"name": "sea_green", "rgb": (51, 255, 125), "cmyk": (80, 0, 51, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC087": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "citron_yellow", "rgb": (166, 212, 13), "cmyk": (35, 17, 95, 0)},
      "B": {"name": "corinthian_pink", "rgb": (255, 166, 217), "cmyk": (0, 35, 15, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC088": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "blue", "rgb": (13, 117, 255), "cmyk": (95, 54, 0, 0)},
      "B": {"name": "seashell_pink", "rgb": (255, 207, 196), "cmyk": (0, 19, 23, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC089": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "yellow_orange", "rgb": (255, 140, 0), "cmyk": (0, 45, 100, 0)},
      "B": {"name": "violet_blue", "rgb": (32, 45, 133), "cmyk": (85, 79, 38, 16)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC090": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "aconite_violet", "rgb": (156, 82, 242), "cmyk": (39, 68, 5, 0)},
      "B": {"name": "eosine_pink", "rgb": (255, 94, 196), "cmyk": (0, 63, 23, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC091": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "vistoris_lake", "rgb": (92, 44, 69), "cmyk": (40, 71, 55, 40)},
      "B": {"name": "orange_rufous", "rgb": (192, 82, 0), "cmyk": (18, 65, 100, 8)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC092": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "coral_red", "rgb": (255, 115, 153), "cmyk": (0, 55, 40, 0)},
      "B": {"name": "benzol_green", "rgb": (0, 217, 115), "cmyk": (100, 15, 55, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC093": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "light_glaucous_blue", "rgb": (166, 230, 219), "cmyk": (35, 10, 14, 0)},
      "B": {"name": "citrine", "rgb": (152, 161, 0), "cmyk": (36, 32, 100, 7)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC094": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dusky_green", "rgb": (0, 89, 46), "cmyk": (100, 30, 64, 50)},
      "B": {"name": "ivory_buff", "rgb": (235, 217, 153), "cmyk": (8, 15, 40, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC095": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "hays_russet", "rgb": (104, 25, 22), "cmyk": (37, 85, 87, 35)},
      "B": {"name": "dull_violet_black", "rgb": (0, 13, 79), "cmyk": (100, 90, 38, 50)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC096": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "olive", "rgb": (113, 134, 0), "cmyk": (48, 38, 100, 15)},
      "B": {"name": "yellow_ocher", "rgb": (224, 184, 31), "cmyk": (12, 28, 88, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC097": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "corinthian_pink", "rgb": (255, 166, 217), "cmyk": (0, 35, 15, 0)},
      "B": {"name": "etruscan_red", "rgb": (201, 48, 62), "cmyk": (16, 80, 74, 6)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC098": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "madder_brown", "rgb": (101, 19, 0), "cmyk": (36, 88, 100, 38)},
      "B": {"name": "violet_blue", "rgb": (32, 45, 133), "cmyk": (85, 79, 38, 16)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC099": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)},
      "B": {"name": "cerulian_blue", "rgb": (41, 189, 173), "cmyk": (84, 26, 32, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC100": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "buffy_citrine", "rgb": (136, 141, 42), "cmyk": (42, 40, 82, 8)},
      "B": {"name": "dull_blue_violet", "rgb": (110, 102, 212), "cmyk": (57, 60, 17, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC101": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "deep_lyons_blue", "rgb": (0, 36, 204), "cmyk": (100, 85, 15, 6)},
      "B": {"name": "cameo_pink", "rgb": (230, 173, 207), "cmyk": (10, 32, 19, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC102": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "ivory_buff", "rgb": (235, 217, 153), "cmyk": (8, 15, 40, 0)},
      "B": {"name": "orange_rufous", "rgb": (192, 82, 0), "cmyk": (18, 65, 100, 8)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC103": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dusky_madder_violet", "rgb": (45, 0, 96), "cmyk": (75, 100, 46, 30)},
      "B": {"name": "cinnamon_rufous", "rgb": (194, 97, 44), "cmyk": (20, 60, 82, 5)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC104": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)},
      "B": {"name": "carmine_red", "rgb": (161, 11, 43), "cmyk": (25, 95, 80, 16)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC105": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cameo_pink", "rgb": (230, 173, 207), "cmyk": (10, 32, 19, 0)},
      "B": {"name": "chromium_green", "rgb": (102, 171, 86), "cmyk": (50, 16, 58, 20)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC106": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dull_violet_black", "rgb": (0, 13, 79), "cmyk": (100, 90, 38, 50)},
      "B": {"name": "antwarp_blue", "rgb": (0, 138, 161), "cmyk": (100, 40, 30, 10)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC107": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "light_grayish_olive", "rgb": (118, 132, 78), "cmyk": (43, 36, 62, 19)},
      "B": {"name": "apricot_yellow", "rgb": (255, 230, 0), "cmyk": (0, 10, 100, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC108": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "eosine_pink", "rgb": (255, 94, 196), "cmyk": (0, 63, 23, 0)},
      "B": {"name": "brick_red", "rgb": (163, 33, 0), "cmyk": (22, 84, 100, 18)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC109": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)},
      "B": {"name": "blackish_olive", "rgb": (50, 78, 42), "cmyk": (56, 32, 63, 55)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC110": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "brown", "rgb": (108, 43, 17), "cmyk": (35, 74, 90, 35)},
      "B": {"name": "vandyke_brown", "rgb": (54, 35, 4), "cmyk": (56, 71, 97, 52)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC111": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)},
      "B": {"name": "yellow_green", "rgb": (166, 255, 71), "cmyk": (35, 0, 72, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC112": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)},
      "B": {"name": "grenadine_pink", "rgb": (255, 97, 107), "cmyk": (0, 62, 58, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC113": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "seashell_pink", "rgb": (255, 207, 196), "cmyk": (0, 19, 23, 0)},
      "B": {"name": "vandyke_brown", "rgb": (54, 35, 4), "cmyk": (56, 71, 97, 52)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC114": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "antwarp_blue", "rgb": (0, 138, 161), "cmyk": (100, 40, 30, 10)},
      "B": {"name": "orange_yellow", "rgb": (255, 171, 0), "cmyk": (0, 33, 100, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC115": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "naples_yellow", "rgb": (250, 237, 143), "cmyk": (2, 7, 44, 0)},
      "B": {"name": "peach_red", "rgb": (255, 51, 25), "cmyk": (0, 80, 90, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC116": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "blue_violet", "rgb": (71, 51, 255), "cmyk": (72, 80, 0, 0)},
      "B": {"name": "cameo_pink", "rgb": (230, 173, 207), "cmyk": (10, 32, 19, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC117": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "carmine", "rgb": (214, 0, 54), "cmyk": (0, 100, 75, 16)},
      "B": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC118": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "vandyke_brown", "rgb": (54, 35, 4), "cmyk": (56, 71, 97, 52)},
      "B": {"name": "yellow_ocher", "rgb": (224, 184, 31), "cmyk": (12, 28, 88, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC119": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dark_tyrian_blue", "rgb": (13, 43, 82), "cmyk": (90, 66, 36, 50)},
      "B": {"name": "light_glaucous_blue", "rgb": (166, 230, 219), "cmyk": (35, 10, 14, 0)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },

  "DCC120": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cameo_pink", "rgb": (230, 173, 207), "cmyk": (10, 32, 19, 0)},
      "B": {"name": "pompeian_red", "rgb": (169, 6, 54), "cmyk": (18, 97, 74, 19)}
    },
    "roles": {"dominant": "A", "accent": ["B"]}
  },
# --- 3-colors
   "PP003": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "Color_5", "rgb": (113,101,115), "cmyk": (56,54,37,24)},
      "B": {"name": "Color_6", "rgb": (240,217,193), "cmyk": ( 6,17,26, 0)},
      "C": {"name": "Color_7", "rgb": (185,195,228), "cmyk": (32,20, 1, 0)}
    },
    "roles": {"dominant": "C", "secondary": ["A"], "accent": ["B"]}    
  },
   
  "PP004": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "Color_8", "rgb": (239,186,120), "cmyk": ( 6,31,58, 0)},
      "B": {"name": "Color_9", "rgb": (121,151,151), "cmyk": (56,28,36, 9)},
      "C": {"name": "Color_10", "rgb": (253,234,227), "cmyk": ( 0,11,10, 0)}
    },
    "roles": {"dominant": "B", "secondary": ["C"], "accent": ["A"]}    
  },

  "PP009": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (217,198,164), "cmyk": (17,20,38,2)},
      "B": {"name": "color_2", "rgb": (224,224,194), "cmyk": (16,8,29,0)},
      "C": {"name": "color_3", "rgb": (120,166,167), "cmyk": (57,20,34,3)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "PP010": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (185,195,228), "cmyk": (32,20,1,0)},
      "B": {"name": "color_2", "rgb": (113,101,115), "cmyk": (56,54,37,24)},
      "C": {"name": "color_3", "rgb": (240,217,193), "cmyk": (6,17,26,0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "PP011": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (131,151,151), "cmyk": (56,28,36,9)},
      "B": {"name": "color_2", "rgb": (253,234,227), "cmyk": (0,11,10,0)},
      "C": {"name": "color_3", "rgb": (239,186,120), "cmyk": (6,31,58,0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "PP012": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (231,243,234), "cmyk": (12,0,11,0)},
      "B": {"name": "color_2", "rgb": (109,119,129), "cmyk": (58,42,36,20)},
      "C": {"name": "color_3", "rgb": (245,239,189), "cmyk": (6,3,34,0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "PP020": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (247,246,247), "cmyk": (4,3,3,0)},
      "B": {"name": "color_2", "rgb": (211,224,242), "cmyk": (20,9,1,0)},
      "C": {"name": "color_3", "rgb": (119,102,116), "cmyk": (57,58,41,15)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "PP021": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (252,219,206), "cmyk": (0,19,18,0)},
      "B": {"name": "color_2", "rgb": (187,217,215), "cmyk": (31,4,18,0)},
      "C": {"name": "color_3", "rgb": (112,117,136), "cmyk": (62,50,35,8)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "PP027": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (243,172,148), "cmyk": (2,41,40,0)},
      "B": {"name": "color_2", "rgb": (246,233,206), "cmyk": (4,9,23,0)},
      "C": {"name": "color_3", "rgb": (114,122,132), "cmyk": (61,47,40,9)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },
  
  "DCC121": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "lincoln_green", "rgb": (64, 84, 22), "cmyk": (60, 48, 86, 37)},
      "B": {"name": "ochraceous_salmon", "rgb": (217, 158, 115), "cmyk": (15, 38, 55, 0)},
      "C": {"name": "brown", "rgb": (108, 43, 17), "cmyk": (35, 74, 90, 35)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC122": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "benzol_green", "rgb": (0, 217, 115), "cmyk": (100, 15, 55, 0)},
      "B": {"name": "cream_yellow", "rgb": (255, 82, 184), "cmyk": (0, 68, 28, 0)},
      "C": {"name": "carmine", "rgb": (214, 0, 54), "cmyk": (0, 100, 75, 16)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC123": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "coral_red", "rgb": (255, 115, 153), "cmyk": (0, 55, 40, 0)},
      "B": {"name": "taupe_brown", "rgb": (107, 46, 99), "cmyk": (30, 70, 35, 40)},
      "C": {"name": "lemon_yellow", "rgb": (242, 255, 38), "cmyk": (5, 0, 85, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC124": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "olive_yellow", "rgb": (153, 178, 51), "cmyk": (40, 30, 80, 0)},
      "B": {"name": "yellow_ocher", "rgb": (224, 184, 31), "cmyk": (12, 28, 88, 0)},
      "C": {"name": "pale_burnt_lake", "rgb": (115, 15, 31), "cmyk": (25, 90, 80, 40)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC125": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cerulian_blue", "rgb": (41, 189, 173), "cmyk": (84, 26, 32, 0)},
      "B": {"name": "fawn", "rgb": (209, 176, 178), "cmyk": (18, 31, 30, 0)},
      "C": {"name": "violet_blue", "rgb": (32, 45, 133), "cmyk": (85, 79, 38, 16)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC126": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "yellow_ocher", "rgb": (224, 184, 31), "cmyk": (12, 28, 88, 0)},
      "B": {"name": "deep_lyons_blue", "rgb": (0, 36, 204), "cmyk": (100, 85, 15, 6)},
      "C": {"name": "ivory_buff", "rgb": (235, 217, 153), "cmyk": (8, 15, 40, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC127": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cinnamon_buff", "rgb": (255, 191, 110), "cmyk": (0, 25, 57, 0)},
      "B": {"name": "pistachio_green", "rgb": (86, 170, 105), "cmyk": (64, 29, 56, 6)},
      "C": {"name": "dark_soft_violet", "rgb": (77, 82, 222), "cmyk": (70, 68, 13, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC128": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "corinthian_pink", "rgb": (255, 166, 217), "cmyk": (0, 35, 15, 0)},
      "B": {"name": "light_mauve", "rgb": (145, 97, 242), "cmyk": (43, 62, 5, 0)},
      "C": {"name": "venice_green", "rgb": (107, 255, 178), "cmyk": (58, 0, 30, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC129": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "khaki", "rgb": (182, 132, 0), "cmyk": (24, 45, 100, 6)},
      "B": {"name": "salvia_blue", "rgb": (150, 191, 230), "cmyk": (41, 25, 10, 0)},
      "C": {"name": "apricot_yellow", "rgb": (255, 230, 0), "cmyk": (0, 10, 100, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC130": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "carmine_red", "rgb": (161, 11, 43), "cmyk": (25, 95, 80, 16)},
      "B": {"name": "violet", "rgb": (38, 25, 209), "cmyk": (85, 90, 18, 0)},
      "C": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC131": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "english_red", "rgb": (222, 69, 0), "cmyk": (13, 73, 100, 0)},
      "B": {"name": "peacock_blue", "rgb": (0, 207, 145), "cmyk": (100, 19, 43, 0)},
      "C": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC132": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "citrine", "rgb": (152, 161, 0), "cmyk": (36, 32, 100, 7)},
      "B": {"name": "golden_yellow", "rgb": (250, 148, 66), "cmyk": (2, 42, 74, 0)},
      "C": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC133": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "sea_green", "rgb": (51, 255, 125), "cmyk": (80, 0, 51, 0)},
      "B": {"name": "vandyke_red", "rgb": (116, 9, 9), "cmyk": (32, 95, 95, 33)},
      "C": {"name": "citrine", "rgb": (152, 161, 0), "cmyk": (36, 32, 100, 7)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC134": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "eosine_pink", "rgb": (255, 94, 196), "cmyk": (0, 63, 23, 0)},
      "B": {"name": "light_mauve", "rgb": (145, 97, 242), "cmyk": (43, 62, 5, 0)},
      "C": {"name": "red_violet", "rgb": (52, 0, 163), "cmyk": (76, 100, 25, 15)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC135": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "salvia_blue", "rgb": (150, 191, 230), "cmyk": (41, 25, 10, 0)},
      "B": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)},
      "C": {"name": "cossack_green", "rgb": (50, 142, 19), "cmyk": (76, 32, 91, 18)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC136": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "red_violet", "rgb": (52, 0, 163), "cmyk": (76, 100, 25, 15)},
      "B": {"name": "scarlet", "rgb": (213, 12, 66), "cmyk": (10, 95, 72, 7)},
      "C": {"name": "dull_viridian_green", "rgb": (25, 204, 51), "cmyk": (90, 20, 80, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC137": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "etruscan_red", "rgb": (201, 48, 62), "cmyk": (16, 80, 74, 6)},
      "B": {"name": "pistachio_green", "rgb": (86, 170, 105), "cmyk": (64, 29, 56, 6)},
      "C": {"name": "cinnamon_buff", "rgb": (255, 191, 110), "cmyk": (0, 25, 57, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC138": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "golden_yellow", "rgb": (250, 148, 66), "cmyk": (2, 42, 74, 0)},
      "B": {"name": "venice_green", "rgb": (107, 255, 178), "cmyk": (58, 0, 30, 0)},
      "C": {"name": "lemon_yellow", "rgb": (242, 255, 38), "cmyk": (5, 0, 85, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC139": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "neutral_gray", "rgb": (181, 209, 204), "cmyk": (29, 18, 20, 0)},
      "B": {"name": "deep_indigo", "rgb": (0, 8, 49), "cmyk": (100, 92, 52, 60)},
      "C": {"name": "salvia_blue", "rgb": (150, 191, 230), "cmyk": (41, 25, 10, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC140": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "golden_yellow", "rgb": (250, 148, 66), "cmyk": (2, 42, 74, 0)},
      "B": {"name": "slate_color", "rgb": (27, 54, 68), "cmyk": (85, 70, 62, 30)},
      "C": {"name": "antwarp_blue", "rgb": (0, 138, 161), "cmyk": (100, 40, 30, 10)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC141": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "orange", "rgb": (255, 82, 0), "cmyk": (0, 68, 100, 0)},
      "B": {"name": "dark_tyrian_blue", "rgb": (13, 43, 82), "cmyk": (90, 66, 36, 50)},
      "C": {"name": "yellow_green", "rgb": (166, 255, 71), "cmyk": (35, 0, 72, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC142": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "hydrangea_red", "rgb": (158, 25, 77), "cmyk": (38, 90, 70, 0)},
      "B": {"name": "salvia_blue", "rgb": (150, 191, 230), "cmyk": (41, 25, 10, 0)},
      "C": {"name": "sulphine_yellow", "rgb": (186, 166, 0), "cmyk": (24, 32, 100, 4)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC143": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "warm_gray", "rgb": (156, 178, 158), "cmyk": (37, 28, 36, 3)},
      "B": {"name": "blue", "rgb": (13, 117, 255), "cmyk": (95, 54, 0, 0)},
      "C": {"name": "lilac", "rgb": (184, 117, 235), "cmyk": (28, 54, 8, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC144": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "orange", "rgb": (255, 82, 0), "cmyk": (0, 68, 100, 0)},
      "B": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)},
      "C": {"name": "rosolanc_purple", "rgb": (178, 25, 171), "cmyk": (30, 90, 33, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC145": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dull_violet_black", "rgb": (0, 13, 79), "cmyk": (100, 90, 38, 50)},
      "B": {"name": "brown", "rgb": (108, 43, 17), "cmyk": (35, 74, 90, 35)},
      "C": {"name": "citron_yellow", "rgb": (166, 212, 13), "cmyk": (35, 17, 95, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC146": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "khaki", "rgb": (182, 132, 0), "cmyk": (24, 45, 100, 6)},
      "B": {"name": "diamine_green", "rgb": (30, 184, 0), "cmyk": (87, 20, 100, 10)},
      "C": {"name": "deep_grayish_olive", "rgb": (80, 84, 35), "cmyk": (50, 48, 78, 37)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC147": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "turquoise_green", "rgb": (181, 255, 194), "cmyk": (29, 0, 24, 0)},
      "B": {"name": "vandyke_red", "rgb": (116, 9, 9), "cmyk": (32, 95, 95, 33)},
      "C": {"name": "spinel_red", "rgb": (255, 77, 201), "cmyk": (0, 70, 21, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC148": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "orange_yellow", "rgb": (255, 171, 0), "cmyk": (0, 33, 100, 0)},
      "B": {"name": "cerulian_blue", "rgb": (41, 189, 173), "cmyk": (84, 26, 32, 0)},
      "C": {"name": "olive_ocher", "rgb": (209, 189, 51), "cmyk": (18, 26, 80, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC149": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "deep_slate_green", "rgb": (15, 38, 31), "cmyk": (80, 50, 60, 70)},
      "B": {"name": "orange", "rgb": (255, 82, 0), "cmyk": (0, 68, 100, 0)},
      "C": {"name": "olive_ocher", "rgb": (209, 189, 51), "cmyk": (18, 26, 80, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC150": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "seashell_pink", "rgb": (255, 207, 196), "cmyk": (0, 19, 23, 0)},
      "B": {"name": "citron_yellow", "rgb": (166, 212, 13), "cmyk": (35, 17, 95, 0)},
      "C": {"name": "glaucous_green", "rgb": (178, 232, 194), "cmyk": (30, 9, 24, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC151": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "yellow_orange", "rgb": (255, 140, 0), "cmyk": (0, 45, 100, 0)},
      "B": {"name": "vandar_poels_blue", "rgb": (0, 62, 131), "cmyk": (100, 73, 43, 10)},
      "C": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC152": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "etruscan_red", "rgb": (201, 48, 62), "cmyk": (16, 80, 74, 6)},
      "B": {"name": "light_glaucous_blue", "rgb": (166, 230, 219), "cmyk": (35, 10, 14, 0)},
      "C": {"name": "hays_russet", "rgb": (104, 25, 22), "cmyk": (37, 85, 87, 35)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC153": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "eosine_pink", "rgb": (255, 94, 196), "cmyk": (0, 63, 23, 0)},
      "B": {"name": "orange_yellow", "rgb": (255, 171, 0), "cmyk": (0, 33, 100, 0)},
      "C": {"name": "citron_yellow", "rgb": (166, 212, 13), "cmyk": (35, 17, 95, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC154": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "carmine", "rgb": (214, 0, 54), "cmyk": (0, 100, 75, 16)},
      "B": {"name": "yellow", "rgb": (255, 255, 0), "cmyk": (0, 0, 100, 0)},
      "C": {"name": "blue", "rgb": (13, 117, 255), "cmyk": (95, 54, 0, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC155": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "benzol_green", "rgb": (0, 217, 115), "cmyk": (100, 15, 55, 0)},
      "B": {"name": "jasper_red", "rgb": (250, 43, 0), "cmyk": (2, 83, 100, 0)},
      "C": {"name": "deep_indigo", "rgb": (0, 8, 49), "cmyk": (100, 92, 52, 60)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC156": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "violet", "rgb": (38, 25, 209), "cmyk": (85, 90, 18, 0)},
      "B": {"name": "olive_ocher", "rgb": (209, 189, 51), "cmyk": (18, 26, 80, 0)},
      "C": {"name": "cobalt_green", "rgb": (148, 255, 148), "cmyk": (42, 0, 42, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC157": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pansy_purple", "rgb": (111, 0, 67), "cmyk": (34, 100, 60, 34)},
      "B": {"name": "olive_ocher", "rgb": (209, 189, 51), "cmyk": (18, 26, 80, 0)},
      "C": {"name": "olympic_blue", "rgb": (79, 143, 230), "cmyk": (69, 44, 10, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC158": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cinnamon_rufous", "rgb": (194, 97, 44), "cmyk": (20, 60, 82, 5)},
      "B": {"name": "night_green", "rgb": (122, 255, 0), "cmyk": (52, 0, 100, 0)},
      "C": {"name": "lemon_yellow", "rgb": (242, 255, 38), "cmyk": (5, 0, 85, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC159": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "calamine_blue", "rgb": (128, 255, 204), "cmyk": (50, 0, 20, 0)},
      "B": {"name": "khaki", "rgb": (182, 132, 0), "cmyk": (24, 45, 100, 6)},
      "C": {"name": "grayish_lavender", "rgb": (184, 184, 255), "cmyk": (28, 28, 0, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC160": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dark_medici_blue", "rgb": (65, 119, 119), "cmyk": (70, 45, 45, 15)},
      "B": {"name": "pale_raw_umber", "rgb": (94, 64, 23), "cmyk": (46, 63, 87, 32)},
      "C": {"name": "sulphine_yellow", "rgb": (186, 166, 0), "cmyk": (24, 32, 100, 4)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC161": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pinkish_cinnamon", "rgb": (242, 173, 120), "cmyk": (5, 32, 53, 0)},
      "B": {"name": "helvetia_blue", "rgb": (0, 87, 186), "cmyk": (100, 62, 19, 10)},
      "C": {"name": "brown", "rgb": (108, 43, 17), "cmyk": (35, 74, 90, 35)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC162": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "rainette_green", "rgb": (106, 147, 70), "cmyk": (42, 20, 62, 28)},
      "B": {"name": "old_rose", "rgb": (217, 77, 153), "cmyk": (15, 70, 40, 0)},
      "C": {"name": "lilac", "rgb": (184, 117, 235), "cmyk": (28, 54, 8, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC163": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "turquoise_green", "rgb": (181, 255, 194), "cmyk": (29, 0, 24, 0)},
      "B": {"name": "antwarp_blue", "rgb": (0, 138, 161), "cmyk": (100, 40, 30, 10)},
      "C": {"name": "apricot_yellow", "rgb": (255, 230, 0), "cmyk": (0, 10, 100, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC164": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "orange_yellow", "rgb": (255, 171, 0), "cmyk": (0, 33, 100, 0)},
      "B": {"name": "violet", "rgb": (38, 25, 209), "cmyk": (85, 90, 18, 0)},
      "C": {"name": "red_orange", "rgb": (232, 25, 0), "cmyk": (9, 90, 100, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC165": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "vistoris_lake", "rgb": (92, 44, 69), "cmyk": (40, 71, 55, 40)},
      "B": {"name": "spinel_red", "rgb": (255, 77, 201), "cmyk": (0, 70, 21, 0)},
      "C": {"name": "cameo_pink", "rgb": (230, 173, 207), "cmyk": (10, 32, 19, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC166": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "grenadine_pink", "rgb": (255, 97, 107), "cmyk": (0, 62, 58, 0)},
      "B": {"name": "naples_yellow", "rgb": (250, 237, 143), "cmyk": (2, 7, 44, 0)},
      "C": {"name": "deep_slate_green", "rgb": (15, 38, 31), "cmyk": (80, 50, 60, 70)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC167": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_kings_blue", "rgb": (171, 245, 237), "cmyk": (33, 4, 7, 0)},
      "B": {"name": "ecru", "rgb": (192, 180, 144), "cmyk": (20, 25, 40, 6)},
      "C": {"name": "vandar_poels_blue", "rgb": (0, 62, 131), "cmyk": (100, 73, 43, 10)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC168": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "vandar_poels_blue", "rgb": (0, 62, 131), "cmyk": (100, 73, 43, 10)},
      "B": {"name": "lemon_yellow", "rgb": (242, 255, 38), "cmyk": (5, 0, 85, 0)},
      "C": {"name": "vernonia_purple", "rgb": (126, 48, 117), "cmyk": (42, 78, 46, 15)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC169": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "corinthian_pink", "rgb": (255, 166, 217), "cmyk": (0, 35, 15, 0)},
      "B": {"name": "warm_gray", "rgb": (156, 178, 158), "cmyk": (37, 28, 36, 3)},
      "C": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC170": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "rosolanc_purple", "rgb": (178, 25, 171), "cmyk": (30, 90, 33, 0)},
      "B": {"name": "orange_yellow", "rgb": (255, 171, 0), "cmyk": (0, 33, 100, 0)},
      "C": {"name": "red_violet", "rgb": (52, 0, 163), "cmyk": (76, 100, 25, 15)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC171": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "yellow_orange", "rgb": (255, 140, 0), "cmyk": (0, 45, 100, 0)},
      "B": {"name": "glaucous_green", "rgb": (178, 232, 194), "cmyk": (30, 9, 24, 0)},
      "C": {"name": "pale_burnt_lake", "rgb": (115, 15, 31), "cmyk": (25, 90, 80, 40)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC172": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "antwarp_blue", "rgb": (0, 138, 161), "cmyk": (100, 40, 30, 10)},
      "B": {"name": "red_violet", "rgb": (52, 0, 163), "cmyk": (76, 100, 25, 15)},
      "C": {"name": "cinnamon_rufous", "rgb": (194, 97, 44), "cmyk": (20, 60, 82, 5)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC173": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "lemon_yellow", "rgb": (242, 255, 38), "cmyk": (5, 0, 85, 0)},
      "B": {"name": "madder_brown", "rgb": (101, 19, 0), "cmyk": (36, 88, 100, 38)},
      "C": {"name": "turquoise_green", "rgb": (181, 255, 194), "cmyk": (29, 0, 24, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC174": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "taupe_brown", "rgb": (107, 46, 99), "cmyk": (30, 70, 35, 40)},
      "B": {"name": "grayish_lavender", "rgb": (184, 184, 255), "cmyk": (28, 28, 0, 0)},
      "C": {"name": "corinthian_pink", "rgb": (255, 166, 217), "cmyk": (0, 35, 15, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC175": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "olive_buff", "rgb": (188, 211, 130), "cmyk": (16, 6, 42, 12)},
      "B": {"name": "pinkish_cinnamon", "rgb": (242, 173, 120), "cmyk": (5, 32, 53, 0)},
      "C": {"name": "blue_violet", "rgb": (71, 51, 255), "cmyk": (72, 80, 0, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC176": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "calamine_blue", "rgb": (128, 255, 204), "cmyk": (50, 0, 20, 0)},
      "B": {"name": "hermosa_pink", "rgb": (255, 178, 240), "cmyk": (0, 30, 6, 0)},
      "C": {"name": "seashell_pink", "rgb": (255, 207, 196), "cmyk": (0, 19, 23, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC177": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "buffy_citrine", "rgb": (136, 141, 42), "cmyk": (42, 40, 82, 8)},
      "B": {"name": "pale_burnt_lake", "rgb": (115, 15, 31), "cmyk": (25, 90, 80, 40)},
      "C": {"name": "grayish_lavender", "rgb": (184, 184, 255), "cmyk": (28, 28, 0, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC178": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "light_glaucous_blue", "rgb": (166, 230, 219), "cmyk": (35, 10, 14, 0)},
      "B": {"name": "ivory_buff", "rgb": (235, 217, 153), "cmyk": (8, 15, 40, 0)},
      "C": {"name": "green_blue", "rgb": (45, 188, 148), "cmyk": (82, 24, 40, 3)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC179": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "red_orange", "rgb": (232, 25, 0), "cmyk": (9, 90, 100, 0)},
      "B": {"name": "deep_lyons_blue", "rgb": (0, 36, 204), "cmyk": (100, 85, 15, 6)},
      "C": {"name": "golden_yellow", "rgb": (250, 148, 66), "cmyk": (2, 42, 74, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC180": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "light_mauve", "rgb": (145, 97, 242), "cmyk": (43, 62, 5, 0)},
      "B": {"name": "neutral_gray", "rgb": (181, 209, 204), "cmyk": (29, 18, 20, 0)},
      "C": {"name": "cinnamon_buff", "rgb": (255, 191, 110), "cmyk": (0, 25, 57, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC181": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cotinga_purple", "rgb": (52, 0, 89), "cmyk": (66, 100, 42, 40)},
      "B": {"name": "violet", "rgb": (38, 25, 209), "cmyk": (85, 90, 18, 0)},
      "C": {"name": "carmine_red", "rgb": (161, 11, 43), "cmyk": (25, 95, 80, 16)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC182": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "vandyke_brown", "rgb": (54, 35, 4), "cmyk": (56, 71, 97, 52)},
      "B": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)},
      "C": {"name": "deep_indigo", "rgb": (0, 8, 49), "cmyk": (100, 92, 52, 60)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC183": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "vernonia_purple", "rgb": (126, 48, 117), "cmyk": (42, 78, 46, 15)},
      "B": {"name": "red_violet", "rgb": (52, 0, 163), "cmyk": (76, 100, 25, 15)},
      "C": {"name": "plumbeous", "rgb": (92, 114, 135), "cmyk": (61, 52, 43, 7)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC184": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "light_grayish_olive", "rgb": (118, 132, 78), "cmyk": (43, 36, 62, 19)},
      "B": {"name": "ivory_buff", "rgb": (235, 217, 153), "cmyk": (8, 15, 40, 0)},
      "C": {"name": "spinel_red", "rgb": (255, 77, 201), "cmyk": (0, 70, 21, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC185": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)},
      "B": {"name": "light_brown_drab", "rgb": (176, 134, 153), "cmyk": (8, 30, 20, 25)},
      "C": {"name": "etruscan_red", "rgb": (201, 48, 62), "cmyk": (16, 80, 74, 6)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC186": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "hays_russet", "rgb": (104, 25, 22), "cmyk": (37, 85, 87, 35)},
      "B": {"name": "blue", "rgb": (13, 117, 255), "cmyk": (95, 54, 0, 0)},
      "C": {"name": "ochraceous_salmon", "rgb": (217, 158, 115), "cmyk": (15, 38, 55, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC187": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "grayish_lavender", "rgb": (184, 184, 255), "cmyk": (28, 28, 0, 0)},
      "B": {"name": "helvetia_blue", "rgb": (0, 87, 186), "cmyk": (100, 62, 19, 10)},
      "C": {"name": "aconite_violet", "rgb": (156, 82, 242), "cmyk": (39, 68, 5, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC188": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cobalt_green", "rgb": (148, 255, 148), "cmyk": (42, 0, 42, 0)},
      "B": {"name": "rainette_green", "rgb": (106, 147, 70), "cmyk": (42, 20, 62, 28)},
      "C": {"name": "salvia_blue", "rgb": (150, 191, 230), "cmyk": (41, 25, 10, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC189": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "venice_green", "rgb": (107, 255, 178), "cmyk": (58, 0, 30, 0)},
      "B": {"name": "lemon_yellow", "rgb": (242, 255, 38), "cmyk": (5, 0, 85, 0)},
      "C": {"name": "deep_slate_olive", "rgb": (23, 39, 19), "cmyk": (76, 60, 80, 62)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC190": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)},
      "B": {"name": "english_red", "rgb": (222, 69, 0), "cmyk": (13, 73, 100, 0)},
      "C": {"name": "ivory_buff", "rgb": (235, 217, 153), "cmyk": (8, 15, 40, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC191": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "blue", "rgb": (13, 117, 255), "cmyk": (95, 54, 0, 0)},
      "B": {"name": "light_brown_drab", "rgb": (176, 134, 153), "cmyk": (8, 30, 20, 25)},
      "C": {"name": "yellow_ocher", "rgb": (224, 184, 31), "cmyk": (12, 28, 88, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC192": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cream_yellow", "rgb": (255, 82, 184), "cmyk": (0, 68, 28, 0)},
      "B": {"name": "plumbeous", "rgb": (92, 114, 135), "cmyk": (61, 52, 43, 7)},
      "C": {"name": "vandyke_brown", "rgb": (54, 35, 4), "cmyk": (56, 71, 97, 52)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC193": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "light_porcelain_green", "rgb": (35, 193, 124), "cmyk": (86, 22, 50, 3)},
      "B": {"name": "naples_yellow", "rgb": (250, 237, 143), "cmyk": (2, 7, 44, 0)},
      "C": {"name": "grenadine_pink", "rgb": (255, 97, 107), "cmyk": (0, 62, 58, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC194": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "jasper_red", "rgb": (250, 43, 0), "cmyk": (2, 83, 100, 0)},
      "B": {"name": "olympic_blue", "rgb": (79, 143, 230), "cmyk": (69, 44, 10, 0)},
      "C": {"name": "seashell_pink", "rgb": (255, 207, 196), "cmyk": (0, 19, 23, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC195": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "spinel_red", "rgb": (255, 77, 201), "cmyk": (0, 70, 21, 0)},
      "B": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)},
      "C": {"name": "neutral_gray", "rgb": (181, 209, 204), "cmyk": (29, 18, 20, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC196": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "citron_yellow", "rgb": (166, 212, 13), "cmyk": (35, 17, 95, 0)},
      "B": {"name": "blue_violet", "rgb": (71, 51, 255), "cmyk": (72, 80, 0, 0)},
      "C": {"name": "pale_kings_blue", "rgb": (171, 245, 237), "cmyk": (33, 4, 7, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC197": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dark_soft_violet", "rgb": (77, 82, 222), "cmyk": (70, 68, 13, 0)},
      "B": {"name": "eosine_pink", "rgb": (255, 94, 196), "cmyk": (0, 63, 23, 0)},
      "C": {"name": "neutral_gray", "rgb": (181, 209, 204), "cmyk": (29, 18, 20, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC198": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "green", "rgb": (64, 201, 69), "cmyk": (75, 21, 73, 0)},
      "B": {"name": "apricot_yellow", "rgb": (255, 230, 0), "cmyk": (0, 10, 100, 0)},
      "C": {"name": "burnt_sienna", "rgb": (169, 52, 0), "cmyk": (22, 76, 100, 15)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC199": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "deep_lyons_blue", "rgb": (0, 36, 204), "cmyk": (100, 85, 15, 6)},
      "B": {"name": "ocher_red", "rgb": (167, 55, 75), "cmyk": (18, 73, 63, 20)},
      "C": {"name": "light_brownish_olive", "rgb": (112, 105, 52), "cmyk": (42, 46, 73, 24)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC200": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "olive_buff", "rgb": (188, 211, 130), "cmyk": (16, 6, 42, 12)},
      "B": {"name": "carmine_red", "rgb": (161, 11, 43), "cmyk": (25, 95, 80, 16)},
      "C": {"name": "chromium_green", "rgb": (102, 171, 86), "cmyk": (50, 16, 58, 20)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC201": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "olive", "rgb": (113, 134, 0), "cmyk": (48, 38, 100, 15)},
      "B": {"name": "grenadine_pink", "rgb": (255, 97, 107), "cmyk": (0, 62, 58, 0)},
      "C": {"name": "cobalt_green", "rgb": (148, 255, 148), "cmyk": (42, 0, 42, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC202": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cobalt_green", "rgb": (148, 255, 148), "cmyk": (42, 0, 42, 0)},
      "B": {"name": "slate_color", "rgb": (27, 54, 68), "cmyk": (85, 70, 62, 30)},
      "C": {"name": "turquoise_green", "rgb": (181, 255, 194), "cmyk": (29, 0, 24, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC203": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "vinaceous_cinnamon", "rgb": (245, 153, 148), "cmyk": (4, 40, 42, 0)},
      "B": {"name": "lincoln_green", "rgb": (64, 84, 22), "cmyk": (60, 48, 86, 37)},
      "C": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC204": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "rosolanc_purple", "rgb": (178, 25, 171), "cmyk": (30, 90, 33, 0)},
      "B": {"name": "light_glaucous_blue", "rgb": (166, 230, 219), "cmyk": (35, 10, 14, 0)},
      "C": {"name": "cinnamon_rufous", "rgb": (194, 97, 44), "cmyk": (20, 60, 82, 5)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC205": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "vinaceous_cinnamon", "rgb": (245, 153, 148), "cmyk": (4, 40, 42, 0)},
      "B": {"name": "pale_burnt_lake", "rgb": (115, 15, 31), "cmyk": (25, 90, 80, 40)},
      "C": {"name": "violet", "rgb": (38, 25, 209), "cmyk": (85, 90, 18, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC206": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "corinthian_pink", "rgb": (255, 166, 217), "cmyk": (0, 35, 15, 0)},
      "B": {"name": "cinnamon_rufous", "rgb": (194, 97, 44), "cmyk": (20, 60, 82, 5)},
      "C": {"name": "golden_yellow", "rgb": (250, 148, 66), "cmyk": (2, 42, 74, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC207": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)},
      "B": {"name": "glaucous_green", "rgb": (178, 232, 194), "cmyk": (30, 9, 24, 0)},
      "C": {"name": "sudan_brown", "rgb": (155, 83, 72), "cmyk": (25, 60, 65, 19)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC208": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "green_blue", "rgb": (45, 188, 148), "cmyk": (82, 24, 40, 3)},
      "B": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)},
      "C": {"name": "antwarp_blue", "rgb": (0, 138, 161), "cmyk": (100, 40, 30, 10)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC209": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "yellow_orange", "rgb": (255, 140, 0), "cmyk": (0, 45, 100, 0)},
      "B": {"name": "salvia_blue", "rgb": (150, 191, 230), "cmyk": (41, 25, 10, 0)},
      "C": {"name": "ivory_buff", "rgb": (235, 217, 153), "cmyk": (8, 15, 40, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC210": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "lemon_yellow", "rgb": (242, 255, 38), "cmyk": (5, 0, 85, 0)},
      "B": {"name": "lincoln_green", "rgb": (64, 84, 22), "cmyk": (60, 48, 86, 37)},
      "C": {"name": "cinnamon_buff", "rgb": (255, 191, 110), "cmyk": (0, 25, 57, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC211": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "deep_indigo", "rgb": (0, 8, 49), "cmyk": (100, 92, 52, 60)},
      "B": {"name": "apricot_orange", "rgb": (255, 115, 64), "cmyk": (0, 55, 75, 0)},
      "C": {"name": "olive_yellow", "rgb": (153, 178, 51), "cmyk": (40, 30, 80, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC212": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "orange_citrine", "rgb": (140, 101, 16), "cmyk": (28, 48, 92, 24)},
      "B": {"name": "salvia_blue", "rgb": (150, 191, 230), "cmyk": (41, 25, 10, 0)},
      "C": {"name": "pompeian_red", "rgb": (169, 6, 54), "cmyk": (18, 97, 74, 19)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC213": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "apricot_yellow", "rgb": (255, 230, 0), "cmyk": (0, 10, 100, 0)},
      "B": {"name": "pale_kings_blue", "rgb": (171, 245, 237), "cmyk": (33, 4, 7, 0)},
      "C": {"name": "vinaceous_cinnamon", "rgb": (245, 153, 148), "cmyk": (4, 40, 42, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC214": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "sudan_brown", "rgb": (155, 83, 72), "cmyk": (25, 60, 65, 19)},
      "B": {"name": "ivory_buff", "rgb": (235, 217, 153), "cmyk": (8, 15, 40, 0)},
      "C": {"name": "violet", "rgb": (38, 25, 209), "cmyk": (85, 90, 18, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC215": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "eupatorium_purple", "rgb": (191, 54, 224), "cmyk": (25, 79, 12, 0)},
      "B": {"name": "cream_yellow", "rgb": (255, 82, 184), "cmyk": (0, 68, 28, 0)},
      "C": {"name": "blue", "rgb": (13, 117, 255), "cmyk": (95, 54, 0, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC216": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "jasper_red", "rgb": (250, 43, 0), "cmyk": (2, 83, 100, 0)},
      "B": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)},
      "C": {"name": "green", "rgb": (64, 201, 69), "cmyk": (75, 21, 73, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC217": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_burnt_lake", "rgb": (115, 15, 31), "cmyk": (25, 90, 80, 40)},
      "B": {"name": "ochraceous_salmon", "rgb": (217, 158, 115), "cmyk": (15, 38, 55, 0)},
      "C": {"name": "diamine_green", "rgb": (30, 184, 0), "cmyk": (87, 20, 100, 10)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC218": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "plumbeous", "rgb": (92, 114, 135), "cmyk": (61, 52, 43, 7)},
      "B": {"name": "grayish_lavender", "rgb": (184, 184, 255), "cmyk": (28, 28, 0, 0)},
      "C": {"name": "helvetia_blue", "rgb": (0, 87, 186), "cmyk": (100, 62, 19, 10)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC219": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "jasper_red", "rgb": (250, 43, 0), "cmyk": (2, 83, 100, 0)},
      "B": {"name": "dusky_green", "rgb": (0, 89, 46), "cmyk": (100, 30, 64, 50)},
      "C": {"name": "chromium_green", "rgb": (102, 171, 86), "cmyk": (50, 16, 58, 20)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC220": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "aconite_violet", "rgb": (156, 82, 242), "cmyk": (39, 68, 5, 0)},
      "B": {"name": "pomegranate_purple", "rgb": (185, 0, 120), "cmyk": (23, 100, 50, 6)},
      "C": {"name": "ochraceous_salmon", "rgb": (217, 158, 115), "cmyk": (15, 38, 55, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC221": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)},
      "B": {"name": "carmine_red", "rgb": (161, 11, 43), "cmyk": (25, 95, 80, 16)},
      "C": {"name": "neutral_gray", "rgb": (181, 209, 204), "cmyk": (29, 18, 20, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC222": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "yellow_orange", "rgb": (255, 140, 0), "cmyk": (0, 45, 100, 0)},
      "B": {"name": "yellow_ocher", "rgb": (224, 184, 31), "cmyk": (12, 28, 88, 0)},
      "C": {"name": "orange_rufous", "rgb": (192, 82, 0), "cmyk": (18, 65, 100, 8)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC223": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "light_brown_drab", "rgb": (176, 134, 153), "cmyk": (8, 30, 20, 25)},
      "B": {"name": "ochraceous_salmon", "rgb": (217, 158, 115), "cmyk": (15, 38, 55, 0)},
      "C": {"name": "turquoise_green", "rgb": (181, 255, 194), "cmyk": (29, 0, 24, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC224": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dark_medici_blue", "rgb": (65, 119, 119), "cmyk": (70, 45, 45, 15)},
      "B": {"name": "spinel_red", "rgb": (255, 77, 201), "cmyk": (0, 70, 21, 0)},
      "C": {"name": "taupe_brown", "rgb": (107, 46, 99), "cmyk": (30, 70, 35, 40)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC225": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dark_slate_purple", "rgb": (83, 34, 92), "cmyk": (64, 85, 60, 10)},
      "B": {"name": "dusky_green", "rgb": (0, 89, 46), "cmyk": (100, 30, 64, 50)},
      "C": {"name": "carmine", "rgb": (214, 0, 54), "cmyk": (0, 100, 75, 16)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC226": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "violet", "rgb": (38, 25, 209), "cmyk": (85, 90, 18, 0)},
      "B": {"name": "cream_yellow", "rgb": (255, 82, 184), "cmyk": (0, 68, 28, 0)},
      "C": {"name": "vistoris_lake", "rgb": (92, 44, 69), "cmyk": (40, 71, 55, 40)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC227": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cerulian_blue", "rgb": (41, 189, 173), "cmyk": (84, 26, 32, 0)},
      "B": {"name": "light_glaucous_blue", "rgb": (166, 230, 219), "cmyk": (35, 10, 14, 0)},
      "C": {"name": "hermosa_pink", "rgb": (255, 178, 240), "cmyk": (0, 30, 6, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC228": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "carmine_red", "rgb": (161, 11, 43), "cmyk": (25, 95, 80, 16)},
      "B": {"name": "neutral_gray", "rgb": (181, 209, 204), "cmyk": (29, 18, 20, 0)},
      "C": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC229": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "neutral_gray", "rgb": (181, 209, 204), "cmyk": (29, 18, 20, 0)},
      "B": {"name": "deep_slate_olive", "rgb": (23, 39, 19), "cmyk": (76, 60, 80, 62)},
      "C": {"name": "golden_yellow", "rgb": (250, 148, 66), "cmyk": (2, 42, 74, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC230": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "grenadine_pink", "rgb": (255, 97, 107), "cmyk": (0, 62, 58, 0)},
      "B": {"name": "turquoise_green", "rgb": (181, 255, 194), "cmyk": (29, 0, 24, 0)},
      "C": {"name": "cobalt_green", "rgb": (148, 255, 148), "cmyk": (42, 0, 42, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC231": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "hays_russet", "rgb": (104, 25, 22), "cmyk": (37, 85, 87, 35)},
      "B": {"name": "cameo_pink", "rgb": (230, 173, 207), "cmyk": (10, 32, 19, 0)},
      "C": {"name": "olympic_blue", "rgb": (79, 143, 230), "cmyk": (69, 44, 10, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC232": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "deep_indigo", "rgb": (0, 8, 49), "cmyk": (100, 92, 52, 60)},
      "B": {"name": "carmine", "rgb": (214, 0, 54), "cmyk": (0, 100, 75, 16)},
      "C": {"name": "pinkish_cinnamon", "rgb": (242, 173, 120), "cmyk": (5, 32, 53, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC233": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "violet_blue", "rgb": (32, 45, 133), "cmyk": (85, 79, 38, 16)},
      "B": {"name": "carmine_red", "rgb": (161, 11, 43), "cmyk": (25, 95, 80, 16)},
      "C": {"name": "buffy_citrine", "rgb": (136, 141, 42), "cmyk": (42, 40, 82, 8)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC234": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_kings_blue", "rgb": (171, 245, 237), "cmyk": (33, 4, 7, 0)},
      "B": {"name": "pale_raw_umber", "rgb": (94, 64, 23), "cmyk": (46, 63, 87, 32)},
      "C": {"name": "cinnamon_buff", "rgb": (255, 191, 110), "cmyk": (0, 25, 57, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC235": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "yellow_orange", "rgb": (255, 140, 0), "cmyk": (0, 45, 100, 0)},
      "B": {"name": "ivory_buff", "rgb": (235, 217, 153), "cmyk": (8, 15, 40, 0)},
      "C": {"name": "grayish_lavender", "rgb": (184, 184, 255), "cmyk": (28, 28, 0, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC236": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "purple_drab", "rgb": (117, 66, 96), "cmyk": (38, 65, 49, 26)},
      "B": {"name": "deep_lyons_blue", "rgb": (0, 36, 204), "cmyk": (100, 85, 15, 6)},
      "C": {"name": "khaki", "rgb": (182, 132, 0), "cmyk": (24, 45, 100, 6)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC237": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "carmine_red", "rgb": (161, 11, 43), "cmyk": (25, 95, 80, 16)},
      "B": {"name": "salvia_blue", "rgb": (150, 191, 230), "cmyk": (41, 25, 10, 0)},
      "C": {"name": "madder_brown", "rgb": (101, 19, 0), "cmyk": (36, 88, 100, 38)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC238": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "warm_gray", "rgb": (156, 178, 158), "cmyk": (37, 28, 36, 3)},
      "B": {"name": "cotinga_purple", "rgb": (52, 0, 89), "cmyk": (66, 100, 42, 40)},
      "C": {"name": "ochraceous_salmon", "rgb": (217, 158, 115), "cmyk": (15, 38, 55, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC239": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "light_brown_drab", "rgb": (176, 134, 153), "cmyk": (8, 30, 20, 25)},
      "B": {"name": "glaucous_green", "rgb": (178, 232, 194), "cmyk": (30, 9, 24, 0)},
      "C": {"name": "pyrite_yellow", "rgb": (196, 191, 51), "cmyk": (23, 25, 80, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },

  "DCC240": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "fresh_color", "rgb": (255, 120, 140), "cmyk": (0, 53, 45, 0)},
      "B": {"name": "cerulian_blue", "rgb": (41, 189, 173), "cmyk": (84, 26, 32, 0)},
      "C": {"name": "yellow", "rgb": (255, 255, 0), "cmyk": (0, 0, 100, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C"]}
  },
# -- 4-colors
  "PP005": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "Color_11", "rgb": (231,243,234), "cmyk": (12, 0,11, 0)},
      "B": {"name": "Color_12", "rgb": (251,221,201), "cmyk": ( 1,17,22, 0)},
      "C": {"name": "Color_13", "rgb": (243,166,142), "cmyk": ( 1,44,42, 0)},
      "D": {"name": "Color_14", "rgb": ( 87, 80, 93), "cmyk": (68,63,47,29)}
    },
    "roles": {"dominant": "C", "secondary": ["B"], "accent": ["A","D"]}    
  },
  
  "PP013": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (223,239,228), "cmyk": (16,0,14,0)},
      "B": {"name": "color_2", "rgb": (211,156,111), "cmyk": (16,42,58,4)},
      "C": {"name": "color_3", "rgb": (155,156,158), "cmyk": (41,31,31,10)},
      "D": {"name": "color_4", "rgb": (60,117,126), "cmyk": (76,35,41,20)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C","D"]}
  },
    
  "PP014": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (243,166,142), "cmyk": (1,44,42,0)},
      "B": {"name": "color_2", "rgb": (251,221,201), "cmyk": (1,17,22,0)},
      "C": {"name": "color_3", "rgb": (87,80,93), "cmyk": (68,63,47,29)},
      "D": {"name": "color_4", "rgb": (231,243,234), "cmyk": (12,0,11,0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C","D"]}
  },
    
  "PP015": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (223,205,170), "cmyk": (15,19,37,0)},
      "B": {"name": "color_2", "rgb": (252,220,207), "cmyk": (0,18,18,0)},
      "C": {"name": "color_3", "rgb": (130,157,150), "cmyk": (53,25,36,7)},
      "D": {"name": "color_4", "rgb": (119,102,116), "cmyk": (57,58,41,15)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C","D"]}
  },
  
  "PP016": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (241,246,249), "cmyk": (7,2,2,0)},
      "B": {"name": "color_2", "rgb": (250,243,196), "cmyk": (4,2,31,0)},
      "C": {"name": "color_3", "rgb": (198,208,207), "cmyk": (27,13,19,0)},
      "D": {"name": "color_4", "rgb": (114,122,132), "cmyk": (61,47,40,9)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C","D"]}
  },
   
  "PP017": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (246,215,192), "cmyk": (3,20,26,0)},
      "B": {"name": "color_2", "rgb": (119,102,116), "cmyk": (57,58,41,15)},
      "C": {"name": "color_3", "rgb": (226,216,236), "cmyk": (12,17,0,0)},
      "D": {"name": "color_4", "rgb": (243,172,148), "cmyk": (2,41,40,0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C","D"]}
  },
  
  "PP022": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (226,216,236), "cmyk": (12,17,0,0)},
      "B": {"name": "color_2", "rgb": (247,246,247), "cmyk": (4,3,3,0)},
      "C": {"name": "color_3", "rgb": (119,102,116), "cmyk": (57,58,41,15)},
      "D": {"name": "color_4", "rgb": (221,193,179), "cmyk": (14,26,28,2)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C","D"]}
  },

  "PP023": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (231,243,234), "cmyk": (12,0,11,0)},
      "B": {"name": "color_2", "rgb": (220,212,207), "cmyk": (16,16,18,0)},
      "C": {"name": "color_3", "rgb": (208,196,145), "cmyk": (21,19,49,3)},
      "D": {"name": "color_4", "rgb": (239,238,163), "cmyk": (10,0,47,0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C","D"]}
  },

  "PP024": {
    "source": "palette_perfect",
    "colors": {
      "A": {"name": "color_1", "rgb": (142,166,166), "cmyk": (49,24,32,5)},
      "B": {"name": "color_2", "rgb": (224,205,171), "cmyk": (15,19,37,0)},
      "C": {"name": "color_3", "rgb": (252,247,233), "cmyk": (2,3,11,0)},
      "D": {"name": "color_4", "rgb": (119,102,116), "cmyk": (57,58,41,15)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C","D"]}
  },

  "DCC241": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "red_orange", "rgb": (232, 25, 0), "cmyk": (9, 90, 100, 0)},
      "B": {"name": "dark_medici_blue", "rgb": (65, 119, 119), "cmyk": (70, 45, 45, 15)},
      "C": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)},
      "D": {"name": "isabella_color", "rgb": (195, 165, 92), "cmyk": (15, 28, 60, 10)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC242": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "eosine_pink", "rgb": (255, 94, 196), "cmyk": (0, 63, 23, 0)},
      "B": {"name": "diamine_green", "rgb": (30, 184, 0), "cmyk": (87, 20, 100, 10)},
      "C": {"name": "burnt_sienna", "rgb": (169, 52, 0), "cmyk": (22, 76, 100, 15)},
      "D": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC243": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)},
      "B": {"name": "olive_green", "rgb": (88, 119, 30), "cmyk": (56, 40, 85, 22)},
      "C": {"name": "ivory_buff", "rgb": (235, 217, 153), "cmyk": (8, 15, 40, 0)},
      "D": {"name": "slate_color", "rgb": (27, 54, 68), "cmyk": (85, 70, 62, 30)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC244": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "light_brown_drab", "rgb": (176, 134, 153), "cmyk": (8, 30, 20, 25)},
      "B": {"name": "antwarp_blue", "rgb": (0, 138, 161), "cmyk": (100, 40, 30, 10)},
      "C": {"name": "vinaceous_tawny", "rgb": (199, 67, 0), "cmyk": (17, 72, 100, 6)},
      "D": {"name": "andover_green", "rgb": (92, 138, 115), "cmyk": (60, 40, 50, 10)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC245": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "oil_green", "rgb": (110, 169, 0), "cmyk": (53, 28, 100, 8)},
      "B": {"name": "slate_color", "rgb": (27, 54, 68), "cmyk": (85, 70, 62, 30)},
      "C": {"name": "dark_tyrian_blue", "rgb": (13, 43, 82), "cmyk": (90, 66, 36, 50)},
      "D": {"name": "carmine_red", "rgb": (161, 11, 43), "cmyk": (25, 95, 80, 16)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC246": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "brick_red", "rgb": (163, 33, 0), "cmyk": (22, 84, 100, 18)},
      "B": {"name": "corinthian_pink", "rgb": (255, 166, 217), "cmyk": (0, 35, 15, 0)},
      "C": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)},
      "D": {"name": "cinnamon_buff", "rgb": (255, 191, 110), "cmyk": (0, 25, 57, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC247": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)},
      "B": {"name": "benzol_green", "rgb": (0, 217, 115), "cmyk": (100, 15, 55, 0)},
      "C": {"name": "deep_lyons_blue", "rgb": (0, 36, 204), "cmyk": (100, 85, 15, 6)},
      "D": {"name": "apricot_yellow", "rgb": (255, 230, 0), "cmyk": (0, 10, 100, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC248": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "grayish_lavender", "rgb": (184, 184, 255), "cmyk": (28, 28, 0, 0)},
      "B": {"name": "khaki", "rgb": (182, 132, 0), "cmyk": (24, 45, 100, 6)},
      "C": {"name": "eosine_pink", "rgb": (255, 94, 196), "cmyk": (0, 63, 23, 0)},
      "D": {"name": "dark_slate_purple", "rgb": (83, 34, 92), "cmyk": (64, 85, 60, 10)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC249": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "olive_ocher", "rgb": (209, 189, 51), "cmyk": (18, 26, 80, 0)},
      "B": {"name": "dark_medici_blue", "rgb": (65, 119, 119), "cmyk": (70, 45, 45, 15)},
      "C": {"name": "hays_russet", "rgb": (104, 25, 22), "cmyk": (37, 85, 87, 35)},
      "D": {"name": "ecru", "rgb": (192, 180, 144), "cmyk": (20, 25, 40, 6)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC250": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pyrite_yellow", "rgb": (196, 191, 51), "cmyk": (23, 25, 80, 0)},
      "B": {"name": "peach_red", "rgb": (255, 51, 25), "cmyk": (0, 80, 90, 0)},
      "C": {"name": "sea_green", "rgb": (51, 255, 125), "cmyk": (80, 0, 51, 0)},
      "D": {"name": "nile_blue", "rgb": (191, 255, 230), "cmyk": (25, 0, 10, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC251": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "red", "rgb": (161, 0, 69), "cmyk": (30, 100, 70, 10)},
      "B": {"name": "diamine_green", "rgb": (30, 184, 0), "cmyk": (87, 20, 100, 10)},
      "C": {"name": "slate_color", "rgb": (27, 54, 68), "cmyk": (85, 70, 62, 30)},
      "D": {"name": "yellow", "rgb": (255, 255, 0), "cmyk": (0, 0, 100, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC252": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "eugenia_red", "rgb": (237, 61, 102), "cmyk": (7, 76, 60, 0)},
      "B": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)},
      "C": {"name": "green_blue", "rgb": (45, 188, 148), "cmyk": (82, 24, 40, 3)},
      "D": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC253": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "apricot_orange", "rgb": (255, 115, 64), "cmyk": (0, 55, 75, 0)},
      "B": {"name": "lemon_yellow", "rgb": (242, 255, 38), "cmyk": (5, 0, 85, 0)},
      "C": {"name": "cotinga_purple", "rgb": (52, 0, 89), "cmyk": (66, 100, 42, 40)},
      "D": {"name": "slate_color", "rgb": (27, 54, 68), "cmyk": (85, 70, 62, 30)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC254": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "laelia_pink", "rgb": (204, 133, 209), "cmyk": (20, 48, 18, 0)},
      "B": {"name": "olive", "rgb": (113, 134, 0), "cmyk": (48, 38, 100, 15)},
      "C": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)},
      "D": {"name": "corinthian_pink", "rgb": (255, 166, 217), "cmyk": (0, 35, 15, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC255": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "calamine_blue", "rgb": (128, 255, 204), "cmyk": (50, 0, 20, 0)},
      "B": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)},
      "C": {"name": "pyrite_yellow", "rgb": (196, 191, 51), "cmyk": (23, 25, 80, 0)},
      "D": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC256": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)},
      "B": {"name": "orange", "rgb": (255, 82, 0), "cmyk": (0, 68, 100, 0)},
      "C": {"name": "vinaceous_cinnamon", "rgb": (245, 153, 148), "cmyk": (4, 40, 42, 0)},
      "D": {"name": "dull_viridian_green", "rgb": (25, 204, 51), "cmyk": (90, 20, 80, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC257": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "blue", "rgb": (13, 117, 255), "cmyk": (95, 54, 0, 0)},
      "B": {"name": "spectrum_red", "rgb": (242, 0, 0), "cmyk": (5, 100, 100, 0)},
      "C": {"name": "aconite_violet", "rgb": (156, 82, 242), "cmyk": (39, 68, 5, 0)},
      "D": {"name": "orange_yellow", "rgb": (255, 171, 0), "cmyk": (0, 33, 100, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC258": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pinkish_cinnamon", "rgb": (242, 173, 120), "cmyk": (5, 32, 53, 0)},
      "B": {"name": "olive", "rgb": (113, 134, 0), "cmyk": (48, 38, 100, 15)},
      "C": {"name": "pale_burnt_lake", "rgb": (115, 15, 31), "cmyk": (25, 90, 80, 40)},
      "D": {"name": "antwarp_blue", "rgb": (0, 138, 161), "cmyk": (100, 40, 30, 10)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC259": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "green_blue", "rgb": (45, 188, 148), "cmyk": (82, 24, 40, 3)},
      "B": {"name": "warm_gray", "rgb": (156, 178, 158), "cmyk": (37, 28, 36, 3)},
      "C": {"name": "lemon_yellow", "rgb": (242, 255, 38), "cmyk": (5, 0, 85, 0)},
      "D": {"name": "helvetia_blue", "rgb": (0, 87, 186), "cmyk": (100, 62, 19, 10)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC260": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "old_rose", "rgb": (217, 77, 153), "cmyk": (15, 70, 40, 0)},
      "B": {"name": "sea_green", "rgb": (51, 255, 125), "cmyk": (80, 0, 51, 0)},
      "C": {"name": "glaucous_green", "rgb": (178, 232, 194), "cmyk": (30, 9, 24, 0)},
      "D": {"name": "vinaceous_cinnamon", "rgb": (245, 153, 148), "cmyk": (4, 40, 42, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC261": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "warm_gray", "rgb": (156, 178, 158), "cmyk": (37, 28, 36, 3)},
      "B": {"name": "red", "rgb": (161, 0, 69), "cmyk": (30, 100, 70, 10)},
      "C": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)},
      "D": {"name": "calamine_blue", "rgb": (128, 255, 204), "cmyk": (50, 0, 20, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC262": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "ivory_buff", "rgb": (235, 217, 153), "cmyk": (8, 15, 40, 0)},
      "B": {"name": "eugenia_red", "rgb": (237, 61, 102), "cmyk": (7, 76, 60, 0)},
      "C": {"name": "cossack_green", "rgb": (50, 142, 19), "cmyk": (76, 32, 91, 18)},
      "D": {"name": "citrine", "rgb": (152, 161, 0), "cmyk": (36, 32, 100, 7)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC263": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pinkish_cinnamon", "rgb": (242, 173, 120), "cmyk": (5, 32, 53, 0)},
      "B": {"name": "slate_color", "rgb": (27, 54, 68), "cmyk": (85, 70, 62, 30)},
      "C": {"name": "burnt_sienna", "rgb": (169, 52, 0), "cmyk": (22, 76, 100, 15)},
      "D": {"name": "turquoise_green", "rgb": (181, 255, 194), "cmyk": (29, 0, 24, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC264": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "corinthian_pink", "rgb": (255, 166, 217), "cmyk": (0, 35, 15, 0)},
      "B": {"name": "cerulian_blue", "rgb": (41, 189, 173), "cmyk": (84, 26, 32, 0)},
      "C": {"name": "red_orange", "rgb": (232, 25, 0), "cmyk": (9, 90, 100, 0)},
      "D": {"name": "dark_greenish_glaucous", "rgb": (178, 217, 163), "cmyk": (30, 15, 36, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC265": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "olive_yellow", "rgb": (153, 178, 51), "cmyk": (40, 30, 80, 0)},
      "B": {"name": "old_rose", "rgb": (217, 77, 153), "cmyk": (15, 70, 40, 0)},
      "C": {"name": "dull_violet_black", "rgb": (0, 13, 79), "cmyk": (100, 90, 38, 50)},
      "D": {"name": "apricot_yellow", "rgb": (255, 230, 0), "cmyk": (0, 10, 100, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC266": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "spectrum_red", "rgb": (242, 0, 0), "cmyk": (5, 100, 100, 0)},
      "B": {"name": "ivory_buff", "rgb": (235, 217, 153), "cmyk": (8, 15, 40, 0)},
      "C": {"name": "rainette_green", "rgb": (106, 147, 70), "cmyk": (42, 20, 62, 28)},
      "D": {"name": "benzol_green", "rgb": (0, 217, 115), "cmyk": (100, 15, 55, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC267": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "blue", "rgb": (13, 117, 255), "cmyk": (95, 54, 0, 0)},
      "B": {"name": "yellow_orange", "rgb": (255, 140, 0), "cmyk": (0, 45, 100, 0)},
      "C": {"name": "benzol_green", "rgb": (0, 217, 115), "cmyk": (100, 15, 55, 0)},
      "D": {"name": "cream_yellow", "rgb": (255, 82, 184), "cmyk": (0, 68, 28, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC268": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "deep_slate_olive", "rgb": (23, 39, 19), "cmyk": (76, 60, 80, 62)},
      "B": {"name": "light_brown_drab", "rgb": (176, 134, 153), "cmyk": (8, 30, 20, 25)},
      "C": {"name": "nile_blue", "rgb": (191, 255, 230), "cmyk": (25, 0, 10, 0)},
      "D": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC269": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "aconite_violet", "rgb": (156, 82, 242), "cmyk": (39, 68, 5, 0)},
      "B": {"name": "pale_burnt_lake", "rgb": (115, 15, 31), "cmyk": (25, 90, 80, 40)},
      "C": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)},
      "D": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC270": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)},
      "B": {"name": "eugenia_red", "rgb": (237, 61, 102), "cmyk": (7, 76, 60, 0)},
      "C": {"name": "olive_green", "rgb": (88, 119, 30), "cmyk": (56, 40, 85, 22)},
      "D": {"name": "cossack_green", "rgb": (50, 142, 19), "cmyk": (76, 32, 91, 18)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC271": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cobalt_green", "rgb": (148, 255, 148), "cmyk": (42, 0, 42, 0)},
      "B": {"name": "deep_slate_green", "rgb": (15, 38, 31), "cmyk": (80, 50, 60, 70)},
      "C": {"name": "pomegranate_purple", "rgb": (185, 0, 120), "cmyk": (23, 100, 50, 6)},
      "D": {"name": "green_blue", "rgb": (45, 188, 148), "cmyk": (82, 24, 40, 3)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC272": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "salvia_blue", "rgb": (150, 191, 230), "cmyk": (41, 25, 10, 0)},
      "B": {"name": "turquoise_green", "rgb": (181, 255, 194), "cmyk": (29, 0, 24, 0)},
      "C": {"name": "orange", "rgb": (255, 82, 0), "cmyk": (0, 68, 100, 0)},
      "D": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC273": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pansy_purple", "rgb": (111, 0, 67), "cmyk": (34, 100, 60, 34)},
      "B": {"name": "neutral_gray", "rgb": (181, 209, 204), "cmyk": (29, 18, 20, 0)},
      "C": {"name": "hermosa_pink", "rgb": (255, 178, 240), "cmyk": (0, 30, 6, 0)},
      "D": {"name": "sudan_brown", "rgb": (155, 83, 72), "cmyk": (25, 60, 65, 19)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC274": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dark_citrine", "rgb": (126, 135, 67), "cmyk": (38, 34, 67, 20)},
      "B": {"name": "light_mauve", "rgb": (145, 97, 242), "cmyk": (43, 62, 5, 0)},
      "C": {"name": "peach_red", "rgb": (255, 51, 25), "cmyk": (0, 80, 90, 0)},
      "D": {"name": "olympic_blue", "rgb": (79, 143, 230), "cmyk": (69, 44, 10, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC275": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "etruscan_red", "rgb": (201, 48, 62), "cmyk": (16, 80, 74, 6)},
      "B": {"name": "ecru", "rgb": (192, 180, 144), "cmyk": (20, 25, 40, 6)},
      "C": {"name": "madder_brown", "rgb": (101, 19, 0), "cmyk": (36, 88, 100, 38)},
      "D": {"name": "taupe_brown", "rgb": (107, 46, 99), "cmyk": (30, 70, 35, 40)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC276": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "seashell_pink", "rgb": (255, 207, 196), "cmyk": (0, 19, 23, 0)},
      "B": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)},
      "C": {"name": "eosine_pink", "rgb": (255, 94, 196), "cmyk": (0, 63, 23, 0)},
      "D": {"name": "yellow_green", "rgb": (166, 255, 71), "cmyk": (35, 0, 72, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC277": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "spinel_red", "rgb": (255, 77, 201), "cmyk": (0, 70, 21, 0)},
      "B": {"name": "dull_violet_black", "rgb": (0, 13, 79), "cmyk": (100, 90, 38, 50)},
      "C": {"name": "olive", "rgb": (113, 134, 0), "cmyk": (48, 38, 100, 15)},
      "D": {"name": "rosolanc_purple", "rgb": (178, 25, 171), "cmyk": (30, 90, 33, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC278": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "olive_ocher", "rgb": (209, 189, 51), "cmyk": (18, 26, 80, 0)},
      "B": {"name": "dusky_green", "rgb": (0, 89, 46), "cmyk": (100, 30, 64, 50)},
      "C": {"name": "cossack_green", "rgb": (50, 142, 19), "cmyk": (76, 32, 91, 18)},
      "D": {"name": "cream_yellow", "rgb": (255, 82, 184), "cmyk": (0, 68, 28, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC279": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)},
      "B": {"name": "dark_tyrian_blue", "rgb": (13, 43, 82), "cmyk": (90, 66, 36, 50)},
      "C": {"name": "vinaceous_cinnamon", "rgb": (245, 153, 148), "cmyk": (4, 40, 42, 0)},
      "D": {"name": "ecru", "rgb": (192, 180, 144), "cmyk": (20, 25, 40, 6)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC280": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "lincoln_green", "rgb": (64, 84, 22), "cmyk": (60, 48, 86, 37)},
      "B": {"name": "taupe_brown", "rgb": (107, 46, 99), "cmyk": (30, 70, 35, 40)},
      "C": {"name": "eugenia_red", "rgb": (237, 61, 102), "cmyk": (7, 76, 60, 0)},
      "D": {"name": "laelia_pink", "rgb": (204, 133, 209), "cmyk": (20, 48, 18, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC281": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "antwarp_blue", "rgb": (0, 138, 161), "cmyk": (100, 40, 30, 10)},
      "B": {"name": "benzol_green", "rgb": (0, 217, 115), "cmyk": (100, 15, 55, 0)},
      "C": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)},
      "D": {"name": "cobalt_green", "rgb": (148, 255, 148), "cmyk": (42, 0, 42, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC282": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "lilac", "rgb": (184, 117, 235), "cmyk": (28, 54, 8, 0)},
      "B": {"name": "maple", "rgb": (194, 151, 90), "cmyk": (5, 26, 56, 20)},
      "C": {"name": "cobalt_green", "rgb": (148, 255, 148), "cmyk": (42, 0, 42, 0)},
      "D": {"name": "eugenia_red", "rgb": (237, 61, 102), "cmyk": (7, 76, 60, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC283": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_burnt_lake", "rgb": (115, 15, 31), "cmyk": (25, 90, 80, 40)},
      "B": {"name": "chromium_green", "rgb": (102, 171, 86), "cmyk": (50, 16, 58, 20)},
      "C": {"name": "venice_green", "rgb": (107, 255, 178), "cmyk": (58, 0, 30, 0)},
      "D": {"name": "ocher_red", "rgb": (167, 55, 75), "cmyk": (18, 73, 63, 20)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC284": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "eugenia_red", "rgb": (237, 61, 102), "cmyk": (7, 76, 60, 0)},
      "B": {"name": "sea_green", "rgb": (51, 255, 125), "cmyk": (80, 0, 51, 0)},
      "C": {"name": "apricot_yellow", "rgb": (255, 230, 0), "cmyk": (0, 10, 100, 0)},
      "D": {"name": "dusky_green", "rgb": (0, 89, 46), "cmyk": (100, 30, 64, 50)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC285": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "light_brown_drab", "rgb": (176, 134, 153), "cmyk": (8, 30, 20, 25)},
      "B": {"name": "peach_red", "rgb": (255, 51, 25), "cmyk": (0, 80, 90, 0)},
      "C": {"name": "burnt_sienna", "rgb": (169, 52, 0), "cmyk": (22, 76, 100, 15)},
      "D": {"name": "turquoise_green", "rgb": (181, 255, 194), "cmyk": (29, 0, 24, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC286": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "orange_yellow", "rgb": (255, 171, 0), "cmyk": (0, 33, 100, 0)},
      "B": {"name": "peacock_blue", "rgb": (0, 207, 145), "cmyk": (100, 19, 43, 0)},
      "C": {"name": "burnt_sienna", "rgb": (169, 52, 0), "cmyk": (22, 76, 100, 15)},
      "D": {"name": "violet_blue", "rgb": (32, 45, 133), "cmyk": (85, 79, 38, 16)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC287": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_kings_blue", "rgb": (171, 245, 237), "cmyk": (33, 4, 7, 0)},
      "B": {"name": "eosine_pink", "rgb": (255, 94, 196), "cmyk": (0, 63, 23, 0)},
      "C": {"name": "pyrite_yellow", "rgb": (196, 191, 51), "cmyk": (23, 25, 80, 0)},
      "D": {"name": "calamine_blue", "rgb": (128, 255, 204), "cmyk": (50, 0, 20, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC288": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "yellow_orange", "rgb": (255, 140, 0), "cmyk": (0, 45, 100, 0)},
      "B": {"name": "taupe_brown", "rgb": (107, 46, 99), "cmyk": (30, 70, 35, 40)},
      "C": {"name": "sepia", "rgb": (80, 61, 0), "cmyk": (48, 60, 100, 40)},
      "D": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC289": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dull_violet_black", "rgb": (0, 13, 79), "cmyk": (100, 90, 38, 50)},
      "B": {"name": "lemon_yellow", "rgb": (242, 255, 38), "cmyk": (5, 0, 85, 0)},
      "C": {"name": "violet_blue", "rgb": (32, 45, 133), "cmyk": (85, 79, 38, 16)},
      "D": {"name": "light_green_yellow", "rgb": (189, 242, 38), "cmyk": (26, 5, 85, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC290": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "lincoln_green", "rgb": (64, 84, 22), "cmyk": (60, 48, 86, 37)},
      "B": {"name": "vistoris_lake", "rgb": (92, 44, 69), "cmyk": (40, 71, 55, 40)},
      "C": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)},
      "D": {"name": "cobalt_green", "rgb": (148, 255, 148), "cmyk": (42, 0, 42, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC291": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "calamine_blue", "rgb": (128, 255, 204), "cmyk": (50, 0, 20, 0)},
      "B": {"name": "cobalt_green", "rgb": (148, 255, 148), "cmyk": (42, 0, 42, 0)},
      "C": {"name": "sea_green", "rgb": (51, 255, 125), "cmyk": (80, 0, 51, 0)},
      "D": {"name": "light_green_yellow", "rgb": (189, 242, 38), "cmyk": (26, 5, 85, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC292": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)},
      "B": {"name": "ecru", "rgb": (192, 180, 144), "cmyk": (20, 25, 40, 6)},
      "C": {"name": "pinkish_cinnamon", "rgb": (242, 173, 120), "cmyk": (5, 32, 53, 0)},
      "D": {"name": "isabella_color", "rgb": (195, 165, 92), "cmyk": (15, 28, 60, 10)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC293": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)},
      "B": {"name": "turquoise_green", "rgb": (181, 255, 194), "cmyk": (29, 0, 24, 0)},
      "C": {"name": "artemisia_green", "rgb": (101, 169, 143), "cmyk": (57, 28, 39, 8)},
      "D": {"name": "green", "rgb": (64, 201, 69), "cmyk": (75, 21, 73, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC294": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cossack_green", "rgb": (50, 142, 19), "cmyk": (76, 32, 91, 18)},
      "B": {"name": "cream_yellow", "rgb": (255, 82, 184), "cmyk": (0, 68, 28, 0)},
      "C": {"name": "salvia_blue", "rgb": (150, 191, 230), "cmyk": (41, 25, 10, 0)},
      "D": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC295": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cream_yellow", "rgb": (255, 82, 184), "cmyk": (0, 68, 28, 0)},
      "B": {"name": "yellow", "rgb": (255, 255, 0), "cmyk": (0, 0, 100, 0)},
      "C": {"name": "dull_violet_black", "rgb": (0, 13, 79), "cmyk": (100, 90, 38, 50)},
      "D": {"name": "blue", "rgb": (13, 117, 255), "cmyk": (95, 54, 0, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC296": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pale_raw_umber", "rgb": (94, 64, 23), "cmyk": (46, 63, 87, 32)},
      "B": {"name": "ochraceous_salmon", "rgb": (217, 158, 115), "cmyk": (15, 38, 55, 0)},
      "C": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)},
      "D": {"name": "slate_color", "rgb": (27, 54, 68), "cmyk": (85, 70, 62, 30)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC297": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "burnt_sienna", "rgb": (169, 52, 0), "cmyk": (22, 76, 100, 15)},
      "B": {"name": "yellow_orange", "rgb": (255, 140, 0), "cmyk": (0, 45, 100, 0)},
      "C": {"name": "violet_blue", "rgb": (32, 45, 133), "cmyk": (85, 79, 38, 16)},
      "D": {"name": "olive_green", "rgb": (88, 119, 30), "cmyk": (56, 40, 85, 22)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC298": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "lemon_yellow", "rgb": (242, 255, 38), "cmyk": (5, 0, 85, 0)},
      "B": {"name": "peach_red", "rgb": (255, 51, 25), "cmyk": (0, 80, 90, 0)},
      "C": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)},
      "D": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC299": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "oil_green", "rgb": (110, 169, 0), "cmyk": (53, 28, 100, 8)},
      "B": {"name": "vinaceous_cinnamon", "rgb": (245, 153, 148), "cmyk": (4, 40, 42, 0)},
      "C": {"name": "antwarp_blue", "rgb": (0, 138, 161), "cmyk": (100, 40, 30, 10)},
      "D": {"name": "indian_lake", "rgb": (204, 26, 151), "cmyk": (12, 89, 35, 9)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC300": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "calamine_blue", "rgb": (128, 255, 204), "cmyk": (50, 0, 20, 0)},
      "B": {"name": "cream_yellow", "rgb": (255, 82, 184), "cmyk": (0, 68, 28, 0)},
      "C": {"name": "grenadine_pink", "rgb": (255, 97, 107), "cmyk": (0, 62, 58, 0)},
      "D": {"name": "turquoise_green", "rgb": (181, 255, 194), "cmyk": (29, 0, 24, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC301": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "spectrum_red", "rgb": (242, 0, 0), "cmyk": (5, 100, 100, 0)},
      "B": {"name": "ivory_buff", "rgb": (235, 217, 153), "cmyk": (8, 15, 40, 0)},
      "C": {"name": "aconite_violet", "rgb": (156, 82, 242), "cmyk": (39, 68, 5, 0)},
      "D": {"name": "rainette_green", "rgb": (106, 147, 70), "cmyk": (42, 20, 62, 28)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC302": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cream_yellow", "rgb": (255, 82, 184), "cmyk": (0, 68, 28, 0)},
      "B": {"name": "ecru", "rgb": (192, 180, 144), "cmyk": (20, 25, 40, 6)},
      "C": {"name": "antwarp_blue", "rgb": (0, 138, 161), "cmyk": (100, 40, 30, 10)},
      "D": {"name": "nile_blue", "rgb": (191, 255, 230), "cmyk": (25, 0, 10, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC303": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "naples_yellow", "rgb": (250, 237, 143), "cmyk": (2, 7, 44, 0)},
      "B": {"name": "peach_red", "rgb": (255, 51, 25), "cmyk": (0, 80, 90, 0)},
      "C": {"name": "neutral_gray", "rgb": (181, 209, 204), "cmyk": (29, 18, 20, 0)},
      "D": {"name": "deep_slate_olive", "rgb": (23, 39, 19), "cmyk": (76, 60, 80, 62)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC304": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "benzol_green", "rgb": (0, 217, 115), "cmyk": (100, 15, 55, 0)},
      "B": {"name": "cream_yellow", "rgb": (255, 82, 184), "cmyk": (0, 68, 28, 0)},
      "C": {"name": "dark_citrine", "rgb": (126, 135, 67), "cmyk": (38, 34, 67, 20)},
      "D": {"name": "hays_russet", "rgb": (104, 25, 22), "cmyk": (37, 85, 87, 35)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC305": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pinkish_cinnamon", "rgb": (242, 173, 120), "cmyk": (5, 32, 53, 0)},
      "B": {"name": "apricot_yellow", "rgb": (255, 230, 0), "cmyk": (0, 10, 100, 0)},
      "C": {"name": "turquoise_green", "rgb": (181, 255, 194), "cmyk": (29, 0, 24, 0)},
      "D": {"name": "citron_yellow", "rgb": (166, 212, 13), "cmyk": (35, 17, 95, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC306": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dull_viridian_green", "rgb": (25, 204, 51), "cmyk": (90, 20, 80, 0)},
      "B": {"name": "nile_blue", "rgb": (191, 255, 230), "cmyk": (25, 0, 10, 0)},
      "C": {"name": "benzol_green", "rgb": (0, 217, 115), "cmyk": (100, 15, 55, 0)},
      "D": {"name": "lemon_yellow", "rgb": (242, 255, 38), "cmyk": (5, 0, 85, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC307": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cotinga_purple", "rgb": (52, 0, 89), "cmyk": (66, 100, 42, 40)},
      "B": {"name": "grayish_lavender", "rgb": (184, 184, 255), "cmyk": (28, 28, 0, 0)},
      "C": {"name": "carmine", "rgb": (214, 0, 54), "cmyk": (0, 100, 75, 16)},
      "D": {"name": "aconite_violet", "rgb": (156, 82, 242), "cmyk": (39, 68, 5, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC308": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "english_red", "rgb": (222, 69, 0), "cmyk": (13, 73, 100, 0)},
      "B": {"name": "fawn", "rgb": (209, 176, 178), "cmyk": (18, 31, 30, 0)},
      "C": {"name": "cobalt_green", "rgb": (148, 255, 148), "cmyk": (42, 0, 42, 0)},
      "D": {"name": "scarlet", "rgb": (213, 12, 66), "cmyk": (10, 95, 72, 7)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC309": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "golden_yellow", "rgb": (250, 148, 66), "cmyk": (2, 42, 74, 0)},
      "B": {"name": "apricot_orange", "rgb": (255, 115, 64), "cmyk": (0, 55, 75, 0)},
      "C": {"name": "vandar_poels_blue", "rgb": (0, 62, 131), "cmyk": (100, 73, 43, 10)},
      "D": {"name": "violet_blue", "rgb": (32, 45, 133), "cmyk": (85, 79, 38, 16)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC310": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "olive", "rgb": (113, 134, 0), "cmyk": (48, 38, 100, 15)},
      "B": {"name": "pinkish_cinnamon", "rgb": (242, 173, 120), "cmyk": (5, 32, 53, 0)},
      "C": {"name": "deep_slate_olive", "rgb": (23, 39, 19), "cmyk": (76, 60, 80, 62)},
      "D": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC311": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pompeian_red", "rgb": (169, 6, 54), "cmyk": (18, 97, 74, 19)},
      "B": {"name": "dark_greenish_glaucous", "rgb": (178, 217, 163), "cmyk": (30, 15, 36, 0)},
      "C": {"name": "cream_yellow", "rgb": (255, 82, 184), "cmyk": (0, 68, 28, 0)},
      "D": {"name": "light_green_yellow", "rgb": (189, 242, 38), "cmyk": (26, 5, 85, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC312": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "burnt_sienna", "rgb": (169, 52, 0), "cmyk": (22, 76, 100, 15)},
      "B": {"name": "artemisia_green", "rgb": (101, 169, 143), "cmyk": (57, 28, 39, 8)},
      "C": {"name": "helvetia_blue", "rgb": (0, 87, 186), "cmyk": (100, 62, 19, 10)},
      "D": {"name": "yellow_orange", "rgb": (255, 140, 0), "cmyk": (0, 45, 100, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC313": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "carmine", "rgb": (214, 0, 54), "cmyk": (0, 100, 75, 16)},
      "B": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)},
      "C": {"name": "diamine_green", "rgb": (30, 184, 0), "cmyk": (87, 20, 100, 10)},
      "D": {"name": "yellow", "rgb": (255, 255, 0), "cmyk": (0, 0, 100, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC314": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "dusky_madder_violet", "rgb": (45, 0, 96), "cmyk": (75, 100, 46, 30)},
      "B": {"name": "deep_lyons_blue", "rgb": (0, 36, 204), "cmyk": (100, 85, 15, 6)},
      "C": {"name": "eosine_pink", "rgb": (255, 94, 196), "cmyk": (0, 63, 23, 0)},
      "D": {"name": "hays_russet", "rgb": (104, 25, 22), "cmyk": (37, 85, 87, 35)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC315": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "golden_yellow", "rgb": (250, 148, 66), "cmyk": (2, 42, 74, 0)},
      "B": {"name": "eupatorium_purple", "rgb": (191, 54, 224), "cmyk": (25, 79, 12, 0)},
      "C": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)},
      "D": {"name": "grenadine_pink", "rgb": (255, 97, 107), "cmyk": (0, 62, 58, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC316": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "red_violet", "rgb": (52, 0, 163), "cmyk": (76, 100, 25, 15)},
      "B": {"name": "vandyke_red", "rgb": (116, 9, 9), "cmyk": (32, 95, 95, 33)},
      "C": {"name": "dull_viridian_green", "rgb": (25, 204, 51), "cmyk": (90, 20, 80, 0)},
      "D": {"name": "violet", "rgb": (38, 25, 209), "cmyk": (85, 90, 18, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC317": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "turquoise_green", "rgb": (181, 255, 194), "cmyk": (29, 0, 24, 0)},
      "B": {"name": "light_pinkish_cinnamon", "rgb": (255, 191, 153), "cmyk": (0, 25, 40, 0)},
      "C": {"name": "lemon_yellow", "rgb": (242, 255, 38), "cmyk": (5, 0, 85, 0)},
      "D": {"name": "ecru", "rgb": (192, 180, 144), "cmyk": (20, 25, 40, 6)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC318": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "light_brownish_olive", "rgb": (112, 105, 52), "cmyk": (42, 46, 73, 24)},
      "B": {"name": "deep_slate_green", "rgb": (15, 38, 31), "cmyk": (80, 50, 60, 70)},
      "C": {"name": "dusky_green", "rgb": (0, 89, 46), "cmyk": (100, 30, 64, 50)},
      "D": {"name": "blackish_olive", "rgb": (50, 78, 42), "cmyk": (56, 32, 63, 55)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC319": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "apricot_yellow", "rgb": (255, 230, 0), "cmyk": (0, 10, 100, 0)},
      "B": {"name": "yellow_orange", "rgb": (255, 140, 0), "cmyk": (0, 45, 100, 0)},
      "C": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)},
      "D": {"name": "cossack_green", "rgb": (50, 142, 19), "cmyk": (76, 32, 91, 18)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC320": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "oil_green", "rgb": (110, 169, 0), "cmyk": (53, 28, 100, 8)},
      "B": {"name": "coral_red", "rgb": (255, 115, 153), "cmyk": (0, 55, 40, 0)},
      "C": {"name": "light_glaucous_blue", "rgb": (166, 230, 219), "cmyk": (35, 10, 14, 0)},
      "D": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC321": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)},
      "B": {"name": "salvia_blue", "rgb": (150, 191, 230), "cmyk": (41, 25, 10, 0)},
      "C": {"name": "light_brown_drab", "rgb": (176, 134, 153), "cmyk": (8, 30, 20, 25)},
      "D": {"name": "deep_slate_olive", "rgb": (23, 39, 19), "cmyk": (76, 60, 80, 62)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC322": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "blue_violet", "rgb": (71, 51, 255), "cmyk": (72, 80, 0, 0)},
      "B": {"name": "eupatorium_purple", "rgb": (191, 54, 224), "cmyk": (25, 79, 12, 0)},
      "C": {"name": "brick_red", "rgb": (163, 33, 0), "cmyk": (22, 84, 100, 18)},
      "D": {"name": "spectrum_red", "rgb": (242, 0, 0), "cmyk": (5, 100, 100, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC323": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cinnamon_buff", "rgb": (255, 191, 110), "cmyk": (0, 25, 57, 0)},
      "B": {"name": "citron_yellow", "rgb": (166, 212, 13), "cmyk": (35, 17, 95, 0)},
      "C": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)},
      "D": {"name": "madder_brown", "rgb": (101, 19, 0), "cmyk": (36, 88, 100, 38)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC324": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "pompeian_red", "rgb": (169, 6, 54), "cmyk": (18, 97, 74, 19)},
      "B": {"name": "aconite_violet", "rgb": (156, 82, 242), "cmyk": (39, 68, 5, 0)},
      "C": {"name": "olympic_blue", "rgb": (79, 143, 230), "cmyk": (69, 44, 10, 0)},
      "D": {"name": "neutral_gray", "rgb": (181, 209, 204), "cmyk": (29, 18, 20, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC325": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "deep_slate_green", "rgb": (15, 38, 31), "cmyk": (80, 50, 60, 70)},
      "B": {"name": "naples_yellow", "rgb": (250, 237, 143), "cmyk": (2, 7, 44, 0)},
      "C": {"name": "eugenia_red", "rgb": (237, 61, 102), "cmyk": (7, 76, 60, 0)},
      "D": {"name": "yellow_ocher", "rgb": (224, 184, 31), "cmyk": (12, 28, 88, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC326": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "night_green", "rgb": (122, 255, 0), "cmyk": (52, 0, 100, 0)},
      "B": {"name": "sulphur_yellow", "rgb": (245, 245, 184), "cmyk": (4, 4, 28, 0)},
      "C": {"name": "peach_red", "rgb": (255, 51, 25), "cmyk": (0, 80, 90, 0)},
      "D": {"name": "yellow_green", "rgb": (166, 255, 71), "cmyk": (35, 0, 72, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC327": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "ecru", "rgb": (192, 180, 144), "cmyk": (20, 25, 40, 6)},
      "B": {"name": "eosine_pink", "rgb": (255, 94, 196), "cmyk": (0, 63, 23, 0)},
      "C": {"name": "grayish_lavender", "rgb": (184, 184, 255), "cmyk": (28, 28, 0, 0)},
      "D": {"name": "raw_sienna", "rgb": (184, 94, 0), "cmyk": (18, 58, 100, 12)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC328": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "brick_red", "rgb": (163, 33, 0), "cmyk": (22, 84, 100, 18)},
      "B": {"name": "light_porcelain_green", "rgb": (35, 193, 124), "cmyk": (86, 22, 50, 3)},
      "C": {"name": "apricot_orange", "rgb": (255, 115, 64), "cmyk": (0, 55, 75, 0)},
      "D": {"name": "vandyke_brown", "rgb": (54, 35, 4), "cmyk": (56, 71, 97, 52)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC329": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "slate_color", "rgb": (27, 54, 68), "cmyk": (85, 70, 62, 30)},
      "B": {"name": "cream_yellow", "rgb": (255, 82, 184), "cmyk": (0, 68, 28, 0)},
      "C": {"name": "grayish_lavender", "rgb": (184, 184, 255), "cmyk": (28, 28, 0, 0)},
      "D": {"name": "cotinga_purple", "rgb": (52, 0, 89), "cmyk": (66, 100, 42, 40)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC330": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "nile_blue", "rgb": (191, 255, 230), "cmyk": (25, 0, 10, 0)},
      "B": {"name": "salvia_blue", "rgb": (150, 191, 230), "cmyk": (41, 25, 10, 0)},
      "C": {"name": "olive_buff", "rgb": (188, 211, 130), "cmyk": (16, 6, 42, 12)},
      "D": {"name": "green_blue", "rgb": (45, 188, 148), "cmyk": (82, 24, 40, 3)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC331": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "light_mauve", "rgb": (145, 97, 242), "cmyk": (43, 62, 5, 0)},
      "B": {"name": "violet", "rgb": (38, 25, 209), "cmyk": (85, 90, 18, 0)},
      "C": {"name": "indian_lake", "rgb": (204, 26, 151), "cmyk": (12, 89, 35, 9)},
      "D": {"name": "dull_violet_black", "rgb": (0, 13, 79), "cmyk": (100, 90, 38, 50)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC332": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "deep_slate_olive", "rgb": (23, 39, 19), "cmyk": (76, 60, 80, 62)},
      "B": {"name": "dusky_green", "rgb": (0, 89, 46), "cmyk": (100, 30, 64, 50)},
      "C": {"name": "coral_red", "rgb": (255, 115, 153), "cmyk": (0, 55, 40, 0)},
      "D": {"name": "scarlet", "rgb": (213, 12, 66), "cmyk": (10, 95, 72, 7)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC333": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cobalt_green", "rgb": (148, 255, 148), "cmyk": (42, 0, 42, 0)},
      "B": {"name": "lemon_yellow", "rgb": (242, 255, 38), "cmyk": (5, 0, 85, 0)},
      "C": {"name": "burnt_sienna", "rgb": (169, 52, 0), "cmyk": (22, 76, 100, 15)},
      "D": {"name": "blue", "rgb": (13, 117, 255), "cmyk": (95, 54, 0, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC334": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "olive", "rgb": (113, 134, 0), "cmyk": (48, 38, 100, 15)},
      "B": {"name": "antwarp_blue", "rgb": (0, 138, 161), "cmyk": (100, 40, 30, 10)},
      "C": {"name": "yellow_green", "rgb": (166, 255, 71), "cmyk": (35, 0, 72, 0)},
      "D": {"name": "seashell_pink", "rgb": (255, 207, 196), "cmyk": (0, 19, 23, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC335": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "vandyke_red", "rgb": (116, 9, 9), "cmyk": (32, 95, 95, 33)},
      "B": {"name": "slate_color", "rgb": (27, 54, 68), "cmyk": (85, 70, 62, 30)},
      "C": {"name": "yellow_orange", "rgb": (255, 140, 0), "cmyk": (0, 45, 100, 0)},
      "D": {"name": "violet", "rgb": (38, 25, 209), "cmyk": (85, 90, 18, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC336": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "hays_russet", "rgb": (104, 25, 22), "cmyk": (37, 85, 87, 35)},
      "B": {"name": "eosine_pink", "rgb": (255, 94, 196), "cmyk": (0, 63, 23, 0)},
      "C": {"name": "pale_lemon_yellow", "rgb": (255, 245, 158), "cmyk": (0, 4, 38, 0)},
      "D": {"name": "blackish_olive", "rgb": (50, 78, 42), "cmyk": (56, 32, 63, 55)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC337": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "vistoris_lake", "rgb": (92, 44, 69), "cmyk": (40, 71, 55, 40)},
      "B": {"name": "violet_carmine", "rgb": (83, 23, 69), "cmyk": (64, 90, 70, 10)},
      "C": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)},
      "D": {"name": "laelia_pink", "rgb": (204, 133, 209), "cmyk": (20, 48, 18, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC338": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "orange_yellow", "rgb": (255, 171, 0), "cmyk": (0, 33, 100, 0)},
      "B": {"name": "grayish_lavender", "rgb": (184, 184, 255), "cmyk": (28, 28, 0, 0)},
      "C": {"name": "dusky_green", "rgb": (0, 89, 46), "cmyk": (100, 30, 64, 50)},
      "D": {"name": "carmine_red", "rgb": (161, 11, 43), "cmyk": (25, 95, 80, 16)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC339": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "english_red", "rgb": (222, 69, 0), "cmyk": (13, 73, 100, 0)},
      "B": {"name": "ochraceous_salmon", "rgb": (217, 158, 115), "cmyk": (15, 38, 55, 0)},
      "C": {"name": "violet_blue", "rgb": (32, 45, 133), "cmyk": (85, 79, 38, 16)},
      "D": {"name": "light_glaucous_blue", "rgb": (166, 230, 219), "cmyk": (35, 10, 14, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC340": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "peach_red", "rgb": (255, 51, 25), "cmyk": (0, 80, 90, 0)},
      "B": {"name": "sea_green", "rgb": (51, 255, 125), "cmyk": (80, 0, 51, 0)},
      "C": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)},
      "D": {"name": "neutral_gray", "rgb": (181, 209, 204), "cmyk": (29, 18, 20, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC341": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cossack_green", "rgb": (50, 142, 19), "cmyk": (76, 32, 91, 18)},
      "B": {"name": "light_glaucous_blue", "rgb": (166, 230, 219), "cmyk": (35, 10, 14, 0)},
      "C": {"name": "deep_slate_olive", "rgb": (23, 39, 19), "cmyk": (76, 60, 80, 62)},
      "D": {"name": "grenadine_pink", "rgb": (255, 97, 107), "cmyk": (0, 62, 58, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC342": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "deep_slate_olive", "rgb": (23, 39, 19), "cmyk": (76, 60, 80, 62)},
      "B": {"name": "cream_yellow", "rgb": (255, 82, 184), "cmyk": (0, 68, 28, 0)},
      "C": {"name": "corinthian_pink", "rgb": (255, 166, 217), "cmyk": (0, 35, 15, 0)},
      "D": {"name": "orange_citrine", "rgb": (140, 101, 16), "cmyk": (28, 48, 92, 24)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC343": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "ivory_buff", "rgb": (235, 217, 153), "cmyk": (8, 15, 40, 0)},
      "B": {"name": "deep_grayish_olive", "rgb": (80, 84, 35), "cmyk": (50, 48, 78, 37)},
      "C": {"name": "vandar_poels_blue", "rgb": (0, 62, 131), "cmyk": (100, 73, 43, 10)},
      "D": {"name": "burnt_sienna", "rgb": (169, 52, 0), "cmyk": (22, 76, 100, 15)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC344": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "aconite_violet", "rgb": (156, 82, 242), "cmyk": (39, 68, 5, 0)},
      "B": {"name": "cinnamon_buff", "rgb": (255, 191, 110), "cmyk": (0, 25, 57, 0)},
      "C": {"name": "black", "rgb": (0, 0, 0), "cmyk": (20, 10, 15, 100)},
      "D": {"name": "deep_lyons_blue", "rgb": (0, 36, 204), "cmyk": (100, 85, 15, 6)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC345": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "blue_violet", "rgb": (71, 51, 255), "cmyk": (72, 80, 0, 0)},
      "B": {"name": "hays_russet", "rgb": (104, 25, 22), "cmyk": (37, 85, 87, 35)},
      "C": {"name": "nile_blue", "rgb": (191, 255, 230), "cmyk": (25, 0, 10, 0)},
      "D": {"name": "venice_green", "rgb": (107, 255, 178), "cmyk": (58, 0, 30, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC346": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "light_green_yellow", "rgb": (189, 242, 38), "cmyk": (26, 5, 85, 0)},
      "B": {"name": "rosolanc_purple", "rgb": (178, 25, 171), "cmyk": (30, 90, 33, 0)},
      "C": {"name": "andover_green", "rgb": (92, 138, 115), "cmyk": (60, 40, 50, 10)},
      "D": {"name": "turquoise_green", "rgb": (181, 255, 194), "cmyk": (29, 0, 24, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC347": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "sea_green", "rgb": (51, 255, 125), "cmyk": (80, 0, 51, 0)},
      "B": {"name": "helvetia_blue", "rgb": (0, 87, 186), "cmyk": (100, 62, 19, 10)},
      "C": {"name": "lilac", "rgb": (184, 117, 235), "cmyk": (28, 54, 8, 0)},
      "D": {"name": "olive_yellow", "rgb": (153, 178, 51), "cmyk": (40, 30, 80, 0)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  },

  "DCC348": {
    "source": "dictionary_of_color_combinations_vol1_2011",
    "colors": {
      "A": {"name": "cotinga_purple", "rgb": (52, 0, 89), "cmyk": (66, 100, 42, 40)},
      "B": {"name": "cossack_green", "rgb": (50, 142, 19), "cmyk": (76, 32, 91, 18)},
      "C": {"name": "deep_slate_olive", "rgb": (23, 39, 19), "cmyk": (76, 60, 80, 62)},
      "D": {"name": "olive_buff", "rgb": (188, 211, 130), "cmyk": (16, 6, 42, 12)}
    },
    "roles": {"dominant": "A", "secondary": ["B"], "accent": ["C", "D"]}
  }
}
