def ex1():
    import pymunk.pygame_util
    import pygame as pg
    import sys
    import random

    pymunk.pygame_util.positive_y_is_up = False  # отключает положительный рост y в низ

    pg.init()  # используется для старта модуля pygame
    pg.display.set_caption("Animation")  # задание загаловка окну
    screen = pg.display.set_mode((800, 600), pg.RESIZABLE)  # создание поверхности с
                                                    # указанными размерами и параметрами
    clock = pg.time.Clock()  # создаем экземпляр класса для управление времени((fps))
    draw_option = pymunk.pygame_util.DrawOptions(screen)

    space = pymunk.Space()
    space.gravity = 0, 2000

    def get_random_color():
        return (random.randint(0, 255), random.randint(0, 255),
                random.randint(0, 255), 0)

    class PhysicBall:
        def __init__(self, position, mass, radius, color,
                     elasticity=0.8, friction=0.5):
            self.mass = mass  # создание массы шарика
            self.radius = radius  # создание радиуса
            self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
            self.body = pymunk.Body(self.mass, self.moment)
            self.body.position = position
            self.shape = pymunk.Circle(self.body, self.radius)
            self.shape.elasticity = elasticity
            self.shape.friction = friction
            self.shape.color = color

    class PhysicRect:
        def __init__(self, position, mass, size, color,
                     elasticity=0.5, friction=0.8):
            self.mass = mass
            self.size = size
            self.moment = pymunk.moment_for_box(self.mass, self.size)
            self.body = pymunk.Body(self.mass, self.moment)
            self.body.position = position
            self.shape = pymunk.Poly.create_box(self.body, self.size)
            self.shape.elasticity = elasticity
            self.shape.friction = friction
            self.shape.color = color

    class PhysicSegment:
        def __init__(self, start_point, end_point, radius,
                     friction=0.7, elasticity=0.8):
            self.shape = pymunk.Segment(space.static_body, start_point, end_point, radius)
            self.shape.friction = friction
            self.shape.elasticity = elasticity

    class PhysicPlatform:
        def __init__(self, speed, start_point, end_point, radius,
                     friction=0.5, elasticity=0.8):
            self.speed = speed
            self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
            self.shape = pymunk.Segment(self.body, start_point, end_point, radius)
            self.shape.body.velocity = (self.speed, 0)
            self.shape.friction = friction
            self.shape.elasticity = elasticity
            self.n = 0

        def change_direction(self):
            self.speed *= -1
            self.shape.body.velocity = (self.speed, 0)

        def update(self):
            self.n += 1
            if self.n == 300:
                self.change_direction()
                self.n = 0

    def spawn_ball(pos):
        ball = PhysicBall(position=pos, mass=50, radius=50, color=get_random_color())
        space.add(ball.body, ball.shape)

    segment = PhysicSegment(start_point=(0,600), end_point=(800,600), radius=15)
    space.add(segment.shape)

    for col in range(720, 40, -62):
        for row in range(530, 220, -42):
            box = PhysicRect(position=(col, row), mass=10, size=(60, 40),
                             color=get_random_color())
            space.add(box.body, box.shape)

    line = PhysicPlatform(speed=100, start_point=(0, 200), end_point=(300, 200), radius=5)
    space.add(line.body, line.shape)


    play = True
    while play:#основной цикл игры
        for event in pg.event.get():#отслеживание всех событий которые происходят на игровом дисплее
            if event.type == pg.QUIT:#если тип события = нажатию на крестик
                sys.exit()#функция выхода из игры и закрытия всех окон(
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    spawn_ball(event.pos)

        screen.fill((0, 0, 0))

        space.step(1 / 60)
        line.update()
        space.debug_draw(draw_option)

        pg.display.update()
        clock.tick(60)

# ex1()

