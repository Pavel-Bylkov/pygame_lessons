"""На стартовом окошке вывести скроялщийся блок текста с информацией
об игре/персонаже/истории. На окне паузы вывести два блока-кнопки,
один для выхода в стартовое окошко, второй для продолжении игры.
"""

import random
import os
import time

import arcade
from arcade.color import *
import arcade.gui
from arcade.experimental.uislider import UISlider

WIDTH = 800
HEIGHT = 600
B_SOUND = f"sounds{os.sep}upgrade4.wav"
COLL_SOUND = f"sounds{os.sep}coin2.wav"
WALK_SOUND = f"sounds{os.sep}hurt1.wav"
COIN_IMG = f"timeanim{os.sep}coinanim.png"
HERO_IMG = f"les2img{os.sep}walking_man.png"

textures = []
for row in range(2):
    textures.append([])
    for col in range(3):
        textures[row].append(arcade.load_texture(
            COIN_IMG, x=col * 220, y=row * 230, width=220, height=230))
textur_for_man = []
for row in range(4):
    textur_for_man.append([])
    for col in range(12):
        textur_for_man[row].append(arcade.load_texture(
            HERO_IMG, x=col * 95, y=row * 158, width=95, height=158))

TEXT = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent eget pellentesque velit.
Nam eu rhoncus nulla. Fusce ornare libero eget ex vulputate, vitae mattis orci eleifend. 
Donec quis volutpat arcu. Proin lacinia velit id imperdiet ultrices. Fusce porta magna leo,
non maximus justo facilisis vel. Duis pretium sem ut eros scelerisque, a dignissim ante 
pellentesque. Cras rutrum aliquam fermentum. Donec id mollis mi.\n
finibus sapien in, lacinia lorem. Proin tincidunt gravida nisl in pellentesque. Aenean sed 
arcu ipsum. Vivamus quam arcu, elementum nec auctor non, convallis non elit. Maecenas id 
scelerisque lectus. Vivamus eget sem tristique, dictum lorem eget, maximus leo. Mauris lorem 
tellus, molestie eu orci ut, porta aliquam est. Nullam lobortis tempor magna, egestas lacinia lectus.\n"""

def ex1():
    TITLE = "Example 1"

    class Person(arcade.AnimatedWalkingSprite):
        def __init__(self, center_x, center_y, scale=0.7):
            super().__init__()
            self.stand_right_textures.append(textur_for_man[2][0])
            self.stand_left_textures.append(textur_for_man[1][0])
            for i in range(12):
                self.walk_right_textures.append(textur_for_man[2][i])
                self.walk_left_textures.append(textur_for_man[1][i])
                self.walk_up_textures.append(textur_for_man[3][i])
                self.walk_down_textures.append(textur_for_man[0][i])
            self.scale = scale
            self.center_x = center_x
            self.center_y = center_y

    class Coin(arcade.AnimatedTimeBasedSprite):
        def __init__(self, center_x, center_y, scale=0.2):
            super().__init__()
            for row in range(2):
                for col in range(3):
                    frame = arcade.AnimationKeyframe(1, 80, textures[row][col])
                    self.frames.append(frame)
                    self._points = textures[row][col].hit_box_points
            self.scale = scale
            self.center_x = center_x
            self.center_y = center_y

    class MyGame(arcade.View):
        def __init__(self):
            super().__init__()

            arcade.set_background_color(AMAZON)
            self.sound_coll = arcade.Sound(COLL_SOUND)
            self.score = 0

            self.coin_list = arcade.SpriteList()
            for i in range(20):
                self.coin = Coin(center_x=random.randint(20, 780),
                                 center_y=random.randint(20, 580))
                self.coin_list.append(self.coin)

            self.player_list = arcade.SpriteList()
            self.player = Person(center_x=WIDTH//2, center_y=HEIGHT//2)
            self.player_list.append(self.player)

        def on_draw(self):
            self.clear()
            self.player_list.draw()
            self.coin_list.draw()
            arcade.draw_text(f"Score: {self.score}", 10, HEIGHT - 30, WHITE, 20)

        def on_update(self, delta_time):
            self.player_list.update()
            self.player_list.update_animation()
            self.coin_list.update_animation()

            coll = arcade.check_for_collision_with_list(self.player, self.coin_list)
            for i in coll:
                i.center_x = random.randint(20, 780)
                i.center_y = random.randint(20, 580)
                self.sound_coll.play(0.5)
                self.score += 1

        def on_key_press(self, symbol, modifiers):
            if symbol == arcade.key.RIGHT:
                self.player.change_x = 5
            elif symbol == arcade.key.LEFT:
                self.player.change_x = -5
            elif symbol == arcade.key.UP:
                self.player.change_y = 5
            elif symbol == arcade.key.DOWN:
                self.player.change_y = -5
            if symbol == arcade.key.ESCAPE:
                pause = GamePause(self)
                self.window.show_view(pause)

        def on_key_release(self, symbol, modifiers):
            if symbol == arcade.key.RIGHT or symbol == arcade.key.LEFT:
                self.player.change_x = 0
            if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
                self.player.change_y = 0

    class Button(arcade.SpriteSolidColor):
        def __init__(self, width, height, color,
                     center_x, center_y, text, text_color):
            super().__init__(width, height, color)
            self.center_x = center_x
            self.center_y = center_y
            self.text = text
            self.text_color = text_color

        def draw_text(self):
            arcade.draw_text(self.text,
                             start_x=self.center_x - len(self.text)//2*20,
                             start_y=self.center_y - self.height//4,
                             color=self.text_color, font_size=self.height//2)

    class ManageWindows(arcade.View):
        def __init__(self):
            super().__init__()
            self.sound_start = arcade.Sound(B_SOUND)
            self.button_list = arcade.SpriteList()
            self.button_list.append(Button(width=150, height=40, color=RED,
                                           center_x=WIDTH//2, center_y=HEIGHT//4,
                                           text="START", text_color=DARK_BLUE))
            self.manage = arcade.gui.UIManager()
            self.manage.enable()
            self.box = arcade.gui.UIBoxLayout()
            self.text = arcade.gui.UITextArea(
                text=TEXT,
                width=600,
                height=150,
                font_name="Kenney Future",
                font_size=10,
                text_color=arcade.color.DARK_GREEN)
            self.box.add(self.text.with_space_around(bottom=20))
            self.manage.add(arcade.gui.UIAnchorWidget(child=self.box))

        def on_show(self):
            arcade.set_background_color(WHITE)

        def on_draw(self):
            self.clear()
            arcade.draw_text("start window", WIDTH // 2 - 100, HEIGHT // 4 * 3, BLACK, 30)
            arcade.draw_text("Press any button to start",
                             WIDTH // 2 - 135, HEIGHT // 4 * 3 - 30, BLACK, 20)
            self.button_list.draw()
            for button in self.button_list:
                button.draw_text()
            self.manage.draw()

        def start_game(self):
            game = MyGame()
            self.sound_start.play(0.5)
            self.window.show_view(game)

        def on_key_press(self, symbol, modifiers):
            self.start_game()

        def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
            if button == arcade.MOUSE_BUTTON_LEFT:
                hit_collisions = arcade.get_sprites_at_point((x, y), self.button_list)
                if hit_collisions:
                    self.start_game()

    class GamePause(arcade.View):
        def __init__(self, game):
            super().__init__()
            self.game = game
            self.sound_menu = arcade.Sound(f"sounds{os.sep}boom.mp3")
            self.rox = arcade.gui.UIManager()

            self.container = arcade.gui.UIBoxLayout()
            self.pausetext = arcade.gui.UITextArea(text="PAUSE MENU",
                                                   width=250,
                                                   height=75,
                                                   font_name="bangkok",
                                                   font_size=25,
                                                   text_color=arcade.color.BLACK)
            self.container.add(self.pausetext.with_space_around(bottom=20))

            self.back_menu = arcade.gui.UIFlatButton(text="BACK TO MENU", width=250)
            self.container.add(self.back_menu.with_space_around(bottom=20))

            self.cont_game = arcade.gui.UIFlatButton(text="CONTINUE", width=250)
            self.container.add(self.cont_game.with_space_around(bottom=20))

            self.back_menu.on_click = self.on_back_menu
            self.cont_game.on_click = self.on_continue

            self.rox.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.container
            ))

        def on_show(self):
            self.rox.enable()

        def start_game(self):
            self.sound_menu.play(0.5)
            self.window.show_view(self.game)

        def on_draw(self):
            arcade.start_render()
            arcade.draw_rectangle_filled(400, 300, 800, 600,
                                         arcade.color.GOLDEN_BROWN)
            self.rox.draw()

        def on_back_menu(self, event):
            self.rox.disable()
            self.sound_menu.play(0.5)
            menu = ManageWindows()
            self.window.show_view(menu)

        def on_continue(self, event):
            self.rox.disable()
            self.start_game()

    def main():
        display = arcade.Window(WIDTH, HEIGHT, TITLE)
        menu = ManageWindows()
        display.show_view(menu)
        display.run()

    main()

# ex1()

"""Добавить на стартовое окно слайдер с полоской для изменения 
параметров звука. Выставленное пользователем значение, должно 
изменить звук подбора монет в самой игре(с помощью функции set_volume).
"""
volume = 0.5

def set_volume(vol):
    global volume

    if vol < 0 or vol > 1:
        raise ValueError("Value Volume is from 0 to 1 float diapason")
    volume = vol

def ex2():
    TITLE = "Example 2"

    class Person(arcade.AnimatedWalkingSprite):
        def __init__(self, center_x, center_y, scale=0.7):
            super().__init__()
            self.stand_right_textures.append(textur_for_man[2][0])
            self.stand_left_textures.append(textur_for_man[1][0])
            self._points = textur_for_man[1][0].hit_box_points
            for i in range(12):
                self.walk_right_textures.append(textur_for_man[2][i])
                self.walk_left_textures.append(textur_for_man[1][i])
                self.walk_up_textures.append(textur_for_man[3][i])
                self.walk_down_textures.append(textur_for_man[0][i])
            self.scale = scale
            self.center_x = center_x
            self.center_y = center_y
            self.timer_walk = time.time()
            self.sound_walk = arcade.Sound(WALK_SOUND)

        def update(self):
            super().update()
            if time.time() - self.timer_walk > 0.3 and (
                    self.change_y != 0 or self.change_x != 0):
                self.sound_walk.play(volume)
                self.timer_walk = time.time()

    class Coin(arcade.AnimatedTimeBasedSprite):
        def __init__(self, center_x, center_y, scale=0.2):
            super().__init__()
            for row in range(2):
                for col in range(3):
                    frame = arcade.AnimationKeyframe(1, 80, textures[row][col])
                    self.frames.append(frame)
                    self._points = textures[row][col].hit_box_points
            self.scale = scale
            self.center_x = center_x
            self.center_y = center_y

    class MyGame(arcade.View):
        def __init__(self):
            super().__init__()

            arcade.set_background_color(AMAZON)
            self.sound_coll = arcade.Sound(COLL_SOUND)
            self.score = 0

            self.coin_list = arcade.SpriteList()
            for i in range(20):
                coin = Coin(center_x=random.randint(20, 780),
                            center_y=random.randint(20, 580))
                self.coin_list.append(coin)

            self.player_list = arcade.SpriteList()
            self.player = Person(center_x=WIDTH//2, center_y=HEIGHT//2)
            self.player_list.append(self.player)

        def on_draw(self):
            self.clear()
            self.player_list.draw()
            self.coin_list.draw()
            arcade.draw_text(f"Score: {self.score}", 10, HEIGHT - 30, WHITE, 20)

        def on_update(self, delta_time):
            if self.player.left <= 0 or self.player.right >= WIDTH:
                self.player.change_x *= -1
            if self.player.bottom <= 0 or self.player.top >= HEIGHT:
                self.player.change_y *= -1

            self.player_list.update()
            self.player_list.update_animation()
            self.coin_list.update_animation()

            coll = arcade.check_for_collision_with_list(self.player, self.coin_list)
            for i in coll:
                i.center_x = random.randint(20, 780)
                i.center_y = random.randint(20, 580)
                self.sound_coll.play(volume)
                self.score += 1

        def on_key_press(self, symbol, modifiers):
            if symbol == arcade.key.RIGHT:
                self.player.change_x = 5
            if symbol == arcade.key.LEFT:
                self.player.change_x = -5
            if symbol == arcade.key.UP:
                self.player.change_y = 5
            if symbol == arcade.key.DOWN:
                self.player.change_y = -5
            if symbol == arcade.key.ESCAPE:
                pause = GamePause(self)
                self.window.show_view(pause)

        def on_key_release(self, symbol, modifiers):
            if symbol == arcade.key.RIGHT or symbol == arcade.key.LEFT:
                self.player.change_x = 0
            if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
                self.player.change_y = 0

    class Button(arcade.SpriteSolidColor):
        def __init__(self, width, height, color,
                     center_x, center_y, text, text_color):
            super().__init__(width, height, color)
            self.center_x = center_x
            self.center_y = center_y
            self.text = text
            self.text_color = text_color

        def draw_text(self):
            arcade.draw_text(self.text,
                             start_x=self.center_x - len(self.text)//2*20,
                             start_y=self.center_y - self.height//4,
                             color=self.text_color, font_size=self.height//2)

    class ManageWindows(arcade.View):
        def __init__(self):
            super().__init__()
            self.sound_start = arcade.Sound(B_SOUND)
            self.button_list = arcade.SpriteList()
            self.button_list.append(Button(width=150, height=40, color=RED,
                                           center_x=WIDTH//2, center_y=HEIGHT//4,
                                           text="START", text_color=DARK_BLUE))
            self.manage = arcade.gui.UIManager()
            self.manage.enable()
            self.box = arcade.gui.UIBoxLayout()
            self.slider = UISlider(value=volume*100)
            self.slider_text = arcade.gui.UILabel(text=f"Volume: {self.slider.value:02.0f}")

            @self.slider.event()
            def on_change(event: arcade.gui.UIOnChangeEvent):
                self.slider_text.text = f"Volume: {self.slider.value:02.0f}"
                self.slider_text.fit_content()
                set_volume(self.slider.value / 100)

            self.box.add(self.slider)
            self.box.add(self.slider_text)

            self.text = arcade.gui.UITextArea(
                text=TEXT,
                width=600,
                height=150,
                font_name="Kenney Future",
                font_size=10,
                text_color=arcade.color.DARK_GREEN)
            self.box.add(self.text.with_space_around(bottom=20))
            self.manage.add(arcade.gui.UIAnchorWidget(child=self.box))

        def on_show(self):
            arcade.set_background_color(WHITE)
            self.manage.enable()

        def on_draw(self):
            self.clear()
            arcade.draw_text("start window", WIDTH // 2 - 100, HEIGHT // 4 * 3, BLACK, 30)
            arcade.draw_text("Press any button to start",
                             WIDTH // 2 - 135, HEIGHT // 4 * 3 - 30, BLACK, 20)
            self.button_list.draw()
            for button in self.button_list:
                button.draw_text()
            self.manage.draw()

        def start_game(self):
            game = MyGame()
            self.sound_start.play(volume)
            self.window.show_view(game)

        def on_key_press(self, symbol, modifiers):
            self.start_game()

        def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
            if button == arcade.MOUSE_BUTTON_LEFT:
                hit_collisions = arcade.get_sprites_at_point((x, y), self.button_list)
                if hit_collisions:
                    self.start_game()

    class GamePause(arcade.View):
        def __init__(self, game):
            super().__init__()
            self.game = game
            self.sound_menu = arcade.Sound(f"sounds{os.sep}boom.mp3")
            self.rox = arcade.gui.UIManager()

            self.container = arcade.gui.UIBoxLayout()
            self.pausetext = arcade.gui.UITextArea(text="PAUSE MENU",
                                                   width=250,
                                                   height=75,
                                                   font_name="bangkok",
                                                   font_size=25,
                                                   text_color=arcade.color.BLACK)
            self.container.add(self.pausetext.with_space_around(bottom=20))

            self.back_menu = arcade.gui.UIFlatButton(text="BACK TO MENU", width=250)
            self.container.add(self.back_menu.with_space_around(bottom=20))

            self.cont_game = arcade.gui.UIFlatButton(text="CONTINUE", width=250)
            self.container.add(self.cont_game.with_space_around(bottom=20))

            self.back_menu.on_click = self.on_back_menu
            self.cont_game.on_click = self.on_continue

            self.rox.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.container
            ))

        def on_show(self):
            self.rox.enable()

        def start_game(self):
            self.sound_menu.play(volume)
            self.window.show_view(self.game)

        def on_draw(self):
            arcade.start_render()
            arcade.draw_rectangle_filled(400, 300, 800, 600,
                                         arcade.color.GOLDEN_BROWN)
            self.rox.draw()

        def on_back_menu(self, event):
            self.rox.disable()
            self.sound_menu.play(volume)
            menu = ManageWindows()
            self.window.show_view(menu)

        def on_continue(self, event):
            self.rox.disable()
            self.start_game()

    def main():
        display = arcade.Window(WIDTH, HEIGHT, TITLE)
        menu = ManageWindows()
        display.show_view(menu)
        display.run()

    main()

ex2()