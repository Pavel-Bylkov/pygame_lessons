import lesson12_2 as l2
from math import sqrt
from lesson12_2 import *

# print(l2.sqrt(9))
# print(l2.summa(2, 5))
# print(l2.sum_list([1, 2, 3, 4, 5]))
# print(l2.number)
# print(sqrt(9))
# print(number)
# # print(math.pi)


# from l2 import *
# print(sqrt(9))
# print(sum_list([1, 2, 3, 4, 5]))
# print(number)
# a = 5
# a = str(a)
# print(a)

# from l2 import sqrt, sum_list, summa
# import math
# import l2
# print(sqrt(9))
# print(sum_list([1, 2, 3, 4, 5]))
# a = 5
# a = str(a)
# print(a)
# print(type(a))
# print(summa(1, 4))
# print(l2.sqrt.__doc__)
# print(print.__doc__)
# # print(random.__doc__)
# print(math.atan2.__doc__)
# print(l2.__doc__)

# number = input()
# # print(number)
# try:
#     number = int(number)
#     print(number)
#     result = number + 5
#     print(result)
#     # print(summa)
# except ValueError as e:  # (ValueError, NameError)
#     print('Ошибка', e)
#
# print('Выполнится код')

# dd = {"d": 5, "c": 6}
#
# a, b = 1, 0
# try:
#     # print(a/b)
#     # print('10' + 10)
#     print(dd["e"])
# except (TypeError, ZeroDivisionError, KeyError):
#     print('Вы сложили значения разных типов')

# number = input("Ввести число в десятичном формате: ")
# try:
#     number = int(number)
#     print(number + 5)
# except Exception as msg:
#     print(msg)

# try:
#     # print('a' + 3)
#     # print(summ)
#     print(1/0)
# except NameError:
#     print('sum не существует')
# except ZeroDivisionError:
#     print('Вы не можете делить на ноль')
# except:
#     print('Какая то ошибка')

# try:
#     print('a')
# print('b')
# except:
#     print('c')

# try:
#     print(1 / 5)
#     # print(1 / 0)
# except ZeroDivisionError:
#     print('Это ошибка значения')
# finally:
#     print('Этот блок выполнится всегда')
# print('Этот блок выполнится всегда')
# try:
#     print(1 / 0)
# except ZeroDivisionError:
#     print('Это ошибка значения')
# finally:
#     print('Этот блок выполнится всегда')

# a, b = int(input()), int(input())
# if b == 0:
#     raise ZeroDivisionError
# print(a / b)

# a, b = int(input()), int(input())
# try:
#     if b == 0:
#         raise ZeroDivisionError
# except ZeroDivisionError:
#     print('Деление на ноль')
# try:
#     print(a / b)
# except:
#     pass
# print('Hello')
# try:
#     print('1' + 1)
# except:
#     raise

# raise ValueError('Неправильное значение')


# class Error(Exception):
#     print('Ошибка')
#
# raise Error('Моя ошибка')