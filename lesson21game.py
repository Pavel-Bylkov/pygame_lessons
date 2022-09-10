"""
Use Pymunk physics engine.

For more info on Pymunk see:
https://www.pymunk.org/en/latest/

To install pymunk:
pip install pymunk

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.pymunk_pegboard

Click and drag with the mouse to move the boxes.
"""
import arcade
import pymunk
from arcade.color import *


def ex1():
    import random
    import timeit
    import math

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_TITLE = "Pymunk Pegboard Example"


    class CircleSprite(arcade.Sprite):
        def __init__(self, filename, pymunk_shape):
            super().__init__(filename, center_x=pymunk_shape.body.position.x, center_y=pymunk_shape.body.position.y)
            self.width = pymunk_shape.radius * 2
            self.height = pymunk_shape.radius * 2
            self.pymunk_shape = pymunk_shape


    class MyGame(arcade.Window):
        """ Main application class. """

        def __init__(self, width, height, title):
            super().__init__(width, height, title)

            self.peg_list = arcade.SpriteList()
            self.ball_list = arcade.SpriteList()

            arcade.set_background_color(AMAZON)

            self.draw_time = 0
            self.processing_time = 0
            self.time = 0

            # -- Pymunk
            self.space = pymunk.Space()
            self.space.gravity = (0.0, -900.0)

            self.static_lines = []

            self.ticks_to_next_ball = 10

            body = pymunk.Body(body_type=pymunk.Body.STATIC)
            shape = pymunk.Segment(body, (0, 10), (SCREEN_WIDTH, 10), 0.0)
            shape.friction = 10
            self.space.add(shape, body)
            self.static_lines.append(shape)

            body = pymunk.Body(body_type=pymunk.Body.STATIC)
            shape = pymunk.Segment(body, (SCREEN_WIDTH - 50, 10), (SCREEN_WIDTH, 30), 0.0)
            shape.friction = 10
            self.space.add(shape, body)
            self.static_lines.append(shape)

            body = pymunk.Body(body_type=pymunk.Body.STATIC)
            shape = pymunk.Segment(body, (50, 10), (0, 30), 0.0)
            shape.friction = 10
            self.space.add(shape, body)
            self.static_lines.append(shape)

            radius = 20
            separation = 150
            for row in range(6):
                for column in range(6):
                    x = column * separation + (separation // 2 * (row % 2))
                    y = row * separation + separation // 2
                    body = pymunk.Body(body_type=pymunk.Body.STATIC)
                    body.position = x, y
                    shape = pymunk.Circle(body, radius, pymunk.Vec2d(0, 0))
                    shape.friction = 0.3
                    self.space.add(body, shape)

                    sprite = CircleSprite(":resources:images/pinball/bumper.png", shape)
                    self.peg_list.append(sprite)

        def on_draw(self):
            self.clear()

            self.peg_list.draw()
            self.ball_list.draw()

            for line in self.static_lines:
                body = line.body

                pv1 = body.position + line.a.rotated(body.angle)
                pv2 = body.position + line.b.rotated(body.angle)
                arcade.draw_line(pv1.x, pv1.y, pv2.x, pv2.y, arcade.color.WHITE, 2)

        def on_update(self, delta_time):

            self.ticks_to_next_ball -= 1
            if self.ticks_to_next_ball <= 0:
                self.ticks_to_next_ball = 20
                mass = 0.5
                radius = 15
                inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
                body = pymunk.Body(mass, inertia)
                x = random.randint(0, SCREEN_WIDTH)
                y = SCREEN_HEIGHT
                body.position = x, y
                shape = pymunk.Circle(body, radius, pymunk.Vec2d(0, 0))
                shape.friction = 0.3
                self.space.add(body, shape)

                sprite = CircleSprite(":resources:images/items/gold_1.png", shape)
                self.ball_list.append(sprite)


            self.space.step(delta_time)

            for ball in self.ball_list:
                ball.center_x = ball.pymunk_shape.body.position.x
                ball.center_y = ball.pymunk_shape.body.position.y
                ball.angle = math.degrees(ball.pymunk_shape.body.angle)

    def main():
        MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.run()

    main()


def ex2():
    from math import degrees

    WIDTH = 800
    HEIGHT = 600
    space = pymunk.Space()
    space.gravity = 0, -1000
    x = 698
    y = 500

    # xr = 550
    # yr = 500

    mass = 1
    # inner = 0
    radius = 25
    segment_shape1 = pymunk.Segment(space.static_body, (400, 300), (700, 320), 2)
    segment_shape1.elasticity = 0.8
    segment_shape1.friction = 1
    space.add(segment_shape1)

    segment_shape2 = pymunk.Segment(space.static_body, (-200, 200), (500, 150), 2)
    segment_shape2.elasticity = 0.8
    segment_shape2.friction = 1
    space.add(segment_shape2)

    class MyGame(arcade.Window):
        def __init__(self, width, height, title):
            super().__init__(width, height, title)

            arcade.set_background_color(arcade.color.AMAZON)

            self.coin_list = arcade.SpriteList()

            self.sprite = arcade.Sprite("les2img/coin.png", 0.1, center_x=600, center_y=500)

        def on_draw(self):
            arcade.start_render()
            self.coin_list.draw()
            self.sprite.draw()
            arcade.draw_line(400, 300, 700, 320, arcade.color.RED, 2)
            arcade.draw_line(-200, 200, 500, 150, arcade.color.RED, 2)

        def on_update(self, delta_time):
            space.step(delta_time)
            for index, sprite in enumerate(self.coin_list):
                sprite.angle = degrees(space.bodies[index].angle)
                sprite.set_position(space.bodies[index].position.x, space.bodies[index].position.y)
                for body in space.bodies:
                    if body.position.y < -100:
                        self.coin_list.remove(sprite)
                        space.remove(body)

        def on_key_press(self, symbol, modifiers):
            if symbol == arcade.key.SPACE:
                # sprite = arcade.Sprite("les2img/coin.png", scale=0.1, )
                circle_moment = pymunk.moment_for_circle(mass, 0, radius)
                circle_body = pymunk.Body(mass, circle_moment)
                circle_body.position = x, y
                circle_shape = pymunk.Circle(circle_body, radius)
                circle_shape.elasticity = 0.2
                circle_shape.friction = 1

                self.sprite = arcade.Sprite("les2img/coin.png", scale=0.1, center_x=circle_body.position.x,
                                            center_y=circle_body.position.y)
                space.add(circle_body, circle_shape)

                self.coin_list.append(
                    arcade.Sprite("les2img/coin.png", center_x=circle_body.position.x, center_y=circle_body.position.y,
                                  scale=0.1))

        def on_key_release(self, symbol, modifiers):
            pass

    def main():
        game = MyGame(WIDTH, HEIGHT, "pymunk")
        arcade.run()

    main()


def ex3():
    from math import degrees

    WIDTH = 800
    HEIGHT = 600
    IMG_COIN = "les2img/coin.png"

    START_POS = (698, 500)

    space = pymunk.Space()
    space.gravity = (0, -1000)

    class Coin(arcade.Sprite):
        def __init__(self, filename, scale, position):
            super().__init__(filename, scale=scale,
                             center_x=position[0], center_y=position[1])
            self.mass = 1
            self.radius = 25
            circle_moment = pymunk.moment_for_circle(self.mass, 0, self.radius)
            self.body = pymunk.Body(self.mass, circle_moment)
            self.body.position = position
            circle_shape = pymunk.Circle(self.body, self.radius)
            circle_shape.elasticity = 0.2
            circle_shape.friction = 1
            space.add(self.body, circle_shape)

        def update(self):
            self.angle = degrees(self.body.angle)
            self.set_position(self.body.position.x, self.body.position.y)
            if self.body.position.y < -100:
                self.remove_from_sprite_lists()
                space.remove(self.body)
                print(len(space.bodies))

    class Line:
        def __init__(self, start_x, start_y, end_x, end_y, color, line_width):
            self.start_x = start_x
            self.start_y = start_y
            self.end_x = end_x
            self.end_y = end_y
            self.color = color
            self.line_width = line_width
            shape = pymunk.Segment(space.static_body, (start_x, start_y),
                                   (end_x, end_y), radius=line_width)
            shape.elasticity = 0.8
            shape.friction = 1
            space.add(shape)

        def draw(self):
            arcade.draw_line(self.start_x, self.start_y, self.end_x, self.end_y,
                             self.color, self.line_width)

    class MyGame(arcade.Window):
        def __init__(self, width, height, title):
            super().__init__(width, height, title)

            arcade.set_background_color(AMAZON)

            self.coin_list = arcade.SpriteList()
            self.line_list = [
                Line(400, 300, 700, 320, RED, 2),
                Line(-200, 200, 500, 150, RED, 2)]

            self.sprite = arcade.Sprite(IMG_COIN, scale=0.1,
                                        center_x=START_POS[0],
                                        center_y=START_POS[1])

        def on_draw(self):
            arcade.start_render()
            self.coin_list.draw()
            self.sprite.draw()
            for line in self.line_list:
                line.draw()

        def on_update(self, delta_time):
            space.step(delta_time)
            self.coin_list.update()

        def on_key_press(self, symbol, modifiers):
            if symbol == arcade.key.SPACE:
                self.coin_list.append(Coin(IMG_COIN, 0.1, START_POS))
                print(len(space.bodies))

    def main():
        game = MyGame(WIDTH, HEIGHT, "pymunk")
        game.run()

    main()


def ex4():
    import random
    from math import degrees

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_TITLE = "Pymunk Pegboard Example"
    IMG_BALL = ":resources:images/items/gold_1.png"
    IMG_PEG = ":resources:images/pinball/bumper.png"

    space = pymunk.Space()
    space.gravity = (0.0, -900.0)

    class Peg(arcade.Sprite):
        def __init__(self, filename, center_x, center_y):
            super().__init__(filename,
                             center_x=center_x, center_y=center_y)
            self.radius = 22
            self.width = self.radius * 2
            self.height = self.radius * 2
            self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
            self.body.position = center_x, center_y
            circle_shape = pymunk.Circle(self.body, self.radius, pymunk.Vec2d(0, 0))
            circle_shape.friction = 0.3
            space.add(self.body, circle_shape)

    class Ball(arcade.Sprite):
        def __init__(self, filename, center_x, center_y):
            super().__init__(filename,
                             center_x=center_x, center_y=center_y)
            self.mass = 0.5
            self.radius = 15
            self.width = self.radius * 2
            self.height = self.radius * 2
            circle_moment = pymunk.moment_for_circle(self.mass, 0, self.radius, (0, 0))
            self.body = pymunk.Body(self.mass, circle_moment)
            self.body.position = center_x, center_y
            circle_shape = pymunk.Circle(self.body, self.radius, pymunk.Vec2d(0, 0))
            circle_shape.friction = 0.3
            space.add(self.body, circle_shape)

        def update(self):
            self.angle = degrees(self.body.angle)
            self.set_position(self.body.position.x, self.body.position.y)
            if self.body.position.y < -100:
                self.remove_from_sprite_lists()
                space.remove(self.body)

    class Line:
        def __init__(self, start_x, start_y, end_x, end_y, color, line_width):
            self.start_x = start_x
            self.start_y = start_y
            self.end_x = end_x
            self.end_y = end_y
            self.color = color
            self.line_width = line_width
            shape = pymunk.Segment(space.static_body, (start_x, start_y),
                                   (end_x, end_y), radius=line_width)
            shape.elasticity = 0.8
            shape.friction = 10
            space.add(shape)

        def draw(self):
            arcade.draw_line(self.start_x, self.start_y, self.end_x, self.end_y,
                             self.color, self.line_width)

    class MyGame(arcade.Window):
        """ Main application class. """

        def __init__(self, width, height, title):
            super().__init__(width, height, title)

            self.peg_list = arcade.SpriteList()
            self.ball_list = arcade.SpriteList()

            arcade.set_background_color(AMAZON)

            self.static_lines = [
                Line(0, 10, SCREEN_WIDTH, 10, WHITE, 2),
                Line(SCREEN_WIDTH - 50, 10, SCREEN_WIDTH, 30, WHITE, 2),
                Line(50, 10, 0, 30, WHITE, 2)
            ]

            self.ticks_to_next_ball = 10

            separation = 150
            for row in range(6):
                for column in range(6):
                    x = column * separation + (separation // 2 * (row % 2))
                    y = row * separation + separation // 2
                    self.peg_list.append(Peg(IMG_PEG, x, y))

        def on_draw(self):
            self.clear()

            self.peg_list.draw()
            self.ball_list.draw()

            for line in self.static_lines:
                line.draw()

        def on_update(self, delta_time):
            self.ticks_to_next_ball -= 1
            if self.ticks_to_next_ball <= 0:
                self.ticks_to_next_ball = 20
                x = random.randint(0, SCREEN_WIDTH)
                y = SCREEN_HEIGHT
                self.ball_list.append(Ball(IMG_BALL, x, y))

            space.step(delta_time)
            self.ball_list.update()

    def main():
        MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.run()

    main()


ex1()

"""
import pymunk -импорт модуля
space = pymunk.Space() -создание пространства
space.gravity = 0, -1000 -создание гравитации
segment_shape1 = pymunk.Segment(space.static_body, (400, 300), (700, 320), 2) 
-создание статичного объекта (линии)

segment_shape1.elasticity = 0.8 -коэффициент отскока
segment_shape1.friction = 1 -коэффициент трения
space.step(delta_time)-задание частоты обновления пространства
circle_moment = pymunk.moment_for_circle(mass, 0, radius) 
-создание момента иннерции для круга
circle_body = pymunk.Body(mass, circle_moment) 
-создание тела с определенной массой и моментом иннерции
circle_shape = pymunk.Circle(circle_body, radius) -задание формы тела
*****game*****
self.ball_list:
    arcade.SpriteList[CircleSprite] = arcade.SpriteList() 
    -создание списка спрайтов, состоящего из списков спрайтов 
    body = pymunk.Body(body_type=pymunk.Body.STATIC) 
    -создание статичного тела
    shape = pymunk.Segment(body, [0, 10], [SCREEN_WIDTH, 10], 0.0) 
    -создание статичного объекта (линии)
"""