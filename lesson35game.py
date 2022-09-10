def ex1():
    import pygame as pg
    import sys
    pg.init()#используется для старта модуля pygame
    pg.display.set_caption("Animation")#заданиезагаловкаокну
    screen = pg.display.set_mode((800,600))#создание поверхности с указанными размерами и параметрами
    clock = pg.time.Clock()#создаем экземпляр класса для управление времени(кадрами игры (fps))
    font = pg.font.Font(None,48)
    text = ""#переменная для записи текста пользователя
    color = (200,200,200)
    color_active = (50,50,200)
    color_inactive = (200,200,200)
    active = False
    input_box = pg.Rect(325,273,150,55)
    play = True
    while play:
        for event in pg.event.get():
            if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                sys.exit()  # функция выхода из игры и закрытия всех окон()
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):#если происходит коллизия между положением мышки и полем для ввода
                    active = not active#переводим поле в активное состояние
                else:
                    active = False#переводим поле в неактивное состояние
                color = color_active if active else color_inactive#выбираемцветполя
            if event.type == pg.KEYDOWN and active:
                if event.key == pg.K_RETURN:#если нажали enter печатаем текст в консоль и сбрасываем переменную
                    print(text)
                    text = ''
                elif event.key ==pg.K_BACKSPACE:#удаляем послдений символ
                    text = text[:-1]
                else:
                    text += event.unicode #записываем текст используя дешифратор unicode
        screen.fill((30,30,30))
        text_img = font.render(text,True,color)
        width = max(input_box.width,text_img.get_width()+10)#сравниваем ширину вводимого текста и изначального поля
        input_box.width =width#присваиваем набиольшую ширину
        screen.blit(text_img,(input_box.x+5,input_box.y+10))
        pg.draw.rect(screen, color, input_box,2)
        pg.display.update()

# ex1()

