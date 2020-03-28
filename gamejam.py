import sys
import random
import hashlib
from datetime import datetime


BASE_GAME = [
    #'Tetris', # DONE 20200314
    'Snake',
    'Boulder Dash',
    'Sokoban',
    'Zatacka / Achtung Die Kurve',
    'Asteroids',
    'Space Invaders',
    'Space shooter',
    'Donky Kong',
    'Pong',
    'Pac-Man',
    'Frogger',
    'Breakout / WinBricks',
    'Tron',

    # by PK
    'Mario Kart / Lotus',
    'Board game',
    'Kret',
    'Dizzy',
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

    # by MC 
    'agar.io',
    'Kveiki',
    'Kulki',
    # 'Frozen Bubble', # DONE 20200321
    'Mamba',
    'Bomberman',
    'Tanks z boku',
    'Czołgi z góry',
    'Scotland Yard',
    
    'MC wybiera',
]


THEME = [
    'Cats',
    # 'Nature', # DONE 20200321
    'City',
    'Otter Space',
    'Ocean / underwater',
    'Cave',

    'Inside A Computer',
    'Castle',
    'Alternate Reality',
    'Polska postapo',
    'D&D',
    'Slavic Mythology',
    'Autostopem przez galaktykę',
    'Nuclear Throne',
    'Ecology / Recycling',
    
    # p******e
    'kucyki i jednorożce / tęcza',
    'Anime Anibe Anikukuryku',
    'Jesteś całką',
    # 'Bimbrownia', # DONE 20200314
    # 'Kraków', # DONE 20200201
    'Animizacja (jestes przedmiotem)',
    'Cząstki elementarne',
    'Pierwsza Wojna Światowa',
    'Coronavirus',
]


MUTATIONS = [
    # positive mutations
    'puszka pepsi dla każdego (from PK)',
    
    # time mutations
    '+42 min',
    '+1 hour',
    '+2 hour',
    '-1/2 hour',

    # visual mutation
    'text mode',
    'monochromatic',
    '16 colors',
    'unicode',
    'emoji',
    'low resolution (<4kPx)',
    'vector',
    '3D',
    'hexy',

    # gameplay
    'AI player',
    '2 players',
    '2+ players',
    'CPU vs CPU',
    'online multiplayer',

    # sound
    '8bit-sound',
    'sound-based',
    'sound-in-bg',

    # controls
    'no-keyboard',
    'one-key',
    'no-hands (in game)',
    
    # technology 
    'no-js',
    'no-python',
    'mobile',
    'scratch',
    
    # game mechanics
    'proceduraly generated',
    'side quest',
    'secret-codes (as in lotus)',
    'user-input (e.g. user can defined levels)',
    'linked-with-real-life',
    'hero-building',
    'achievements',
    'highscore-table',
    'game-require-pressing-at-least-5-keys-at-once',
    'game-require-paper-and-pencil',
    'map-based',
    'in-game-programming',
    
    # other
    'opengameart.org assets',
    'handcrafted assets',
    '13kB (gziped)',

    # hardcore
    'code-without-w',  # by MC
    'no internet (after start)',  # by GŻ
    # 'pair-coding',

    # yokers
    'yoker', 'yoker',  # can rerandom if anyone wants
    'wybuchający kotek'  # must rerandom
]


if __name__ == '__main__':
    seed_str = str([datetime.today().strftime('%Y%m%d')] + sys.argv[1:])

    seed = hashlib.sha512(seed_str.encode('utf-8')).digest()
    random.seed(seed)
    
    print("""RULES:
    Base Time Limit: 3h
    Submitions: public github, only own code allowed, with screenshot
    Last Wish: Each player can commment-out single "feature"
    Retry: If **all** contestants agree, we can once rerandom
    
    Score: 
        - 0pts for non runnable game 
        - voting 3/pts (each player, no self votes),
        - (-1pts) x breaking rules
        - Kaspair™ judge -> 3pts

    Awards: Pizza at the end free4all
    """)

    print('BASE GAME:\n   ', random.choice(BASE_GAME), "\n")
    
    print('THEME:\n   ', random.choice(THEME), "\n")

    idx = set()
    while len(idx) < 3:
        idx.add(random.randint(0, len(MUTATIONS)-1))

    print('MUTATIONS:')
    for mutation in sorted(idx):
        print(f"    {MUTATIONS[mutation]}")

