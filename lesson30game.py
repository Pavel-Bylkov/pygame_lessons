def ex1():
    import pygame as pg
    import sys  # модуль для выхода из игры и закрытия всех окон
    from random import randint

    pg.init()  # используется для старта модуля pygame
    pg.display.set_caption("Collision")  # задание загаловка окну
    screen = pg.display.set_mode((800, 600), pg.RESIZABLE)  # создание поверхности с указанными размерами и параметрами
    clock = pg.time.Clock()  # создаем экземпляр класса для управление времени(кадрами игры (fps))

    r1 = pg.Rect(50, 300, 50, 50)
    r2 = pg.Rect(700, 300, 50, 50)

    def move(keys, r1):
        global DIRECTION
        if keys[pg.K_LEFT]:
            r1.centerx -= 5  # обращение к точке элемента объекта класса
        if keys[pg.K_UP]:
            r1.centery -= 5
        if keys[pg.K_DOWN]:
            r1.centery += 5
        if keys[pg.K_RIGHT]:
            r1.centerx += 5

    rect_list = []
    for i in range(10):
        a = pg.Rect(randint(25, 775), randint(25, 575), 50, 50)
        rect_list.append(a)
    play = True
    # pg.display.flip() - обновление всего экрана
    while play:  # основной цикл игры
        for event in pg.event.get():  # отслеживание всех событий которые происходят на игровом дисплее
            if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                sys.exit()  # функция выхода из игры и закрытия всех окон(
        screen.fill((20, 50, 40))
        keys = pg.key.get_pressed()
        move(keys, r1)
        pg.draw.rect(screen, (155, 200, 150), r1)
        # pg.draw.rect(screen, (70, 120, 220), r2)
        for i in rect_list:
            pg.draw.rect(screen, (0, 255, 0), i)

        d = {}
        for i in range(len(rect_list)):
            d[tuple(rect_list[i])] = i + 100

        collision = r1.collidepoint(400, 300)
        print(collision)
        # if collision!=None:
        #     rect_list.remove(collision[0])

        pg.display.update()
        clock.tick(60)

# ex1()


def ex2():
    import pygame as pg
    import sys  # модуль для выхода из игры и закрытия всех окон
    from random import randint
    from pygame.sprite import Group

    pg.init()  # используется для старта модуля pygame
    pg.display.set_caption("Collision")  # задание загаловка окну
    screen = pg.display.set_mode((800, 600), pg.RESIZABLE)  # создание поверхности с указанными размерами и параметрами
    clock = pg.time.Clock()  # создаем экземпляр класса для управление времени(кадрами игры (fps))

    play = True

    class Player(pg.sprite.Sprite):
        def __init__(self, screen):
            super(Player, self).__init__()
            self.screen = screen
            self.iamge = pg.image.load("animations/0.png")
            self.image = pg.transform.scale(self.iamge, (50, 73))
            self.rect = self.image.get_rect()

        def update(self, keys):
            if keys[pg.K_LEFT]:
                self.rect.centerx -= 5  # обращение к точке элемента объекта класса
            if keys[pg.K_UP]:
                self.rect.centery -= 5
            if keys[pg.K_DOWN]:
                self.rect.centery += 5
            if keys[pg.K_RIGHT]:
                self.rect.centerx += 5

        def draw(self):
            self.screen.blit(self.iamge, self.rect)

        def collidepoint(self, x, y):
            return self.rect.collidepoint(x, y)

    class Apple(pg.sprite.Sprite):
        def __init__(self, screen, x, y):
            super(Apple, self).__init__()
            self.screen = screen
            self.image = pg.image.load("apple (2).png")
            self.image = pg.transform.scale(self.image, (30, 30))
            self.rect = self.image.get_rect(center=(x, y))

        def draw(self):
            self.screen.blit(self.image, self.rect)

        def update(self, speed):
            self.rect.x += speed


    mario = Player(screen)

    map = pg.image.load("animations/map.png")
    map = pg.transform.scale(map, (800, 600))

    apple_group = Group()
    mario_group = Group()
    for i in range(10):
        mario = Player(screen)
        mario_group.add(mario)
    for i in range(10):
        apple = Apple(screen, randint(20, 780), randint(20, 580))
        apple_group.add(apple)

    while play:  # основной цикл игры
        for event in pg.event.get():  # отслеживание всех событий которые происходят на игровом дисплее
            if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                sys.exit()  # функция выхода из игры и закрытия всех окон(
        screen.blit(map, (0, 0))
        keys = pg.key.get_pressed()

        mario.update(keys)
        mario.draw()

        apple_group.draw(screen)
        mario_group.draw(screen)
        # apple_group.update(6)
        mario_group.update(keys)

        collisions = pg.sprite.spritecollide(mario, apple_group, True)
        if mario.collidepoint(400, 300):
            print("collide center")
        print(collisions)

        pg.display.update()
        clock.tick(60)

ex2()


"""
############## коллизия между объектами класса Rect ######################
collision = pg.Rect.collidepoint(#объект класса Rect,#x точки,#у точки)
-обработка коллизи между объектом rect и точкой

collision = pg.Rect.colliderect(#объект класса Rect,#объект класса Rect)
-обработка коллизии между двумя прямоугольниками,
true -если накладываются, False -если нет

collision = pg.Rect.collidelist(#объект класса Rect,#список с объектами класса Rect)
-при коллизииосновного объекта со элементом списка,
выводит индекс элемента с которым произошла коллизия

pg.Rect.collidelistall(#объект класса Rect,#список с объектами класса Rect)
-при коллизии основного объекта со элементом списка,
выводит список с номерами элементов с которыми произошла коллизия

collision = pg.Rect.collidedict((#объект класса Rect,
    #словарь ключами которого являются объекты класса Rect)
-если коллизия найдена,возвращает кортеж,
где первый элемент -объект класса рект, второй -его значение в словаре

collision = pg.Rect.collidedictall((#объект класса Rect,
    #словарь ключами которого являются объекты класса Rect)
-если коллизия найдена,возвращает список с кортежами,
в котором первый элемент -объект класса рект, второй -его значение в словаре

############ коллизия между объектами класса Sprite ###################
collisions = pg.sprite.spritecollide(#объект класса Sprite,
    #объект класса Group,
    #уничтожение спрайта с которым произошла коллизия
    (boll)= отслеживание коллизии между спрайтом и
    группой спрайтов

collisions = pg.sprite.collide_mask(#объект класса Sprite,
    #объект класса Sprite)
-создаем маску пересечения области двух спрайтов

collisions = pg.sprite.groupcollide(,#объект класса Group,,
    #объект класса Group,
    #уничтожение спрайта с которым произошла коллизия из 1 группы,
    #уничтожение спрайта с которым произошла коллизия из 2 группы)
-проверка коллизии между двух групп
"""