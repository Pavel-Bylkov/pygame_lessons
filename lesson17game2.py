import arcade
from random import randint

screen_width=700
screen_height =700

arcade.open_window(screen_width, screen_height, "display")

arcade.set_background_color(arcade.color.GREEN)

arcade.start_render()

def draw_pine(x,y):
    arcade.draw_triangle_filled(x,y,
                                x-40,y-100,
                                x+40,y-100,
                                arcade.color.DARK_GREEN)

    arcade.draw_lrtb_rectangle_filled(x-10,x+10,y-100,y-140,arcade.color.DARK_BROWN)
def draw_smile(x,y):
    arcade.draw_circle_filled(x,y,50,arcade.color.YELLOW)
    arcade.draw_circle_filled(x+20 ,y+10, 5, arcade.color.BLACK)
    arcade.draw_circle_filled(x - 20, y + 10, 5,  arcade.color.BLACK)
    arcade.draw_arc_outline(x,y-20,60,35,arcade.color.BLACK,190,350,5)
radius=50
for row in range(screen_width//radius*2):
    for col in range(screen_height//radius*2):
        x = col*radius*2 + radius
        y = row*radius*2 + radius
        draw_smile(x,y)

for i in range(15):
    x=randint(0,700)
    y=randint(0,700)
    draw_pine(x,y)
arcade.finish_render()

arcade.run()