def ex2():
    import pymunk.pygame_util
    import pygame as pg
    import sys
    import random

    pymunk.pygame_util.positive_y_is_up = False

    pg.init()  # используется для старта модуля pygame
    pg.display.set_caption("Animation")  # задание загаловка окну
    screen = pg.display.set_mode((800, 600), pg.RESIZABLE)  # создание поверхности с указанными размерами и параметрами
    clock = pg.time.Clock()  # создаем экземпляр класса для управление времени(кадрами игры (fps))

    space = pymunk.Space()
    space.gravity = 0, 2000

    def get_random_color():
        return (random.randint(0, 255), random.randint(0, 255),
                random.randint(0, 255))

    class IPhysicSprite:
        """Interface for PhysicSprites
        - must be implement self.draw() and self.update()"""

        def draw(self, *args, **kwargs):
            pass

        def update(self, *args, **kwargs):
            pass

    class PhysicSpriteGroup(list):
        def append(self, sprite):
            if isinstance(sprite, IPhysicSprite):
                super().append(sprite)
            else:
                raise TypeError("Type must be is PhysicSprite")

        def draw(self, *args, **kwargs):
            for sprite in self:
                sprite.draw(*args, **kwargs)

        def update(self, *args, **kwargs):
            for sprite in self:
                sprite.update(*args, **kwargs)

    class PhysicBall(IPhysicSprite):
        def __init__(self, position, mass, radius, color,
                     elasticity=0.8, friction=0.5):
            self.mass = mass  # создание массы шарика
            self.radius = radius  # создание радиуса
            self.moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
            self.body = pymunk.Body(self.mass, self.moment)
            self.body.position = position
            self.shape = pymunk.Circle(self.body, self.radius)
            self.shape.elasticity = elasticity
            self.shape.friction = friction
            self.shape.color = color

        def draw(self, win):
            pg.draw.circle(win, color=self.shape.color,
                           center=self.body.position, radius=self.radius)

    class PhysicRect(IPhysicSprite):
        def __init__(self, position, mass, size, color,
                     elasticity=0.5, friction=0.8):
            self.mass = mass
            self.size = size
            self.moment = pymunk.moment_for_box(self.mass, self.size)
            self.body = pymunk.Body(self.mass, self.moment)
            self.body.position = position
            self.shape = pymunk.Poly.create_box(self.body, self.size)
            self.shape.elasticity = elasticity
            self.shape.friction = friction
            self.shape.color = color
            self.rect = pg.Rect(*position, *size)
            self.rect.center = position

        def draw(self, win):
            pg.draw.rect(win, color=self.shape.color, rect=self.rect)

        def update(self):
            self.rect.center = self.body.position

    class PhysicSegment(IPhysicSprite):
        def __init__(self, start_point, end_point, radius, color,
                     friction=0.7, elasticity=0.8):
            self.start_point = start_point
            self.end_point = end_point
            self.width = radius * 2
            self.shape = pymunk.Segment(space.static_body, start_point, end_point, radius)
            self.shape.friction = friction
            self.shape.elasticity = elasticity
            self.shape.color = color

        def draw(self, win):
            pg.draw.line(win, color=self.shape.color, start_pos=self.start_point,
                         end_pos=self.end_point, width=self.width)

    class PhysicPlatform(IPhysicSprite):
        def __init__(self, speed, position, size, color,
                     friction=0.5, elasticity=0.8):
            self.speed = speed
            self.size = size
            self.body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
            self.body.position = position
            self.shape = pymunk.Poly.create_box(self.body, self.size)
            self.shape.body.velocity = (self.speed, 0)
            self.shape.friction = friction
            self.shape.elasticity = elasticity
            self.shape.color = color
            self.n = 0
            self.rect = pg.Rect(*position, *size)
            self.rect.center = position

        def change_direction(self):
            self.speed *= -1
            self.shape.body.velocity = (self.speed, 0)

        def update(self):
            self.n += 1
            if self.n == 300:
                self.change_direction()
                self.n = 0
            self.rect.center = self.body.position

        def draw(self, win):
            pg.draw.rect(win, color=self.shape.color, rect=self.rect)

    def spawn_ball(pos):
        ball = PhysicBall(position=pos, mass=50, radius=50, color=get_random_color())
        space.add(ball.body, ball.shape)
        sprites.append(ball)

    sprites = PhysicSpriteGroup()
    segment = PhysicSegment(start_point=(0, 600), end_point=(800, 600), radius=15,
                            color=get_random_color())
    space.add(segment.shape)
    sprites.append(segment)

    for col in range(720, 40, -62):
        for row in range(530, 220, -42):
            box = PhysicRect(position=(col, row), mass=10, size=(60, 40),
                             color=get_random_color())
            space.add(box.body, box.shape)
            sprites.append(box)

    line = PhysicPlatform(speed=100, position=(100, 200), size=(300, 15),
                          color=get_random_color())
    space.add(line.body, line.shape)
    sprites.append(line)

    play = True
    while play:  # основной цикл игры
        for event in pg.event.get():  # отслеживание всех событий которые происходят на игровом дисплее
            if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                sys.exit()  # функция выхода из игры и закрытия всех окон(
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    spawn_ball(event.pos)

        screen.fill((0, 0, 0))

        space.step(1 / 60)

        sprites.update()
        sprites.draw(screen)

        pg.display.update()
        clock.tick(60)

# ex2()

def ex3():
    fruts = {"apple": 5, "bannan": 4, "grape": 3}
    for number, frut in enumerate(fruts, 1):
        print(number, frut, fruts[frut])
    number = 1
    for frut in fruts:
        print(number, frut, fruts[frut])
        number += 1

ex3()

"""
pymunk.pygame_util.positive_y_is_up = False -отключает положительный рост y в низ

draw_option = pymunk.pygame_util.DrawOptions(screen)
-указываем pymunk где отрисовывать объекты

space = pymunk.Space() -создание пространства

space.gravity= 0,2000 -создание параметров гравитации

pymunk.moment_for_circle(#масса мяча,#внутренний радиус,#радиус мяча)
-создание момента иннерции у мячика

pymunk.Body(#масса,#момент иннерции) -создание физического тела

pymunk.Circle(#физическое тело мяча,#радиус мяча)
#форма_тела.elasticity = 0.8 -упругость тела
#форма_тела.friction = 0.5 -трение тела
#форма_тела.color = (r,g,b,a) -задание цвета фигуре

space.add(ball_body,ball_shape) -добавление тела в пространство

segment_shape = pymunk.Segment(#физичекоетело,#точка старта,#точка конца,
    #(толищина или радуис)
    -создание статического тела

box_moment = pymunk.moment_for_box(#масса прямоугольника,#размер прямоугольника)
-создание момента иннерции у прямоугольника

box_shape = pymunk.Poly.create_box(#тело прямоуг,#размеры прямоуг)
-создание формы прямоугольника

line_body = pymunk.Body(#тип тела) -создание кинематического тела
line_shape.body.velocity = (#изменение по x,#изменение по у) -задание направления
"""