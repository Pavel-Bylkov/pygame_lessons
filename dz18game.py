"""Создать поверхность. Найти в интернете изображение персонажа
(или использовать моего), добавить его на дисплей.
Реализовать управление по стрелкам при помощи изменение координат
и присваивания этих координат спрайту при помощи функции set_position().

"""

def ex1():
    import arcade

    WIDTH = 800
    HEIGHT = 600

    class MyGame(arcade.Window):
        def __init__(self, width, height):
            super().__init__(width, height)

            arcade.set_background_color(arcade.color.AMAZON)

            self.x = 100
            self.y = 100
            self.speedx = 10
            self.speedy = 10
            self.playerx = 400
            self.playery = 350

            self.sprite1 = arcade.Sprite(filename="les2img/boy.png",
                                         scale=0.2, center_x=400, center_y=300)

            self.right = False
            self.left = False
            self.down = False
            self.up = False

        def on_draw(self):
            self.clear()
            self.sprite1.draw()

        def on_update(self, delta_time):
            if self.right:
                self.playerx += self.speedx  # * delta_time
            if self.left:
                self.playerx -= self.speedx  # * delta_time
            if self.up:
                self.playery += self.speedy  # * delta_time
            if self.down:
                self.playery -= self.speedy  # * delta_time
            self.sprite1.set_position(self.playerx, self.playery)

        def on_key_press(self, symbol, modifiers):
            if symbol == arcade.key.RIGHT:
                self.right = True
            if symbol == arcade.key.LEFT:
                self.left = True
            if symbol == arcade.key.UP:
                self.up = True
            if symbol == arcade.key.DOWN:
                self.down = True

        def on_key_release(self, symbol, modifiers):
            if symbol == arcade.key.RIGHT:
                self.right = False
            if symbol == arcade.key.LEFT:
                self.left = False
            if symbol == arcade.key.UP:
                self.up = False
            if symbol == arcade.key.DOWN:
                self.down = False

    def main():
        win = MyGame(WIDTH, HEIGHT)
        win.run()

    main()

# ex1()

"""Добавить ещё один спрайт(монетки или любой другой) для будущего 
взаимодействия с персонажем и вывести их на экран."""

def ex2():
    import arcade, random

    WIDTH = 800
    HEIGHT = 600

    class MyGame(arcade.Window):
        def __init__(self, width, height):
            super().__init__(width, height)

            arcade.set_background_color(arcade.color.AMAZON)

            self.x = 100
            self.y = 100
            self.speedx = 10
            self.speedy = 10
            self.playerx = 400
            self.playery = 350

            self.sprite1 = arcade.Sprite(filename="les2img/boy.png",
                                         scale=0.2, center_x=400, center_y=300)

            self.coin_list = arcade.SpriteList()
            for i in range(12):
                coin = arcade.Sprite(filename="les2img/coin.png", scale=0.1,
                                     center_x=random.randint(30, 770),
                                     center_y=random.randint(30, 570))
                self.coin_list.append(coin)

            self.right = False
            self.left = False
            self.down = False
            self.up = False

        def on_draw(self):
            arcade.start_render()
            self.coin_list.draw()
            self.sprite1.draw()

        def on_update(self, delta_time):
            if self.right:
                self.playerx += self.speedx  # * delta_time
            if self.left:
                self.playerx -= self.speedx  # * delta_time
            if self.up:
                self.playery += self.speedy  # * delta_time
            if self.down:
                self.playery -= self.speedy  # * delta_time
            self.sprite1.set_position(self.playerx, self.playery)

        def on_key_press(self, symbol, modifiers):
            if symbol == arcade.key.RIGHT:
                self.right = True
            if symbol == arcade.key.LEFT:
                self.left = True
            if symbol == arcade.key.UP:
                self.up = True
            if symbol == arcade.key.DOWN:
                self.down = True

        def on_key_release(self, symbol, modifiers):
            if symbol == arcade.key.RIGHT:
                self.right = False
            if symbol == arcade.key.LEFT:
                self.left = False
            if symbol == arcade.key.UP:
                self.up = False
            if symbol == arcade.key.DOWN:
                self.down = False

    def main():
        win = MyGame(WIDTH, HEIGHT)
        win.run()

    main()

ex2()
