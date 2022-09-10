import pygame as pg
from random import randint
import sys, os
from time import time
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.mouse import Mouse


class Conf:
    WIDTH, HEIGHT = 800, 600
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

    img_bum = f"les2img{os.sep}Взрыв4.png"
    img_tube = f"les2img{os.sep}tube.png"


pg.init()
pg.display.set_caption("Menu")
screen = pg.display.set_mode((Conf.WIDTH, Conf.HEIGHT), pg.RESIZABLE)
clock = pg.time.Clock()


def create_img(filename, width, height):
    """конвертация любого формата изображений в формат pygame"""
    return pg.transform.scale(pg.image.load(filename), (width, height))


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


class Bum(pg.sprite.Sprite):
    def __init__(self, center_x, center_y, speed, frames):
        super().__init__()
        self.frames = frames
        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=(center_x, center_y))
        self.speed = speed
        self.index = 0
        self.timer = time()

    def update(self):
        if time() - self.timer >= 1 / self.speed:
            self.timer = time()
            self.index += 1
        if self.index < len(self.frames):
            center_x, center_y = self.rect.centerx, self.rect.centery
            self.image = self.frames[self.index]
            self.rect = self.image.get_rect(center=(center_x, center_y))
        else:
            self.kill()

    def draw(self, win):
        win.blit(self.image, self.rect)


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
                 color=Conf.WHITE, background=None):
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
    def __init__(self, win, filename="", pos=(Conf.WIDTH // 2, Conf.HEIGHT // 2),
                 size=(Conf.WIDTH // 8, Conf.HEIGHT // 8), on_click=(lambda: None), text="",
                 text_color=Conf.WHITE, fill=Conf.BlACK):
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
    def __init__(self, win, filename="", pos=(Conf.WIDTH // 2, Conf.HEIGHT // 2),
                 size=(Conf.WIDTH // 2, Conf.HEIGHT // 2), fill=(60, 60, 60), title="",
                 text_color=Conf.WHITE, back=None):
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

    def stop(self, *args):
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
    def __init__(self, width, height, ambient_color=Conf.NIGHT_COLOR):
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
    filename = Conf.SCORE_BASE
    players_score = {"Noname": 0}
    player_name = "Noname"

    @classmethod
    def init(cls):
        # Создать файл если отсутствует
        if not os.path.exists(Conf.SCORE_BASE):
            open(Conf.SCORE_BASE, "w").close()

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

class Background:
    def __init__(self, win, img, width, height, speed):
        self.image = pg.transform.scale(pg.image.load(img), (width, height))
        self.rect1 = self.image.get_rect()
        self.rect2 = self.image.get_rect()
        self.rect2.x += width
        self.width = width
        self.speed = speed
        self.win = win

    def update(self):
        self.rect1.x -= self.speed
        self.rect2.x -= self.speed
        if self.rect1.right <= 0:
            self.rect1.x = self.width
        if self.rect2.right <= 0:
            self.rect2.x = self.width

    def draw(self):
        self.win.blit(self.image, self.rect1)
        self.win.blit(self.image, self.rect2)

class Barier(pg.sprite.Sprite):
    def __init__(self, x, y, height, speed):
        super().__init__()
        self.rect = pg.Rect(x, y, 50, height)
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right <= 0:
            self.kill()  # удаляем из всех групп

    def draw(self, win):
        pg.draw.rect(win, (60, 80, 60), self.rect)

class BarierGroup(pg.sprite.Group):
    def draw(self, win):
        for sprite in self:
            sprite.draw(win)

class Generator:
    def __init__(self, timer):
        self.sprites = BarierGroup()
        self.timer = timer
        self.last_add_time = time() - timer

    def draw(self, win):
        self.sprites.draw(win)

    def update(self):
        self.sprites.update()
        if time() - self.last_add_time > self.timer:
            height = randint(Conf.HEIGHT//8, Conf.HEIGHT//4)
            light = randint(Conf.HEIGHT//4, Conf.HEIGHT//3)
            self.sprites.add(Barier(x=Conf.WIDTH, y=0,
                       height=height, speed=5))
            # self.sprites.add(Barier(x=Conf.WIDTH, y=height+light,
            #            height=Conf.HEIGHT - height - light, speed=5))

    def check_collide(self, hero):
        collide = pg.sprite.spritecollide(hero, self.sprites, dokill=False)
        if collide:
            return True
        return False


def restart():
    global background, hero, gen_bariers, coins
    background = Background(win=screen, img=Conf.IMG_BACK,
                            width=Conf.WIDTH, height=Conf.HEIGHT, speed=5)

    hero = AnimationWalkSprite(center_x=400, center_y=300, speed=5, size=(60, 100))

    gen_bariers = Generator(timer=30)

    coins = pg.sprite.Group()
    for n in range(10):
        coin = AnimationTimeSprite(center_x=randint(30, Conf.WIDTH - 30),
                                   center_y=randint(30, Conf.HEIGHT - 30), speed=30,
                                   frames=load_frames(Conf.IMG_COIN, row=2, col=3, size=(30, 30)))
        coins.add(coin)

restart()
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

light_layer = LightLayer(Conf.WIDTH, Conf.HEIGHT, Conf.NIGHT_COLOR)
light_layer.active = False
player_light = Light(layer=light_layer, center_x=0, center_y=0,
                     radius=100, img=Conf.MIDLE)
dinamic_light = DinamicLight(layer=light_layer, center_x=100, center_y=100,
                             radius=75, img=Conf.DINAMIC, speed=2)
static_light1 = StaticLight(layer=light_layer, center_x=100, center_y=100,
                            radius=100, img=Conf.STATIC)
static_light2 = StaticLight(layer=light_layer, center_x=Conf.WIDTH-100,
                            center_y=100, radius=100, img=Conf.STATIC)
static_light3 = StaticLight(layer=light_layer, center_x=100,
                            center_y=Conf.HEIGHT-100, radius=100, img=Conf.STATIC)
static_light4 = StaticLight(layer=light_layer, center_x=Conf.WIDTH-100,
                            center_y=Conf.HEIGHT-100, radius=100, img=Conf.STATIC)

main_menu = Menu(win=screen, filename=Conf.IMG_MENU, title="Main Menu", text_color=Conf.BlACK)
menu_settings = Menu(win=screen, filename=Conf.IMG_MENU, title="Settings", text_color=Conf.BlACK)
main_menu.add_button(
    Button(win=screen, filename="", pos=(Conf.WIDTH // 2, Conf.HEIGHT // 2 - 60),
           size=(150, 60), text="Settings", on_click=menu_settings.run,
           text_color=Conf.WHITE, fill=(200, 50, 50))
)
main_menu.add_button(
    Button(win=screen, filename="", pos=(Conf.WIDTH // 2, Conf.HEIGHT // 2),
           size=(150, 60), text="Restart", on_click=lambda: main_menu.stop(restart()),
           text_color=Conf.WHITE, fill=(50, 200, 50))
)
main_menu.add_button(
    Button(win=screen, filename="", pos=(Conf.WIDTH // 2, Conf.HEIGHT // 2 + 60),
           size=(150, 60), text="Quit", on_click=game_quit,
           text_color=Conf.WHITE, fill=(50, 200, 50))
)

slider = MySlider(screen, Conf.WIDTH // 2 + 80, Conf.HEIGHT // 2, 100, 10)
menu_settings.add_widget(slider)

background2 = pg.transform.scale(pg.image.load(Conf.IMG_BACK2), (Conf.WIDTH, Conf.HEIGHT))
start_menu = Menu(win=screen, filename=Conf.IMG_MENU, title="Enter Name", text_color=Conf.BlACK,
                  back=background2)

input_box = InputBox(win=screen, x=Conf.WIDTH // 2 - 120, y=Conf.HEIGHT // 2 - 70, width=250)
start_menu.add_button(input_box)
start_menu.add_button(
    Button(win=screen, filename=Conf.IMG_MENU, pos=(Conf.WIDTH // 2, Conf.HEIGHT // 2 + 60),
           size=(150, 60), text="Start",
           on_click=lambda: ScoreBase.add_player_name(input_box, start_menu),
           text_color=Conf.BlACK, fill=(50, 200, 50))
)

ScoreBase.init()
ScoreBase.read()  # чтение файла с достижениями
start_menu.run()

text_group = Group()
name_text = Text(win=screen, text=f"Name: {ScoreBase.player_name}", x=Conf.WIDTH - 180, y=30)
text_group.append(name_text)
score_text = Text(win=screen, text=f"Score: {ScoreBase.get_score()}", x=80, y=30)
text_group.append(score_text)

game_over = Text(win=screen, text=f"GAME OVER", x=Conf.WIDTH//2, y=Conf.HEIGHT//2)

imgs_bum = [create_img(Conf.img_bum, i * 5, i * 5) for i in range(1, 20)]
bums = pg.sprite.Group()

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

    background.update()
    background.draw()
    gen_bariers.update()
    gen_bariers.draw(screen)

    sounds.set_volume(slider.getValue() / 100)

    hero.update()
    hero.update_frame()
    hero.draw(screen)



    if gen_bariers.check_collide(hero):
        game_over.draw()

    coins.update()
    coins.draw(screen)
    bums.update()
    bums.draw(screen)

    collisions = pg.sprite.spritecollide(hero, coins, True)
    for coin in collisions:
        ScoreBase.up_score()
        score_text.update(f"Score: {ScoreBase.get_score()}")
        point.set_volume(slider.getValue() / 100)
        point.play()
        bums.add(Bum(coin.rect.centerx, coin.rect.centery, 30, imgs_bum))

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