def ex1():
    """Использование текста в pygame"""
    import pygame as pg
    import sys

    pg.init()
    pg.font.init()

    pg.display.set_caption("Example text")
    screen = pg.display.set_mode((800, 600), pg.RESIZABLE)
    clock = pg.time.Clock()

    font = pg.font.Font(None, 50)  # можно использовать системные или пользовательские шрифты
    text = font.render("Text", True, (200, 250, 230), (0, 200, 20))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        screen.fill((60, 60, 60))

        screen.blit(text, (300, 400))
        pg.display.update()
        clock.tick(60)

# ex1()

def ex2():
    """Использование текста в pygame"""
    import pygame as pg
    import sys

    import time

    pg.init()
    pg.font.init()

    pg.display.set_caption("Example text2")
    screen = pg.display.set_mode((800, 600), pg.RESIZABLE)
    clock = pg.time.Clock()

    WHITE_COLOR = (255, 255, 255)
    GREEN_COLOR = (0, 255, 0)

    class Text:
        def __init__(self, x, y, font=None, font_size=50, text="Test",
                     color=WHITE_COLOR, background=None):
            # создаем шрифт
            self.font = pg.font.Font(font, font_size)
            # Картинка из шрифта
            self.color = color
            self.background = background
            self.image = self.font.render(text, 1, self.color, self.background)
            self.rect = self.image.get_rect(center=(x, y))

        def update(self, text):
            self.image = self.font.render(text, 1, self.color, self.background)

        def change_color(self, new_color):
            self.color = new_color

        def change_pos(self, x, y):
            self.rect.center = (x, y)

        def draw(self, win):
            win.blit(self.image, self.rect)

    class TextGroup(list):
        def append(self, text) -> None:
            if isinstance(text, Text):
                super().append(text)
            else:
                raise TypeError("Type must be is Text")

        def draw(self, *args, **kwargs):
            for text in self:
                text.draw(*args, **kwargs)

    text_group = TextGroup()
    score = 0
    text = Text(text=f"Score: {score}", x=400, y=300)
    text_group.append(text)

    timer = 10
    curent_time = time.time()
    text_timer = Text(text=f"Time: {timer}", x=600, y=50, background=GREEN_COLOR)
    text_group.append(text_timer)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        screen.fill((60, 60, 60))

        if timer > 0 and time.time() - curent_time >= 1:
            curent_time = time.time()
            timer -= 1
            score += 1
            text.update(f"Score: {score}")
            text_timer.update(f"Time: {timer}")

        text_group.draw(screen)

        pg.display.update()
        clock.tick(60)

# ex2()

