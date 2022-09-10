# Урок 5
# **Цели занятия:
# *** Изучить функции
# * Изучить запись и сохранение в файл

# ## Функции
# Как мы знаем, функции могут быть принимающими, возвращающими.
# Принимающая функция может принимать, как ограниченное количество
# аргументов:
# def summa(a, b):
#     return a * 2 + b * 2
#
# s = summa(3, 4)
# print(s)


# Также функция может принимать и неизвестное количество аргументов.
# Для этого используются позиционные аргументы (*args) или
# именнованные аргументы (**kwargs):
# def list_number(x, y=0, *args, **kwargs):
#     print(f'{x=}')
#     print(f'{y=}')
#     print(f'{args=}')
#     print(f'{kwargs=}')
#
# list_number(6)
#
# list_number(4, 6, 2, {3, 4}, 5, 6, a=4, b=[5, 5])

# *args - возвращаются в виде кортежа,
# а **kwargs - словаря

# При написании функции, мы можем указать значение, которое она
# принимает по умолчанию. Это значит, что если пользователь не
# укажет при вызове функции, данный параметр, то ошибки не возникнет,
# а сам аргумент примет значение по умолчанию:

# def test(name, age=10, school=10):
#     print(f'{name=}')
#     print(f'{age=}')
#     print(f'{school=}')
#
# test('Вася', school=12, age=13)

# a = [1, 2, 3, 4, 5]
# print(sum(a))
# # print(max(a))
# # print(min(a))
# sum = 6
# a.append(sum)
# print(a)
# # print(sum(a))
# print = 'hello'
# print(a)

## Рекурсия
# Python поддерживает работу с рекурсивными функциями.
# >Рекурсивная функция -функция, которая вызывает сама себя,
# для создание цикличности.
# Пример создания простейшей рекурсивной функции:
# def recursion_func(x):
#     if x == 5:
#         return "hello"
#     print(x)
#     print(recursion_func(x + 1))
#     print(x)
#
# recursion_func(1)

# list1 = [1, 2, 3, 4, 5, 6]
#
# def summa(list1):
#     print(list1)
#     if not list1:
#         return 0
#     return list1[0] + summa(list1[1:])
# print(summa(list1))

# Код выше приведет к ошибке превышения глубины рекурсии.
# Глубину рекурсии можно увеличить указав ее в функции setrecursionlimit,
# находящейся в модуле sys:
# import sys
# sys.setrecursionlimit(5000)
#
# def recursion_func(x):
#     if x == 1235:
#         return 0
#     print(x)
#     return recursion_func(x + 1)
#
# recursion_func(1)

# Синтаксис тернарного выражения:
# *<что будет если условие верно> <условие> <иначе> <что будет если условие не верно>*

# list1 = [1, 2, 3, 4, 5, 6]
# list2 = [x for x in range(1, 7) if x % 2 == 0]
# print(list2)
# def summa(list1):
#     return 0 if not list1 else list1[0] + summa(list1[1:])
#
# print(summa(list1))
# x = 3
# result = 'YES' if x % 2 == 0 else 'NO'
# print(result)
# if x % 2 == 0:
#     print('YES')
# else:
#     print('NO')

# list1 = [1, 2, 3, 4, 5, 6]
# def summa(list1):
#     return list1[0] if len(list1) == 1 else list1[0] + summa(list1[1:])

# Рекурсивные функции выше являются **прямыми**.
# Существуют и **косвенные** рекурсивные функции
# >Косвенная рекурсивная функция -функция, которая вызывает другую функцию,
# которая потом вызывает первую функцию
# print(summa(list1))
# list1 = [1, 2, 3, 4, 5, 6]
# def summa(list1):
#     if not list1: return 0
#     return nonempty(list1)
#
# def nonempty(list1):
#     return list1[0] + summa(list1[1:])
#
# print(summa(list1))
# print(4 + 3)
# name = 'Ruslan'
# file = open("text.txt", "w")
# print('Ваше имя', name, sep=':', end='!', file=file)
# file.close()
# print()
# def summa(x) -> int:
#     return x + 6
#
# print(summa(5))

# '''
# Это 5 занятие по Python,
# в котором мы рассматриваем
# функции
# '''
#
# def calc_summa(x):
#     """
#     Функция принимает целое число
#     и расчитывает сумму данного числа
#     с числом 5
#     """
#     return x + 5
#
# print(calc_summa(2))
# print(calc_summa.__doc__)
# print(__doc__)

# from pprint import pformat, pprint
#
# dict1= {'a': 1, 'b': 2, 'c': 3, 'd': [4,[5, 6]]}
# print(dict1)
# pprint(dict1, width=1)
# pprint(dict1, depth=3)
# #
# dict1= {'a': 1, 'b': 2, 'c': 3, 'd': [4,[5, 6]]}
# pretty = pformat(dict1, depth=1)
# print(pretty)
# #
#
# file_name = 'text.txt'
# file = open(file_name, 'w')
# file.write('Hello')
# file.close()
#
# file = open(file_name, 'a')
# file.write('\nworld')
# file.close()
#
# file = open(file_name, "r")
# print(file.read())

# Существует еще один способ работы с файлами.
# Для этого применяется менеджер контекста with..as.
# >Кстати при использовании данного способа файл закрывать не надо.
# Он закрывается автоматически
# with open('text.txt', 'a') as file:
#     file.write('\nNew Line')
#     file.write('\nNew Line')
#     file.write('\nNew Line')

# Для считывания файла,также есть методы readline() и  readlines()
# readline() -Считывает файл построчно
# readlines-читает и возвращает список всех строк в файле
# with open('text.txt', 'r') as file:
#     # file.writelines(['\nnew', '\nline', '\npython'])
#     # print(file.readline())
#     for line in file.readlines():
#         print(line, end="")
#     # for line in file:
#     #     print(line, end="")

# print(line)

# import os
# os.rename('text.txt', 'rename.txt')