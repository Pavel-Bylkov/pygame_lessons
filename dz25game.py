"""Добавить взрыв частиц при коллизии основного персонажа и монетки.
Взрыв должен происходить из объекта с которым произошла коллизия в
circle форме. Сделать продолжительностью в одну секунду, с
постепенным затуханием."""


import time
import os
import random

import arcade, arcade.gui
from arcade.experimental.uislider import UISlider
from arcade.experimental.lights import Light, LightLayer

WIDTH = 800
HEIGHT = 600
TITLE = "Money Man"
VIEW_MARGIN = 100
default_color = (100, 100, 100)
WALK_SOUND = f"sounds{os.sep}shag.mp3"
HERO_IMG = f"les2img{os.sep}walking_man.png"
COIN_IMG = f"timeanim{os.sep}coinanim.png"
IMG = ":resources:images/pinball/bumper.png"

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

mystyle = {"font_name": ("bangkok"),
           "font_size": 20,
           "font_color": arcade.color.BLACK,
           "border_width": 2,
           "border_color": arcade.color.BLACK,
           "bg_color": arcade.color.YELLOW,
           "bg_color_pressed": arcade.color.BLACK,
           "border_color_pressed": arcade.color.YELLOW,
           "font_color_pressed": arcade.color.YELLOW
           }