def ex3():
    import pygame as pg
    import sys  # модуль для выхода из игры и закрытия всех окон
    from pygame.sprite import Group
    from random import randint
    import pygame_widgets
    from pygame_widgets.slider import Slider
    from pygame_widgets.textbox import TextBox
    pg.init()  # используется для старта модуля pygame
    pg.display.set_caption("Animation")  # задание загаловка окну
    screen = pg.display.set_mode((800, 600))  # создание поверхности с указанными размерами и параметрами
    clock = pg.time.Clock()  # создаем экземпляр класса для управление времени(кадрами игры (fps))

    slider = Slider(screen, 100, 100, 100, 10)
    output = TextBox(screen, 140, 140, 20, 20, fontSize=16)
    output.disable()

    animation_right = [pg.transform.scale(pg.image.load(f"animations/r{i}.png"), (60, 100)) for i in range(1, 7)]

    animation_left = [pg.transform.scale(pg.image.load(f"animations/l{i}.png"), (60, 100)) for i in range(1, 7)]

    map = pg.image.load("animations/map.png")
    map = pg.transform.scale(map, (800, 600))

    stand = pg.image.load("animations/0.png")
    stand = pg.transform.scale(stand, (60, 100))
    rect = stand.get_rect(center=(100, 100))

    sound1 = pg.mixer.Sound("Sound/gamesound.wav")
    sound1.set_volume(0.3)

    sound2 = pg.mixer.Sound("Sound/cowboy.wav")
    sound2.set_volume(0.3)

    sound3 = pg.mixer.Sound("Sound/happy.wav")
    sound3.play(-1)
    sound3.set_volume(0.3)

    sound4 = pg.mixer.Sound("Sound/sample.wav")
    sound4.set_volume(0.3)

    apple_group = Group()

    point = pg.mixer.Sound("Sound/point.wav")

    def update(keys, person):
        if keys[pg.K_d]:
            person.centerx += 5  # обращение к точке элемента объекта класса
        if keys[pg.K_w]:
            person.centery -= 5
        if keys[pg.K_s]:
            person.centery += 5
        if keys[pg.K_a]:
            person.centerx -= 5

    class Apple(pg.sprite.Sprite):
        def __init__(self, screen, x, y):
            super(Apple, self).__init__()
            self.screen = screen
            self.image = pg.image.load("apple (2).png")
            self.image = pg.transform.scale(self.image, (30, 30))
            self.rect = self.image.get_rect(center=(x, y))

        def draw(self):
            self.screen.blit(self.image, self.rect)

    for i in range(10):
        apple = Apple(screen, randint(20, 780), randint(20, 580))
        apple_group.add(apple)

    def draw(screen, keys):
        nonlocal index  # в случае если код запускается внутри функции
        # global index  # в случае если код запускается не внутри функции
        if keys[pg.K_d]:
            screen.blit(animation_right[index // 10], rect)
        elif keys[pg.K_a]:
            screen.blit(animation_left[index // 10], rect)
        elif keys[pg.K_w]:
            screen.blit(animation_right[index // 10], rect)
        elif keys[pg.K_s]:
            screen.blit(animation_left[index // 10], rect)
        else:
            screen.blit(stand, rect)
        index += 2
        if index == 60:
            index = 0

        for i in apple_group:
            i.draw()

    play_music = True
    index = 0
    play = True
    while play:  # основной цикл игры
        for event in pg.event.get():  # отслеживание всех событий которые происходят на игровом дисплее
            if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                sys.exit()  # функция выхода из игры и закрытия всех окон(
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    if play_music == True:
                        sound1.stop()
                        sound2.stop()
                        sound3.stop()
                        sound4.stop()
                        play_music = False
                    else:
                        sound1.play(-1)
                        sound2.stop()
                        sound3.stop()
                        sound4.stop()
                        play_music = True
                if event.key == pg.K_r:
                    sound1.stop()
                    sound2.stop()
                    sound3.stop()
                    sound4.stop()
                if event.key == pg.K_l:
                    sound1.play()

                if event.key == pg.K_KP1:
                    sound1.play()
                    sound2.stop()
                    sound3.stop()
                    sound4.stop()
                if event.key == pg.K_KP2:
                    sound1.stop()
                    sound2.play()
                    sound3.stop()
                    sound4.stop()
                if event.key == pg.K_KP3:
                    sound1.stop()
                    sound2.stop()
                    sound3.play()
                    sound4.stop()
                if event.key == pg.K_KP4:
                    sound1.stop()
                    sound2.stop()
                    sound3.stop()
                    sound4.play()

        screen.blit(map, (0, 0))
        keys = pg.key.get_pressed()

        draw(screen, keys)
        update(keys, rect)

        output.setText(slider.getValue())
        sound1.set_volume(slider.getValue() / 100)
        sound2.set_volume(slider.getValue() / 100)
        sound3.set_volume(slider.getValue() / 100)
        sound4.set_volume(slider.getValue() / 100)
        events = pg.event.get()
        pygame_widgets.update(events)

        for sprite in apple_group:
            collision = pg.Rect.colliderect(rect, sprite.rect)
            if collision:
                sprite.kill()
                point.play()

        pg.display.update()
        clock.tick(60)

# ex3()

def ex4():
    import pygame_widgets
    import pygame
    import sys
    from pygame_widgets.slider import Slider
    from pygame_widgets.textbox import TextBox

    pygame.init()
    screen = pygame.display.set_mode((1000, 800))

    slider = Slider(screen, 100, 100, 800, 10, min=0, max=99, step=1)
    output = TextBox(screen, 475, 200, 50, 50, fontSize=30)

    v_slider = Slider(screen, 900, 200, 10, 300, min=0, max=99, step=1, vertical=True)
    v_output = TextBox(screen, 800, 320, 50, 50, fontSize=30)

    output.disable()
    v_output.disable()

    play = True
    while play:
        events = pygame.event.get()
        for event in events:  # отслеживание всех событий которые происходят на игровом дисплее
            if event.type == pygame.QUIT:  # если тип события = нажатию на крестик
                sys.exit()  # функция выхода из игры и закрытия всех окон(

        screen.fill((255, 255, 255))

        output.setText(slider.getValue())
        v_output.setText(v_slider.getValue())

        pygame_widgets.update(events)
        pygame.display.update()

# ex4()

def ex5():
    import pygame as pg
    import sys  # модуль для выхода из игры и закрытия всех окон
    from random import randint

    pg.init()  # используется для старта модуля pygame
    pg.display.set_caption("Sound")  # задание загаловка окну
    screen = pg.display.set_mode((800, 600), pg.RESIZABLE)  # создание поверхности с указанными размерами и параметрами
    clock = pg.time.Clock()  # создаем экземпляр класса для управление времени(кадрами игры (fps))

    pg.mixer.music.load("Sound/music.mp3")

    s1 = pg.mixer.Sound("Sound/gamesound.wav")

    s1.set_volume(0.2)
    ch1 = s1.play()
    ch2 = s1.play()

    pg.mixer.music.play(-1, 10)
    vol = 1
    play_music = True
    play = True
    # pg.display.flip() - обновление всего экрана
    while play:  # основной цикл игры
        for event in pg.event.get():  # отслеживание всех событий которые происходят на игровом дисплее
            if event.type == pg.KEYDOWN:
                print(event.key)
                if event.key == pg.K_p:
                    if play_music == True:
                        pg.mixer.music.pause()
                        play_music = False
                    else:
                        pg.mixer.music.unpause()
                        play_music = True
                if event.key == pg.K_r:
                    pg.mixer.music.rewind()
                if event.key == pg.K_s:
                    pg.mixer.music.stop()
                if event.key == pg.K_l:
                    pg.mixer.music.play(-1, 10)
                if event.key == pg.K_RIGHT:
                    vol += 0.1
                    pg.mixer.music.set_volume(vol)
                    print(pg.mixer.music.get_volume())
                if event.key == pg.K_LEFT:
                    vol -= 0.1
                    pg.mixer.music.set_volume(vol)
                    print(pg.mixer.music.get_volume())
                if event.key == pg.K_RETURN:
                    s1.play()
                if event.key == pg.K_z:
                    ch1.pause()
                if event.key == pg.K_x:
                    ch1.unpause()
                if event.key == pg.K_c:
                    ch2.pause()
                if event.key == pg.K_v:
                    ch2.unpause()
            if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                sys.exit()  # функция выхода из игры и закрытия всех окон(

        pg.display.update()
        clock.tick(60)

# ex5()

def ex3_2():
    import pygame as pg
    from random import randint
    import sys
    from time import time
    import pygame_widgets
    from pygame_widgets.slider import Slider

    WIDTH, HEIGHT = 800, 600
    pg.init()
    pg.display.set_caption("Sounds")
    screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
    clock = pg.time.Clock()
    WHITE_COLOR = (255, 255, 255)
    GREEN_COLOR = (0, 255, 0)

    class Text:
        def __init__(self, win, x, y, font=None, font_size=50, text="Test",
                     color=WHITE_COLOR, background=None):
            # создаем шрифт
            self.font = pg.font.Font(font, font_size)
            # Картинка из шрифта
            self.color = color
            self.background = background
            self.image = self.font.render(str(text), 1, self.color, self.background)
            self.rect = self.image.get_rect(center=(x, y))
            self.win = win

        def update(self, text):
            self.image = self.font.render(str(text), 1, self.color, self.background)

        def change_color(self, new_color):
            self.color = new_color

        def change_pos(self, x, y):
            self.rect.center = (x, y)

        def draw(self):
            self.win.blit(self.image, self.rect)

    class TextGroup(list):
        def append(self, text) -> None:
            if isinstance(text, Text):
                super().append(text)
            else:
                raise TypeError("Type must be is Text")

        def draw(self, *args, **kwargs):
            for text in self:
                text.draw(*args, **kwargs)

    text_group = TextGroup()

    class Sound:
        def __new__(cls):
            """Реализация паттерна 'Сингелтон' - при попытке создать новый объект
            будет возвращаться ссылка на уже созданный"""
            if not hasattr(cls, 'instance'):
                cls.instance = super(Sound, cls).__new__(cls)
            return cls.instance

        def __init__(self):
            if not hasattr(self, 'sounds'):  # чтобы дважды не вызывался конструктор
                self.sounds = []
                self.volume = 0.5
                self.current_sound = None
                self.is_playing = False

        def add(self, filename):
            self.sounds.append(pg.mixer.Sound(filename))

        def stop(self):
            if self.current_sound is not None:
                self.sounds[self.current_sound].stop()
                self.is_playing = False

        def play_current(self):
            if self.current_sound is not None:
                self.sounds[self.current_sound].set_volume(self.volume)
                self.sounds[self.current_sound].play(loops=-1)
                self.is_playing = True

        def play(self, index=0):
            if self.sounds and index < len(self.sounds):
                self.stop()
                self.current_sound = index
                self.play_current()

        def play_next(self):
            if self.current_sound + 1 == len(self.sounds):
                self.play(0)
            else:
                self.play(self.current_sound + 1)

        def set_volume(self, volume):
            self.volume = volume
            if self.current_sound is not None:
                self.sounds[self.current_sound].set_volume(self.volume)

        def control(self, key):
            if key == pg.K_p:
                if self.is_playing:
                    # self.stop()
                    pg.mixer.pause()
                    self.is_playing = False
                else:
                    # self.play_current()
                    pg.mixer.unpause()
                    self.is_playing = True
            comand = {pg.K_r: self.stop,
                      pg.K_l: self.play,
                      pg.K_n: self.play_next}
            if key in comand:
                comand[key]()
            comand2 = (pg.K_1, pg.K_2, pg.K_3, pg.K_4)
            if key in comand2:
                self.play(comand2.index(key))

    class MySlider(Slider):
        def __init__(self, win, x, y, width, height):
            super().__init__(win=win, x=x, y=y, width=width, height=height)
            self.text = Text(win=win, x=(x+width//2), y=(y+height*2), font=None,
                             font_size=30, text=f"Volume: {self.getValue()}%",
                             color=WHITE_COLOR)

        def draw(self):
            super().draw()
            self.text.update(f"Volume: {self.getValue()}%")
            self.text.draw()

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

    background = pg.transform.scale(pg.image.load("animations/map.png"), (800, 600))

    hero = AnimationWalkSprite(center_x=400, center_y=300, speed=5, size=(60, 100))

    coins = pg.sprite.Group()
    for n in range(10):
        coin = AnimationTimeSprite(center_x=randint(30, WIDTH-30),
                                   center_y=randint(30, HEIGHT-30),
                                   speed=30, size=(30, 30))
        coins.add(coin)
    score = 0
    score_text = Text(win=screen, text=f"Score: {score}", x=80, y=30)
    text_group.append(score_text)

    point = pg.mixer.Sound("Sound/point.wav")
    point.set_volume(0.3)

    sounds = Sound()  # создаем сингелтон объект для управления музыкой
    sounds.add("Sound/gamesound.wav")
    sounds.add("Sound/cowboy.wav")
    sounds.add("Sound/happy.wav")
    sounds.add("Sound/sample.wav")
    sounds.play()

    # если попытаемся создать второй объект Sound - то вернется тот же объект
    sounds2 = Sound()
    print(sounds, sounds2, sounds is sounds2)

    slider = MySlider(screen, 200, 20, WIDTH-400, 10)

    play = True
    while play:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                sounds.control(event.key)

        screen.blit(background, (0, 0))
        pygame_widgets.update(events)
        sounds.set_volume(slider.getValue()/100)

        hero.update()
        hero.update_frame()
        hero.draw(screen)

        coins.update()
        coins.draw(screen)

        colisions = pg.sprite.spritecollide(hero, coins, True)
        for _ in colisions:
            score += 1
            score_text.update(f"Score: {score}")
            point.set_volume(slider.getValue()/100)
            point.play()

        text_group.draw()
        pg.display.update()
        clock.tick(60)

# ex3_2()

"""
pg.mixer.music.load("Sound/music.mp3") -загрузка в один поток

s1 = pg.mixer.Sound("Sound/gamesound.wav") 
-создание экземпляра класса для многопотокового аудио

sound1.play() -проигрыш мелодии

s1.set_volume() -установка громкости
s1.пet_volume() -получение значения громкости

sound4.stop() -завершение воспроизведение 

Слайдер
slider = Slider(screen,левый верхний х,лев верх у,ширина,высота) 
-создание самого слайдера с помощью виджета из модуля  pygame_widgets

output = TextBox(screen,левый верхний х,лев верх у,ширина,высота,fontSize=16) 
-создание текстового окна с цифрами

events = pygame.event.get()
pygame_widgets.update(events) -обновление виджета
"""