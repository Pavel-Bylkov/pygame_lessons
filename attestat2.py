"""Написать модуль с функциями суммы, вычитания, умножения, деления.
В основном файле создать консольную программу калькулятор и
воспользоваться для расчета функциями из модуля
"""

def ex1():

    from attestat2_modul1 import summ, div, multi, sub

    def choice(op):
        """Возвращает функцию соответствующую знаку оператора"""
        if op == "+":
            return summ
        if op == "-":
            return sub
        if op == "*":
            return multi
        if op == "/":
            return div
        raise ValueError("Применен не известный оператор. Действительны [+, -, *, /]")

    def parser(string):
        """Преобразовывает строку.
        Возвращает список - первый аргумент, оператор и второй аргумент"""
        items = string.split()
        if len(items) != 3:
            raise ValueError("Недопустимое количество параметров. Верный формат 'value1 operator value2'")
        return items

    def detect_type(num):
        """Определяет подходящий тип для числа и возвращает нужный"""
        try:
            value = int(num)
        except:
            value = float(num)
        return value

    def main():
        print("\n********* Калькулятор 1.0 *********")
        while True:
            string = input("Введите выражение в формате 'value1 operator value2' или нажмите Enter для выхода\n")
            if not string:
                break
            try:
                num1, op, num2 = parser(string)
                func = choice(op)
                print(string, "=", func(detect_type(num1), detect_type(num2)))
            except ValueError as e:
                print("Ошибка:", e)
            except ZeroDivisionError:
                print("Ошибка: На ноль делить нельзя!")
            print()
        print("\n********* До новых встреч! *********")

    main()

# ex1()

"""Написать функцию вычисляющую площадь прямоугольника. 
Создать декоратор для данной функции, для расчета времени 
работы функции. Результат вывести в консоль
"""

def ex2():
    import time
    import functools

    def dec_func(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            s = time.time()
            value = func(*args, **kwargs)
            print("Время выполнения", time.time() - s, "сек.")
            return value
        return wrapper

    @dec_func
    def foo(a, b):
        """функция вычисляющая площадь прямоугольника"""
        return a * b

    print("Площадь прямоугольника размером 3 на 4 равна", foo(3, 4))
    print(foo.__name__)
    print(foo.__doc__)


# ex2()

"""Реализовать класс итератора и перебрать список 
a = [1, 2, 3, 4, 5, 6] с использованием итератора
"""

def ex3():

    class MyIter:
        def __init__(self, a):
            self.a = a
            self.i = 0

        def __iter__(self):
            self.i = 0
            return self

        def __next__(self):
            if self.i == len(self.a):
                raise StopIteration
            value = self.a[self.i]
            self.i += 1
            return value

    a = [1, 2, 3, 4, 5, 6]
    for i in MyIter(a):
        print(i, end=" ")
    print()


# ex3()
