
# GPU Tiers: 1=Intel UHD/Iris, 2=GTX 1050/RX 560, 3=GTX 1660/RX 5600, 4=RTX 3070/RX 6800, 5=RTX 4090/RX 7900XTX
# CPU Tiers: 1=Dual-core <2GHz, 2=i3/Ryzen 3 budget, 3=i5/Ryzen 5 mid, 4=i7/Ryzen 7, 5=i9/Ryzen 9/Threadripper

GAMES = [
  {
    "id": "cyberpunk2077",
    "name": "Cyberpunk 2077",
    "genre": "RPG",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Cyberpunk+2077",
    "release_year": 2020,
    "platform": [
      "PC"
    ],
    "min": {
      "ram_gb": 8,
      "gpu_tier": 2,
      "cpu_tier": 3,
      "storage_gb": 70,
      "os": [
        "Windows 10"
      ]
    },
    "recommended": {
      "ram_gb": 16,
      "gpu_tier": 4,
      "cpu_tier": 4,
      "storage_gb": 70,
      "os": [
        "Windows 10",
        "Windows 11"
      ]
    }
  },
  {
    "id": "eldenring",
    "name": "Elden Ring",
    "genre": "Action RPG",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Elden+Ring",
    "release_year": 2022,
    "platform": [
      "PC"
    ],
    "min": {
      "ram_gb": 12,
      "gpu_tier": 3,
      "cpu_tier": 3,
      "storage_gb": 60,
      "os": [
        "Windows 10",
        "Windows 11"
      ]
    },
    "recommended": {
      "ram_gb": 16,
      "gpu_tier": 4,
      "cpu_tier": 4,
      "storage_gb": 60,
      "os": [
        "Windows 10",
        "Windows 11"
      ]
    }
  },
  {
    "id": "gtav",
    "name": "GTA V",
    "genre": "Open World",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=GTA+V",
    "release_year": 2015,
    "platform": [
      "PC"
    ],
    "min": {
      "ram_gb": 4,
      "gpu_tier": 2,
      "cpu_tier": 2,
      "storage_gb": 72,
      "os": [
        "Windows 10"
      ]
    },
    "recommended": {
      "ram_gb": 8,
      "gpu_tier": 3,
      "cpu_tier": 3,
      "storage_gb": 72,
      "os": [
        "Windows 10",
        "Windows 11"
      ]
    }
  },
  {
    "id": "rdr2",
    "name": "Red Dead Redemption 2",
    "genre": "Open World",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Red+Dead+Redemption+2",
    "release_year": 2019,
    "platform": [
      "PC"
    ],
    "min": {
      "ram_gb": 8,
      "gpu_tier": 3,
      "cpu_tier": 3,
      "storage_gb": 150,
      "os": [
        "Windows 10"
      ]
    },
    "recommended": {
      "ram_gb": 16,
      "gpu_tier": 4,
      "cpu_tier": 4,
      "storage_gb": 150,
      "os": [
        "Windows 10",
        "Windows 11"
      ]
    }
  },
  {
    "id": "msfs2020",
    "name": "Microsoft Flight Simulator",
    "genre": "Simulation",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Microsoft+Flight+Simulator",
    "release_year": 2020,
    "platform": [
      "PC"
    ],
    "min": {
      "ram_gb": 8,
      "gpu_tier": 3,
      "cpu_tier": 3,
      "storage_gb": 150,
      "os": [
        "Windows 10"
      ]
    },
    "recommended": {
      "ram_gb": 32,
      "gpu_tier": 5,
      "cpu_tier": 5,
      "storage_gb": 150,
      "os": [
        "Windows 10",
        "Windows 11"
      ]
    }
  },
  {
    "id": "hogwartslegacy",
    "name": "Hogwarts Legacy",
    "genre": "Action RPG",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Hogwarts+Legacy",
    "release_year": 2023,
    "platform": [
      "PC"
    ],
    "min": {
      "ram_gb": 8,
      "gpu_tier": 3,
      "cpu_tier": 3,
      "storage_gb": 85,
      "os": [
        "Windows 10"
      ]
    },
    "recommended": {
      "ram_gb": 16,
      "gpu_tier": 4,
      "cpu_tier": 4,
      "storage_gb": 85,
      "os": [
        "Windows 10",
        "Windows 11"
      ]
    }
  },
  {
    "id": "valorant",
    "name": "Valorant",
    "genre": "FPS",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Valorant",
    "release_year": 2020,
    "platform": [
      "PC"
    ],
    "min": {
      "ram_gb": 4,
      "gpu_tier": 1,
      "cpu_tier": 2,
      "storage_gb": 8,
      "os": [
        "Windows 7",
        "Windows 8",
        "Windows 10"
      ]
    },
    "recommended": {
      "ram_gb": 8,
      "gpu_tier": 3,
      "cpu_tier": 3,
      "storage_gb": 8,
      "os": [
        "Windows 10",
        "Windows 11"
      ]
    }
  },
  {
    "id": "fortnite",
    "name": "Fortnite",
    "genre": "Battle Royale",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Fortnite",
    "release_year": 2017,
    "platform": [
      "PC"
    ],
    "min": {
      "ram_gb": 8,
      "gpu_tier": 2,
      "cpu_tier": 3,
      "storage_gb": 29,
      "os": [
        "Windows 10"
      ]
    },
    "recommended": {
      "ram_gb": 16,
      "gpu_tier": 4,
      "cpu_tier": 4,
      "storage_gb": 29,
      "os": [
        "Windows 10",
        "Windows 11"
      ]
    }
  },
  {
    "id": "minecraft",
    "name": "Minecraft",
    "genre": "Sandbox",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Minecraft",
    "release_year": 2011,
    "platform": [
      "PC"
    ],
    "min": {
      "ram_gb": 4,
      "gpu_tier": 1,
      "cpu_tier": 2,
      "storage_gb": 4,
      "os": [
        "Windows 10"
      ]
    },
    "recommended": {
      "ram_gb": 8,
      "gpu_tier": 3,
      "cpu_tier": 3,
      "storage_gb": 4,
      "os": [
        "Windows 10",
        "Windows 11"
      ]
    }
  },
  {
    "id": "cs2",
    "name": "Counter-Strike 2",
    "genre": "FPS",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Counter-Strike+2",
    "release_year": 2023,
    "platform": [
      "PC"
    ],
    "min": {
      "ram_gb": 4,
      "gpu_tier": 2,
      "cpu_tier": 2,
      "storage_gb": 15,
      "os": [
        "Windows 10"
      ]
    },
    "recommended": {
      "ram_gb": 8,
      "gpu_tier": 3,
      "cpu_tier": 3,
      "storage_gb": 15,
      "os": [
        "Windows 10",
        "Windows 11"
      ]
    }
  },
  {
    "id": "rocketleague",
    "name": "Rocket League",
    "genre": "Sports",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Rocket+League",
    "release_year": 2015,
    "platform": [
      "PC"
    ],
    "min": {
      "ram_gb": 4,
      "gpu_tier": 1,
      "cpu_tier": 2,
      "storage_gb": 20,
      "os": [
        "Windows 7",
        "Windows 8",
        "Windows 10"
      ]
    },
    "recommended": {
      "ram_gb": 8,
      "gpu_tier": 3,
      "cpu_tier": 3,
      "storage_gb": 20,
      "os": [
        "Windows 10",
        "Windows 11"
      ]
    }
  },
  {
    "id": "witcher3",
    "name": "The Witcher 3",
    "genre": "RPG",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=The+Witcher+3",
    "release_year": 2015,
    "platform": [
      "PC"
    ],
    "min": {
      "ram_gb": 6,
      "gpu_tier": 2,
      "cpu_tier": 2,
      "storage_gb": 35,
      "os": [
        "Windows 7",
        "Windows 10"
      ]
    },
    "recommended": {
      "ram_gb": 8,
      "gpu_tier": 3,
      "cpu_tier": 3,
      "storage_gb": 35,
      "os": [
        "Windows 10",
        "Windows 11"
      ]
    }
  },
  {
    "id": "cyberpunkphantom",
    "name": "Cyberpunk 2077: Phantom Liberty",
    "genre": "DLC/RPG",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Cyberpunk+2077:+Phantom+Liberty",
    "release_year": 2023,
    "platform": [
      "PC"
    ],
    "min": {
      "ram_gb": 8,
      "gpu_tier": 3,
      "cpu_tier": 3,
      "storage_gb": 70,
      "os": [
        "Windows 10"
      ]
    },
    "recommended": {
      "ram_gb": 16,
      "gpu_tier": 5,
      "cpu_tier": 5,
      "storage_gb": 70,
      "os": [
        "Windows 10",
        "Windows 11"
      ]
    }
  },
  {
    "id": "stardewvalley",
    "name": "Stardew Valley",
    "genre": "Simulation",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Stardew+Valley",
    "release_year": 2016,
    "platform": [
      "PC"
    ],
    "min": {
      "ram_gb": 2,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 2,
      "os": [
        "Windows XP",
        "Windows 10"
      ]
    },
    "recommended": {
      "ram_gb": 4,
      "gpu_tier": 1,
      "cpu_tier": 2,
      "storage_gb": 2,
      "os": [
        "Windows 10",
        "Windows 11"
      ]
    }
  },
  {
    "id": "among_us",
    "name": "Among Us",
    "genre": "Party",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Among+Us",
    "release_year": 2018,
    "platform": [
      "PC"
    ],
    "min": {
      "ram_gb": 1,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 1,
      "os": [
        "Windows 7",
        "Windows 10"
      ]
    },
    "recommended": {
      "ram_gb": 2,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 1,
      "os": [
        "Windows 10",
        "Windows 11"
      ]
    }
  },
  {
    "id": "pubgmobile",
    "name": "PUBG Mobile",
    "genre": "Battle Royale",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=PUBG+Mobile",
    "release_year": 2018,
    "platform": [
      "Mobile"
    ],
    "min": {
      "ram_gb": 2,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 4,
      "os": [
        "Android 5.1",
        "iOS 11"
      ]
    },
    "recommended": {
      "ram_gb": 4,
      "gpu_tier": 2,
      "cpu_tier": 2,
      "storage_gb": 8,
      "os": [
        "Android 8",
        "iOS 13"
      ]
    }
  },
  {
    "id": "coc",
    "name": "Clash of Clans",
    "genre": "Strategy",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Clash+of+Clans",
    "release_year": 2012,
    "platform": [
      "Mobile"
    ],
    "min": {
      "ram_gb": 1,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 1,
      "os": [
        "Android 5",
        "iOS 9"
      ]
    },
    "recommended": {
      "ram_gb": 2,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 2,
      "os": [
        "Android 8",
        "iOS 12"
      ]
    }
  },
  {
    "id": "freefire",
    "name": "Free Fire",
    "genre": "Battle Royale",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Free+Fire",
    "release_year": 2017,
    "platform": [
      "Mobile"
    ],
    "min": {
      "ram_gb": 2,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 2,
      "os": [
        "Android 4.1",
        "iOS 11"
      ]
    },
    "recommended": {
      "ram_gb": 3,
      "gpu_tier": 1,
      "cpu_tier": 2,
      "storage_gb": 4,
      "os": [
        "Android 8",
        "iOS 12"
      ]
    }
  },
  {
    "id": "bgmi",
    "name": "Battlegrounds Mobile India",
    "genre": "Battle Royale",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Battlegrounds+Mobile+India",
    "release_year": 2021,
    "platform": [
      "Mobile"
    ],
    "min": {
      "ram_gb": 2,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 4,
      "os": [
        "Android 5.1",
        "iOS 11"
      ]
    },
    "recommended": {
      "ram_gb": 4,
      "gpu_tier": 2,
      "cpu_tier": 2,
      "storage_gb": 8,
      "os": [
        "Android 8",
        "iOS 13"
      ]
    }
  },
  {
    "id": "codmobile",
    "name": "Call of Duty Mobile",
    "genre": "FPS",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Call+of+Duty+Mobile",
    "release_year": 2019,
    "platform": [
      "Mobile"
    ],
    "min": {
      "ram_gb": 2,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 3,
      "os": [
        "Android 5.1",
        "iOS 9"
      ]
    },
    "recommended": {
      "ram_gb": 4,
      "gpu_tier": 2,
      "cpu_tier": 2,
      "storage_gb": 6,
      "os": [
        "Android 8",
        "iOS 13"
      ]
    }
  },
  {
    "id": "ge\u043d\u0448\u0438\u043d",
    "name": "Genshin Impact",
    "genre": "Action RPG",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Genshin+Impact",
    "release_year": 2020,
    "platform": [
      "Mobile"
    ],
    "min": {
      "ram_gb": 3,
      "gpu_tier": 1,
      "cpu_tier": 2,
      "storage_gb": 30,
      "os": [
        "Android 8",
        "iOS 12"
      ]
    },
    "recommended": {
      "ram_gb": 4,
      "gpu_tier": 2,
      "cpu_tier": 2,
      "storage_gb": 30,
      "os": [
        "Android 9",
        "iOS 14"
      ]
    }
  },
  {
    "id": "mobilelegends",
    "name": "Mobile Legends",
    "genre": "MOBA",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Mobile+Legends",
    "release_year": 2016,
    "platform": [
      "Mobile"
    ],
    "min": {
      "ram_gb": 1,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 1,
      "os": [
        "Android 4.1",
        "iOS 8"
      ]
    },
    "recommended": {
      "ram_gb": 2,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 2,
      "os": [
        "Android 7",
        "iOS 11"
      ]
    }
  },
  {
    "id": "brawlstars",
    "name": "Brawl Stars",
    "genre": "Action",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Brawl+Stars",
    "release_year": 2018,
    "platform": [
      "Mobile"
    ],
    "min": {
      "ram_gb": 1,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 1,
      "os": [
        "Android 5",
        "iOS 13"
      ]
    },
    "recommended": {
      "ram_gb": 2,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 2,
      "os": [
        "Android 8",
        "iOS 13"
      ]
    }
  },
  {
    "id": "asphalt9",
    "name": "Asphalt 9 Legends",
    "genre": "Racing",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Asphalt+9+Legends",
    "release_year": 2018,
    "platform": [
      "Mobile"
    ],
    "min": {
      "ram_gb": 2,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 2,
      "os": [
        "Android 5",
        "iOS 11"
      ]
    },
    "recommended": {
      "ram_gb": 3,
      "gpu_tier": 2,
      "cpu_tier": 2,
      "storage_gb": 4,
      "os": [
        "Android 8",
        "iOS 13"
      ]
    }
  },
  {
    "id": "honkaistarrail",
    "name": "Honkai Star Rail",
    "genre": "RPG",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Honkai+Star+Rail",
    "release_year": 2023,
    "platform": [
      "Mobile"
    ],
    "min": {
      "ram_gb": 3,
      "gpu_tier": 1,
      "cpu_tier": 2,
      "storage_gb": 15,
      "os": [
        "Android 8",
        "iOS 12"
      ]
    },
    "recommended": {
      "ram_gb": 6,
      "gpu_tier": 2,
      "cpu_tier": 2,
      "storage_gb": 20,
      "os": [
        "Android 10",
        "iOS 14"
      ]
    }
  },
  {
    "id": "minecraftpe",
    "name": "Minecraft Pocket Edition",
    "genre": "Sandbox",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Minecraft+Pocket+Edition",
    "release_year": 2011,
    "platform": [
      "Mobile"
    ],
    "min": {
      "ram_gb": 1,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 1,
      "os": [
        "Android 5",
        "iOS 13"
      ]
    },
    "recommended": {
      "ram_gb": 2,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 2,
      "os": [
        "Android 8",
        "iOS 14"
      ]
    }
  },
  {
    "id": "clashroyal",
    "name": "Clash Royale",
    "genre": "Strategy",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Clash+Royale",
    "release_year": 2016,
    "platform": [
      "Mobile"
    ],
    "min": {
      "ram_gb": 1,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 1,
      "os": [
        "Android 5",
        "iOS 9"
      ]
    },
    "recommended": {
      "ram_gb": 2,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 1,
      "os": [
        "Android 7",
        "iOS 12"
      ]
    }
  },
  {
    "id": "roblox_mobile",
    "name": "Roblox",
    "genre": "Sandbox",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Roblox",
    "release_year": 2006,
    "platform": [
      "Mobile"
    ],
    "min": {
      "ram_gb": 1,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 1,
      "os": [
        "Android 5",
        "iOS 13"
      ]
    },
    "recommended": {
      "ram_gb": 2,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 2,
      "os": [
        "Android 7",
        "iOS 14"
      ]
    }
  },
  {
    "id": "subway_surfers",
    "name": "Subway Surfers",
    "genre": "Endless Runner",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Subway+Surfers",
    "release_year": 2012,
    "platform": [
      "Mobile"
    ],
    "min": {
      "ram_gb": 1,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 1,
      "os": [
        "Android 4.1",
        "iOS 12"
      ]
    },
    "recommended": {
      "ram_gb": 1,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 1,
      "os": [
        "Android 7",
        "iOS 13"
      ]
    }
  },
  {
    "id": "candycrush",
    "name": "Candy Crush Saga",
    "genre": "Puzzle",
    "image_url": "https://placehold.co/600x400/0D0D0D/00FF9C?text=Candy+Crush+Saga",
    "release_year": 2012,
    "platform": [
      "Mobile"
    ],
    "min": {
      "ram_gb": 1,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 1,
      "os": [
        "Android 4",
        "iOS 12"
      ]
    },
    "recommended": {
      "ram_gb": 1,
      "gpu_tier": 1,
      "cpu_tier": 1,
      "storage_gb": 1,
      "os": [
        "Android 6",
        "iOS 12"
      ]
    }
  }
]
