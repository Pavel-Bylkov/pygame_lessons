import pygame as pg
import sys  # модуль для выхода из игры и закрытия всех окон

pg.init()  # используется для старта модуля pygame
pg.display.set_caption("Pygame")  # задание загаловка окну
screen = pg.display.set_mode((800, 600), pg.RESIZABLE)  # создание поверхности с указанными размерами и параметрами
clock = pg.time.Clock()  # создаем экземпляр класса для управление времени(кадрами игры (fps))

rectangle = pg.Rect(100,100,50,50)

class Apple():
    def __init__(self, screen):
        self.screen = screen
        image = pg.image.load("les2img/apple.png")
        self.image = pg.transform.scale(image, (30, 30))
        self.rect = self.image.get_rect(center=(150, 150))
        self.speedx = 5
        self.speedy = 5

    def update(self):
        if self.rect.top < 0:
            self.speedy *=-1
        if self.rect.bottom > 600:
            self.speedy *=-1
        if self.rect.right > 800:
            self.speedx*=-1
        if self.rect.left < 0:
            self.speedx*=-1
        self.rect.x +=self.speedx
        self.rect.y += self.speedy

    def draw(self):
        self.screen.blit(self.image, self.rect)

# def move(keys,r1):
#     global DIRECTION
#     if keys[pg.K_LEFT]:
#         #DIRECTION = [-SPEED,0]
#         #r1.move_ip(-SPEED,0)
#         sprite_rect.centerx -= 5 #обращение к точке элемента объекта класса
#         # sprite_rect.x += 5
#     if keys[pg.K_UP]:
#         #DIRECTION = [0,-SPEED]
#         #r1.move_ip(0,-SPEED)
#         sprite_rect.centery -= 5
#     if keys[pg.K_DOWN]:
#         #DIRECTION = [0,SPEED]
#         #r1.move_ip(0,SPEED)
#         sprite_rect.centery += 5
#     if keys[pg.K_RIGHT]:
#         #DIRECTION = [SPEED,0]
#         #r1.move_ip(SPEED,0)
#         sprite_rect.centerx += 5
    #r1.move_ip(DIRECTION)
    # if sprite_rect.top < 0:
    #     sprite_rect.bottom = 600
    # if sprite_rect.bottom > 600:
    #     sprite_rect.top = 0
    # if sprite_rect.right > 800:
    #     sprite_rect.left = 0
    # if sprite_rect.left < 0:
    #     sprite_rect.right = 800


# sprite = pg.image.load("les2img/Walk.png")
# sprite = pg.transform.scale(sprite,(150,200))
# sprite_rect = sprite.get_rect(center=(400,300))

class MySprite(pg.sprite.Sprite):
    def __init__(self, filename, center_x, center_y, witdh, height):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(filename), (witdh, height))
        self.rect = self.image.get_rect(center=(center_x, center_y))

    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.rect.centerx -= 5  # обращение к точке элемента объекта класса
        if keys[pg.K_UP]:
            self.rect.centery -= 5
        if keys[pg.K_DOWN]:
            self.rect.centery += 5
        if keys[pg.K_RIGHT]:
            self.rect.centerx += 5

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))


apple_sprite = Apple(screen)
sprite = MySprite("les2img/Walk.png", 400,300, 150,200)

place = pg.image.load("les2img/place.png")
place = pg.transform.scale(place,(800,600))

play = True
#pg.display.flip() - обновление всего экрана
while play:#основной цикл игры
    for event in pg.event.get():#отслеживание всех событий которые происходят на игровом дисплее
        if event.type == pg.QUIT:#если тип события = нажатию на крестик
            sys.exit()#функция выхода из игры и закрытия всех окон
        # if event.type == pg.KEYDOWN:
        #     if event.key ==pg.K_s:#если нажатая клавиша - s
        #         r1.move_ip(0, 15)
        #     if event.key ==pg.K_a:#если нажатая клавиша - s
        #         r1.move_ip(-15, 0)
        #     if event.key ==pg.K_d:#если нажатая клавиша - s
        #         r1.move_ip(15, 0)
        #     if event.key ==pg.K_w:#если нажатая клавиша - s
        #         r1.move_ip(0, -15)

    keys = pg.key.get_pressed()


    screen.blit(place,(0,0))
    #pg.draw.rect(screen, (50, 200, 10), r1)
    sprite.update()
    sprite.draw(screen)

    apple_sprite.update()
    apple_sprite.draw()

    pg.display.update()# - обновление части экрана, но если аргумент не указан, то обновляется весь
    clock.tick(60)#устанавливаем максимальное указанное количество кадров


"""
r1.move_ip(#координата x,#координата x)
-сдвигает объект класса Rect на указанное количество координат

if event.type == pg.KEYDOWN:
-если тип события=нажатие клавиши
    keys = pg.key.get_pressed()
    -создает список из всех нажатых клавиш, если клавиша нажата записывается True,
    если нет, то False

pg.image.load(#путь до файла со спрайтом)
-функция для загрузки картинки в проект

pg.transform.scale(#картинка которую хотим преобразовать,
    #размеры которые должна принять картинка)

sprite.get_rect() -функция для получения из картинки объекта класса Rect

screen.blit(#изображение, #координаты записанные в кортеже (x,y))
-вывод изображения на экран

sprite_rect.centerx -= 5
"""