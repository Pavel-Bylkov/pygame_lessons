import pygame as pg

from arcade.color import *
import sys  # модуль для выхода из игры и закрытия всех окон

pg.init()  # используется для старта модуля pygame
pg.display.set_caption("Pygame")  # задание заголовка окну
screen = pg.display.set_mode((800, 600), pg.RESIZABLE)  # создание поверхности с указанными размерами и параметрами
clock = pg.time.Clock()  # создаем экземпляр класса для управление времени(кадрами игры (fps))

play = True

FPS = 60

# pg.display.flip() - обновление всего экрана
while play:  # основной цикл игры

    for event in pg.event.get():  # отслеживание всех событий которые происходят на игровом дисплее
        print(event)
        if event.type == pg.QUIT:  # если тип события = нажатию на крестик
            sys.exit()  # функция выхода из игры и закрытия всех окон

    screen.fill(DARK_GREEN)

    print(screen.get_size(), screen.get_width(), screen.get_height())
    pg.display.update()  # - обновление части экрана, но если аргумент не указан, то обновляется весь

    clock.tick(FPS)  # устанавливаем максимальное указанное количество кадров


"""

"""