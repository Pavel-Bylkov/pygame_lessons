"""Создать окно входа в игру, при нажатии на одну из клавиш,
должен проигрываться звук и окошко сменятся игрой."""

import random
import os

import arcade
from arcade.color import *

WIDTH = 800
HEIGHT = 600
B_SOUND = f":resources:sounds{os.sep}upgrade4.wav"
COLL_SOUND = f":resources:sounds{os.sep}upgrade2.wav"
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

        def reset_pos(self):
            self.center_x = random.randint(20, 780)
            self.center_y = random.randint(20, 580)

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
                i.reset_pos()
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

        def on_key_release(self, symbol, modifiers):
            if symbol == arcade.key.RIGHT or symbol == arcade.key.LEFT:
                self.player.change_x = 0
            if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
                self.player.change_y = 0

    class ManageWindows(arcade.View):
        def on_show(self):
            arcade.set_background_color(WHITE)
            self.sound_start = arcade.Sound(B_SOUND)

        def on_draw(self):
            arcade.start_render()
            arcade.draw_text("start window", WIDTH // 2 - 100, HEIGHT // 2, BLACK, 30)
            arcade.draw_text("Press any button to start",
                             WIDTH // 2 - 135, HEIGHT // 2 - 30, BLACK, 20)

        def on_key_press(self, symbol, modifiers):
            game = MyGame()
            self.sound_start.play(0.5)
            self.window.show_view(game)

    def main():
        display = arcade.Window(WIDTH, HEIGHT, TITLE)
        menu = ManageWindows()
        display.show_view(menu)
        display.run()

    main()

# ex1()


"""Добавить на экран входа прямоугольники с текстом, и 
реализовать нажатие мышкой по ним. Звук нажатия и смена 
экрана игрой должны сохранится."""


def ex2():
    TITLE = "Example 2"

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

        def on_show(self):
            arcade.set_background_color(WHITE)

        def on_draw(self):
            arcade.start_render()
            arcade.draw_text("start window", WIDTH // 2 - 100, HEIGHT // 2, BLACK, 30)
            arcade.draw_text("Press any button to start",
                             WIDTH // 2 - 135, HEIGHT // 2 - 30, BLACK, 20)
            self.button_list.draw()
            for button in self.button_list:
                button.draw_text()

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

    def main():
        display = arcade.Window(WIDTH, HEIGHT, TITLE)
        menu = ManageWindows()
        display.show_view(menu)
        display.run()

    main()

ex2()