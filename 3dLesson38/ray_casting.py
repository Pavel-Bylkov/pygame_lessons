import pygame as pg
from setting import *
from map import world_map


class Cache:
    _sin = {}
    _cos = {}

    @classmethod
    def cos(cls, angle):
        if angle not in cls._cos:
            cls._cos[angle] = math.cos(angle)
        return cls._cos[angle]

    @classmethod
    def sin(cls, angle):
        if angle not in cls._sin:
            cls._sin[angle] = math.sin(angle)
        return cls._sin[angle]

def ray_casting(screen,player_pos,player_angle):
    cur_angle = player_angle - HALF_FOV
    x0, y0 = player_pos
    for ray in range(NUM_RAYS):
        sin_a = Cache.sin(cur_angle)
        cos_a = Cache.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = x0+depth*cos_a
            y = y0+depth*sin_a
            #pg.draw.line(screen,(70,70,70),(x0,y0),(x,y),2)
            if (x//TILE * TILE,y//TILE * TILE) in world_map:
                depth *=Cache.cos((player_angle-cur_angle))
                try:
                    proj_height = PROJ_COEF/depth
                except Exception as e:
                    print(e)
                    break
                c = 255/(1+depth*depth*0.00001)
                color = (c,c,c)
                pg.draw.rect(screen,color,(ray*SCALE,HALF_HEIGHT - proj_height//2,SCALE,proj_height))
                break
        cur_angle += DELTA_ANGLE
    return False
