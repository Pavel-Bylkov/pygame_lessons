"""Создать пространство. В нём нарисовать горизонтальную линию(сегмент)
с коэффициентом трения и отскока. Сделать спрайт круга с физическими
величинами и с коэффициентом трения и отскока, который, при нажатии
клавиши пробел, будет падать на линию и отскакивать."""

import arcade
import pymunk

WIDTH = 800
HEIGHT = 600
IMG_COIN = "les2img/coin.png"

def ex1():

    START_POS = (WIDTH // 2, 500)

    space = pymunk.Space()
    space.gravity = (0, -1000)

    class Coin(arcade.Sprite):
        def __init__(self, filename, pos):
            super().__init__(filename, center_x=pos[0], center_y=pos[1])
            self.mass = 1
            self.radius = 25
            self.width = self.radius * 2
            self.height = self.radius * 2
            circle_moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
            self.body = pymunk.Body(self.mass, circle_moment)
            self.body.position = pos
            circle_shape = pymunk.Circle(self.body, self.radius)
            circle_shape.elasticity = 1
            circle_shape.friction = 0.04
            space.add(self.body, circle_shape)

        def update(self):
            self.set_position(self.body.position.x, self.body.position.y)

    class Line:
        def __init__(self, start_x, start_y, end_x, end_y, color, line_width):
            self.param = (start_x, start_y, end_x, end_y, color, line_width)
            shape = pymunk.Segment(space.static_body, (start_x, start_y),
                                   (end_x, end_y), radius=line_width)
            shape.elasticity = 0.95
            shape.friction = 0.04
            space.add(shape)

        def draw(self):
            arcade.draw_line(*self.param)

    class MyGame(arcade.Window):
        def __init__(self, width, height, title):
            super().__init__(width, height, title)

            arcade.set_background_color(arcade.color.AMAZON)

            self.coin = Coin(IMG_COIN, START_POS)

            self.line = Line(40, 30, WIDTH - 40, 30, arcade.color.RED, 5)
            self.pause = True

        def on_draw(self):
            self.clear()

            self.coin.draw()
            self.line.draw()

        def on_update(self, delta_time):
            if not self.pause:
                space.step(delta_time)
                self.coin.update()

        def on_key_press(self, symbol, modifiers):
            if not self.pause and symbol == arcade.key.SPACE:
                self.pause = True
            elif self.pause and symbol == arcade.key.SPACE:
                self.pause = False

    def main():
        game = MyGame(WIDTH, HEIGHT, "example 1")
        game.run()

    main()

# ex1()


"""Дополнение к первому заданию:
Реализовать счётчик шариков и вывести его на экран, при падении шарика вниз, 
удалять его из списка спрайтов, и тел space."""

def ex2():

    START_POS = (WIDTH // 2, 500)

    space = pymunk.Space()
    space.gravity = (0, -1000)

    class Coin(arcade.Sprite):
        def __init__(self, filename, pos):
            super().__init__(filename, center_x=pos[0], center_y=pos[1])
            self.mass = 1
            self.radius = 25
            self.width = self.radius * 2
            self.height = self.radius * 2
            circle_moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
            self.body = pymunk.Body(self.mass, circle_moment)
            self.body.position = pos
            circle_shape = pymunk.Circle(self.body, self.radius)
            circle_shape.elasticity = 1
            circle_shape.friction = 0.04
            space.add(self.body, circle_shape)

        def update(self):
            self.set_position(self.body.position.x, self.body.position.y)

    class Line(arcade.Sprite):
        def __init__(self, start_x, start_y, end_x, end_y, color, line_width):
            super().__init__(center_x=end_x // 2, center_y=start_y)
            self.width = end_x - start_x + 1
            self.height = end_y - start_y + 1
            self.param = (start_x, start_y, end_x, end_y, color, line_width)
            shape = pymunk.Segment(space.static_body, (start_x, start_y),
                                   (end_x, end_y), radius=line_width)
            shape.elasticity = 0.95
            shape.friction = 0.04
            space.add(shape)

        def draw(self):
            super().draw()
            arcade.draw_line(*self.param)

    class MyGame(arcade.Window):
        def __init__(self, width, height, title):
            super().__init__(width, height, title)

            arcade.set_background_color(arcade.color.AMAZON)
            self.score = 0

            self.coin = Coin(IMG_COIN, START_POS)

            self.line = Line(40, 30, WIDTH - 40, 30, arcade.color.RED, 2)
            self.pause = True

        def on_draw(self):
            self.clear()

            self.coin.draw()
            self.line.draw()
            arcade.draw_text(f"Score: {self.score}", 10, HEIGHT - 30, arcade.color.WHITE, 20)

        def on_update(self, delta_time):
            if not self.pause:
                space.step(delta_time)
                self.coin.update()
                collision = arcade.check_for_collision(self.coin, self.line)
                if collision:
                    self.score += 1

        def on_key_press(self, symbol, modifiers):
            if not self.pause and symbol == arcade.key.SPACE:
                self.pause = True
            elif self.pause and symbol == arcade.key.SPACE:
                self.pause = False

    def main():
        game = MyGame(WIDTH, HEIGHT, "example 2")
        game.run()

    main()

ex2()