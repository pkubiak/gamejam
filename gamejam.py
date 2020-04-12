"""
GAMEJAM RULES:
    Base Time Limit: 3h
    Submitions: public github with screenshot, only own code allowed
    Last Wish: Each player can commment-out single "feature"
    Retry: If **all** contestants agree, we can once rerandom
    
    Score: 
      - 0pts for non runnable game 
      - voting 3/pts (each player, no self votes)
      - (-1pts) x breaking rules
      - Kaspair™ judge -> 3pts

    Awards: Pizza at the end free4all
"""

import sys
import random
import hashlib
from datetime import datetime

TODAY = datetime.today().strftime('%Y%m%d')

BASE_GAME = [
  #'Tetris', # DONE 20200314
  'Snake',
  'Boulder Dash',
  'Sokoban',
  'Zatacka / Achtung Die Kurve',
  'Asteroids',
  'Space Invaders', # https://codeheir.com/2019/03/17/how-to-code-space-invaders-1978-7/
  'Space shooter',
  'Donky Kong',
  'Pong', # https://codeheir.com/2019/02/04/how-to-code-pong-1972-1/
  'Pac-Man',
  'Frogger',
  'Breakout / WinBricks',
  'Tron',

  # by PK
  'Mario Kart / Lotus',
  'Board game',
  'Kret',
  'Dizzy / Platform',
  'Bejeweled'
  'Duck Hunt',
  'Blobby Valley',
  'Jumping T-Rex',
  'Flappy Bird',
  'Card game',
  'Puzzle Game / Arcade',
  'gra paragrafowa',
  'Tamagotchi',
  'Bloxorz',
  # '3D Maze', # DONE 20200201
  'Rougelike',
  'Minesweeper',
  'Tower Defense',
  'Text based',
  'Tetris Racing / Monaco GP',# https://youtu.be/ZRQXzOL4iOA
  'Memory',
  '2048',
  'Ships',
  'Dobble', # https://youtu.be/lhTMr8RzUr8
  'Gran Trak 10', # https://codeheir.com/2019/02/17/how-to-code-gran-trak-10-1974-3/
  'Jet Figter', # https://codeheir.com/2019/02/24/how-to-code-jet-fighter-1975-4/
  'Canyon Bomber', # https://codeheir.com/2019/03/10/how-to-code-canyon-bomber-1977-6/
  'Word Game (scrabble, Codename, Panśtwa-Miasta)',
  'Paper Soccer', 

  # by MC 
  'agar.io',
  'Kveiki',
  'Kulki',
  # 'Frozen Bubble', # DONE 20200321
  'Mamba',
  'Bomberman',
  'Tanks z boku',
  'Czołgi z góry',
  # 'Scotland Yard', # DONE 20200328
  
  'MC wybiera',
]


THEME = [
  'Cats',
  # 'Nature', # DONE 20200321
  'City',
  'Otter Space',
  'Ocean / underwater',
  'Cave',
  'Future SciFi',
  'Steampunk', 
  'Dinosaurs', 
  'Stealth', 
  'Time travel',
  'Zombies',
  

  'Inside A Computer',
  'Castle',
  'Alternate Reality',
  'Polska postapo',
  'Dungeons&Dragons',
  'Slavic Mythology',
  'Autostopem przez galaktykę',
  'Nuclear Throne',
  # 'Ecology / Recycling',  # DONE 20200328
  
  # p******e
  'kucyki i jednorożce / tęcza',
  'Anime Anibe Anikukuryku',
  'Jesteś całką',
  # 'Bimbrownia', # DONE 20200314
  # 'Kraków', # DONE 20200201
  'Animizacja (jesteś przedmiotem)',
  'Cząstki elementarne',
  'Pierwsza Wojna Światowa',
  'Coronavirus',
] + ['Happy Easter']*(4**9 if '0409' <= TODAY[4:] <= '0416' else 0)


MUTATIONS = [
  # positive mutations
  'puszka pepsi dla każdego (from PK)',
  
  # time mutations
  [
    '+42 min',
    '+1 hour',
    '+2 hour',
    '-1/2 hour',
  ],

  # visual mutation
  [
    'text mode',
    'monochromatic',
    '16 colors',
    'unicode',
    'emoji',
    'low resolution (<4kPx)',
    'vector',
    '3D',
    'hexy',
    'isometric',
  ],

  # gameplay
  [
    'AI player',
    '2 players',
    '2+ players',
    'CPU vs CPU',
    'online multiplayer',
    'co-op',
  ],

  # sound
  [
    '8bit-sound',
    'sound-based (sound is essential for gameplay)',
    'sound-in-bg',
  ],

  # controls
  [
    'no-keyboard',
    'one-key',
    'no-hands (in game)',
    'game-require-pressing-at-least-5-keys-at-once',
  ],

  # technology 
  [
    'no-js',
    'no-python',
    'mobile',
    'scratch',
  ],

  # game mechanics
  'proceduraly generated',
  'side quests',
  'secret-codes (as in lotus)',
  'user-content (e.g. user can defined levels)',
  'game-require-interaction-with-real-life',
  'hero-building',
  'word-building',
  'achievements',
  'highscore-table',
  'game-require-paper-and-pencil',
  'map-based',
  'in-game-programming',
  
  # other
  [
    'opengameart.org assets',
    'handcrafted assets',
    'game-of-one-asset',
  ],

  '13kB (gziped)',

  # hardcore
  'code-without-w',  # by MC
  'no internet (after start)',  # by GŻ
  'unit-tests',  # by MC
  # 'pair-coding',

  # yokers
  [
    'yoker', 'yoker',  # can rerandom if anyone wants
    'wybuchający kotek'  # must rerandom
  ],
]


def sample_mutations(count=3):
  """Sample `count` different mutations but only one from each group."""
  mutations = []
  for gid, group in enumerate(MUTATIONS):
    if isinstance(group, str):
      group = (group,)
    for name in group:
      mutations.append((name, gid))

  idxs, gidxs = set(), set()

  while len(idxs) < count:
    idx = random.randint(0, len(mutations)-1)
    name, gidx = mutations[idx]

    if (idx in idxs) or (gidx in gidxs):
      continue

    idxs.add(idx)
    gidxs.add(gidx)

    yield name


def sample_game(seed):
  seed = hashlib.sha512(str(seed).encode('utf-8')).digest()
  random.seed(seed)

  return (
    random.choice(BASE_GAME),
    random.choice(THEME),
    list(sample_mutations(count=3))
  )


if __name__ == '__main__':
  base_game, theme, mutations = sample_game([TODAY] + sys.argv[1:])

  print(__doc__)

  print(f"BASE GAME:\n    {base_game}\n")

  print(f"THEME:\n    {theme}\n")

  print('MUTATIONS:')
  for mutation in mutations:
    print(f"    {mutation}")