def ex1():
    class MyView(arcade.View):
        def __init__(self):
            super().__init__()
            self.sound_menu = arcade.Sound(f"sounds{os.sep}boom.mp3")

        def soundmenu(self):
            self.sound_menu.play(self.window.volume)

    class Person(arcade.AnimatedWalkingSprite):
        def __init__(self, center_x, center_y, volume, scale=0.7):
            super().__init__()
            self.volume = volume
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
            self.timer_walk = time.time()
            self.sound_walk = arcade.Sound(WALK_SOUND)
            self.texture_change_distance = 40

        def update(self):
            super().update()
            if time.time() - self.timer_walk > 0.5 and (
                    self.change_y != 0 or self.change_x != 0):
                self.sound_walk.play(self.volume)
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

    class QuitButton(arcade.gui.UIFlatButton):
        def on_click(self, event: arcade.gui.UIOnClickEvent):
            arcade.exit()

    class GamePause(MyView):
        def __init__(self):
            super().__init__()
            self.rox = arcade.gui.UIManager()

            self.container = arcade.gui.UIBoxLayout()
            self.pausetext = arcade.gui.UITextArea(text="PAUSE MENU",
                                                   width=250,
                                                   height=75,
                                                   font_name="bangkok",
                                                   font_size=25,
                                                   text_color=arcade.color.BLACK)
            self.container.add(self.pausetext.with_space_around(bottom=20))

            self.back_menu = arcade.gui.UIFlatButton(text="BACK TO MENU", width=250, style=mystyle)
            self.container.add(self.back_menu.with_space_around(bottom=20))

            self.cont_game = arcade.gui.UIFlatButton(text="CONTINUE", width=250, style=mystyle)
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

        def on_update(self, delta_time):
            arcade.set_viewport(0, WIDTH,
                                0, HEIGHT)

        def on_draw(self):
            arcade.start_render()
            arcade.draw_rectangle_filled(400, 300, 800, 600,
                                         arcade.color.GOLDEN_BROWN)
            self.rox.draw()

        def on_back_menu(self, event):
            self.rox.disable()
            self.soundmenu()
            self.window.show_view(self.window.menu)

        def on_continue(self, event):
            self.soundmenu()
            self.window.show_view(self.window.game)

    class StartButton(arcade.gui.UIFlatButton):
        def on_click(self, event: arcade.gui.UIOnClickEvent):
            win = arcade.get_window()
            if win.game is None:
                win.game = MyGame()
            else:
                win.game.restart()
            win.game.soundmenu()
            win.show_view(win.game)

    class ManageWindows(MyView):
        def __init__(self):
            super().__init__()
            self.manage = arcade.gui.UIManager()

            self.box = arcade.gui.UIBoxLayout()

            self.title = arcade.gui.UITextArea(text="MONEY MAN",
                                               width=250,
                                               height=75,
                                               font_name="bangkok",
                                               font_size=25,
                                               text_color=arcade.color.YELLOW)
            self.text = arcade.gui.UITextArea(text=TEXT,
                                              width=400,
                                              height=150,
                                              font_name="bangkok",
                                              font_size=15,
                                              text_color=arcade.color.WHITE)
            self.start_button = StartButton(text="Start Button",
                                            width=200, style=mystyle)
            self.quit_button = QuitButton(text="Quit Button", width=200, style=mystyle)

            self.slider = UISlider(value=50)
            self.slider_text = arcade.gui.UILabel(text=f"Volume: {self.slider.value:02.0f}")

            self.box.add(self.title.with_space_around(bottom=20))
            self.box.add(self.text.with_space_around(bottom=20))
            self.box.add(self.start_button.with_space_around(bottom=20))
            self.box.add(self.quit_button.with_space_around(bottom=20))
            self.box.add(self.slider)
            self.box.add(self.slider_text)
            self.manage.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.box
            ))

            @self.slider.event()
            def on_change(event: arcade.gui.UIOnChangeEvent):
                self.sound_collect = arcade.Sound(f"sounds{os.sep}money.mp3")
                self.slider_text.text = f"Volume: {self.slider.value:02.0f}"
                self.slider_text.fit_content()
                self.window.volume = self.slider.value / 100

        def on_show(self):
            self.manage.enable()
            arcade.set_background_color(arcade.color.RED_BROWN)

        def on_draw(self):
            self.clear()
            self.manage.draw()

        def on_update(self, delta_time):
            arcade.set_viewport(0, WIDTH,
                                0, HEIGHT)

    class Bum(arcade.Emitter):
        def __init__(self, x, y):
            super().__init__((x, y),
                             emit_controller=arcade.EmitterIntervalWithTime(0.02, 1),
                             particle_factory=lambda emitter: arcade.LifetimeParticle(
                                 filename_or_texture=IMG,
                                 change_xy=arcade.rand_on_circle((0, 0), 0.9),
                                 lifetime=1.0, scale=0.2, alpha=127)
                             )
            self.started = False

        def is_started(self):
            return self.started

        def update(self):
            super().update()
            if self.get_count() > 0:
                self.started = True

    class BumList(list):
        def append(self, bum):
            if not isinstance(bum, Bum):
                raise TypeError(f"Type {type(bum)} is not Bum")
            super().append(bum)

        def update(self):
            for bum in self:
                bum.update()
                if bum.is_started() and bum.get_count() == 0:
                    self.remove(bum)

        def draw(self):
            for bum in self:
                bum.draw()

    class MyGame(MyView):
        def __init__(self):
            super().__init__()
            self.score = 0
            self.view_left = 0
            self.view_bottom = 0
            self.background_list = arcade.SpriteList()
            self.light_layer = LightLayer(WIDTH, HEIGHT)
            self.sound_collect = arcade.Sound(f"sounds{os.sep}money.mp3")

            self.coin_list = arcade.SpriteList()
            for i in range(20):
                coin = Coin(center_x=random.randint(20, 780),
                            center_y=random.randint(20, 580))
                self.coin_list.append(coin)

            for x in range(-128, 928, 128):
                for y in range(-128, 728, 128):
                    self.brick = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png")
                    self.brick.position = x, y
                    self.background_list.append(self.brick)

            self.player_list = arcade.SpriteList()
            self.player = Person(center_x=WIDTH // 2,
                                 center_y=HEIGHT // 2,
                                 volume=self.window.volume)
            self.player_list.append(self.player)
            self.player_light = Light(center_x=self.player.center_x,
                                      center_y=self.player.center_y,
                                      radius=80, color=arcade.color.WHITE,
                                      mode="soft")
            self.light_layer.add(self.player_light)
            self.bum_list = BumList()

        def restart(self):
            self.score = 0
            self.view_left = 0
            self.view_bottom = 0
            self.player.center_x = WIDTH // 2
            self.player.center_y = HEIGHT // 2
            self.player_light.position = self.player.position

        def on_show(self):
            arcade.set_background_color(arcade.color.DARK_GREEN)

        def on_draw(self):
            self.clear()
            self.player_list.draw()

            with self.light_layer:
                self.background_list.draw()
                arcade.draw_rectangle_outline(400, 300, 810, 610, arcade.color.RED, 5)
                self.coin_list.draw()
                self.bum_list.draw()
                self.player_list.draw()

            self.light_layer.draw(ambient_color=default_color)
            arcade.draw_text("PRESS SPACE TO TURN ON LIGHT", 10 + self.view_left,
                             20 + self.view_bottom, arcade.color.WHITE, 20)
            arcade.draw_text(f"Score: {self.score}", 10 + self.view_left,
                             560 + self.view_bottom, arcade.color.WHITE, 20)

        def on_update(self, delta_time):
            self.player_list.update()
            self.player_list.update_animation(delta_time*2)
            self.coin_list.update_animation()
            self.view_point()
            collision = arcade.check_for_collision_with_list(self.player, self.coin_list)
            for i in collision:
                self.sound_collect.play(self.window.volume)
                bum = Bum(i.center_x, i.center_y)
                i.center_x = random.randint(20, 780)
                i.center_y = random.randint(20, 580)
                self.score += 1
                self.bum_list.append(bum)
            self.player_light.position = self.player.position
            self.bum_list.update()

        def view_point(self):
            left_boundary = self.view_left + VIEW_MARGIN
            if self.player.left < left_boundary:
                self.view_left -= left_boundary - self.player.left

            right_boundary = self.view_left + WIDTH - VIEW_MARGIN
            if self.player.right > right_boundary:
                self.view_left += self.player.right - right_boundary

            bottom_boundary = self.view_bottom + VIEW_MARGIN
            if self.player.bottom < bottom_boundary:
                self.view_bottom -= bottom_boundary - self.player.bottom

            top_boundary = self.view_bottom + HEIGHT - VIEW_MARGIN
            if self.player.top > top_boundary:
                self.view_bottom += self.player.top - top_boundary

            arcade.set_viewport(self.view_left,
                                self.view_left + WIDTH,
                                self.view_bottom,
                                self.view_bottom + HEIGHT)

        def on_key_press(self, symbol, modifiers):
            if symbol == arcade.key.ESCAPE:
                self.soundmenu()
                self.window.show_view(self.window.pause)
            if symbol == arcade.key.D:
                self.player.change_x = 3
            elif symbol == arcade.key.A:
                self.player.change_x = -3
            elif symbol == arcade.key.W:
                self.player.change_y = 3
            elif symbol == arcade.key.S:
                self.player.change_y = -3
            elif symbol == arcade.key.SPACE:
                if self.player_light in self.light_layer:
                    self.light_layer.remove(self.player_light)
                else:
                    self.light_layer.add(self.player_light)

        def on_key_release(self, symbol, modifiers):
            if symbol == arcade.key.D or symbol == arcade.key.A:
                self.player.change_x = 0
            if symbol == arcade.key.W or symbol == arcade.key.S:
                self.player.change_y = 0

    class MainWindow(arcade.Window):
        def __init__(self):
            super().__init__(WIDTH, HEIGHT, TITLE)
            self.menu = ManageWindows()
            self.game = None
            self.volume = 0.5
            self.pause = GamePause()
            self.show_view(self.menu)

    def main():
        display = MainWindow()
        display.run()

    main()

