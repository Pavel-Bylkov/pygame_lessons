
def ex1():
    import pygame as pg
    import sys
    WIDTH = 800
    HEIGHT = 600
    pg.init()
    pg.display.set_caption("Geometry")
    screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
    clock = pg.time.Clock()

    r1 = pg.Rect(100, 100, 100, 100)
    countrow = 0
    countcol = 0

    play = True
    while play:
        for event in pg.event.get():  # отслеживание всех событий которые происходят на игровом дисплее
            if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                sys.exit()  # функция выхода из игры и закрытия всех окон
        while countrow < WIDTH:
            while countcol < HEIGHT:
                pg.draw.circle(screen, (255, 0, 0), (countrow + 25, countcol + 25), 25)
                countcol += 25
                countrow += 50
        pg.display.update()

# ex1()

def ex2():
    import random

    import pygame as pg
    import sys
    WIDTH = 800
    HEIGHT = 600
    pg.init()
    pg.display.set_caption("Geometry")
    screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
    clock = pg.time.Clock()

    def draw_tree(x, y):
        pg.draw.polygon(screen, (0, 255, 0), [[x, y], [x - 25, y + 50], [x + 25, y + 50]])
        pg.draw.polygon(screen, (0, 255, 0), [[x, y + 50], [x - 50, y + 100], [x + 50, y + 100]])
        pg.draw.rect(screen, (115, 66, 34), (x - 20, y + 175, 40, 100))
        pg.draw.polygon(screen, (0, 255, 0), [[x, y + 100], [x - 75, y + 175], [x + 75, y + 175]])

    for i in range(15):
        draw_tree(random.randint(50, 750), random.randint(0, 400))
    pg.display.update()
    play = True
    while play:
        for event in pg.event.get():  # отслеживание всех событий которые происходят на игровом дисплее
            if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                sys.exit()  # функция выхода из игры и закрытия всех окон

# ex2()


def ex3():
    import pygame as pg
    import sys
    pg.init()
    pg.display.set_caption("Geometry")
    screen = pg.display.set_mode((800, 600), pg.RESIZABLE)

    WHITE = (255, 255, 255)

    r1 = pg.Rect(0, 200, 800, 50)  # объект класса Rect
    # pg.draw.rect(screen,WHITE,r1,0,30,10,20,50,70)

    pg.draw.circle(screen, (255, 0, 0), (400, 300), 50, 15)

    pg.draw.line(screen, color=(0, 255, 0), start_pos=(0, 200), end_pos=(800, 205), width=5)

    pg.draw.aaline(screen, (0, 255, 0), (0, 196), (800, 202))

    # pg.draw.lines(screen,(0,0,255),True,[[0,0],[150,150],[200,450],[700,100]],10)

    # pg.draw.ellipse(screen,(180,30,200),(200,200,100,300),60)

    pg.draw.arc(screen, (180, 30, 200), r1, 0, 3.14, 10)

    pg.draw.polygon(screen, (0, 0, 255), [[0, 0], [150, 150], [200, 450], [700, 100]])
    pg.draw.aalines(screen, (0, 0, 255), True, [[0, 0], [150, 150], [200, 450], [700, 100]])

    pg.display.update()

    play = True
    while play:
        for event in pg.event.get():  # отслеживание всех событий которые происходят на игровом дисплее
            if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                sys.exit()  # функция выхода из игры и закрытия всех окон

# ex3()

"""
pg.draw.rect(#поверхность,
    #цвет,#объект класса Rect,
    ##ширина границ, 
    ##общее закругление, 
    ##закругление верхнего левого угла,
    ##верхнего правого,##нижний левый,##нижний правый)

pg.draw.circle(#поверхность,#цвет,
    #кортежиз координат центра, #радиус,##ширина границ)

pg.draw.line(#поверхность,#цвет,#кортеж из координат точки старта, 
    #кортеж из координат точки конца,#ширина)

pg.draw.aaline(#поверхность,#цвет,#кортеж из координат точки старта, 
    #кортеж из координат точки конца)

pg.draw.lines(#поверхность,#цвет,#замкнутость(bool), 
    #список из списков из точек ломанной линии,#ширина)

pg.draw.aalines(#поверхность,#цвет,#замкнутость(bool), 
    #список из списков из точек ломанной линии)

pg.draw.ellipse(#поверхность,#цвет,#объект класса Rect, 
    ##ширина границ)

pg.draw.arc(#поверхность,#цвет,#объект класса Rect,
    #начальный угол в радианах, 
    #конечный угол в радианах,##ширина границ)

pg.draw.polygon(#поверхность,#цвет,
    #список из списков из точек ломанной линии,##ширина границ)
"""