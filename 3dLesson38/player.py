from setting import *
import pygame as pg
import math
class Player:
    def __init__(self):
        self.x,self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def update(self):
        keys = pg.key.get_pressed()
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        if keys[pg.K_w]:
            self.x += player_speed*cos_a
            self.y += player_speed*sin_a
            print("w")
        if keys[pg.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
            print("s")
        if keys[pg.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
            print("d")
        if keys[pg.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
            print("a")
        if keys[pg.K_LEFT]:
            self.angle -= 0.02
        if keys[pg.K_RIGHT]:
            self.angle += 0.02