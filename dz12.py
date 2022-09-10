"""Создать дополнительный модуль и написать в нем функцию по
вычислению площади треугольника(0.5 * a * h, где a - сторона
треугольника, а h - высота). Импортировать данный модуль и
вызвать функцию расчета площади"""

def ex1():

    # from dz12_1 import square
    # print(f"Площадь треугольника со сторонами 3 и 5 равна {square(3, 5)}")

    import dz12_1
    print(f"Площадь треугольника со сторонами 3 и 5 равна {dz12_1.square(3, 5)}")

# ex1()

"""Создать дополнительный модуль и написать в нем функцию по 
вычислению площади прямоугольника. Необходимо обработать все 
возможные ошибки. Импортировать данный модуль и вызвать 
функцию расчета площади"""

def ex2():
    import dz12_2

    try:
        print(f"Площадь при сторонах 3 и 4 равна {dz12_2.square_rectangle(3, 4)}")
        print(f"Площадь при сторонах -3 и 4 равна {dz12_2.square_rectangle(-3, 4)}")
    except ValueError as e:
        print("Ошибка ввода!", e)
    try:
        print(f"Площадь при сторонах f и 4 равна {dz12_2.square_rectangle('f', 4)}")
    except ValueError as e:
        print("Ошибка ввода!", e)
    try:
        print(f'Площадь при сторонах "3" и "4" равна {dz12_2.square_rectangle("3", "4")}')
    except ValueError as e:
        print("Ошибка ввода!", e)


def ex2_2():
    import dz12_2

    print(f"Площадь при сторонах 3 и 4 равна {dz12_2.square_rectangle2(3, 4)}")
    try:
        a, b = -3, 4
        if a < 0 or b < 0:
            raise ValueError(f"Стороны должны быть положительными! {a=}, {b=}")
        print(f"Площадь при сторонах -3 и 4 равна {dz12_2.square_rectangle2(a, b)}")
    except ValueError as e:
        print("Ошибка ввода!", e)
    try:
        print(f"Площадь при сторонах f и 4 равна {dz12_2.square_rectangle2('f', 4)}")
    except TypeError as e:
        print("Ошибка ввода!", e)
    try:
        print(f'Площадь при сторонах "3" и "4" равна {dz12_2.square_rectangle2("3", "4")}')
    except TypeError as e:
        print("Ошибка ввода!", e)


ex2()
# ex2_2()