import arcade,random
WIDTH = 800
HEIGHT = 600


def ex1():
    textures = []
    for row in range(2):
        textures.append([])
        for col in range(3):
            textures[row].append(
                arcade.load_texture("timeanim/coinanim.png",
                                    x=col * 220, y=row * 230,
                                    width=220, height=230))

    class Coin(arcade.AnimatedTimeBasedSprite):
        def __init__(self, center_x, center_y, scale=0.2):
            super().__init__(scale=scale, center_x=center_x, center_y=center_y)
            for row in range(2):
                for col in range(3):
                    frame = arcade.AnimationKeyframe(1, 80, textures[row][col])
                    self.frames.append(frame)
                    self._points = textures[row][col].hit_box_points

    class Hero(arcade.AnimatedWalkingSprite):
        def __init__(self, center_x, center_y, scale=0.1):
            super().__init__(scale=scale, center_x=center_x, center_y=center_y)
            self.stand_right_textures.append(
                arcade.load_texture("walking_jack/Walk (1).png"))
            for i in range(1, 11):
                self.walk_right_textures.append(
                    arcade.load_texture(f"walking_jack/Walk ({i}).png"))
                self.walk_left_textures.append(
                    arcade.load_texture(f"walking_jack/Walk ({i}).png", mirrored=True))
            self.stand_left_textures.append(
                arcade.load_texture("walking_jack/Walk (1).png", mirrored=True))

        def player_motion(self, vel_x, vel_y):
            dist_x= vel_x-self.center_x
            dist_y = vel_y - self.center_y

            distance = pow(dist_x * dist_x + dist_y *dist_y,0.5)

            if distance>1:
                self.center_x += dist_x*0.1
                self.center_y += dist_y * 0.1

    class GamePause(arcade.View):
        def __init__(self, contgame):
            super().__init__()
            self.contgame = contgame

        def on_draw(self):
            arcade.start_render()
            self.contgame.player_list.draw()
            self.contgame.coin_list.draw()

            arcade.draw_rectangle_filled(400, 300, 300, 200, arcade.color.ORANGE)
            arcade.draw_text("PAUSE", WIDTH // 2, HEIGHT // 2, arcade.color.BLACK, 30)
            arcade.draw_text("press escape to continue",
                             WIDTH // 2-50, HEIGHT // 2 - 60, arcade.color.BLACK, 20)
            arcade.draw_text("press enter to restart",
                             WIDTH // 2-50, HEIGHT // 2 - 30, arcade.color.BLACK, 20)

        def on_key_press(self, symbol, modifiers):
            if symbol == arcade.key.ESCAPE:
                self.window.show_view(self.contgame)

            if symbol == arcade.key.RETURN:
                game = MyGame()
                self.window.show_view(game)

    class ManageWindows(arcade.View):
        def on_show(self):
            arcade.set_background_color(arcade.color.WHITE)

        def on_draw(self):
            arcade.start_render()
            arcade.draw_text("start window", WIDTH//2, HEIGHT//2, arcade.color.BLACK, 30)
            arcade.draw_text("click to start", WIDTH // 2, HEIGHT // 2 - 30, arcade.color.BLACK,20)

        def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
            game = MyGame()
            self.window.show_view(game)

    class MyGame(arcade.View):
        def __init__(self):
            super().__init__()

            arcade.set_background_color(arcade.color.AMAZON)
            self.sound_collect = arcade.Sound(":resources:sounds/upgrade2.wav")
            self.coin_list = arcade.SpriteList()

            self.vel_x = 0
            self.vel_y = 0

            for i in range(30):
                self.coin = Coin(center_x=random.randint(20, 780),
                                 center_y=random.randint(20, 580))
                self.coin_list.append(self.coin)

            self.player_list = arcade.SpriteList()
            self.player = Hero(400, 300)
            self.player_list.append(self.player)

        def on_draw(self):
            arcade.start_render()
            self.player_list.draw()
            self.coin_list.draw()

        def on_update(self, delta_time):
            self.player_list.update()
            self.player_list.update_animation()
            self.coin_list.update_animation()
            self.player.player_motion(self.vel_x, self.vel_y)
            collision = arcade.check_for_collision_with_list(self.player, self.coin_list)
            for i in collision:
                self.sound_collect.play(0.5)
                self.coin_list.remove(i)

        def on_key_press(self, symbol, modifiers):
            if symbol == arcade.key.ESCAPE:
                pause = GamePause(self)
                self.window.show_view(pause)
        def on_key_release(self, symbol, modifiers):
            pass
        def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
            self.vel_x=x
            self.vel_y=y


    def main():
        display = arcade.Window(WIDTH, HEIGHT, "supergame")
        menu = ManageWindows()
        display.show_view(menu)
        arcade.run()
    
    main()


def ex2():
    import math

    class MyGame(arcade.Window):
        def __init__(self, width, height):
            super().__init__(width, height)

            arcade.set_background_color(arcade.color.BLACK)

            self.green_x = 400
            self.green_y = 300

            self.yel_x = 300
            self.yel_y = 200

            self.red_x = 200
            self.red_y = 100

            self.vel_x = 0
            self.vel_y = 0

        def on_draw(self):
            arcade.start_render()
            arcade.draw_circle_filled(self.green_x, self.green_y, 50, arcade.color.GREEN)
            arcade.draw_circle_filled(self.yel_x, self.yel_y, 50, arcade.color.YELLOW)
            arcade.draw_circle_outline(self.red_x, self.red_y, 50, arcade.color.RED)

        def on_update(self, delta_time: float):
            self.circle_motion()

        def on_mouse_press(self, x, y, button, modifiers):
            if button == arcade.MOUSE_BUTTON_LEFT:
                self.green_x = x
                self.green_y = y

            if button == arcade.MOUSE_BUTTON_RIGHT:
                self.yel_x = x
                self.yel_y = y

        def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):

            self.vel_x = x
            self.vel_y = y

        def circle_motion(self):
            dist_x = self.vel_x - self.red_x
            dist_y = self.vel_y - self.red_y

            # distance = math.sqrt(dist_x * dist_x + dist_y *dist_y)

            distance = pow(dist_x * dist_x + dist_y * dist_y, 0.5)

            if distance > 1:
                self.red_x += dist_x * 0.1
                self.red_y += dist_y * 0.1

    def main():
        game = MyGame(WIDTH, HEIGHT)
        arcade.run()

    main()


def ex3():
    import typing

    TITLE = "Starting Template"
    BUTTON_SIZE = 40

    B_SOUND = ":resources:sounds/upgrade4.wav"

    class SoundButton(arcade.SpriteSolidColor):
        def __init__(self, file, volume, pan):
            super().__init__(BUTTON_SIZE, BUTTON_SIZE, arcade.color.WHITE)
            self.sound = arcade.Sound(file)
            self.volume = volume
            self.pan = pan

        def play(self):
            self.sound.play(self.volume, self.pan)

    class MyGame(arcade.Window):
        def __init__(self, width, height, title):
            super().__init__(width, height, title)

            arcade.set_background_color(arcade.color.BLACK)

            self.button_list = arcade.SpriteList()
            self.setup()

        def setup(self):
            rows = [HEIGHT // 2 + 50, HEIGHT // 2, HEIGHT // 2 - 50]
            colums = [BUTTON_SIZE, WIDTH // 4, WIDTH // 2,
                      WIDTH // 4 * 3, WIDTH - BUTTON_SIZE]
            volumes = [0.1, 0.5, 1]
            pans = [-1, -0.5, 0, 0.5, 1]
            for i in range(len(rows)):
                for j in range(len(colums)):
                    button = SoundButton(B_SOUND, volume=volumes[i], pan=pans[j])
                    button.center_x = colums[j]
                    button.center_y = rows[i]
                    self.button_list.append(button)

        def on_draw(self):
            arcade.start_render()
            self.button_list.draw()

        def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
            hit_collisions = arcade.get_sprites_at_point((x, y), self.button_list)
            for sprite in hit_collisions:
                button_sprite = typing.cast(SoundButton, sprite)
                if button == arcade.MOUSE_BUTTON_LEFT:
                    button_sprite.play()

    def main():
        game = MyGame(WIDTH, HEIGHT, TITLE)
        arcade.run()

    main()

def ex4():
    import typing

    class Base:
        def __init__(self, name):
            self.name = name

    class A(Base):
        def __init__(self):
            super().__init__("class A")
            self.m = 50

    class B(Base):
        def __init__(self):
            super().__init__("class B")

    class C(Base):
        def __init__(self):
            super().__init__("class C")

        def play(self):
            print("...melody...")

    bag = [typing.cast(Base, A()), typing.cast(Base, B()), typing.cast(Base, C())]
    for obj in bag:
        if obj.name == "class C":
            full_obj = typing.cast(C, obj)
            full_obj.play()
            # obj.play()

ex4()


"""
***mouse***
def on_mouse_press(self, x, y, button, modifiers) 
-отслеживание нажатия кнопок мышки 
if button == arcade.MOUSE_BUTTON_LEFT: -условие на кнопку 

def on_mouse_release(self, x, y, button, modifiers) 
-отслеживание отжатия кнопок мышки 

def on_mouse_motion(self, x: float, y: float, dx: float, dy: float) 
-отслеживание положения

***sound***
arcade.Sound(file) -основной класс музыки в arcade
(переменная с музыкой).play(self.volume,self.pan) 
-проигрыш с указанием громкости и панорамирования

***display***
arcade.View -класс для управления экранами и передаваемым видом 
display.show_view(menu) 
-функция для выбора показа экрана в следующем кадре"""