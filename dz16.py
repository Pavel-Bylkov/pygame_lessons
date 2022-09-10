"""Написать простой декоратор, используя декоратор wraps, для передачи
данных от оригинальной функции. Реализовать простую функцию с print()
и строкой документации. Вывести __name__ и __doc__
"""

def ex1():
    import functools

    def dec(func):
        @functools.wraps(func)
        def wraper(*argc, **kwargs):
            print("Декоратор")
            return func(*argc, **kwargs)
        return wraper

    @dec
    def foo():
        """Функция ничего не делающая))"""
        print("Привет")

    foo()
    print(foo.__name__)
    print(foo.__doc__)

# ex1()

"""Написать класс декоратор и декорировать им функцию. В функции 
реализовать вывод сообщения hello. Реализовать в классе декораторе, 
вывод сообщения bye через 3 секунды.
"""

def ex2():
    import time
    import functools

    class Bye:
        def __init__(self, func):
            functools.update_wrapper(self, func)
            self.func = func

        def __call__(self, *args, **kwargs):
            value = self.func(*args, **kwargs)
            time.sleep(3)
            print("Bye")
            return value

    @Bye
    def hello():
        """Func Hello"""
        print("Hello")

    hello()
    print(hello.__name__)
    print(hello.__doc__)


ex2()
