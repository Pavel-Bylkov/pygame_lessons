def ex1():
    import pygame as pg
    import sys  # модуль для выхода из игры и закрытия всех окон
    from pygame.sprite import Group
    from random import randint
    import pygame_widgets
    from pygame_widgets.slider import Slider
    from pygame_widgets.textbox import TextBox
    import time

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

    # инициализация переменных для создания светого слоя
    NIGHT_COLOR = (20, 20, 20)
    fog = pg.Surface((800, 600))  # создание доп поверхности
    fog.fill((NIGHT_COLOR))  # заливка
    night = False

    light_mask = pg.image.load("Lights/light_350_med.png").convert_alpha()  # загрузка луча в проект
    light_mask = pg.transform.scale(light_mask, (300, 300))
    light_mask_rect = light_mask.get_rect()

    static_light_mask = pg.image.load("Lights/Vector_Smar33t_Objec.png").convert_alpha()  # загрузка луча в проект
    static_light_mask = pg.transform.scale(static_light_mask, (100, 100))
    static_light_mask_rect = static_light_mask.get_rect()
    start_time_static = 0

    dinamic_light_mask = pg.image.load("Lights/light_350_hard.png").convert_alpha()  # загрузка луча в проект
    dinamic_light_mask = pg.transform.scale(dinamic_light_mask, (150, 150))
    dinamic_light_mask_rect = dinamic_light_mask.get_rect()
    dinamic_light_speed_y = 2
    dinamic_light_speed_x = 2
    dinamic_light_direction = [dinamic_light_speed_x, dinamic_light_speed_y]

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
    stand_rect = stand.get_rect(center=(100, 100))

    sound1 = pg.mixer.Sound("Sound/gamesound.wav")
    sound1.set_volume(0.3)

    sound2 = pg.mixer.Sound("Sound/cowboy.wav")
    sound2.set_volume(0.3)

    sound3 = pg.mixer.Sound("Sound/happy.wav")
    sound3.set_volume(0.3)

    sound4 = pg.mixer.Sound("Sound/sample.wav")
    sound4.set_volume(0.3)

    soundSirena = pg.mixer.Sound("Sound/sample.wav")
    soundSirena.set_volume(0.7)
    point = pg.mixer.Sound("Sound/point.wav")

    apple_group = Group()

    slider_value = slider.getValue()

    names = {}

    def update_dinamic_light_mask():
        nonlocal dinamic_light_speed_x, dinamic_light_speed_y, dinamic_light_direction
        if dinamic_light_mask_rect.right > 820:
            dinamic_light_speed_x *= -1
        if dinamic_light_mask_rect.left < -20:
            dinamic_light_speed_x *= -1
        if dinamic_light_mask_rect.top < -20:
            dinamic_light_speed_y *= -1
        if dinamic_light_mask_rect.bottom > 620:
            dinamic_light_speed_y *= -1
        dinamic_light_direction = [dinamic_light_speed_x, dinamic_light_speed_y]
        dinamic_light_mask_rect.move_ip(dinamic_light_direction)
        collision = pg.Rect.colliderect(stand_rect, dinamic_light_mask_rect)
        if collision:
            dinamic_light_mask_rect.center = stand_rect.center
        return collision

    def render_fog(chek):  # функция для отображения тумана на основной поверхности
        fog.fill(NIGHT_COLOR)
        fog.blit(dinamic_light_mask, dinamic_light_mask_rect)  # отображение луча на поверхности с туманом
        if chek and time.time() % 1 > 0.5:
            fog.blit(static_light_mask, (50, 50))
            fog.blit(static_light_mask, (700, 50))
            fog.blit(static_light_mask, (50, 500))
            fog.blit(static_light_mask, (700, 500))
        screen.blit(fog, (0, 0),
                    special_flags=pg.BLEND_MULT)  # наложение поверхности с туманом на основную с перемножением светимости пикселей

    def render_static_lights():
        pass

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
            screen.blit(animation_right[index // 10], stand_rect)
        elif keys[pg.K_a]:
            screen.blit(animation_left[index // 10], stand_rect)
        elif keys[pg.K_w]:
            screen.blit(animation_right[index // 10], stand_rect)
        elif keys[pg.K_s]:
            screen.blit(animation_left[index // 10], stand_rect)
        else:
            screen.blit(stand, stand_rect)
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
                if event.key == pg.K_n:
                    if night:
                        night = False
                    else:
                        night = True
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
        update(keys, stand_rect)
        if night:
            check = update_dinamic_light_mask()
            render_fog(check)
            if check:
                soundSirena.play(-1)
            else:
                soundSirena.stop()

        for sprite in apple_group:
            collision = pg.Rect.colliderect(stand_rect, sprite.rect)
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
    import sys  # модуль для выхода из игры и закрытия всех окон

    pg.init()  # используется для старта модуля pygame
    pg.display.set_caption("Animation")  # задание загаловка окну
    screen = pg.display.set_mode((800, 600))  # создание поверхности с указанными размерами и параметрами
    clock = pg.time.Clock()  # создаем экземпляр класса для управление времени(кадрами игры (fps))

    NIGHT_COLOR = (20, 20, 20)
    fog = pg.Surface((800, 600))  # создание доп поверхности
    fog.fill((NIGHT_COLOR))  # заливка

    light_mask = pg.image.load("Lights/light_350_med.png").convert_alpha()  # загрузка луча в проект
    light_mask = pg.transform.scale(light_mask, (300, 300))
    light_mask_rect = light_mask.get_rect()

    def render_fog():  # функция для отображения тумана на основной поверхности
        fog.fill(NIGHT_COLOR)
        light_mask_rect.center = stand_rect.center  # присваивание координаты луча к координате игрока
        fog.blit(light_mask, light_mask_rect)  # отображение луча на поверхности с туманом
        screen.blit(fog, (0, 0),
                    special_flags=pg.BLEND_MULT)  # наложение поверхности с туманом на основную с перемножением светимости пикселей

    animation_right = [pg.transform.scale(pg.image.load(f"animations/r{i}.png"), (60, 100)) for i in range(1, 7)]
    animation_left = [pg.transform.scale(pg.image.load(f"animations/l{i}.png"), (60, 100)) for i in range(1, 7)]

    map = pg.image.load("animations/map.png")
    map = pg.transform.scale(map, (800, 600))

    stand = pg.image.load("animations/0.png")
    stand = pg.transform.scale(stand, (60, 100))
    stand_rect = stand.get_rect(center=(100, 100))

    def update(keys, person):
        if keys[pg.K_d]:
            person.centerx += 5  # обращение к точке элемента объекта класса
        if keys[pg.K_w]:
            person.centery -= 5
        if keys[pg.K_s]:
            person.centery += 5
        if keys[pg.K_a]:
            person.centerx -= 5

    def draw(screen, keys):
        nonlocal index
        if keys[pg.K_d]:
            screen.blit(animation_right[index // 10], stand_rect)
        elif keys[pg.K_a]:
            screen.blit(animation_left[index // 10], stand_rect)
        elif keys[pg.K_w]:
            screen.blit(animation_right[index // 10], stand_rect)
        elif keys[pg.K_s]:
            screen.blit(animation_left[index // 10], stand_rect)
        else:
            screen.blit(stand, stand_rect)
        index += 2
        if index == 60:
            index = 0

    night = False
    index = 0
    play = True
    while play:  # основной цикл игры
        events = pg.event.get()
        for event in events:  # отслеживание всех событий которые происходят на игровом дисплее
            if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                sys.exit()  # функция выхода из игры и закрытия всех окон(
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_n:
                    if night:
                        night = False
                    else:
                        night = True

        screen.blit(map, (0, 0))
        keys = pg.key.get_pressed()
        if night:
            render_fog()
        draw(screen, keys)
        update(keys, stand_rect)

        pg.display.update()
        clock.tick(60)

# ex2()

def ex3():
    import pygame as pg
    import sys  # модуль для выхода из игры и закрытия всех окон

    pg.init()  # используется для старта модуля pygame
    pg.display.set_caption("Animation")  # задание загаловка окну
    WIDTH, HEIGHT = 800, 600
    screen = pg.display.set_mode((WIDTH, HEIGHT))  # создание поверхности с указанными размерами и параметрами
    clock = pg.time.Clock()  # создаем экземпляр класса для управление времени(кадрами игры (fps))

    NIGHT_COLOR = (20, 20, 20)
    HARD = "Lights/light_350_hard.png"
    MIDLE = "Lights/light_350_med.png"
    SOFT = "Lights/light_350_soft.png"

    class LightLayer(list):
        def __init__(self, width, height, ambient_color=NIGHT_COLOR):
            super().__init__()
            self.surface = pg.Surface((width, height))  # создание доп поверхности
            self.ambient_color = ambient_color
            self.active = True

        def add(self, light):
            self.append(light)

        def remove(self, light):
            super().remove(light)

        def update(self):
            for light in self:
                light.update()

        def switch_visible(self):
            self.active = not self.active

        def draw(self, win):
            if self.active:
                self.surface.fill(self.ambient_color)  # заливка
                for light in self:
                    light.draw(self.surface)  # отображение луча на поверхности с туманом
                win.blit(self.surface, (0, 0), special_flags=pg.BLEND_MULT)

    class Light:
        def __init__(self, center_x, center_y, radius, img):
            image = pg.image.load(img).convert_alpha()
            self.image = pg.transform.scale(image, (radius*2, radius*2))
            self.rect = self.image.get_rect(center=(center_x, center_y))
            self.active = True

        def update(self):
            pass

        def set_position(self, x, y):
            self.rect.center = (x, y)

        def switch_visible(self):
            self.active = not self.active

        def draw(self, surface):
            if self.active:
                surface.blit(self.image, self.rect)

    animation_right = [pg.transform.scale(pg.image.load(f"animations/r{i}.png"), (60, 100)) for i in range(1, 7)]
    animation_left = [pg.transform.scale(pg.image.load(f"animations/l{i}.png"), (60, 100)) for i in range(1, 7)]

    map = pg.image.load("animations/map.png")
    map = pg.transform.scale(map, (800, 600))

    stand = pg.image.load("animations/0.png")
    stand = pg.transform.scale(stand, (60, 100))
    stand_rect = stand.get_rect(center=(100, 100))

    def update(keys, person):
        if keys[pg.K_d]:
            person.centerx += 5  # обращение к точке элемента объекта класса
        if keys[pg.K_w]:
            person.centery -= 5
        if keys[pg.K_s]:
            person.centery += 5
        if keys[pg.K_a]:
            person.centerx -= 5

    def draw(screen, keys):
        nonlocal index
        if keys[pg.K_d]:
            screen.blit(animation_right[index // 10], stand_rect)
        elif keys[pg.K_a]:
            screen.blit(animation_left[index // 10], stand_rect)
        elif keys[pg.K_w]:
            screen.blit(animation_right[index // 10], stand_rect)
        elif keys[pg.K_s]:
            screen.blit(animation_left[index // 10], stand_rect)
        else:
            screen.blit(stand, stand_rect)
        index += 2
        if index == 60:
            index = 0


    light_layer = LightLayer(WIDTH, HEIGHT, NIGHT_COLOR)
    light_layer.active = False
    player_light = Light(center_x=0, center_y=0, radius=200, img=MIDLE)
    light_layer.add(player_light)

    index = 0
    play = True
    while play:  # основной цикл игры
        events = pg.event.get()
        for event in events:  # отслеживание всех событий которые происходят на игровом дисплее
            if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                sys.exit()  # функция выхода из игры и закрытия всех окон(
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_n:
                    light_layer.switch_visible()
                if event.key == pg.K_SPACE:
                    player_light.switch_visible()

        screen.blit(map, (0, 0))
        keys = pg.key.get_pressed()

        draw(screen, keys)
        update(keys, stand_rect)
        player_light.set_position(stand_rect.centerx, stand_rect.centery)

        light_layer.update()
        light_layer.draw(screen)

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
    pg.display.set_caption("Menu")
    screen = pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
    clock = pg.time.Clock()
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BlACK = (0, 0, 0)

    IMG_BACK = f"animations{os.sep}map.png"
    IMG_BACK2 = f"Sprite{os.sep}place.png"
    IMG_MENU = f"Sprite{os.sep}base_menu.png"
    IMG_COIN = f"timeanim{os.sep}coinanim.png"

    NIGHT_COLOR = (20, 20, 20)
    HARD = f"Lights{os.sep}light_350_hard.png"
    MIDLE = f"Lights{os.sep}light_350_med.png"
    SOFT = f"Lights{os.sep}light_350_soft.png"

    STATIC = f"Lights{os.sep}Vector_Smar33t_Objec.png"
    DINAMIC = f"Lights{os.sep}light_350_hard.png"

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

        def get_position(self):
            return self.rect.centerx, self.rect.centery

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

    class LightLayer(list):
        def __init__(self, width, height, ambient_color=NIGHT_COLOR):
            super().__init__()
            self.surface = pg.Surface((width, height))  # создание доп поверхности
            self.ambient_color = ambient_color
            self.active = True

        def add(self, light):
            self.append(light)

        def remove(self, light):
            super().remove(light)

        def update(self):
            if self.active:
                for light in self:
                    light.update()

        def switch_visible(self):
            self.active = not self.active

        def draw(self, win):
            if self.active:
                self.surface.fill(self.ambient_color)  # заливка
                for light in self:
                    light.draw(self.surface)  # отображение луча на поверхности с туманом
                win.blit(self.surface, (0, 0), special_flags=pg.BLEND_MULT)

    class Light(pg.sprite.Sprite):
        def __init__(self, layer, center_x, center_y, radius, img):
            super().__init__()
            image = pg.image.load(img).convert_alpha()
            self.image = pg.transform.scale(image, (radius*2, radius*2))
            self.rect = self.image.get_rect(center=(center_x, center_y))
            self.active = True
            layer.add(self)

        def update(self):
            pass

        def set_position(self, x, y):
            self.rect.center = (x, y)

        def switch_visible(self):
            self.active = not self.active

        def draw(self, surface):
            if self.active:
                surface.blit(self.image, self.rect)

    class DinamicLight(Light):
        def __init__(self, layer, center_x, center_y, radius, img, speed):
            super().__init__(layer, center_x, center_y, radius, img)
            self.speed_x = speed
            self.speed_y = speed

        def update(self):
            if self.rect.left < -20 or self.rect.right > 820:
                self.speed_x *= -1
            if self.rect.top < -20 or self.rect.bottom > 620:
                self.speed_y *= -1
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y

    class StaticLight(Light):
        def __init__(self, layer, center_x, center_y, radius, img):
            super().__init__(layer, center_x, center_y, radius, img)
            self.active = False
            self.start = False

        def update(self):
            if self.start:
                if time() % 1 > 0.5:
                    self.active = True
                else:
                    self.active = False

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
            print(cls.players_score[cls.player_name])
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
    sound_sirena = pg.mixer.Sound(f"Sound{os.sep}sample.wav")
    sound_sirena.set_volume(0.7)

    sounds = Sound()  # создаем сингелтон объект для управления музыкой
    sounds.add(f"Sound{os.sep}gamesound.wav")
    sounds.add(f"Sound{os.sep}cowboy.wav")
    sounds.add(f"Sound{os.sep}happy.wav")
    sounds.add(f"Sound{os.sep}sample.wav")
    sounds.play()

    light_layer = LightLayer(WIDTH, HEIGHT, NIGHT_COLOR)
    light_layer.active = False
    player_light = Light(layer=light_layer, center_x=0, center_y=0, radius=100, img=MIDLE)
    dinamic_light = DinamicLight(layer=light_layer, center_x=100, center_y=100, radius=75, img=DINAMIC, speed=2)
    static_light1 = StaticLight(layer=light_layer, center_x=100, center_y=100, radius=100, img=STATIC)
    static_light2 = StaticLight(layer=light_layer, center_x=WIDTH-100, center_y=100, radius=100, img=STATIC)
    static_light3 = StaticLight(layer=light_layer, center_x=100, center_y=HEIGHT-100, radius=100, img=STATIC)
    static_light4 = StaticLight(layer=light_layer, center_x=WIDTH-100, center_y=HEIGHT-100, radius=100, img=STATIC)

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
                if event.key == pg.K_b:
                    light_layer.switch_visible()
                if event.key == pg.K_SPACE:
                    player_light.switch_visible()

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

        player_light.set_position(*hero.get_position())

        light_layer.update()
        collision = pg.sprite.collide_mask(hero, dinamic_light)
        if collision:
            dinamic_light.set_position(*hero.get_position())
            if not static_light1.start:
                static_light1.start = True
                static_light2.start = True
                static_light3.start = True
                static_light4.start = True
                sounds.stop()
                sound_sirena.play(-1)

        light_layer.draw(screen)

        text_group.draw()
        pg.display.update()
        clock.tick(60)

# ex4()

"""
light layer
"""