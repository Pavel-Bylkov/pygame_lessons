# result = {'a': 1, 'b': 2}
# result['c'] = 3
# result['a'] = 4
# result['b'] = result['a'] + 1
# print(result)
# print(result['b'])
# a = {1, 2, 3, 4}
# a = {'a': 1, 'b': 2}
# print('a' in a)
# a = ' pencil'
# print(' pen' in a)

# constants = {'pi': 3.14, 'e': 2.71, 'root 2': 1.41}
# # for k in constants:
# #     print(f'Значение, ассоциированное с ключом {k}: {constants[k]}')
# total = 0
# for k, v in constants.items():
#     total += v
#     print(f'Значение, ассоциированное с ключом {k}: {v}')
# print(f'Сумма значений составляет {total}')

# counts = {}
# while len(counts) < 5:
#     s = input('Введите строку: ')
#     if s in counts:
#         counts[s] = counts[s] + 1
#     else:
#         counts[s] = 1
#
# for k in counts:
#     print(f'{k} появилось в словаре {counts[k]} раз')

# Задача: Код Цезаря

# message = input('Введите сообщение: ')
# shift = int(input('Введите сдвиг: '))
# new_message = ''
# for ch in message:
#     if ch >= 'a' and ch <= 'z':
#         pos = ord(ch) - ord('a')
#         pos = (pos + shift) % 26
#         new_char = chr(pos + ord('a'))
#         new_message += new_char
#     elif ch >= 'A' and ch <= 'Z':
#         pos = ord(ch) - ord('A')
#         pos = (pos + shift) % 26
#         new_char = chr(pos + ord('A'))
#         new_message += new_char
#     else:
#         new_message += ch
#
# print(f'Новое сообщение {new_message}')

# print(ord('b'))
# print(chr(98))


# Задача 2: Отрицательные, положительные и нули

# negatives = []
# zeros = []
# positives = []
# line = input('Введите целое цисло (Enter для окончания ввода): ')
# while line != '':
#     num = int(line)
#     if num < 0:
#         negatives.append(num)
#     elif num > 0:
#         positives.append(num)
#     else:
#         zeros.append(num)
#     line = input('Введите целое цисло (Enter для окончания ввода): ')
#
# print('Введенные числа: ')
# for n in negatives:
#     print(n, end=' ')
# for n in zeros:
#     print(n, end=' ')
# for n in positives:
#     print(n, end=' ')
# print(*negatives, sep=", ")

# Задача 3: Случайные лотерейные билеты

# from random import randrange
#
# MIN_NUM = 1
# MAX_NUM = 49
# NUM_NUMS = 6
#
# ticket_nums = []
# for i in range(NUM_NUMS):
#     rand = randrange(MIN_NUM, MAX_NUM + 1)
#     while rand in ticket_nums:
#         rand = randrange(MIN_NUM, MAX_NUM + 1)
#     ticket_nums.append(rand)
# ticket_nums.sort()
# print('Номера билетов ', end=' ')
# for n in ticket_nums:
#     print(n, end=' ')
# print()

# Задача 4: Эрудит

# points = {"A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, \
#          "J": 2, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, \
#          "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10}
# word = input('Введите слово: ')
# uppercase = word.upper()
# score = 0
# for ch in uppercase:
#     score += points[ch]
# print(f'{word} оценивается в {score} очков')

# Функции

# def Say():
#     print('Hello')
#
# Say()
# def area_sq():
#     side = 5
#     area = side * side
#     print(area)
#
# area_sq()
# print(area + 1)
# side_sq = int(input())
# def area_sq(side):
#     area = side * side
#     print(area)
#
#
# print(area_sq(10))
#
# def area_sq(number):
#     result = number ** 2
#     return result
#
# result = area_sq(5)
# print(result)
# print(area_sq())
# import random
#
# def lottery(tickets):
#     ticket1 = random.choice(tickets)
#     tickets.remove(ticket1)
#     ticket2 = random.choice(tickets)
#     return ticket1, ticket2
#
# a, b = lottery([1, 11, 22, 34, 56, 18, 7])
# print(a, b)

# def factorial(num):
#     result = 1
#     for i in range(1, num + 1):
#         result *= i
#     return result

# print(factorial(5))
# area = 0
# def area_sq():
#     global area
#     side = 5
#     area = side * side
#
# print(f'До функции {area}')
# area_sq()
# print(f'После функции {area}')
# number = 0
# def test():
#     global number
#     number = 5
#     number2 = 1
#     def test2():
#         nonlocal number2
#         number = 3
#         number2 = 5
#     print(f'{number2=}')
#     test2()
#     print(f'{number2=}')
#
# print(number)
# test()
# test3 = test
# print(number)
# number = 3
# test3()
# print(number)
# inp()

# area = []
# count = 1
# for i in range(3):
#     area.append([])
#     for j in range(3):
#         area[i].append(count)
#         count += 1
# for i in area:
#     print(i)

# for i in range(3):
#     for j in range(3):
#         for l in range(3):
#             print(i, j, l)

# def season(n):
#     if 1 <= n <= 2 or n == 12:
#         return 'Зима'
#
# print(season(12))
#
# def isPrime(n):
#     for i in range(2, n // 2):
#         if n % i == 0:
#             return False
#     return True
#
# print(isPrime(71))