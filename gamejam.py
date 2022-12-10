"""
GAMEJAM RULES:
    Base Time Limit: 3h
    To participate you must star gamejam repo on github
    Submitions: public github repo, only own code allowed
    Retry: If **all** contestants agree, we can once rerandom
    
    Score: 
      - 0pts for non runnable game (user interactions, possible win)
      - voting 3/pts (each player, no self votes)
      - (+1pts) x (theme and each mutation)
      - +1pts for readme with screenshot

"""

import sys
import random
import hashlib
from datetime import datetime

TODAY = datetime.today().strftime('%Y%m%d')

BASE_GAME = [
  #'Tetris', # DONE 20200314
  ('Snake', 'https://youtu.be/i7PCbZmZlwM'),
  ('Boulder Dash', 'https://youtu.be/mLQzL8vsNVM'),
  ('Sokoban', 'https://youtu.be/yZNxZDVemWY'),
  ('Zatacka / Achtung Die Kurve', 'https://youtu.be/865R57w5hmk'),
  ('Asteroids', 'https://youtu.be/WYSupJ5r2zo'),
  ('Space Invaders', 'https://youtu.be/MU4psw3ccUI', 'https://codeheir.com/2019/03/17/how-to-code-space-invaders-1978-7/'),
  ('Space shooter', 'https://youtu.be/tKobl50jrLk'),
  ('Pong', 'https://youtu.be/fiShX2pTz9A', 'https://codeheir.com/2019/02/04/how-to-code-pong-1972-1/'),
  # 'Pac-Man',  # DONE 20200614
  ('Frogger', 'https://youtu.be/WNrz9_Fe-Us'),
  # 'Breakout / WinBricks',  # DONE 20200503
  ('Tron', 'https://youtu.be/1zv333wxZFU'),

  # by PK
  ('Lotus Turbo', 'https://youtu.be/oLQiwjGrEjE', 'https://youtu.be/vAf0whWrXt4'),
  'Board game',
  # 'Kret',
  # 'Dizzy / Platform',
  ('Bejeweled', 'https://youtu.be/PZZp8m_jcdo'),
  ('Duck Hunt', 'https://youtu.be/vbypwNjNcVI'),
  ('Blobby Valley', 'https://youtu.be/clhuvirGeHY'),
  ('Jumping T-Rex', 'https://youtu.be/yj1TuVetVgQ'),
  # 'Flappy Bird',  # DONE 20200413
  'Card game',
  'Puzzle Game / Arcade',
  ('Gra paragrafowa', 'https://youtu.be/m-OjuPHDOEo'),
  ('Tamagotchi', 'https://youtu.be/h3pMVCYM_EM'),
  # 'Bloxorz',
  # '3D Maze', # DONE 20200201
  ('Rougelike', 'https://youtu.be/tjGT-sRdiUk', 'https://youtu.be/vxF1osPkplA'),
  ('Minesweeper', 'https://youtu.be/GrZCWx0fnfc'),
  ('Tower Defense', 'https://youtu.be/dZ56Y2FYYU0'),
  ('Text based', 'https://youtu.be/D9qrZC7WUio', 'https://youtu.be/u8X6TiJA8as'),
  ('Tetris Racing / Monaco GP', 'https://youtu.be/ZRQXzOL4iOA', 'https://codeheir.com/2019/03/31/how-to-code-monaco-gp-1979-8/'),
  ('Memory', 'https://youtu.be/EpTWD-pplMo', 'https://youtu.be/dqqxkrKhfS4'),
  ('2048', 'https://youtu.be/7w-KZ5Pcc2E'),
  ('Battleships', 'https://youtu.be/k4kc_rqsP5I', 'https://youtu.be/MgJBgnsDcF0'),
  'Dobble', # https://youtu.be/lhTMr8RzUr8
  ('Gran Trak 10', 'https://youtu.be/RuPEoLkVwtI', 'https://codeheir.com/2019/02/17/how-to-code-gran-trak-10-1974-3/'),
  ('Jet Fighter', 'https://youtu.be/MMObEpsy7Eg', 'https://codeheir.com/2019/02/24/how-to-code-jet-fighter-1975-4/'),
  ('Canyon Bomber', 'https://youtu.be/u4b48yoIRkg', 'https://codeheir.com/2019/03/10/how-to-code-canyon-bomber-1977-6/'),
  ('Hangman', 'https://youtu.be/boVXrxx5RYQ', 'https://youtu.be/ynwB-QfOPRw'),
  'Word Game', # eg. scrabble, Codename, Panśtwa-Miasta, Hangman
  'Paper & Pencil', # https://en.wikipedia.org/wiki/Category:Paper-and-pencil_games
  # 'pinball', # DONE 20221206
  ('Falling ball', 'https://youtu.be/FxfmSIsoHXU'),
  ('Whack a mole', 'https://youtu.be/RKekuvkWrOQ?t=24'),
  'Tic Tac Toe',
  ('Helicopter', 'https://youtu.be/Jpy0PEy9NQI'),
  'Puzzles',
  ('Billard', 'https://youtu.be/0BR8whlSz1U'),
  ('Connect Four', 'https://youtu.be/3R1Cx6uGjMw'),
  ('Fruit Ninja', 'https://youtu.be/COFeh96bfWI'),
  ('Typespeed', 'https://youtu.be/SRVV3Y7WjOo'),
  ('Pipe Dream', 'https://youtu.be/DkV8PqlMwNc'),
  ('GeoGuessr', 'https://youtu.be/EACQkecWsww'),
  ('Gold Sprinter', 'https://youtu.be/X7UkwUvUxZE'),
  ('Battle Painters', 'https://youtu.be/fk0uHjdhQw8'),
  ('Who Wants to Be a Millionaire?', 'https://youtu.be/3hExsR6qmQM'),
  ('Fishy', 'https://youtu.be/6TaIXdGgPwI'),
  ("Rodent's Revenge", 'https://youtu.be/lEQtboM2R1w'),
  ('Bierki / Pick-up sticks', 'https://youtu.be/EpTWD-pplMo?t=262'),
  ('Knucklebones', 'https://youtu.be/EpTWD-pplMo?t=197', 'https://youtu.be/P8zx2UfcP1E'),
  ('Skifree', 'https://youtu.be/Tr_xvHMR6P0', 'https://youtu.be/STfkwi2ZGIg'),

  # by MC 
  ('agar.io', 'https://youtu.be/hgsy1Lzg5UU'),
  ('Kveiki', 'https://github.com/marek-ciazynski/kveiki'),
  ('Kulki', 'https://youtu.be/NM31opSsH7I'),
  # 'Frozen Bubble', # DONE 20200321
  ('Mamba', 'https://youtu.be/NCpGDv0ljes'),
  ('Bomberman', 'https://youtu.be/CZ9Pu9Usk5o'),
  ('Scorched Earth ', 'https://youtu.be/nDw_mpjKlpg'),
  ('Tanks', 'https://youtu.be/fe3oO3zMWWk'),
  # 'Scotland Yard', # DONE 20200328
  
  # 'MC wybiera', # DONE 20201004
  'PC wybiera',
  # 'Pac-Man', # DONE 20200614
  # 'Nuclear Throne', # DONE 20201025
  'Open topic',
]


