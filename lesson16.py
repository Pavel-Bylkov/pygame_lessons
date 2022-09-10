# def dec_func(func):
#     def wrapper(*args, **kwargs):
#         return f'{func(*args, **kwargs)}'
#     return wrapper

import functools

def cache_func(func):
    _cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        name = func.__name__
        key = (name, args, frozenset(kwargs.items()))
        if key in _cache:
            return _cache[key]
        result = func(*args, **kwargs)
        _cache[key] = result
        return result
    return wrapper

@cache_func
def func(a, b):
    """Функция возвращает результат сложения a и b"""
    return a + b

print(func(5, 6))
print(func(5, 6))
print(func(5, 6))

# #
# @dec_func
# def summa(*args):
#     """Возвращает сумму чисел"""
#     total = 0
#     for item in args:
#         total += item
#     return total
#
# print(func(1, 5) + summa(1, 2, 3, 4, 5))
# print(summa(1, 2, 3, 4, 5))
# print(func.__name__)
# print(summa.__name__)
# print(func.__doc__)
# print(summa.__doc__)

# class Counter:
#     def __init__(self, s=0):
#         self.count = s
#
#     def __call__(self):
#         self.count += 1
#         print(f'Вызовов {self.count}')
#
# counter = Counter()
# counter()
# counter()
# counter()

# class Counter:
#     def __init__(self, func):
#         functools.update_wrapper(self, func)
#         self.func = func
#         self.num = 0
#
#     def __call__(self, *args, **kwargs):
#         self.num += 1
#         print(f'Вызов {self.func.__name__}: {self.num}')
#         return self.func(*args, **kwargs)
#
# @Counter
# def func(name):
#     print(f'Привет {name}')
# #
# func('Иван')
# func('Сергей')
# func('Петр')
# func('Алексей')


# class ClassTest:
#     @staticmethod
#     def staticmetod():
#         print('Это статичный метод')
#
# ClassTest.staticmetod()
# a = ClassTest()
# a.staticmetod()
#
# class Person:
#     a = 0
#     @staticmethod
#     def your_age(age):
#         # cls.a += 1
#         if age > 18:
#             return True
#         else:
#             return False

# a = Person()
# print(Person.your_age(16))
# print(a.your_age(16))

# class Test:
#     a = 0
#     @classmethod
#     def func(cls):
#         cls.a += 1
#         print('Это метод класса')
#
# Test.func()
# a = Test()
# a.func()

# class Test:
#     total = 0
#     def __init__(self):
#         Test.total = Test.total + 1
#
#     @classmethod
#     def total_obj(cls):
#         print(f'Количество {cls.total}')
# #
# a = Test()
# b = Test()
# c = Test()
# Test.total_obj()
#
# class ChildTest(Test):
#     total = 0
#
#
# ChildTest.total_obj()

# class Test(object):
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#
#     @property
#     def get_full_name(self):
#         return f'{self.name} {self.last_name}'
#
# person = Test('Иван', 'Петров')
# print(person.get_full_name)
# # person.get_full_name = 'Петр'
# import time
# def slow(_func=None, *, rate=1):
#     def dec_func(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             time.sleep(rate)
#             return func(*args, **kwargs)
#         return wrapper
#     if _func is None:
#         return dec_func
#     else:
#         return dec_func(_func)
# #
# @slow(rate=2)
# def count(number):
#     if number < 1:
#         print('Hello')
#     else:
#         print(number)
#         count(number - 1)
#
# count(3)

import time
def slow(rate=1):
    def dec_func(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapper
    return dec_func
#
@slow(rate=2)
def count(number):
    if number < 1:
        print('Hello')
    else:
        print(number)
        count(number - 1)

count(3)