"""Дополнение к предыдущему домашнему заданию. Создать поверхность.
Вывести на него основной спрайт и монету. Реализовать управление
спрайтом по кнопкам. Сделать обработку коллизии, чтобы когда спрайт
касался монеты, монета перемещалась на новое, рандомное место, а
счёт увеличивался. Сделать вывод счёта."""

def ex1():
    import arcade, random

    WIDTH = 800
    HEIGHT = 600
    Screen_title = "Man collecting coin"
    hero_scale = 0.2

    class MyGame(arcade.Window):
        def __init__(self, width, height):
            super().__init__(width, height, Screen_title)

            self.player_sprite = arcade.Sprite("les2img/boy.png", hero_scale)

            arcade.set_background_color(arcade.color.AMAZON)

            self.score = 0
            self.x = 100
            self.y = 100
            self.speedx = 300
            self.speedy = 300
            self.playerx = 400
            self.playery = 350

            self.coin = arcade.Sprite("les2img/coin.png", 0.1)
            self.coin.center_x = random.randint(30, 770)
            self.coin.center_y = random.randint(30, 570)

            self.right = False
            self.left = False
            self.down = False
            self.up = False

        def on_draw(self):
            arcade.start_render()
            self.player_sprite.draw()
            self.coin.draw()
            arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 20)

        def on_update(self, delta_time):
            if self.right:
                self.playerx += self.speedx * delta_time
            if self.left:
                self.playerx -= self.speedx * delta_time
            if self.up:
                self.playery += self.speedy * delta_time
            if self.down:
                self.playery -= self.speedy * delta_time
            self.player_sprite.set_position(self.playerx, self.playery)

            collisions = arcade.check_for_collision(self.player_sprite, self.coin)
            if collisions:
                self.coin.center_x = random.randint(30, 770)
                self.coin.center_y = random.randint(30, 570)
                self.score += 1

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
        game = MyGame(WIDTH, HEIGHT)
        arcade.run()

    main()

# ex1()

"""Добавить в игру список из спрайтов(например, оружие из моего 
проекта). Реализовать коллизию основного спрайта со списком. 
В случае её возникновения, перемещать спрайт из списка на новую, 
рандомную точку"""

def ex2():
    import arcade, random

    WIDTH = 800
    HEIGHT = 600
    Screen_title = "Man collecting coin"
    hero_scale = 0.2
    coin_count = 10

    class MyGame(arcade.Window):
        def __init__(self, width, height):
            super().__init__(width, height, Screen_title)

            self.player_sprite = arcade.Sprite("les2img/boy.png", hero_scale)
            self.coin_list = arcade.SpriteList()

            arcade.set_background_color(arcade.color.AMAZON)

            self.score = 0
            self.x = 100
            self.y = 100
            self.speedx = 300
            self.speedy = 300
            self.playerx = 400
            self.playery = 350

            for i in range(coin_count):
                coin = arcade.Sprite("les2img/coin.png", 0.1)
                coin.center_x = random.randint(30, 770)
                coin.center_y = random.randint(30, 570)
                self.coin_list.append(coin)

            self.right = False
            self.left = False
            self.down = False
            self.up = False

        def on_draw(self):
            arcade.start_render()
            self.player_sprite.draw()
            self.coin_list.draw()
            arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 20)

        def on_update(self, delta_time):
            if self.right:
                self.playerx += self.speedx * delta_time
            if self.left:
                self.playerx -= self.speedx * delta_time
            if self.up:
                self.playery += self.speedy * delta_time
            if self.down:
                self.playery -= self.speedy * delta_time
            self.player_sprite.set_position(self.playerx, self.playery)

            self.coin_list.update()

            collisions = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
            for coin in collisions:
                coin.center_x = random.randint(30, 770)
                coin.center_y = random.randint(30, 570)
                self.score += 1

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
        game = MyGame(WIDTH, HEIGHT)
        arcade.run()

    main()

ex2()