ex1()

"""Добавить взрыв частиц из основного персонажа при нажатии кнопки 
spase. Частицы должны быть более прозрачной копией основного персонажа. 
Частицы должны разлетаться в форме прямоугольника и постепенно затухать 
через 1 секунду."""

def ex2():
    class MyView(arcade.View):
        def __init__(self):
            super().__init__()
            self.sound_menu = arcade.Sound(f"sounds{os.sep}boom.mp3")

        def soundmenu(self):
            self.sound_menu.play(self.window.volume)

    class Person(arcade.AnimatedWalkingSprite):
        def __init__(self, center_x, center_y, volume, scale=0.7):
            super().__init__()
            self.volume = volume
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
            self.timer_walk = time.time()
            self.sound_walk = arcade.Sound(WALK_SOUND)

        def update(self):
            super().update()
            if time.time() - self.timer_walk > 0.5 and (
                    self.change_y != 0 or self.change_x != 0):
                self.sound_walk.play(self.volume)
                self.timer_walk = time.time()

        def get_bum(self):
            return Bum2(self.center_x, self.center_y, textur_for_man[2][0])

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

    class QuitButton(arcade.gui.UIFlatButton):
        def on_click(self, event: arcade.gui.UIOnClickEvent):
            arcade.exit()

    class GamePause(MyView):
        def __init__(self):
            super().__init__()
            self.rox = arcade.gui.UIManager()

            self.container = arcade.gui.UIBoxLayout()
            self.pausetext = arcade.gui.UITextArea(text="PAUSE MENU",
                                                   width=250,
                                                   height=75,
                                                   font_name="bangkok",
                                                   font_size=25,
                                                   text_color=arcade.color.BLACK)
            self.container.add(self.pausetext.with_space_around(bottom=20))

            self.back_menu = arcade.gui.UIFlatButton(text="BACK TO MENU", width=250, style=mystyle)
            self.container.add(self.back_menu.with_space_around(bottom=20))

            self.cont_game = arcade.gui.UIFlatButton(text="CONTINUE", width=250, style=mystyle)
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

        def on_update(self, delta_time):
            arcade.set_viewport(0, WIDTH,
                                0, HEIGHT)

        def on_draw(self):
            arcade.start_render()
            arcade.draw_rectangle_filled(400, 300, 800, 600,
                                         arcade.color.GOLDEN_BROWN)
            self.rox.draw()

        def on_back_menu(self, event):
            self.rox.disable()
            self.soundmenu()
            self.window.show_view(self.window.menu)

        def on_continue(self, event):
            self.soundmenu()
            self.window.show_view(self.window.game)

    class StartButton(arcade.gui.UIFlatButton):
        def on_click(self, event: arcade.gui.UIOnClickEvent):
            win = arcade.get_window()
            if win.game is None:
                win.game = MyGame()
            else:
                win.game.restart()
            win.game.soundmenu()
            win.show_view(win.game)

    class ManageWindows(MyView):
        def __init__(self):
            super().__init__()
            self.manage = arcade.gui.UIManager()

            self.box = arcade.gui.UIBoxLayout()

            self.title = arcade.gui.UITextArea(text="MONEY MAN",
                                               width=250,
                                               height=75,
                                               font_name="bangkok",
                                               font_size=25,
                                               text_color=arcade.color.YELLOW)
            self.text = arcade.gui.UITextArea(text=TEXT,
                                              width=400,
                                              height=150,
                                              font_name="bangkok",
                                              font_size=15,
                                              text_color=arcade.color.WHITE)
            self.start_button = StartButton(text="Start Button",
                                            width=200, style=mystyle)
            self.quit_button = QuitButton(text="Quit Button", width=200, style=mystyle)

            self.slider = UISlider(value=50)
            self.slider_text = arcade.gui.UILabel(text=f"Volume: {self.slider.value:02.0f}")

            self.box.add(self.title.with_space_around(bottom=20))
            self.box.add(self.text.with_space_around(bottom=20))
            self.box.add(self.start_button.with_space_around(bottom=20))
            self.box.add(self.quit_button.with_space_around(bottom=20))
            self.box.add(self.slider)
            self.box.add(self.slider_text)
            self.manage.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.box
            ))

            @self.slider.event()
            def on_change(event: arcade.gui.UIOnChangeEvent):
                self.sound_collect = arcade.Sound(f"sounds{os.sep}money.mp3")
                self.slider_text.text = f"Volume: {self.slider.value:02.0f}"
                self.slider_text.fit_content()
                self.window.volume = self.slider.value / 100

        def on_show(self):
            self.manage.enable()
            arcade.set_background_color(arcade.color.RED_BROWN)

        def on_draw(self):
            self.clear()
            self.manage.draw()

        def on_update(self, delta_time):
            arcade.set_viewport(0, WIDTH,
                                0, HEIGHT)

    class Bum(arcade.Emitter):
        def __init__(self, x, y, img):
            super().__init__((x, y),
                             emit_controller=arcade.EmitterIntervalWithTime(0.02, 1),
                             particle_factory=lambda emitter: arcade.LifetimeParticle(
                                 filename_or_texture=img,
                                 change_xy=arcade.rand_on_circle((0, 0), 0.9),
                                 lifetime=1.0, scale=0.2, alpha=127)
                             )
            self.started = False

        def is_started(self):
            return self.started

        def update(self):
            super().update()
            if self.get_count() > 0:
                self.started = True

    class Bum2(arcade.Emitter):
        def __init__(self, x, y, img):
            super().__init__((x, y),
                             emit_controller=arcade.EmitBurst(50),
                             particle_factory=lambda emitter: arcade.LifetimeParticle(
                                 filename_or_texture=img,
                                 change_xy=arcade.rand_in_rect((-2, -3), 4, 6),
                                 lifetime=1.0, scale=0.5, alpha=127)
                             )
            self.started = False

        def is_started(self):
            return self.started

        def update(self):
            super().update()
            if self.get_count() > 0:
                self.started = True

    class BumList(list):
        def append(self, bum):
            if not isinstance(bum, arcade.Emitter):
                raise TypeError(f"Type {type(bum)} is not arcade.Emitter")
            super().append(bum)

        def update(self):
            for bum in self:
                bum.update()
                if bum.is_started() and bum.get_count() == 0:
                    self.remove(bum)

        def draw(self):
            for bum in self:
                bum.draw()

    class MyGame(MyView):
        def __init__(self):
            super().__init__()
            self.score = 0
            self.view_left = 0
            self.view_bottom = 0
            self.background_list = arcade.SpriteList()
            self.light_layer = LightLayer(WIDTH, HEIGHT)
            self.sound_collect = arcade.Sound(f"sounds{os.sep}money.mp3")

            self.coin_list = arcade.SpriteList()
            for i in range(20):
                coin = Coin(center_x=random.randint(20, 780),
                            center_y=random.randint(20, 580))
                self.coin_list.append(coin)

            for x in range(-128, 928, 128):
                for y in range(-128, 728, 128):
                    self.brick = arcade.Sprite(":resources:images/tiles/brickTextureWhite.png")
                    self.brick.position = x, y
                    self.background_list.append(self.brick)

            self.player_list = arcade.SpriteList()
            self.player = Person(center_x=WIDTH // 2,
                                 center_y=HEIGHT // 2,
                                 volume=self.window.volume)
            self.player_list.append(self.player)
            self.player_light = Light(center_x=self.player.center_x,
                                      center_y=self.player.center_y,
                                      radius=80, color=arcade.color.WHITE,
                                      mode="soft")
            self.light_layer.add(self.player_light)
            self.bum_list = BumList()

        def restart(self):
            self.score = 0
            self.view_left = 0
            self.view_bottom = 0
            self.player.center_x = WIDTH // 2
            self.player.center_y = HEIGHT // 2
            self.player_light.position = self.player.position

        def on_show(self):
            arcade.set_background_color(arcade.color.DARK_GREEN)

        def on_draw(self):
            self.clear()
            self.player_list.draw()

            with self.light_layer:
                self.background_list.draw()
                arcade.draw_rectangle_outline(400, 300, 810, 610, arcade.color.RED, 5)
                self.coin_list.draw()
                self.bum_list.draw()
                self.player_list.draw()

            self.light_layer.draw(ambient_color=default_color)
            arcade.draw_text("PRESS SPACE TO TURN ON LIGHT", 10 + self.view_left,
                             20 + self.view_bottom, arcade.color.WHITE, 20)
            arcade.draw_text(f"Score: {self.score}", 10 + self.view_left,
                             560 + self.view_bottom, arcade.color.WHITE, 20)

        def on_update(self, delta_time):
            self.player_list.update()
            self.player_list.update_animation()
            self.coin_list.update_animation()
            self.view_point()
            collision = arcade.check_for_collision_with_list(self.player, self.coin_list)
            for i in collision:
                self.sound_collect.play(self.window.volume)
                bum = Bum(i.center_x, i.center_y, IMG)
                i.center_x = random.randint(20, 780)
                i.center_y = random.randint(20, 580)
                self.score += 1
                self.bum_list.append(bum)
            self.player_light.position = self.player.position
            self.bum_list.update()

        def view_point(self):
            left_boundary = self.view_left + VIEW_MARGIN
            if self.player.left < left_boundary:
                self.view_left -= left_boundary - self.player.left

            right_boundary = self.view_left + WIDTH - VIEW_MARGIN
            if self.player.right > right_boundary:
                self.view_left += self.player.right - right_boundary

            bottom_boundary = self.view_bottom + VIEW_MARGIN
            if self.player.bottom < bottom_boundary:
                self.view_bottom -= bottom_boundary - self.player.bottom

            top_boundary = self.view_bottom + HEIGHT - VIEW_MARGIN
            if self.player.top > top_boundary:
                self.view_bottom += self.player.top - top_boundary

            arcade.set_viewport(self.view_left,
                                self.view_left + WIDTH,
                                self.view_bottom,
                                self.view_bottom + HEIGHT)

        def on_key_press(self, symbol, modifiers):
            if symbol == arcade.key.ESCAPE:
                self.soundmenu()
                self.window.show_view(self.window.pause)
            if symbol == arcade.key.D:
                self.player.change_x = 3
            elif symbol == arcade.key.A:
                self.player.change_x = -3
            elif symbol == arcade.key.W:
                self.player.change_y = 3
            elif symbol == arcade.key.S:
                self.player.change_y = -3
            elif symbol == arcade.key.SPACE:
                self.bum_list.append(self.player.get_bum())
                if self.player_light in self.light_layer:
                    self.light_layer.remove(self.player_light)
                else:
                    self.light_layer.add(self.player_light)

        def on_key_release(self, symbol, modifiers):
            if symbol == arcade.key.D or symbol == arcade.key.A:
                self.player.change_x = 0
            if symbol == arcade.key.W or symbol == arcade.key.S:
                self.player.change_y = 0

    class MainWindow(arcade.Window):
        def __init__(self):
            super().__init__(WIDTH, HEIGHT, TITLE)
            self.menu = ManageWindows()
            self.game = None
            self.volume = 0.5
            self.pause = GamePause()
            self.show_view(self.menu)

    def main():
        display = MainWindow()
        display.run()

    main()

# ex2()