THEME = [
  'Cats',
  # 'Nature', # DONE 20200321
  'City',
  'Otter Space',
  # 'Ocean / underwater',  # DONE 20200614
  'Cave / underground',  # DONE 20201025
  'Future SciFi',
  'Steampunk', 
  'Dinosaurs', 
  'Stealth', 
  'Time travel',
  'Zombies',
  'Food',
  'Fantasy',
    
  'Inside A Computer',
  'Castle',
  # 'Alternate Reality',# DONE 20200503
  # 'Polska postapo', # DONE 20201004
  'Dungeons&Dragons',
  'Slavic Mythology',
  'Autostopem przez galaktykę',
  # 'Ecology / Recycling',  # DONE 20200328
  'Wojna klanów',
  'Pokemons',
  'Farm / Countryside',
  'Cyberpunk',
  
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
] + \
['Happy Easter'] * (4**9 if '0409' <= TODAY[4:] <= '0416' else 0) + \
['Santa Claus'] * (4**9 if '1205' <= TODAY[4:] <= '1207' else 0) + \
["New Year's Eve"] * (4**9 if TODAY[4:] == '1231' else 0)


MUTATIONS = [
  # positive mutations
  #'puszka pepsi dla każdego (from PK)',
  
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
    'raycasting',
    'non-euclidean',
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
  #[
  #  'no-js',
  #  'no-python',
  #  'mobile',
  #  'scratch',
  #  'powerpoint',  # by PK: https://itch.io/jam/powerpoint-game-jam
  #  'brython',
  #],

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
  'game-require-paper-and-pencil', # e.g. you must take notes or draw map to complete game
  'map-based',
  'in-game-programming',
  'motyw-edukacyjny',
    
  # other
  [
    'opengameart.org assets',
    'handcrafted assets',
    'game-of-one-asset',
  ],

  '13kB (gziped)',

  # hardcore
  [
  #  'code-without-w',  # by MC
  #  'no internet (after start)',  # by GŻ
    'unit-tests',  # by MC
  #  'pair-coding',  # via VS LiveShare
  ],
    
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

  if isinstance(base_game, tuple):
        base_game = f"{base_game[0]} ({base_game[1]})"
    
  print(f"BASE GAME:\n    {base_game}\n")

  print(f"THEME:\n    {theme}\n")

  print('MUTATIONS:')
  for mutation in mutations:
    print(f"    - {mutation}")


