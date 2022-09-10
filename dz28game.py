"""Создать дисплей и на нём с помощью модуля pygame.draw_
нарисовать картинку из геометрических фигур. Создать округлую
зелёную  землю с помощью арки. С помощью прямоугольника и
треугольника нарисовать дом. Добавьте окружность для создания
солнца и окон домов. Лучики и перегородки окон можно сделать
 с помощью линий """

def ex1():
    import pygame as pg
    import sys

    pg.init()
    pg.display.set_caption("House")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    BROWN = (139, 69, 19)
    YELLOW = (249, 232, 20)
    YELLOW2 = (249, 224, 112)
    BARNRED = (124, 10, 2)
    BLACK = (0, 0, 0)
    rect1 = pg.Rect(-100, 465, 1000, 500)
    rect2 = pg.Rect(250, 350, 300, 200)

    play = True

    while play:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        screen.fill(BLUE)

        pg.draw.arc(screen, GREEN, rect1, 0, 3.14, 300)
        pg.draw.rect(screen, BROWN, rect2)
        pg.draw.circle(screen, YELLOW, (700, 100), 80)
        pg.draw.line(screen, YELLOW, (620, 100), (525, 120), 2)
        pg.draw.line(screen, YELLOW, (670, 140), (575, 235), 2)
        pg.draw.line(screen, YELLOW, (690, 150), (670, 270), 2)
        pg.draw.line(screen, YELLOW, (730, 145), (760, 270), 2)
        pg.draw.line(screen, YELLOW, (650, 120), (560, 170), 2)
        pg.draw.line(screen, YELLOW, (630, 70), (525, 74), 2)
        pg.draw.circle(screen, YELLOW2, (350, 440), 30)
        pg.draw.circle(screen, YELLOW2, (450, 440), 30)
        pg.draw.line(screen, BLACK, (350, 410), (350, 470), 2)
        pg.draw.line(screen, BLACK, (450, 410), (450, 470), 2)
        pg.draw.line(screen, BLACK, (320, 440), (380, 440), 2)
        pg.draw.line(screen, BLACK, (420, 440), (480, 440), 2)
        pg.draw.polygon(screen, BARNRED, [[200, 355], [400, 240], [600, 355]])
        pg.display.update()
        clock.tick(60)

# ex1()

"""
Написать функцию, принимающую два значения x и y, которая 
заполняет две диагонали экрaна кругами выбранного цвета, 
на каждому круге отрисовать глаза и улыбку.
"""

def ex2():
    import pygame as pg
    import sys

    pg.init()
    pg.display.set_caption("Smile")
    HEIGHT = 800
    WIDTH = 800
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()

    BLUE = (0, 0, 255)
    YELLOW = (249, 232, 20)
    BLACK = (0, 0, 0)

    def smile(x, y, radius):
        pg.draw.circle(screen, YELLOW, (x, y), radius)
        pg.draw.arc(screen, BLACK,
                    (x - radius//2, y + radius//3, radius, radius//2), 3.14, 6.28, 2)
        pg.draw.circle(screen, BLACK, (x - radius//4, y - radius//4), radius//10)
        pg.draw.circle(screen, BLACK, (x + radius//4, y - radius//4), radius//10)

    def print_smile(radius):
        for row in range(HEIGHT//radius-1):
            for col in range(WIDTH//radius-1):
                if row == col or WIDTH//radius-2 == row + col:
                    smile(col*radius+radius, row*radius+radius, radius//1.5)

    play = True

    while play:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

        screen.fill(BLUE)

        print_smile(50)
        pg.display.update()
        clock.tick(60)

ex2()