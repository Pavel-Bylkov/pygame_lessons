def ex1():
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
    FONT_head = pg.font.Font(None, 35)
    FONT_head.set_bold(True)
    FONT_head.set_italic(True)
    FONT_vol = pg.font.Font(None, 28)
    FONT_score = pg.font.Font(None, 30)
    SCORE = 0

    slider = Slider(screen, 408, 216, 100, 10)
    output = TextBox(screen, 375, 210, 20, 20, fontSize=16)
    output.disable()

    animation_right = [pg.transform.scale(pg.image.load(f"animations/r{i}.png"), (60, 100)) for i in range(1, 7)]
    animation_left = [pg.transform.scale(pg.image.load(f"animations/l{i}.png"), (60, 100)) for i in range(1, 7)]

    map = pg.image.load("animations/map.png")
    map = pg.transform.scale(map, (800, 600))

    menu_esc = pg.image.load("Sprite/menu_esc.png")  # загрузка картинок для меню
    menu_esc = pg.transform.scale(menu_esc, (400, 400))  # изменение размера
    menu_esc_rect = menu_esc.get_rect(center=(400, 300))  # получение объекта класса рект и установка координат на центр

    base_menu = pg.image.load("Sprite/base_menu.png")  # загрузка картинок для меню
    base_menu = pg.transform.scale(base_menu, (350, 350))  # изменение размера
    base_menu_rect = base_menu.get_rect(
        center=(395, 300))  # получение объекта класса рект и установка координат на центр

    stand = pg.image.load("animations/0.png")
    stand = pg.transform.scale(stand, (60, 100))
    rect = stand.get_rect(center=(100, 100))

    sound1 = pg.mixer.Sound("Sound/gamesound.wav")
    sound1.set_volume(0.3)

    sound2 = pg.mixer.Sound("Sound/cowboy.wav")
    sound2.set_volume(0.3)

    sound3 = pg.mixer.Sound("Sound/happy.wav")
    sound3.set_volume(0.3)

    sound4 = pg.mixer.Sound("Sound/sample.wav")
    sound4.set_volume(0.3)

    point = pg.mixer.Sound("Sound/point.wav")

    apple_group = Group()

    slider_value = slider.getValue()

    def draw_setting():  # функция с бесконечным циклом для меню с настройками
        nonlocal slider_value
        screen.blit(base_menu, base_menu_rect)

        text_head = FONT_head.render("Settings", True, (0, 0, 0))
        text_rect_head = text_head.get_rect(center=(395, 180))
        screen.blit(text_head, text_rect_head)

        text_vol = FONT_vol.render("Volume: ", True, (0, 0, 0))
        text_rect_vol = text_vol.get_rect(center=(320, 220))
        screen.blit(text_vol, text_rect_vol)

        play = True
        while play:
            events = pg.event.get()
            for event in events:  # отслеживание всех событий которые происходят на игровом дисплее
                if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                    sys.exit()  # функция выхода из игры и закрытия всех окон(
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        play = False

            output.setText(slider.getValue())
            pygame_widgets.update(events)
            slider_value = slider.getValue()

            sound1.set_volume(slider_value / 100)
            sound2.set_volume(slider_value / 100)
            sound3.set_volume(slider_value / 100)
            sound4.set_volume(slider_value / 100)

            pg.display.update(base_menu_rect)

    def draw_menu():  # функция с бесконечным циклом для меню
        play = True
        while play:
            events = pg.event.get()
            for event in events:  # отслеживание всех событий которые происходят на игровом дисплее
                if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                    sys.exit()  # функция выхода из игры и закрытия всех окон(
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 340 < event.pos[0] < 465 and 250 < event.pos[1] < 280:
                            # если позиция мышки находится в нужных координатах
                            play = False
                        if 340 < event.pos[0] < 465 and 306 < event.pos[1] < 336:
                            draw_setting()
                        if 340 < event.pos[0] < 465 and 356 < event.pos[1] < 386:
                            sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        play = False

            screen.blit(map, (0, 0))
            screen.blit(menu_esc, menu_esc_rect)
            pg.display.update(menu_esc_rect)

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
            self.image = pg.image.load("Sprite/apple (2).png")
            self.image = pg.transform.scale(self.image, (30, 30))
            self.rect = self.image.get_rect(center=(x, y))

        def draw(self):
            self.screen.blit(self.image, self.rect)

    for i in range(10):
        apple = Apple(screen, randint(20, 780), randint(20, 580))
        apple_group.add(apple)

    def draw(screen, keys):
        nonlocal index
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

        apple_group.draw(screen)

    play_music = True
    index = 0
    play = True

    screen.blit(map, (0, 0))
    pg.display.update()
    draw_menu()

    while play:  # основной цикл игры
        events = pg.event.get()
        for event in events:  # отслеживание всех событий которые происходят на игровом дисплее
            if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                sys.exit()  # функция выхода из игры и закрытия всех окон(
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    draw_menu()
                if event.key == pg.K_p:
                    if play_music == True:
                        sound1.stop()
                        sound2.stop()
                        sound3.stop()
                        sound4.stop()
                        play_music = False
                    else:
                        sound1.play()
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

        for sprite in apple_group:
            collision = pg.Rect.colliderect(rect, sprite.rect)
            if collision:
                sprite.kill()
                SCORE += 1
                point.play()

        score_text = FONT_score.render(f"Score: {SCORE}", True, (150, 120, 200))
        score_text_rect = score_text.get_rect(center=(750, 40))
        screen.blit(score_text, score_text_rect)
        pg.display.update()
        clock.tick(60)

