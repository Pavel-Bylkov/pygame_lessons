import arcade as ar

ar.open_window(width=700, height=700, window_title="display")
ar.set_background_color(color=(0, 35, 149))

ar.start_render()

ar.draw_rectangle_filled(center_x=350, center_y=350, width=100, height=200,
                         color=(133, 45, 220), tilt_angle=30)
# ar.draw_rectangle_outline(350,350,100,200,(133,45,220),15,20)
# ar.draw_circle_filled(350,350, 75, ar.color.LIGHT_BLUE,0,5)
# ar.draw_circle_outline(350,350, 75, ar.color.LIGHT_BLUE,10,30,15)
#
# ar.draw_line(start_x=0, start_y=0, end_x=700, end_y=700, color=ar.color.PINK,
#              line_width=5)
# ar.draw_line_strip(point_list=[[300, 300], [600, 700], [500, 0], [300, 300]],
#                    color=ar.color.LIVER, line_width=15)
# ar.draw_lines(point_list=[[300, 300], [600, 700], [500, 0], [400, 300]],
#               color=ar.color.LIVER, line_width=15)

# ar.draw_triangle_outline(x1=0, y1=0, x2=300, y2=300, x3=300, y3=0,
#                          color=ar.color.FIREBRICK, border_width=5)

# ar.draw_ellipse_filled(center_x=300, center_y=300, width=300, height=150,
#                        color=ar.color.GREEN, tilt_angle=10)

# ar.draw_point(x=350, y=350, color=ar.color.AO, size=30)

# ar.draw_arc_outline(center_x=350, center_y=350, width=400, height=250,
#                     color=ar.color.AERO_BLUE, start_angle=0, end_angle=250,
#                     border_width=5, tilt_angle=40, num_segments=10)
# ar.draw_parabola_filled(start_x=150, start_y=150, end_x=400, height=200,
#                         color=ar.color.AMARANTH)
#
# ar.draw_polygon_filled(point_list=[[300, 300], [600, 700], [500, 0], [400, 300]],
#                        color=ar.color.FAWN)
#
# image = ar.get_image(x=0, y=0, width=700, height=700)
# image.save("screen1.png", format="PNG")
# #
# print(ar.get_pixel(x=350, y=350, components=4))  # 3 components (RGB). 4 - would be RGBA
#
ar.finish_render()


ar.run()

# arcade.start_render()#Начало отрисовки

# arcade.draw_rectangle_filled(центр x,y,ширина, высота, цвет в формате ргб, наклон)
# arcade.draw_rectangle_outline(центр x,y,ширина, высота, цвет в формате ргб,толщина обводки, наклон)
# arcade.draw_circle_filled(центр x,y, радиус, цвет, наклон, количество секторов)
# arcade.draw_circle_outline(центр x,y, радиус, цвет,толщина, наклон, количество секторов)
# arcade.draw_line(координаты начала, конца, цвет, толщина)
# arcade.draw_line_strip(список координат, цвет, толщина)
# arcade.draw_lines(список координат, цвет, толщина)
# arcade.draw_triangle_filled(координаты точек(6), цвет)
# arcade.draw_ellipse_filled(центр x,y,ширина, высота, цвет в формате ргб, наклон)
# arcade.draw_point(центр x,y,цвет, размер)
# arcade.draw_arc_outline(центр x,y,ширина, высота, цвет в формате ргб,угол старта, угол конца)
# arcade.draw_parabola_filled(точка старта x,y,точка конца х, высота, цвет в формате ргб)
# arcade.draw_polygon_filled(список координат, цвет)
# arcade.finish_render()#Конец отрисовки
# arcade.run()# ожидание закрытия окна