# a = 5
# b = 'hello'
# class Test:
#     pass
#
# def func():
#     pass


# def foo(func):
#     func("Hello")
#     return 5
#
# p = print
# p("Test")
# print = foo
# p(print(p))

# print(type(a))
# print(type(b))
# print(type(func))
# print(type(Test))

# def func():
#     print('hello')
#
# a = func
#
# a()

# def func():
#     # global func1
#     def func1():
#         print('func1')
#     func1()
#
# func()
# func1()
#
# def wrapper_func():
#     def func():
#         print('Hello')
#     func()
#
# wrapper_func()

# def func1(func):
#     print(f'Получена функция {func}')
#     func()
#     return func
#
# def func():
#     print('Hello')
#
# print(func1(func))
#
# def dec_func(func):
#     def wrapper():
#         print('Это функция обертка')
#         print(f'Оборачиваем функцию {func}')
#         print('Вызываем функцию func')
#         func()
#         print('Выходим из обертки')
#     return wrapper
#
# @dec_func
# def func():
#     print('Hello')
#
# func()
# # func = dec_func(func)
# func()
#
#
# func = dec_func(func)
# func()

import time
import requests
#
# def dec_func(func):
#     def wrapper():
#         s = time.time()
#         func()
#         e = time.time()
#         print(f'Время выполнения {e - s}')
#     return wrapper

# @dec_func
# def func():
#     result = requests.get('https://google.com')
#
# @dec_func
# def foo():
#     time.sleep(2)
#
# func()
# foo()
#
# def dec_func(func):
#     def wrapper(*args, **kwargs):  #
#         s = time.time()
#         value = func(*args, **kwargs)
#         e = time.time()
#         print(f'Время выполнения {e - s}')
#         return value
#     return wrapper

# @dec_func
# def func(u):
#     r = requests.get(u)
#     return r.text
#
# func(u='https://google.com')
# # func = dec_func(func)
# a = func(u='https://google.com')
# print(a)
#
# def dec_func(iters):
#     def new_dec(func):
#         def wrapper(*args, **kwargs):
#             result = 0
#             for i in range(iters):
#                 s = time.time()
#                 value = func(*args, **kwargs)
#                 e = time.time()
#                 result += e - s
#             print(f'Среднее время {result/iters}')
#             return value
#         return wrapper
#     return new_dec
# #
# @dec_func(iters=5)
# def func(u):
#     r = requests.get(u)
#     return r.text
#
# @dec_func(2)
# def foo():
#     time.sleep(1)
#
# result = func('https://python.org')
# print(result)
# foo()

# @dec_func(iters=5)
# class Test:
#     def __call__(self, value):
#         print(f'Вывод функции {value}')
#
#
# a = Test()
#
# a('Hello')