# ex1()


def ex2():
    import pygame as pg
    from random import randint
    import sys
    from time import time
    import pygame_widgets
    from pygame_widgets.slider import Slider
    from pygame_widgets.mouse import Mouse

    WIDTH, HEIGHT = 800, 600
    pg.init()
    pg.display.set_caption("Menu")
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

        def set_italic(self, value):
            self.font.set_italic(value)

        def set_bold(self, value):
            self.font.set_bold(value)

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
                    self.stop()
                else:
                    self.play_current()
            comand = {pg.K_r: self.stop, pg.K_l: self.play, pg.K_n: self.play_next}
            if key in comand:
                comand[key]()
            comand2 = (pg.K_1, pg.K_2, pg.K_3, pg.K_4)
            if key in comand2:
                self.play(comand2.index(key))

    class MySlider(Slider):
        def __init__(self, win, x, y, width, height):
            super().__init__(win=win, x=x-width//2, y=y-height//2,
                             width=width, height=height)
            self.text = Text(win=win, x=(x - 100 - width//2), y=y,
                             font_size=30, text=f"Volume: {self.getValue()}%",
                             color=(0, 0, 0))

        def draw(self):
            super().draw()
            self.text.update(f"Volume: {self.getValue()}%")
            self.text.draw()

    class Button:
        def __init__(self, win, filename="", pos=(WIDTH//2, HEIGHT//2),
                     size=(WIDTH//8, HEIGHT//8), on_click=(lambda:None), text="",
                     text_color=WHITE_COLOR, fill=(0, 0, 0)):
            self.win = win
            self.image = None
            if filename:
                menu = pg.image.load(filename)  # загрузка картинок для меню
                self.image = pg.transform.scale(menu, size)  # изменение размера
                self.rect = self.image.get_rect(center=pos)
            else:
                self.rect = pg.Rect(0, 0, *size)
                self.rect.center = pos
            self.text = Text(win=win, text=text, color=text_color, font_size=40,
                             x=self.rect.centerx, y=self.rect.centery)
            self.fill = fill
            self.on_click = on_click

        def draw(self):
            if self.image is None:
                pg.draw.rect(self.win, self.fill, self.rect)
            else:
                self.win.blit(self.image, self.rect)
            self.text.draw()

        def update(self, events):
            for event in events:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1 and self.rect.collidepoint(*event.pos):
                        self.on_click()

    class ButtonGroup(list):
        def add(self, button) -> None:
            if isinstance(button, Button):
                super().append(button)
            else:
                raise TypeError("Type must be is Button")

        def draw(self, *args, **kwargs):
            for button in self:
                button.draw(*args, **kwargs)

        def update(self, *args, **kwargs):
            for button in self:
                button.update(*args, **kwargs)

    class WidgetGroup(list):
        def add(self, widget) -> None:
            if isinstance(widget, pygame_widgets.widget.WidgetBase):
                super().append(widget)
            else:
                raise TypeError("Type must be is WidgetBase")

        def draw(self, *args, **kwargs):
            for widget in self:
                widget.draw(*args, **kwargs)

        def update(self, events):
            Mouse.updateMouseState()
            blocked = False
            for widget in self:
                if not blocked or not widget.contains(*Mouse.getMousePos()):
                    widget.listen(events)
                if widget.contains(*Mouse.getMousePos()):
                    blocked = True

        def hide(self):
            for widget in self:
                widget.hide()

        def show(self):
            for widget in self:
                widget.show()

    class Menu:
        def __init__(self, win, filename="", pos=(WIDTH//2, HEIGHT//2),
                     size=(WIDTH//2, HEIGHT//2), fill=(60, 60, 60), title="",
                     text_color=WHITE_COLOR):
            self.win = win
            self.image = None
            if filename:
                menu = pg.image.load(filename)  # загрузка картинок для меню
                self.image = pg.transform.scale(menu, size)  # изменение размера
                self.rect = self.image.get_rect(center=pos)
            else:
                self.rect = pg.Rect(0, 0, *size)
                self.rect.center = pos
            self.fill = fill
            self.title = Text(win=win, text=title, color=text_color, font_size=60,
                              x=self.rect.centerx, y=self.rect.top+40)
            self.title.set_italic(True)
            self.title.set_bold(True)
            self.buttons = ButtonGroup()
            self.widgets = WidgetGroup()

        def add_button(self, button):
            self.buttons.add(button)

        def add_widget(self, widget):
            self.widgets.add(widget)

        def draw(self):
            if self.image is None:
                pg.draw.rect(self.win, self.fill, self.rect)
            else:
                self.win.blit(self.image, self.rect)
            self.title.draw()
            self.buttons.draw()
            self.widgets.draw()

        def run(self):
            play = True
            self.widgets.show()
            while play:
                events = pg.event.get()
                for event in events:
                    if event.type == pg.QUIT:
                        sys.exit()
                    if event.type == pg.KEYDOWN:
                        sounds.control(event.key)
                        if event.key == pg.K_ESCAPE:
                            play = False

                self.draw()
                self.widgets.update(events)
                self.buttons.update(events)
                pg.display.update(self.rect)
                clock.tick(60)
            self.widgets.hide()

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

    background = pg.transform.scale(
        pg.image.load("animations/map.png"), (WIDTH, HEIGHT))

    hero = AnimationWalkSprite(center_x=400, center_y=300, speed=5, size=(60, 100))

    coins = pg.sprite.Group()
    for n in range(10):
        coin = AnimationTimeSprite(center_x=randint(30, WIDTH - 30),
                                   center_y=randint(30, HEIGHT - 30),
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

    main_menu = Menu(win=screen, filename="Sprite/base_menu.png",
                     title="Main Menu", text_color=(0, 0, 0))
    menu_settings = Menu(win=screen, filename="Sprite/base_menu.png",
                         title="Settings", text_color=(0, 0, 0))
    main_menu.add_button(
        Button(win=screen, filename="", pos=(WIDTH // 2, HEIGHT // 2 - 40),
               size=(150, 60), text="Settings", on_click=menu_settings.run,
               text_color=WHITE_COLOR, fill=(200, 50, 50))
    )
    main_menu.add_button(
        Button(win=screen, filename="", pos=(WIDTH // 2, HEIGHT // 2 + 60),
               size=(150, 60), text="Quit", on_click=sys.exit,
               text_color=WHITE_COLOR, fill=(50, 200, 50))
    )

    slider = MySlider(screen, WIDTH // 2 + 80, HEIGHT // 2, 100, 10)
    menu_settings.add_widget(slider)

    play = True
    while play:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                sounds.control(event.key)
                if event.key == pg.K_ESCAPE:
                    main_menu.run()

        screen.blit(background, (0, 0))
        sounds.set_volume(slider.getValue() / 100)

        hero.update()
        hero.update_frame()
        hero.draw(screen)

        coins.update()
        coins.draw(screen)

        colisions = pg.sprite.spritecollide(hero, coins, True)
        for _ in colisions:
            score += 1
            score_text.update(f"Score: {score}")
            point.set_volume(slider.getValue() / 100)
            point.play()

        text_group.draw()
        pg.display.update()
        clock.tick(60)

ex2()

"""
FONT_head = pg.font.Font(#шрифт,#размер текста)
-создание экзампляра класса со шрифтом

text_head = FONT_head.render(#текст, #сглаживание,
    #цвет текста,##цвет фона для текста)
    -преобразование текста в картинку

text_rect_head = text_head.get_rect(center= (395,180))
-получение из картинки с текстом экземпляра класса Rect

FONT_head.set_bold(True) -установка жирности на шрифт
FONT_head.set_italic(True) -установка курсива на шрифт

pg.display.update(#объект класса Rect)
-обновления только части экрана(часть экрана -прямоугольник(объект класса Rect))
"""