def ex2():
    import pygame as pg
    import sys
    pg.init()  # используется для старта модуля pygame
    pg.display.set_caption("Animation")  # задание заголовка окну
    WIDTH = 800
    HEIGHT = 600
    screen = pg.display.set_mode((WIDTH, HEIGHT))  # создание поверхности с указанными размерами и параметрами
    clock = pg.time.Clock()  # создаем экземпляр класса для управление времени(кадрами игры (fps))

    class InputBox:
        def __init__(self, x, y, width=250, height=50, place_holder_text="input here...",
                     font=None, font_size=48, style=None):
            self.font = pg.font.Font(font, font_size)
            self.place_holder_text = place_holder_text
            default_style = {
                "text_color": (200, 200, 200),
                "holder_text": (150, 50, 80),
                "background": (50, 50, 50),
                "border_width": 2,
                "color_active": (50, 50, 200),
                "border_color": (200, 200, 200),
                "padding": 5,
                "align_text": "center"
            }
            self.style = default_style if style is None else style
            one_symbol = self.font.render("X", True, (0, 0, 0))
            default_width = one_symbol.get_width()
            default_height = one_symbol.get_height()
            if "padding" in self.style:
                default_width += self.style["padding"] * 2
                default_height += self.style["padding"] * 2
            self.width = width if width and width > default_width else default_width
            self.height = height if height and height > default_height else default_height
            self.input_box = pg.Rect(x, y, self.width, self.height)
            self.input_text = ""  # переменная для записи текста пользователя
            self.active = False
            self.text = ""

        def cut_text(self):
            text = self.input_text if self.active or self.input_text else self.place_holder_text
            max_length = len(text)
            width = self.width
            if "padding" in self.style:
                width -= self.style["padding"] * 2
            else:
                width -= 2
            while self.font.render(text, True, (0, 0, 0)).get_width() > width:
                max_length -= 1
                text = text[-max_length:]
            self.text = text

        def update(self, events):
            for event in events:
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.active = self.input_box.collidepoint(event.pos)
                if self.active and event.type == pg.KEYDOWN:
                    if event.key in (pg.K_RETURN, pg.K_ESCAPE):
                        self.active = False
                    elif event.key == pg.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    else:
                        self.input_text += event.unicode  # записываем текст используя дешифратор unicode
            self.cut_text()

        def draw(self, win):
            try:
                if self.input_text:
                    image = self.font.render(self.text, True, self.style["text_color"])
                else:
                    image = self.font.render(self.text, True, self.style["holder_text"])
                border_color = self.style["color_active"] if self.active else self.style["border_color"]
                if "background" in self.style and self.style["background"] is not None:
                    pg.draw.rect(win, self.style["background"], self.input_box)
                pg.draw.rect(win, border_color, self.input_box, self.style["border_width"])
                if "align_text" in self.style and self.style["align_text"] == "center":
                    rect = image.get_rect(center=self.input_box.center)
                    win.blit(image, rect)
                elif "padding" in self.style:
                    win.blit(image, (self.input_box.x + self.style["padding"],
                                     self.input_box.y + self.style["padding"]))
                else:
                    win.blit(image, (self.input_box.x + 1, self.input_box.y + 1))
            except Exception as e:
                print("Error with InputBox:", e)

        def get_text(self):
            return self.input_text

        def clear(self):
            self.input_text = ""

    class Text:
        def __init__(self, win, x, y, font=None, font_size=50, text="Test",
                     color=(250, 250, 250), background=None):
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

    class Button:
        def __init__(self, win, filename="", pos=(WIDTH//2, HEIGHT//2),
                     size=(WIDTH//8, HEIGHT//8), on_click=(lambda: None), text="",
                     text_color=(250, 250, 250), fill=(0, 0, 0)):
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
                    if event.button == 1 and self.rect.collidepoint(event.pos):
                        self.on_click()

    input_box = InputBox(x=WIDTH//2-150, y=HEIGHT//2-30, width=300, height=10)
    button = Button(win=screen, pos=(WIDTH // 2, HEIGHT // 2 + 100), size=(150, 60),
                    text="PRINT", fill=(200, 50, 50), )
    button.on_click = lambda: print(input_box.get_text())
    button2 = Button(win=screen, pos=(WIDTH // 2, HEIGHT // 2 + 180), size=(150, 60),
                     text="CLEAR", fill=(20, 50, 150), on_click=input_box.clear)

    play = True
    while play:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                sys.exit()

        screen.fill((30, 30, 30))

        input_box.update(events)
        input_box.draw(screen)

        button.update(events)
        button.draw()

        button2.update(events)
        button2.draw()

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
    FONT_head = pg.font.Font(None, 35)
    FONT_button = pg.font.Font(None, 29)
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
    menu_esc = pg.transform.scale(menu_esc, (350, 350))  # изменение размера
    menu_esc_rect = menu_esc.get_rect(center=(400, 300))  # получение объекта класса рект и установка координат на центр

    button = pg.image.load("Sprite/base_menu.png")  # загрузка картинок для меню
    button = pg.transform.scale(button, (200, 40))  # изменение размера
    button_rect = button.get_rect(center=(400, 240))  # получение объекта класса рект и установка координат на центр

    base_menu = pg.image.load("Sprite/base_menu.png")  # загрузка картинок для меню
    base_menu = pg.transform.scale(base_menu, (350, 350))  # изменение размера
    base_menu_rect = base_menu.get_rect(
        center=(400, 300))  # получение объекта класса рект и установка координат на центр

    start_pic = pg.image.load("Sprite/place.png")  # загрузка картинок для меню
    start_pic = pg.transform.scale(start_pic, (800, 600))  # изменение размера
    start_pic_rect = base_menu.get_rect()  # получение объекта класса рект и установка координат на центр

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

    names = {}

    def start_window_menu():
        text_menu = FONT_head.render("Menu", True, (0, 0, 0))
        text_menu_rect = text_menu.get_rect(center=(395, 180))

        text_start = FONT_button.render("Start", True, (0, 0, 0))
        text_start_rect = text_start.get_rect(center=(400, 240))

        screen.blit(start_pic, start_pic_rect)

        screen.blit(base_menu, base_menu_rect)
        screen.blit(button, button_rect)

        screen.blit(text_menu, text_menu_rect)

        screen.blit(text_start, text_start_rect)
        play = True
        while play:
            for event in pg.event.get():
                if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                    sys.exit()  # функция выхода из игры и закрытия всех окон()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        play = False
            pg.display.update()

    def start_window_registration():
        # параметры для поля ввода
        nonlocal SCORE
        text = ""
        color = (200, 200, 200)
        color_active = (50, 50, 200)
        color_inactive = (200, 200, 200)
        active = False
        input_box = pg.Rect(325, 273, 150, 55)

        text_menu = FONT_head.render("Menu", True, (0, 0, 0))
        text_menu_rect = text_menu.get_rect(center=(395, 180))

        text_name = FONT_button.render("Input your name", True, (0, 0, 0))
        text_name_rect = text_name.get_rect(center=(400, 240))

        # text_start = FONT_button.render("Start", True, (0, 0, 0))
        # text_start_rect = text_start.get_rect(center=(400,240))

        screen.blit(start_pic, start_pic_rect)

        screen.blit(base_menu, base_menu_rect)
        # screen.blit(button, button_rect)

        screen.blit(text_menu, text_menu_rect)
        screen.blit(text_name, text_name_rect)
        # screen.blit(text_start, text_start_rect)

        pg.display.update()
        play = True
        while play:
            for event in pg.event.get():
                if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                    sys.exit()  # функция выхода из игры и закрытия всех окон()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pg.KEYDOWN and active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        names[text] = SCORE
                        text = ''
                        print(names)
                        play = False
                        start_window_menu()

                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

            text_img = FONT_button.render(text, True, color)

            width = max(input_box.width, text_img.get_width() + 10)
            input_box.width = width

            screen.blit(text_img, (input_box.x + 5, input_box.y + 10))

            pg.draw.rect(screen, color, input_box, 2)

            pg.display.update()

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

            pg.display.update(menu_esc_rect)

    def draw_menu():  # функция с бесконечным циклом для меню
        play = True
        while play:
            events = pg.event.get()
            for event in events:  # отслеживание всех событий которые происходят на игровом дисплее
                if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                    sys.exit()  # функция выхода из игры и закрытия всех окон(
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 340 < event.pos[0] < 465 and 250 < event.pos[
                            1] < 280:  # если позиция мышки находится в нужных координатах
                            play = False
                        if 340 < event.pos[0] < 465 and 306 < event.pos[1] < 336:
                            draw_setting()
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

    start_window_registration()

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

# ex3()

def ex4():
    import pygame as pg
    from random import randint
    import sys, os
    from time import time
    import pygame_widgets
    from pygame_widgets.slider import Slider
    from pygame_widgets.mouse import Mouse

    WIDTH, HEIGHT = 800, 600
    pg.init()
    pg.display.set_caption("Input Box")
    screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
    clock = pg.time.Clock()
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BlACK = (0, 0, 0)
    
    IMG_BACK = f"animations{os.sep}map.png"
    IMG_BACK2 = f"Sprite{os.sep}place.png"
    IMG_MENU = f"Sprite{os.sep}base_menu.png"
    IMG_COIN = f"timeanim{os.sep}coinanim.png"

    SCORE_BASE = "players_score.txt"

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

    class Group(list):
        def add(self, element) -> None:
            super().append(element)

        def draw(self, *args, **kwargs):
            for element in self:
                element.draw(*args, **kwargs)

        def update(self, *args, **kwargs):
            for element in self:
                element.update(*args, **kwargs)

    class Text:
        def __init__(self, win, x, y, font=None, font_size=50, text="Test",
                     color=WHITE, background=None):
            # создаем шрифт
            self.font = pg.font.Font(font, font_size)
            # Картинка из шрифта
            self.color = color
            self.background = background
            self.image = self.font.render(str(text), 1, self.color, self.background)
            self.rect = self.image.get_rect(center=(x, y))
            self.win = win

        def update(self, text):
            self.image = self.font.render(str(text), True, self.color, self.background)

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
                self.channel = None

        def add(self, filename):
            self.sounds.append(pg.mixer.Sound(filename))

        def stop(self):
            if self.current_sound is not None:
                self.sounds[self.current_sound].stop()
                self.is_playing = False

        def play_current(self):
            if self.current_sound is not None:
                self.sounds[self.current_sound].set_volume(self.volume)
                self.channel = self.sounds[self.current_sound].play(loops=-1)
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
                if self.is_playing and self.channel is not None:
                    self.channel.pause()
                    self.is_playing = False
                else:
                    self.channel.unpause()
                    self.is_playing = True
            comand = {pg.K_r: self.stop, pg.K_l: self.play, pg.K_n: self.play_next}
            if key in comand:
                comand[key]()
            comand2 = (pg.K_1, pg.K_2, pg.K_3, pg.K_4)
            if key in comand2:
                self.play(comand2.index(key))

    class MySlider(Slider):
        def __init__(self, win, x, y, width, height):
            super().__init__(win=win, x=x - width // 2, y=y - height // 2,
                             width=width, height=height)
            self.text = Text(win=win, x=(x - 100 - width // 2), y=y,
                             font_size=30, text=f"Volume: {self.getValue()}%",
                             color=(0, 0, 0))

        def draw(self):
            super().draw()
            self.text.update(f"Volume: {self.getValue()}%")
            self.text.draw()

    class Button:
        def __init__(self, win, filename="", pos=(WIDTH // 2, HEIGHT // 2),
                     size=(WIDTH // 8, HEIGHT // 8), on_click=(lambda: None), text="",
                     text_color=WHITE, fill=BlACK):
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
        def __init__(self, win, filename="", pos=(WIDTH // 2, HEIGHT // 2),
                     size=(WIDTH // 2, HEIGHT // 2), fill=(60, 60, 60), title="",
                     text_color=WHITE, back=None):
            self.win = win
            self.image = None
            self.background = back
            if filename:
                menu = pg.image.load(filename)  # загрузка картинок для меню
                self.image = pg.transform.scale(menu, size)  # изменение размера
                self.rect = self.image.get_rect(center=pos)
            else:
                self.rect = pg.Rect(0, 0, *size)
                self.rect.center = pos
            self.fill = fill
            self.title = Text(win=win, text=title, color=text_color, font_size=60,
                              x=self.rect.centerx, y=self.rect.top + 40)
            self.title.set_italic(True)
            self.title.set_bold(True)
            self.buttons = Group()
            self.widgets = WidgetGroup()
            self.play = True

        def add_button(self, button):
            self.buttons.add(button)

        def add_widget(self, widget):
            self.widgets.add(widget)

        def draw(self):
            if self.background is not None:
                self.win.blit(self.background, (0, 0))
            if self.image is None:
                pg.draw.rect(self.win, self.fill, self.rect)
            else:
                self.win.blit(self.image, self.rect)
            self.title.draw()
            self.buttons.draw()
            self.widgets.draw()

        def run(self):
            self.play = True
            self.widgets.show()
            while self.play:
                events = pg.event.get()
                for event in events:
                    if event.type == pg.QUIT:
                        game_quit()
                    if event.type == pg.KEYDOWN:
                        # sounds.control(event.key)
                        if event.key == pg.K_ESCAPE:
                            self.play = False

                self.draw()
                self.widgets.update(events)
                self.buttons.update(events)
                if self.background is not None:
                    pg.display.update()
                else:
                    pg.display.update(self.rect)
                clock.tick(60)
            self.widgets.hide()

        def stop(self):
            self.play = False

    class AnimationTimeSprite(pg.sprite.Sprite):
        def __init__(self, center_x, center_y, speed, frames):
            super().__init__()
            self.frames = frames
            self.image = self.frames[0]
            self.rect = self.image.get_rect(center=(center_x, center_y))
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

    class InputBox:
        def __init__(self, win, x, y, width=250, height=50, place_holder_text="input here...",
                     font=None, font_size=48, style=None):
            self.win = win
            self.font = pg.font.Font(font, font_size)
            self.place_holder_text = place_holder_text
            default_style = {
                "text_color": (200, 200, 200),
                "holder_text": (150, 50, 80),
                "background": (50, 50, 50),
                "border_width": 2,
                "color_active": (50, 50, 200),
                "border_color": (200, 200, 200),
                "padding": 5,
                "align_text": "center"
            }
            self.style = default_style if style is None else style
            one_symbol = self.font.render("X", True, (0, 0, 0))
            default_width = one_symbol.get_width()
            default_height = one_symbol.get_height()
            if "padding" in self.style:
                default_width += self.style["padding"] * 2
                default_height += self.style["padding"] * 2
            self.width = width if width and width > default_width else default_width
            self.height = height if height and height > default_height else default_height
            self.input_box = pg.Rect(x, y, self.width, self.height)
            self.input_text = ""  # переменная для записи текста пользователя
            self.active = False
            self.text = ""

        def cut_text(self):
            text = self.input_text if self.active or self.input_text else self.place_holder_text
            max_length = len(text)
            width = self.width
            if "padding" in self.style:
                width -= self.style["padding"] * 2
            else:
                width -= 2
            while self.font.render(text, True, (0, 0, 0)).get_width() > width:
                max_length -= 1
                text = text[-max_length:]
            self.text = text

        def update(self, events):
            for event in events:
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.active = self.input_box.collidepoint(event.pos)
                if self.active and event.type == pg.KEYDOWN:
                    if event.key in (pg.K_RETURN, pg.K_ESCAPE):
                        self.active = False
                    elif event.key == pg.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    else:
                        self.input_text += event.unicode  # записываем текст используя дешифратор unicode
            self.cut_text()

        def draw(self):
            try:
                if self.input_text:
                    image = self.font.render(self.text, True, self.style["text_color"])
                else:
                    image = self.font.render(self.text, True, self.style["holder_text"])
                border_color = self.style["color_active"] if self.active else self.style["border_color"]
                if "background" in self.style and self.style["background"] is not None:
                    pg.draw.rect(self.win, self.style["background"], self.input_box)
                pg.draw.rect(self.win, border_color, self.input_box, self.style["border_width"])
                if "align_text" in self.style and self.style["align_text"] == "center":
                    rect = image.get_rect(center=self.input_box.center)
                    self.win.blit(image, rect)
                elif "padding" in self.style:
                    self.win.blit(image, (self.input_box.x + self.style["padding"],
                                     self.input_box.y + self.style["padding"]))
                else:
                    self.win.blit(image, (self.input_box.x + 1, self.input_box.y + 1))
            except Exception as e:
                print("Error with InputBox:", e)

        def get_text(self):
            return self.input_text

        def clear(self):
            self.input_text = ""

    class ScoreBase:
        filename = SCORE_BASE
        players_score = {"Noname": 0}
        player_name = "Noname"

        @classmethod
        def init(cls):
            # Создать файл если отсутствует
            if not os.path.exists(SCORE_BASE):
                open(SCORE_BASE, "w").close()

        @classmethod
        def write(cls):
            with open(cls.filename, "w", encoding='utf-8') as file:
                print(cls.players_score, end="", file=file)

        @classmethod
        def read(cls):
            with open(cls.filename, "r", encoding='utf-8') as file:
                data = file.read()
                if data:
                    cls.players_score = eval(data)

        @classmethod
        def add_player_name(cls, box: InputBox, menu: Menu):
            if box.get_text():
                cls.player_name = box.get_text()
            cls.players_score[cls.player_name] = 0
            # print(cls.players_score[cls.player_name])
            menu.stop()

        @classmethod
        def get_score(cls):
            return cls.players_score[cls.player_name]

        @classmethod
        def up_score(cls):
            cls.players_score[cls.player_name] += 1

    def game_quit():
        ScoreBase.write()
        sys.exit()

    background = pg.transform.scale(pg.image.load(IMG_BACK), (WIDTH, HEIGHT))

    hero = AnimationWalkSprite(center_x=400, center_y=300, speed=5, size=(60, 100))

    coins = pg.sprite.Group()
    for n in range(10):
        coin = AnimationTimeSprite(center_x=randint(30, WIDTH - 30),
                                   center_y=randint(30, HEIGHT - 30), speed=30,
                                   frames=load_frames(IMG_COIN, row=2, col=3, size=(30, 30)))
        coins.add(coin)

    point = pg.mixer.Sound(f"Sound{os.sep}point.wav")
    point.set_volume(0.3)

    sounds = Sound()  # создаем сингелтон объект для управления музыкой
    sounds.add(f"Sound{os.sep}gamesound.wav")
    sounds.add(f"Sound{os.sep}cowboy.wav")
    sounds.add(f"Sound{os.sep}happy.wav")
    sounds.add(f"Sound{os.sep}sample.wav")
    sounds.play()

    main_menu = Menu(win=screen, filename=IMG_MENU, title="Main Menu", text_color=BlACK)
    menu_settings = Menu(win=screen, filename=IMG_MENU, title="Settings", text_color=BlACK)
    main_menu.add_button(
        Button(win=screen, filename="", pos=(WIDTH // 2, HEIGHT // 2 - 40),
               size=(150, 60), text="Settings", on_click=menu_settings.run,
               text_color=WHITE, fill=(200, 50, 50))
    )
    main_menu.add_button(
        Button(win=screen, filename="", pos=(WIDTH // 2, HEIGHT // 2 + 60),
               size=(150, 60), text="Quit", on_click=game_quit,
               text_color=WHITE, fill=(50, 200, 50))
    )

    slider = MySlider(screen, WIDTH // 2 + 80, HEIGHT // 2, 100, 10)
    menu_settings.add_widget(slider)

    background2 = pg.transform.scale(pg.image.load(IMG_BACK2), (WIDTH, HEIGHT))
    start_menu = Menu(win=screen, filename=IMG_MENU, title="Enter Name", text_color=BlACK,
                      back=background2)

    input_box = InputBox(win=screen, x=WIDTH // 2 - 120, y=HEIGHT // 2 - 70, width=250)
    start_menu.add_button(input_box)
    start_menu.add_button(
        Button(win=screen, filename=IMG_MENU, pos=(WIDTH // 2, HEIGHT // 2 + 60),
               size=(150, 60), text="Start",
               on_click=lambda: ScoreBase.add_player_name(input_box, start_menu),
               text_color=BlACK, fill=(50, 200, 50))
    )

    ScoreBase.init()
    ScoreBase.read()  # чтение файла с достижениями
    start_menu.run()

    text_group = Group()
    name_text = Text(win=screen, text=f"Name: {ScoreBase.player_name}", x=WIDTH - 180, y=30)
    text_group.append(name_text)
    score_text = Text(win=screen, text=f"Score: {ScoreBase.get_score()}", x=80, y=30)
    text_group.append(score_text)

    play = True
    while play:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                game_quit()
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
            ScoreBase.up_score()
            score_text.update(f"Score: {ScoreBase.get_score()}")
            point.set_volume(slider.getValue() / 100)
            point.play()

        text_group.draw()
        pg.display.update()
        clock.tick(60)

# ex4()

"""
input box
"""