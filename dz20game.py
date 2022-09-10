"""Анимировать уже имеющиеся спрайты. Добавить анимацию ходьбы для
основного персонажа, и анимацию для подсобных спрайтов(например,
вращение монет). Реализовать коллизию между ними.

"""

import arcade, random
import os

WIDTH = 800
HEIGHT = 600

def ex1():
    textures = []
    for row in range(2):
        textures.append([])
        for col in range(3):
            textures[row].append(
                arcade.load_texture(f"timeanim{os.sep}coinanim.png",
                                    x=col * 220, y=row * 230,
                                    width=220, height=230))

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


    class MyGame(arcade.Window):
        def __init__(self, width, height):
            super().__init__(width, height)

            arcade.set_background_color(arcade.color.AMAZON)
            self.coin_list = arcade.SpriteList()
            for i in range(30):
                self.coin = Coin(center_x=random.randint(20, 780),
                                 center_y=random.randint(20, 580))
                self.coin_list.append(self.coin)

            self.player_list = arcade.SpriteList()
            self.player = arcade.AnimatedWalkingSprite()

            self.player.stand_right_textures.append(arcade.load_texture(f"walking_jack{os.sep}Walk (1).png"))
            for i in range(1, 11):
                self.player.walk_right_textures.append(arcade.load_texture(f"walking_jack{os.sep}Walk ({i}).png"))
                self.player.walk_left_textures.append(
                    arcade.load_texture(f"walking_jack{os.sep}Walk ({i}).png", mirrored=True))
            self.player.stand_left_textures.append(
                arcade.load_texture(f"walking_jack{os.sep}Walk (1).png", mirrored=True))

            self.player.center_x = 400
            self.player.center_y = 300
            self.player.scale = 0.1
            self.player_list.append(self.player)

        def on_draw(self):
            arcade.start_render()
            self.player_list.draw()
            self.coin_list.draw()

        def on_update(self, delta_time):
            self.player_list.update()
            self.player_list.update_animation()
            self.coin_list.update_animation()

            collision = arcade.check_for_collision_with_list(self.player, self.coin_list)
            for i in collision:
                # self.coin_list.remove(i)
                i.center_x = random.randint(20, 780)
                i.center_y = random.randint(20, 580)
                # self.coin = Coin(center_x=random.randint(20, 780),
                #                  center_y=random.randint(20, 580))
                # self.coin_list.append(self.coin)

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

    def main():
        game = MyGame(WIDTH, HEIGHT)
        game.run()

    main()

# ex1()

"""Найти большой лист со спрайтом персонажа и реализовать анимацию 
движения в вверх, вниз, влево, вправо."""

def ex2():
    textures = []
    for row in range(4):
        textures.append([])
        for col in range(12):
            textures[row].append(
                arcade.load_texture("les2img/walking_man.png",
                                    x=col * 95, y=row * 158,
                                    width=95, height=158))

    class Person(arcade.AnimatedWalkingSprite):
        def __init__(self, center_x, center_y, scale=0.7):
            super().__init__()
            self.stand_right_textures.append(textures[2][0])
            self.stand_left_textures.append(textures[1][0])
            for i in range(12):
                self.walk_right_textures.append(textures[2][i])
                self.walk_left_textures.append(textures[1][i])
                self.walk_up_textures.append(textures[3][i])
                self.walk_down_textures.append(textures[0][i])

            self.scale = scale
            self.center_x = center_x
            self.center_y = center_y


    class MyGame(arcade.Window):
        def __init__(self, width, height):
            super().__init__(width, height)

            arcade.set_background_color(arcade.color.AMAZON)

            self.player_list = arcade.SpriteList()
            self.player = Person(center_x=width//2, center_y=height//2)
            self.player_list.append(self.player)

        def on_draw(self):
            arcade.start_render()
            self.player_list.draw()

        def on_update(self, delta_time):
            self.player_list.update()
            self.player_list.update_animation()

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

    def main():
        game = MyGame(WIDTH, HEIGHT)
        game.run()

    main()


ex2()
