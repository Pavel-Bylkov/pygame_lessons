"""Реализовать простейший декоратор, который выводит любое сообщение.
Создать обычную функцию, принимающую имя и вывести в консоль.
"""
def ex1():
    def dec_func(func):
        def wrapper(*args, **kwargs):
            print("Работает декоратор до вызова")
            result = func(*args, **kwargs)
            print("Работает декоратор после вызова")
            return result
        return wrapper

    @dec_func   # foo = dec_func(foo)
    def foo(name):
        """doc string"""
        print(name)

    # foo = dec_func(foo)
    @dec_func
    def foo2(name):
        print("Hello", name)
        return 555
    foo("Pavel")
    print(foo2("Pavel"))

# ex1()

"""Создать функцию, которая находит периметр квадрата. Функция 
должна принимать сторону квадрата. Реализовать декоратор, замеряющий 
время выполнения функции."""

import time

def ex2():
    def dec_func(func):
        def wraper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            print(f"Время выполнения - {(time.time() - start):.6f} сек")
            return result
        return wraper

    @dec_func
    def foo(a):
        # time.sleep(1)
        print(f"Периметр квадрата со стороной {a} = {a * 4}")

    foo(500000000)


ex2()