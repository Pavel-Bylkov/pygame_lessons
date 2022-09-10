"""Создать дисплей и на нём с помощью модуля arcade.draw_ нарисовать
картинку из геометрических фигур. Создать округлую зелёную  землю с
помощью арки. С помощью прямоугольника и треугольника нарисовать дом.
Добавьте окружность для создания солнца и окон домов.
Лучики и прегородки окон можно сделать с помощью линий"""

def ex1():
    import arcade

    screen_width = 500
    screen_height = 500

    arcade.open_window(screen_width, screen_height, "display")

    arcade.set_background_color(arcade.color.BLUE)

    arcade.start_render()

    def arca(x,y):
        arcade.draw_arc_outline(x,y-250,370,150,arcade.color.GREEN,0,180,300)
    arca(250,250)

    def house(x,y):
        arcade.draw_rectangle_filled(x,y-100,200,150,arcade.color.BROWN)
        arcade.draw_circle_filled(x-50,y-100,25,arcade.color.BLUEBERRY)
        arcade.draw_circle_filled(x+50,y-100,25,arcade.color.BLUEBERRY)
        arcade.draw_line(x+100,y-100,150,150,arcade.color.BROWN,3)
        arcade.draw_triangle_filled(120,220,260,300,380,220,arcade.color.BLACK)
    house(250,250)

    def sun(x,y):
        arcade.draw_circle_filled(x,y+20,50,arcade.color.YELLOW)
        arcade.draw_line(x-50,y-100,370,350,arcade.color.YELLOW)
        arcade.draw_line(x+20,y-35,435,320,arcade.color.YELLOW)
        arcade.draw_line(x+20,y+40,280,350,arcade.color.YELLOW)
    sun(400,400)

    arcade.finish_render()

    arcade.run()

# ex1()

"""Написать функцию, которая заполняет две диагонали экрaна снеговиками, 
состоящими из двух кругов, залитых белым цветом"""

def ex2():
    import arcade

    screen_width = 500
    screen_height = 500

    arcade.open_window(screen_width, screen_height, "display")

    arcade.set_background_color(arcade.color.ROSE_GOLD)

    def snowman(x, y):
        arcade.draw_circle_filled(x, y, 25, arcade.color.WHITE)
        arcade.draw_circle_filled(x, y + 40, 20, arcade.color.WHITE)
        arcade.draw_point(x, y + 35, arcade.color.ORANGE, 4)
        arcade.draw_point(x - 6, y + 42, arcade.color.BLACK, 4)
        arcade.draw_point(x + 6, y + 42, arcade.color.BLACK, 4)
        arcade.draw_point(x, y + 28, arcade.color.BLACK, 3)
        arcade.draw_point(x - 6, y + 30, arcade.color.BLACK, 3)
        arcade.draw_point(x + 6, y + 30, arcade.color.BLACK, 3)
        arcade.draw_point(x, y + 15, arcade.color.BLACK, 4)
        arcade.draw_point(x, y + 5, arcade.color.BLACK, 4)
        arcade.draw_point(x, y - 5, arcade.color.BLACK, 4)
        arcade.draw_arc_outline(x, y + 50, 17, 20, arcade.color.RED, 0, 180, 40)
        arcade.draw_circle_filled(x, y + 75, 8, arcade.color.WHITE)

    def snows(distance):
        for row in range(50, screen_height, distance):
            for col in range(50, screen_width, distance):
                if row == col or screen_height - row == col:
                    snowman(col, row)


    arcade.start_render()
    snows(50)
    arcade.finish_render()
    arcade.run()

ex2()