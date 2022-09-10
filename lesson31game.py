def ex1():
    import pygame as pg
    import sys  # модуль для выхода из игры и закрытия всех окон

    pg.init()  # используется для старта модуля pygame
    pg.display.set_caption("Anim")  # задание загаловка окну
    screen = pg.display.set_mode((800, 600), pg.RESIZABLE)  # создание поверхности с указанными размерами и параметрами
    clock = pg.time.Clock()  # создаем экземпляр класса для управление времени(кадрами игры (fps))

    def load_frames(filename, row, col, size):
        frames = []
        image = pg.image.load(filename)
        width, height = image.get_size()

        width_one = width // col
        height_one = height // row

        for r in range(row):
            frames.append([])
            for c in range(col):
                frames[r].append(
                    pg.transform.scale(
                        image.subsurface(
                            c * width_one, height_one * r, width_one, height_one),
                        size))
        return frames

    class AnimationWalkSprite(pg.sprite.Sprite):
        def __init__(self, center_x, center_y, speed, size):
            super().__init__()
            self.frames = load_frames("les2img/walking_man.png",
                                      row=4, col=12, size=size)
            self.image = self.frames[0][0]
            self.rect = self.image.get_rect()
            self.rect.center = center_x, center_y
            self.speed = speed
            self.r = 0
            self.l = 0
            self.f = 0
            self.b = 0

        def update(self, keys):
            if keys[pg.K_d]:
                self.rect.centerx += self.speed
            if keys[pg.K_s]:
                self.rect.centery += self.speed
            if keys[pg.K_w]:
                self.rect.centery -= self.speed
            if keys[pg.K_a]:
                self.rect.centerx -= self.speed

        def update_frame(self, keys):
            if keys[pg.K_d]:
                self.image = self.frames[2][self.r]
                self.r += 1
                if self.r >= len(self.frames[2]):
                    self.r = 0
            elif keys[pg.K_a]:
                self.image = self.frames[1][self.l]
                self.l += 1
                if self.l >= len(self.frames[1]):
                    self.l = 0
            elif keys[pg.K_w]:
                self.image = self.frames[3][self.f]
                self.f += 1
                if self.f >= len(self.frames[3]):
                    self.f = 0
            elif keys[pg.K_s]:
                self.image = self.frames[0][self.b]
                self.b += 1
                if self.b >= len(self.frames[0]):
                    self.b = 0

        def draw(self, win):
            win.blit(self.image, self.rect)

    hero = AnimationWalkSprite(center_x=400, center_y=300, speed=5, size=(112, 180))
    play = True
    while play:  # основной цикл игры
        for event in pg.event.get():  # отслеживание всех событий которые происходят на игровом дисплее
            if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                sys.exit()  # функция выхода из игры и закрытия всех окон
        keys = pg.key.get_pressed()
        screen.fill((0, 0, 0))

        hero.update(keys)
        hero.update_frame(keys)
        hero.draw(screen)

        pg.display.update()
        clock.tick(30)

# ex1()

def ex2():
    import pygame as pg
    from random import randint
    import sys  # модуль для выхода из игры и закрытия всех окон
    from time import time

    pg.init()  # используется для старта модуля pygame
    pg.display.set_caption("Animation")  # задание загаловка окну
    screen = pg.display.set_mode((800, 600), pg.RESIZABLE)  # создание поверхности с указанными размерами и параметрами
    clock = pg.time.Clock()  # создаем экземпляр класса для управление времени(кадрами игры (fps))

    def load_frames(filename, row, col, size):
        frames = []
        image = pg.image.load(filename)
        width, height = image.get_size()

        width_one = width // col
        height_one = height // row

        for r in range(row):
            for c in range(col):
                frames.append(
                    pg.transform.scale(
                        image.subsurface(
                            c * width_one, height_one * r, width_one, height_one),
                        size))
        return frames

    class AnimationTimeSprite(pg.sprite.Sprite):
        def __init__(self, center_x, center_y, speed, size):
            super().__init__()
            self.frames = load_frames("timeanim/coinanim.png",
                                      row=2, col=3, size=size)
            self.image = self.frames[0]
            self.rect = self.image.get_rect()
            self.rect.center = center_x, center_y
            self.speed = speed
            self.index = 0
            self.timer = time()

        def update(self):
            self.update_frame()

        def update_frame(self):
            if time() - self.timer >= 1 / self.speed:
                self.timer = time()
                self.index += 1
            self.index %= len(self.frames)
            self.image = self.frames[self.index]

        def draw(self, win):
            win.blit(self.image, self.rect)

    class AnimationWalkSprite(pg.sprite.Sprite):
        def __init__(self, center_x, center_y, speed, size):
            super().__init__()
            self.frames_right = [
                pg.transform.scale(pg.image.load(f"animations/r{i}.png"), size)
                for i in range(1, 7)]
            self.frames_left = [
                pg.transform.scale(pg.image.load(f"animations/l{i}.png"), size)
                for i in range(1, 7)]
            self.stand_frame = pg.transform.scale(pg.image.load("animations/0.png"), size)
            self.image = self.stand_frame
            self.rect = self.image.get_rect(center=(center_x, center_y))
            self.speed = speed
            self.index = 0

        def update(self):
            keys = pg.key.get_pressed()
            if keys[pg.K_d]:
                self.rect.centerx += self.speed
            if keys[pg.K_w]:
                self.rect.centery -= self.speed
            if keys[pg.K_s]:
                self.rect.centery += self.speed
            if keys[pg.K_a]:
                self.rect.centerx -= self.speed

        def update_frame(self):
            keys = pg.key.get_pressed()
            if keys[pg.K_d]:
                self.image = self.frames_right[self.index // 5]
            elif keys[pg.K_a]:
                self.image = self.frames_left[self.index // 5]
            elif keys[pg.K_w]:
                self.image = self.frames_right[self.index // 5]
            elif keys[pg.K_s]:
                self.image = self.frames_left[self.index // 5]
            else:
                self.image = self.stand_frame
            self.index += 1
            self.index %= 30

        def draw(self, win):
            win.blit(self.image, self.rect)

    map = pg.transform.scale(pg.image.load("animations/map.png"), (800, 600))

    hero = AnimationWalkSprite(center_x=400, center_y=300, speed=5, size=(100, 145))

    coins = pg.sprite.Group()
    for n in range(10):
        coin = AnimationTimeSprite(center_x=randint(30, 750), center_y=randint(30, 550),
                                   speed=30, size=(30, 30))
        coins.add(coin)
    score = 0
    play = True
    while play:  # основной цикл игры
        for event in pg.event.get():  # отслеживание всех событий которые происходят на игровом дисплее
            if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                sys.exit()  # функция выхода из игры и закрытия всех окон(
        screen.blit(map, (0, 0))

        hero.update()
        hero.update_frame()
        hero.draw(screen)

        coins.update()
        coins.draw(screen)

        colisions = pg.sprite.spritecollide(hero, coins, True)
        for coin in colisions:
            score += 1
            print(score)

        pg.display.update()
        clock.tick(60)

ex2()

"""
image.get_size() -возвращает кортеж из ширины и высоты изображения 
к которому применяется

image.subsurface(#объект класса Rect(прямоугольник, который необходимо 
    вырезать из исходного изображения)) 
    -создает поверхность из части поверхности к которой применяется

for row in range(4):#создание суб поверхностей их всех картинок листа
    for col in range(12):
        frames.append(pg.transform.scale(
            image.subsurface(pg.Rect(
                col*width_one,height_one*row,width_one,height_one)
                ),(112,180))
                )
"""