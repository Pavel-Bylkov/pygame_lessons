def ex1():
    import pygame as pg
    import sys
    import time
    from math import cos, sin, radians
    pg.init()
    pg.display.set_caption("Animation")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()

    IMG = "les2img/coin.png"
    img_coin = pg.transform.scale(pg.image.load(IMG), (20, 20))

    def int_r(num):
        num = int(num + (0.5 if num > 0 else -0.5))
        return num

    class Cache:
        _sin = {}
        _cos = {}

        @classmethod
        def cos(cls, angle):
            if angle not in cls._cos:
                cls._cos[angle] = cos(radians(angle))
            return cls._cos[angle]

        @classmethod
        def sin(cls, angle):
            if angle not in cls._sin:
                cls._sin[angle] = sin(radians(angle))
            return cls._sin[angle]

    class LifeTimeSprite(pg.sprite.Sprite):
        def __init__(self, timer):
            super().__init__()
            self.timer = timer
            self.time_start = time.time()

        def update(self, *args):
            if time.time() - self.time_start > self.timer:
                self.kill()

    class MoveLineSprite(LifeTimeSprite):
        def __init__(self, img, center_x, center_y, angle, speed, timer):
            super().__init__(timer)
            self.image = img
            self.rect = self.image.get_rect(center=(center_x, center_y))
            self.angle = angle
            self.speedx = int_r(speed * Cache.cos(angle))
            self.speedy = int_r(speed * Cache.sin(angle))

        def update(self, *args):
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            super().update(*args)

    class EmitterCircleLifeTime:
        def __init__(self, img, center_x, center_y, speed, timer, number=360):
            self.sprites = pg.sprite.Group()
            for angle in range(0, 360, 360//number):
                self.sprites.add(
                    MoveLineSprite(img, center_x, center_y, angle, speed, timer)
                )

        def update(self):
            self.sprites.update()

        def is_empty(self):
            return not bool(self.sprites)

        def draw(self, win):
            self.sprites.draw(win)

    class EmittersGroup(list):
        def add(self, element) -> None:
            super().append(element)

        def draw(self, *args, **kwargs):
            for element in self:
                element.draw(*args, **kwargs)

        def update(self, *args, **kwargs):
            for element in self[::-1]:
                element.update(*args, **kwargs)
                if element.is_empty():
                    self.remove(element)

    emitters = EmittersGroup()

    play = True
    while play:
        for e in pg.event.get():
            if e.type == pg.QUIT:  # если тип события = нажатию на крестик
                sys.exit()  # функция выхода из игры и закрытия всех окон()
            if e.type == pg.MOUSEBUTTONDOWN:
                if e.button == 1:
                    emitters.add(
                        EmitterCircleLifeTime(img=img_coin,
                                              center_x=e.pos[0], center_y=e.pos[1],
                                              speed=6, timer=0.5, number=10))

        screen.fill((30, 30, 30))

        emitters.update()
        emitters.draw(screen)

        pg.display.update()
        clock.tick(30)

# ex1()

def les_game():
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
    FONT_head = pg.font.Font("Fonts/aBraggaStars.ttf", 35)
    FONT_button = pg.font.Font(None, 29)
    FONT_head.set_bold(True)
    FONT_head.set_italic(True)
    FONT_vol = pg.font.Font(None, 28)
    FONT_score = pg.font.Font(None, 30)
    SCORE = 0

    particles = []
    particle_image = pg.image.load("Sprite/apple (2).png")

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

    button = pg.image.load("Sprite/button.png")  # загрузка картинок для меню
    button = pg.transform.scale(button, (200, 40))  # изменение размера
    button_rect = button.get_rect(center=(400, 240))  # получение объекта класса рект и установка координат на центр

    base_menu = pg.image.load("Sprite/base_menu.png")  # загрузка картинок для меню
    base_menu = pg.transform.scale(base_menu, (350, 350))  # изменение размера
    base_menu_rect = base_menu.get_rect(
        center=(400, 300))  # получение объекта класса рект и установка координат на центр

    start_pic = pg.image.load("Sprite/background.jpg")  # загрузка картинок для меню
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

    soundSirena = pg.mixer.Sound("Sound/sirena.wav")
    soundSirena.set_volume(0.1)

    point = pg.mixer.Sound("Sound/point.wav")

    lose = pg.mixer.Sound("Sound/lose.wav")

    apple_group = Group()

    spikes_group = Group()

    slider_value = slider.getValue()

    names = {}

    # создание частиц

    def emit_particle(x, y, x_vel, y_vel, radius):  # создание частицы и добавление ее в список
        particles.append([[x, y], [x_vel, y_vel], radius])

    def update_draw_particle():
        for i, particle in reversed(
                list(enumerate(particles))):  # перебор элементов списка по элемента и индексам задом наперед
            particle[0][0] += particle[1][0]  # увеличение координаты х на скорость
            particle[0][1] += particle[1][1]  # увеличение координаты Y на скорость
            particle[2] -= 0.8  # уменьшение радиуса частицы

            if particle[2] <= 0:  # удаление частицы если ее радиус меньше нуля
                particles.pop(i)

            if len(particles) == 0:  # проверка, есть ли в списке еще частицы
                break
            reverse_particle = particles[len(particles) - i - 1]  # Обращаемся к созданной частице
            image_copy = pg.transform.scale(particle_image,
                                            (reverse_particle[2], reverse_particle[2]))  # отрисовка созданной частицы

            screen.blit(image_copy, (reverse_particle[0][0], reverse_particle[0][1]))  # отрисовка картинки вместо круга

    # функции создания света
    def update_dinamic_light_mask():
        global dinamic_light_speed_x, dinamic_light_speed_y, dinamic_light_direction
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
        global SCORE
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
        global slider_value

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

    for i in range(20):  # цикл для создания яблок
        apple = Apple(screen, randint(20, 780), randint(20, 580))
        apple_group.add(apple)

    class Spikes(pg.sprite.Sprite):
        def __init__(self, screen, x, y):
            super(Spikes, self).__init__()
            self.screen = screen
            self.image = pg.image.load("Sprite/shipi.png")
            self.image = pg.transform.scale(self.image, (70, 40))
            self.rect = self.image.get_rect(center=(x, y))

        def draw(self):
            self.screen.blit(self.image, self.rect)

    for i in range(6):  # цикл для создания шипов
        spike = Spikes(screen, randint(75, 725), randint(45, 555))
        spikes_group.add(spike)

    def draw(screen, keys):
        global index
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
        spikes_group.draw(screen)

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
                        soundSirena.stop()
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
                emit_particle(sprite.rect.centerx, sprite.rect.centery, randint(-2, 2), randint(-2, 2), 40)

                sprite.kill()
                SCORE += 1
                point.play()

        for sprite in spikes_group:
            collision = pg.Rect.colliderect(stand_rect, sprite.rect)
            if collision:
                emit_particle(stand_rect.centerx, sprite.rect.centery, -2, 0, 40)
                emit_particle(stand_rect.centerx, sprite.rect.centery, -1, -1, 40)
                emit_particle(stand_rect.centerx, sprite.rect.centery, 0, -1, 40)
                emit_particle(stand_rect.centerx, sprite.rect.centery, 1, -1, 40)
                emit_particle(stand_rect.centerx, sprite.rect.centery, 2, 0, 40)
                sprite.kill()
                SCORE -= 5
                lose.play()
        update_draw_particle()
        score_text = FONT_score.render(f"Score: {SCORE}", True, (150, 120, 200))
        score_text_rect = score_text.get_rect(center=(750, 40))
        screen.blit(score_text, score_text_rect)
        pg.display.update()
        clock.tick(60)

# les_game()

def partical():
    import pygame as pg
    import sys
    import random

    pg.init()  # используется для старта модуля pygame
    pg.display.set_caption("Animation")  # задание загаловка окну
    screen = pg.display.set_mode((800, 600))  # создание поверхности с указанными размерами и параметрами
    clock = pg.time.Clock()  # создаем экземпляр класса для управление времени(кадрами игры (fps))
    FPS = 150

    image = pg.image.load("Sprite/apple (2).png")

    particles = []

    def emit_particle(x, y, x_vel, y_vel, radius, color):  # создание частицы и добавление ее в список
        particles.append([[x, y], [x_vel, y_vel], radius, color])

    def update_draw_particle():
        for i, particle in reversed(
                list(enumerate(particles))):  # перебор элементов списка по элемента и индексам задом наперед
            particle[0][0] += particle[1][0]  # увеличение координаты х на скорость
            particle[0][1] += particle[1][1]  # увеличение координаты Y на скорость
            particle[2] -= 0.3  # уменьшение радиуса частицы

            if particle[2] <= 0:  # удаление частицы если ее радиус меньше нуля
                particles.pop(i)

            reverse_particle = particles[len(particles) - i - 1]  # Обращаемся к созданной частице
            image_copy = pg.transform.scale(image,
                                            (reverse_particle[2], reverse_particle[2]))  # отрисовка созданной частицы

            screen.blit(image_copy, (reverse_particle[0][0], reverse_particle[0][1]))  # отрисовка картинки вместо круга

            # pg.draw.circle(screen,reverse_particle[3],(reverse_particle[0][0],reverse_particle[0][1]),reverse_particle[2])#отрисовка круга

    play = True
    while play:  # основной цикл игры
        events = pg.event.get()
        for event in events:  # отслеживание всех событий которые происходят на игровом дисплее
            if event.type == pg.QUIT:  # если тип события = нажатию на крестик
                sys.exit()  # функция выхода из игры и закрытия всех окон(
        screen.fill((0, 0, 0))
        mx, my = pg.mouse.get_pos()  # получаение позиции курсора мышки
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        emit_particle(mx, my, 5, random.randint(-2, 2), 40, color)
        update_draw_particle()

        pg.display.update()
        clock.tick(FPS)

# partical()

