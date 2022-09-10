import pygame as pg
import sys
from setting import *
from player import Player
import math
from map import world_map
from ray_casting import ray_casting
pg.init()
pg.display.set_caption("3d")
screen = pg.display.set_mode((1200,800))
clock = pg.time.Clock()

sky = pg.Rect(0, 0, 1200, 400)
floor = pg.Rect(0, 400, 1200, 400)

player = Player()

play = True
while play:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    # screen.fill((0,0,0))
    pg.draw.rect(screen, (0, 0, 150), sky)
    pg.draw.rect(screen, (0, 100, 0), floor)
    last_pos = player.pos
    player.update()

    if ray_casting(screen,player.pos,player.angle):
        player.x = last_pos[0]
        player.y = last_pos[1]



    pg.draw.rect(screen, (40, 40, 40), (0, 0, WIDTH//5, HEIGHT//5))
    pg.draw.circle(screen, (0, 220, 0), (player.x // 5, player.y // 5), 2)
    pg.draw.line(screen, (0, 220, 0), (player.x // 5, player.y // 5),
                 (player.x // 5 + WIDTH // 5 * math.cos(player.angle),
                  player.y // 5 + HEIGHT // 5 * math.sin(player.angle)))
    for x,y in world_map:
        pg.draw.rect(screen,(250,250,250),(x//5,y//5,TILE//5,TILE//5),2)


    pg.display.update()
    clock.tick(FPS)




