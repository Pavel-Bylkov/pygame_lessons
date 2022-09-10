from setting import *

text_map = [
    "WWWWWWWWWWWWWWWWWWWWWWWW",
    "W......................W",
    "W......................W",
    "W......................W",
    "W....W...........WWW...W",
    "W....WWW. .............W",
    "W.WW...................W",
    "W.WW....WWWWWWWWWW.....W",
    "W.........WWWWWW.......W",
    "W......................W",
    "W......................W",
    "W......................W",
    "W......................W",
    "WWWWWWWWWWWWWWWWWWWWWWWW",
]

world_map = set()
for j,row in enumerate(text_map):
    for i,symbol in enumerate(row):
        if symbol == "W":
            world_map.add((i*TILE, j*TILE))
