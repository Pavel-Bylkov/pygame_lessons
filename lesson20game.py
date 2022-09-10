import arcade, random

WIDTH = 800
HEIGHT = 600

def example1():
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

            self.player.stand_right_textures.append(arcade.load_texture("walking_jack/Walk (1).png"))
            for i in range(1, 11):
                self.player.walk_right_textures.append(arcade.load_texture(f"walking_jack/Walk ({i}).png"))
                self.player.walk_left_textures.append(
                    arcade.load_texture(f"walking_jack/Walk ({i}).png", mirrored=True))
            self.player.stand_left_textures.append(
                arcade.load_texture("walking_jack/Walk (1).png", mirrored=True))

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
                self.coin_list.remove(i)

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
        arcade.run()

    main()


def example2():
    class MyGame(arcade.Window):
        def __init__(self, width, height):
            super().__init__(width, height)

            arcade.set_background_color(arcade.color.AMAZON)

            self.player_list = arcade.SpriteList()
            self.player = arcade.AnimatedWalkingSprite()

            self.player.stand_right_textures.append(arcade.load_texture("green dragon/5.png"))
            for i in range(5, 16):
                self.player.walk_right_textures.append(arcade.load_texture(f"green dragon/{i}.png"))
                self.player.walk_left_textures.append(
                    arcade.load_texture(f"green dragon/{i}.png", mirrored=True))
            self.player.stand_left_textures.append(
                arcade.load_texture("green dragon/5.png", mirrored=True))


            self.player.center_x = 400
            self.player.center_y = 300
            self.player.scale = 0.2
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
                self.player.stop()
            if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
                self.player.stop()

    def main():
        game = MyGame(WIDTH, HEIGHT)
        arcade.run()

    main()


def example3():
    class MyGame(arcade.Window):
        def __init__(self, width, height):
            super().__init__(width, height)

            arcade.set_background_color(arcade.color.AMAZON)

            self.coin_list = arcade.SpriteList()
            self.coin = arcade.AnimatedTimeBasedSprite()
            self.coin.frames = []

            for row in range(2):
                for col in range(3):
                    tex = arcade.load_texture("timeanim/coinanim.png",
                                              x=col * 220, y=row * 230, width=220,
                                              height=230)
                    frame = arcade.AnimationKeyframe(1, 100, tex)
                    self.coin.frames.append(frame)
            self.coin.scale = 0.2
            self.coin.center_x = 200
            self.coin.center_y = 450
            self.coin_list.append(self.coin)

            self.cat = arcade.AnimatedTimeBasedSprite()
            self.cat_list = arcade.SpriteList()

            for row in range(4):
                for col in range(2):
                    texcat = arcade.load_texture("timeanim/runningcat.png",
                                                 x=col * 512, y=row * 256, width=512,
                                                 height=256)
                    framecat = arcade.AnimationKeyframe(1, 60, texcat)
                    self.cat.frames.append(framecat)
            self.cat.center_x = WIDTH // 2
            self.cat.center_y = HEIGHT // 2
            self.cat_list.append(self.cat)

        def on_draw(self):
            arcade.start_render()
            self.coin_list.draw()
            self.cat_list.draw()

        def on_update(self, delta_time):
            self.coin_list.update_animation()
            self.cat_list.update_animation()

    def main():
        game = MyGame(WIDTH, HEIGHT)
        arcade.run()

    main()

example1()

"""self.player = arcade.AnimatedWalkingSprite() -создаем объект класса,
в котором реализованны параметры для хранения картинок движения спрайта

self.player_list.update() -обновление всех элементов, которые переданы в список
self.player_list.update_animation() -обновление параметров класса
AnimatedWalkingSprite()

arcade.load_texture(#текстура) -загружает текстуру из вашего диска в проект

self.player = arcade.AnimatedTimeBasedSprite() -объект класса, в котором
реализованы функции хранения кадров спрайта

frame = arcade.AnimationKeyframe(#id, #длительность показа слайда, #текстура)
-объект класса, который используется для хранения элементов в объекте
arcade.AnimatedTimeBasedSprite()

self.frames = [] -список для хранения кадров спрайта
self._points-присваивание объекту списка точек для коллизии

#текстура.hit_box_points -получение размеров изображения по 4 точкам
(верние -левая, правая, нижние -левая, правая)"""