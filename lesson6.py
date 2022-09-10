# i = 0
# while i < 10:
#     print(f'{i} меньше 10')
#     i += 1
# else:
#     print('Условие не верно')

# def season(n):
#     if 1 <= n <= 2 or n == 12:
#         return 'Зима'
#     elif 3 <= n <= 5:
#         return 'Весна'
#     elif 6 <= n <= 8:
#         return 'Лето'
#     elif 9 <= 11:
#         return 'Осень'
# print(season(2))

# x = 14
# if x % 4 == 0:
#     print(x // 4)
# else:
#     print(x // 4 + 1)
# print(-5 // 2)
# print(-(-x // 4))

# print([int(x) for x in input().split()])
# print(round(-4 / 3))
# a = 5
# print(type(a))

# PROCENT = 10
#
# money = int(input('Введите сумму: '))
# year = int(input('На сколько лет: '))
#
#
# for i in range(year):
#     money += money / 100 * PROCENT
# print(money)

# a = ' hello   '
# print("|" + a.strip() + "|")

# a = ['a', 'b', 'c', 'd']
# for i, letter in enumerate(a, 1):
#     print(i, letter)

# numbers = [1, 2, 3, 4, 5]
# names = ['Вася', 'Петя', 'Коля', 'Миша']
# print(list(zip(numbers, names)))
# print(dict(zip(numbers, names)))
# zip_obj = zip(names)
# print(list(zip_obj))
# for name, number in zip(names, numbers):
#     print(f'{name=} {number=}')
# zip_v = list(zip(numbers, names))
# number, name = zip(*zip_v)
# print(list(name))
# print(number)

# a = {i ** 2: i**3 for i in range(1, 11) if i % 2 == 0}
# print(a)
# b = ['1', '2', '3', '4']
# a = [int(i) for i in input().split() if i not in b]
# print(a)

# SECONDS_PER_DAY = 86400
# SECOND_PER_HOUR = 3600
# SECOND_PER_MINUTE = 60
#
# seconds = int(input('Введите кол-во секунд: '))
# days = seconds / SECONDS_PER_DAY
# seconds = seconds % SECONDS_PER_DAY
# hours = seconds / SECOND_PER_HOUR
# seconds = seconds % SECOND_PER_HOUR
# minutes = seconds / SECOND_PER_MINUTE
# seconds = seconds % SECOND_PER_MINUTE
# # printf("text %0d %f", 60, 5.6)
# print('Длительность ', "%d:%02d:%02d:%02d" % (days, hours, minutes, seconds))
# print(f'Длительность дней {days}, часов {hours}, минут {minutes}, секунд {seconds}')

# if name := 'Вася':
#     print('hello ' + name)
# import random
#
# x = random.randint(1, 10)
# print(x)

# a = random.randrange(1, 10, 2)
# print(a)

# a = [1, 2, 3, 4, 5, 6 ]
# random.shuffle(a)
# print(a)
# a = [1, 2, 3, 4, 5, 6 ]
# print(random.choice(a))
# a = [1, 2, 3, 4, 5, 6 ]
# print(random.sample(a, 3))
# print(random.random())
# print(random.uniform(1, 10))

# import tkinter as tk
#
# window = tk.Tk()
#
# window.title('Крестики нолики')
# window.geometry('300x300')
# window.resizable(False, False)
# area = []
# turn = 1
# def push(button):
#     global turn
#     if turn % 2 == 0:
#         turn_char = '0'
#     else:
#         turn_char = 'x'
#     button['text'] = turn_char
#     turn += 1
#
# for x in range(3):
#     area.append([])
#     for y in range(3):
#         button = tk.Button(window, text='', width=13, height=6)
#         area[x].append(button)
#         area[x][y].place(x=x*100, y=y*100)
#         # area[x][y]['command'] = push(button)
#         area[x][y]['command'] = lambda selected_button=button:push(selected_button)
#
# window.mainloop()
# def foo1(x):
#     return x * x
#
# foo = lambda x="lambda": print(x)
# print(foo())
# print(foo1(4))
# cities = ['Москва', 'Санкт-Петербург', 'Воронеж']
# result = lambda cities: ', '.join(cities) + '.'
# print(result(cities))
# print(', '.join(cities) + '.')
# def round_num(num):
#     return 5 * round(num / 5)
#
# print(round_num(41.7))

# list1, list2 = [7, 17, 1, 9, 1, 17, 56, 56, 23], [56, 17, 17, 1, 23, 34, 1, 8, 1]
# def repeat_list(list1, list2):
#     result = []
#     for i in list1:
#         if list1.count(i) > 1 and list2.count(i) > 1:
#             result.append(i)
#     return sorted(list(set(result)))
#
# print(repeat_list(list1, list2))

# IN_PER_FT = 12
# CM_PER_IN = 2.54
#
# feet = int(input('Количество футов: '))
# inches = int(input('Количество дюймов: '))
# cm = (feet * IN_PER_FT + inches) * CM_PER_IN
#
# print(f'Ваш рост в сантиметрах {cm}')

## Библиотека дня
# ### Random
# Модуль random предоставляет функции для генерации случайных чисел,
# букв, случайного выбора элементов последовательности.

# **random.randint(a, b)
# ** -возвращает случайное целое число от aдо b
# ex = random.randint(1, 10)
# print(x)

# **random.randrange(a, b, step)
# ** -возвращает случайно выбранное число из последовательности
# от a до b(step(шаг) -необязательный)
# a = random.randrange(1, 10, 2)
# print(a)

# **random.shuffle(a)
# ** -перемешивает список
# a = [1, 2, 3, 4, 5, 6 ]
# random.shuffle(a)
# print(a)

# **random.choice(a)
# ** -выбирает случайный элемент из списка
# a = [1, 2, 3, 4, 5, 6 ]
# print(random.choice(a))

# **random.sample(a, k)
# ** -создает список длиной k из последовательности a
# a = [1, 2, 3, 4, 5, 6 ]
# print(random.sample(a, 3))

# **random.random()
# ** -возвращает случайное дробное число от 0 до 1
# print(random.random())

# **random.uniform(a, b)
# ** -возвращает случайное дробное число от a до b
# print(random.uniform(1, 10))
