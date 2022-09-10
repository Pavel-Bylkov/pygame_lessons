"""Создать дисплей, залить его цветом. Вывести на него квадрат.
Реализовать управление квадратом по стрелкам.
"""

def ex1():
    import arcade

    WIDTH = 800
    HEIGHT = 600

    class Square:
        def __init__(self, center_x, center_y, length, color):
            self.center_x = center_x
            self.center_y = center_y
            self.length = length
            self.color = color
            self.change_x = 0
            self.change_y = 0

        def draw(self):
            arcade.draw_rectangle_filled(center_x=self.center_x,
                                         center_y=self.center_y,
                                         width=self.length,
                                         height=self.length, color=self.color)

        def update(self):
            self.center_x += self.change_x
            self.center_y += self.change_y

    class MyGame(arcade.Window):
        def __init__(self):
            super().__init__(WIDTH, HEIGHT, "Ex 1")
            arcade.set_background_color(arcade.color.BUFF)
            self.sprite = Square(center_x=WIDTH//2, center_y=HEIGHT//2,
                                 length=50, color=arcade.color.RED)

        def on_draw(self):
            self.clear()
            self.sprite.draw()

        def on_update(self, delta):
            self.sprite.update()

        def on_key_press(self, key, modifer):
            if key == arcade.key.LEFT:
                self.sprite.change_x = -5
            if key == arcade.key.RIGHT:
                self.sprite.change_x = 5
            if key == arcade.key.UP:
                self.sprite.change_y = 5
            if key == arcade.key.DOWN:
                self.sprite.change_y = -5

        def on_key_release(self, key, modifer):
            if key == arcade.key.LEFT or key == arcade.key.RIGHT:
                self.sprite.change_x = 0
            if key == arcade.key.UP or key == arcade.key.DOWN:
                self.sprite.change_y = 0

    def main():
        game = MyGame()
        game.run()

    main()

# ex1()


"""
Создать дисплей, залить его цветом. Добавить в игру спрайт персонажа. 
Реализовать управление спрайта по клавишам, а также анимацию ходьбы. 
Добавить мелодию на задний фон."""


def ex2():
    import arcade
    import os

    WIDTH = 800
    HEIGHT = 600

    WALK_SOUND = f"sounds{os.sep}hurt1.wav"
    HERO_IMG = f"les2img{os.sep}walking_man.png"

    volume = 0.3

    textur_for_man = []
    for row in range(4):
        textur_for_man.append([])
        for col in range(12):
            textur_for_man[row].append(arcade.load_texture(
                HERO_IMG, x=col * 95, y=row * 158, width=95, height=158))

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

    class MyGame(arcade.Window):
        def __init__(self):
            super().__init__(WIDTH, HEIGHT, "Ex 1")
            arcade.set_background_color(arcade.color.BUFF)
            self.sprite = Person(center_x=WIDTH // 2, center_y=HEIGHT // 2)
            self.sound = arcade.Sound(WALK_SOUND)
            self.sound.play(volume, loop=True)

        def on_draw(self):
            self.clear()
            self.sprite.draw()

        def on_update(self, delta):
            self.sprite.update()
            self.sprite.update_animation()

        def on_key_press(self, key, modifer):
            if key == arcade.key.LEFT:
                self.sprite.change_x = -5
            if key == arcade.key.RIGHT:
                self.sprite.change_x = 5
            if key == arcade.key.UP:
                self.sprite.change_y = 5
            if key == arcade.key.DOWN:
                self.sprite.change_y = -5

        def on_key_release(self, key, modifer):
            if key == arcade.key.LEFT or key == arcade.key.RIGHT:
                self.sprite.change_x = 0
            if key == arcade.key.UP or key == arcade.key.DOWN:
                self.sprite.change_y = 0

    def main():
        game = MyGame()
        game.run()

    main()


# ex2()

"""Добавить к прошлой задаче фрукты, добавить коллизию между персонажем 
и фруктом. Вывести счёт съеденных фруктов на экран."""

def ex3():
    import arcade
    import os
    from random import randint

    WIDTH = 800
    HEIGHT = 600

    WALK_SOUND = f"sounds{os.sep}hurt1.wav"
    HERO_IMG = f"les2img{os.sep}walking_man.png"
    STAR = f":resources:images{os.sep}items{os.sep}star.png"

    volume = 0.3

    textur_for_man = []
    for row in range(4):
        textur_for_man.append([])
        for col in range(12):
            textur_for_man[row].append(arcade.load_texture(
                HERO_IMG, x=col * 95, y=row * 158, width=95, height=158))

    class Star(arcade.Sprite):
        def __init__(self, center_x, center_y):
            super().__init__(filename=STAR, scale=0.5,
                             center_x=center_x, center_y=center_y)
        def reset_pos(self):
            self.center_x = randint(20, WIDTH-20)
            self.center_y = randint(20, HEIGHT-20)

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

    class MyGame(arcade.Window):
        def __init__(self):
            super().__init__(WIDTH, HEIGHT, "Ex 3")
            arcade.set_background_color(arcade.color.DARK_GREEN)
            self.sprite = Person(center_x=WIDTH // 2, center_y=HEIGHT // 2)
            self.sound = arcade.Sound(WALK_SOUND)
            self.sound.play(volume, loop=True)
            self.score = 0
            self.stars = arcade.SpriteList()
            for i in range(20):
                star = Star(center_x=randint(20, WIDTH-20),
                            center_y=randint(20, HEIGHT-20))
                self.stars.append(star)

        def on_draw(self):
            self.clear()
            self.sprite.draw()
            self.stars.draw()
            arcade.draw_text(f"Score {self.score}", start_x=20, start_y=HEIGHT-30,
                             font_size=20)

        def on_update(self, delta):
            self.sprite.update()
            self.sprite.update_animation()

            collisions = arcade.check_for_collision_with_list(self.sprite, self.stars)
            for star in collisions:
                star.reset_pos()
                self.score += 1

        def on_key_press(self, key, modifer):
            if key == arcade.key.LEFT:
                self.sprite.change_x = -5
            if key == arcade.key.RIGHT:
                self.sprite.change_x = 5
            if key == arcade.key.UP:
                self.sprite.change_y = 5
            if key == arcade.key.DOWN:
                self.sprite.change_y = -5

        def on_key_release(self, key, modifer):
            if key == arcade.key.LEFT or key == arcade.key.RIGHT:
                self.sprite.change_x = 0
            if key == arcade.key.UP or key == arcade.key.DOWN:
                self.sprite.change_y = 0

    def main():
        game = MyGame()
        game.run()

    main()


# ex3()
