# Задача 1
# Составить из элементов списка целое число

# list1 = [1, 14, 36]

# result = ''
# for i in list1:
#     result += str(i)
#
#
# result = int(result)
# print(type(result))
# print(result)

# num = list(map(int, input().split()))

# str(lis1)
# result = int(''.join(map(str, list1)))
#
# print(type(result))
# print(result)


# Задача 2
# Написать программу, которая из строки создает список слов, длинна которых не менее n
# def long_word(n, str1):
#     words = []
#     word_current = str1.split()
#     # print(word_current)
#     for word in word_current:
#         if len(word) > n:
#             words.append(word)
#     return words
# print(long_word(4, 'Я изучаю базовый курс языка Python'))

# words = []
# def long_word(n, str1):
#     word_current = str1.split(' ')
#     # print(word_current)
#     for word in word_current:
#         if len(word) > n:
#             words.append(word)
#
#
#
# long_word(4, 'Я изучаю базовый курс языка Python')
# print(words)
# x = 1
# def func(x):
#
#     x += 3
#     return x
#
# x = func(x)
# print(x)


# Задача 3
# Написать программу, которая изменяет значение словаря на среднее арифметическое

# def sum_math_average(list1):
#     for d in list1:
#         n1 = d.pop('A')
#         n2 = d.pop('B')
#         # print(n1, n2)
#         d['A+B'] = (n1 + n2) / 2
#     # return list1
#
#
# list1 = [
#     {'name': 'Петя', 'A': 70, 'B': 82},
#     {'name': 'Вася', 'A': 73, 'B': 75},
#     {'name': 'Иван', 'A': 76, 'B': 86}
# ]
#
# sum_math_average(list1)
# print(list1)

# Задача 4
# Написать программу, которая из строки создает словарь. Каждый символ строки, является ключом словаря

# str1 = 'helloworld'
# dict1 = {}
# # for char in str1:
# #     dict1[char] = 1
# for char in str1:
#     dict1[char] = dict1.get(char, 0) + 1
#     if char in dict1:
#         dict1[char] += 1
#     else:
#         dict1[char] = 1
    # dict1[char] = dict1[char] + 1 if char in dict1 else 1
#
# print(dict1)

# Задача 5
# Написать программу, которая выводит отсортированный по ключу словарь

# dict1 = {'b': 1, 'z': 4, 'a': 11, 'w': 7, 'c': 3}
# for key in sorted(dict1):
#     print(f'{key}: {dict1[key]}')

# Фукнния map()
# map(функция, итерируемый объект]

# numbers = [1, 2, 3, 4, 5]
# def square(number):
#     return number ** 2
#
# squared = list(map(square, numbers))
# # # for num in numbers:
# # #     squared.append(num ** 2)
# #
# print(squared)

# squared = list(map(lambda num: num ** 2, numbers))
# print(squared)
# first = [1, 2, 3, 4]
# second = [4, 5, 6, 7]
# result = list(map(lambda num1,num2: num1 * num2, first, second))
# print(result)


#Метод get у словаря

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# for char in dict1:
#     dict1[char] = dict1.get(char, 0) + 1
# #
# #
# print(dict1)

# print(dict1.get('d', 0))
# if dict1.get('d') == None:
#     print('Ключа нет')


# Библиотека дня datetime

# date - хранит дату
# time - хранит время
# datetime -хранит время и дату

# import datetime
#
# dt_current = datetime.datetime.now()
# print(dt_current)

# from datetime import date
# #
# current_date = date.today()
# current_date += date.
# print()
# print(current_date)
#
# import datetime
#
# current_date_time = datetime.datetime.now()
# current_time = current_date_time.time()
# print(current_time)
#
# import datetime

# dirs = dir(datetime)
# print(dirs)

# time = datetime.time(14,14,22)
#
# print(time)
#
# date = datetime.datetime(2022, 2, 3, 14, 14, 22)
# print(date)
#
# tdelta = datetime.timedelta(days=2, seconds=0, microseconds=0, milliseconds=0, minutes=42, hours=1, weeks=1)
# print(tdelta)
# print(date + tdelta)
# print(datetime.timedelta(weeks=1))

# first = datetime.date(2020, 1, 1)
# second = datetime.date(2022, 2, 3)
# tdelta = second - first
# print(tdelta)

# from time import sleep
#
# def foo():
#     sleep(3)
#
#
# import datetime
#
# current_datetime = datetime.datetime.now()
# foo()
# new_datetime = datetime.datetime.now()
# print(new_datetime - current_datetime)
# print(f'Текущее время: {current_time}')
# result = current_time - datetime.time(hour=1)
# print(result)
#
# current_date = datetime.datetime.today()
# date = datetime.datetime.today() - datetime.timedelta(days=4)
# fdate = datetime.datetime.today() + datetime.timedelta(days=7)
# print(date, fdate)

# now = datetime.time(9, 30, 0)
# next_hour = datetime.time(10, 30, 0)
# print(now < next_hour)

# now = datetime.datetime.utcnow()
# print(now)
# import pytz
#
# tz_san_luis = pytz.timezone('America/Argentina/San_Luis')
# dt_san_luis = datetime.datetime.now(tz_san_luis)
# print(dt_san_luis)
# print(datetime.datetime.toordinal(datetime.datetime.today()))