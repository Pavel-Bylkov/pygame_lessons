# Решение задач

# Задача 1
# Написать программу, расчитывающую минимальное количество монет для размена.
# Используются монеты номиналом 10, 5, 2, 1 руб.

# coin_denomination = (10, 5, 2, 1)
# surrender = 69
#
# coins = 0
# for coin in coin_denomination:
#     coins += surrender // coin
#     surrender = surrender % coin
#
# print(f'Понадобится монет: {coins}')


# Задача 2
# Написать программу, которая расчитывает минимальное количество эльфов,
# которые покроют все города

# all_city = set(['Ма', 'СП', 'Ха', 'Ва', 'Хе', 'Вл', 'Ки', 'Ми', 'Ка', 'Но'])
#
# all_elfs = {}
# all_elfs['elf_one'] = set(['Ма', 'СП', 'Ми'])
# all_elfs['elf_two'] = set(['СП', 'Ха', 'Хе'])
# all_elfs['elf_three'] = set(['Ха', 'Ва'])
# all_elfs['elf_four'] = set(['Ки', 'Ми', 'Но'])
# all_elfs['elf_five'] = set(['Вл', 'Ка'])
# all_elfs['elf_six'] = set(['Ха', 'Вл', 'Ки', 'Ми', 'Ка'])
#
# final_set_elfs = set()
# while len(all_city) > 0:
#     best_elf = ''
#     largest_elf = set()
#     for name, cities in all_elfs.items():
#         current_area = all_city & cities
#         # print(current_area)
#         if len(current_area) > len(largest_elf):
#             best_elf = name
#             largest_elf = current_area
#     final_set_elfs.add(best_elf)
#     all_city -= largest_elf
#
# print(final_set_elfs)

# Задача 3

# Написать программу, находящую минимальное количество заправок автомобиля

# all_gas_station = [0, 200, 375, 500, 700, 855, 1000, 1200, 1300, 1555]
# all_gas_station = sorted(all_gas_station)
# next_station = 0
# current_station = 0
# stop_counter = 0
#
# while current_station < len(all_gas_station) -1:
#     if next_station + 1 > len(all_gas_station) - 1:
#         break
#     else:
#         if all_gas_station[next_station + 1] - all_gas_station[current_station] < 400:
#             next_station += 1
#         else:
#             stop_counter += 1
#             current_station = next_station
#             if all_gas_station[current_station + 1] - all_gas_station[current_station] > 400:
#                 print('До следующей остановки не добраться')
#                 break
#
# print(f'Минимальное количество останов: {stop_counter}')

# class Car:
#     speed = 100
#     color = 'black'
#
#     def say_beep(self):
#         self.x = 10
#         print(f'hello')

# print(dir(Car))
# Car.say_beep()
# print(Car.color)
# Car.speed = 70
# a = Car()
# Car.say_beep(a)
# a.say_beep()
# print(id(Car.speed))
# b = Car()
# b.speed = 10
# b.speed = 82
# print(Car.speed)
# print(id(a.speed))
# print(id(b.speed))
# print(a.speed)
# print(b.speed)

# a = Car()
# a.say_beep = lambda x :print(f'Я теперь {x}')
# a.say_beep(5)
# a.say_beep()
# print(id(Car.say_beep))
# print(id(a.say_beep))
# print(dir(Car))
# print(dir(a))
# print(Car.__dict__)
# print(a.__dict__)
# a.speed = 10
# print(a.__dict__)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# #
# #
# person1 = Person(age=15, name='Вася')
# print(person1.age)

# class Person:
#     def __init__(self,name,  *args, **kwargs):
#         self.args = args
#         self.kwargs = kwargs
#         print(f'{name}, {args}, {kwargs}')
#
# person1 = Person('Вася', *[1, 2, 3, 4, 5], **{'school': 100, 'age': 15})

# class PersonClass:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_name(self):
#         print(self.name)
#
#     def say_age(self):
#         print(self.age)
#
#
# person1 = PersonClass('Вася', 15)
# person1.say_name()
# person2 = PersonClass('Петя', 13)
# person2.say_name()
#
# person1.name = 'Коля'
# person2.name = 'Федя'
# person1.say_name()
# person2.say_name()
# person1.say_age()
# person2.say_age()

# class Test:
#     def __init__(self, name='Петр', age=15):
#         self.name = name
#         self.age = age
#
# a = Test(15)
# print(a.name)
# print(a.age)



# class Test:
#     name = 'Вася'
#     age = 15
#
#     def set_name(self, name):
#         self.name = name
# #
# #
# a = Test()
# # b = Test()
# print(getattr(Test, 'name'))
# print(getattr(a, 'name'))
# print(getattr(Test, 'surname', 'None'))
# print(getattr(a, 'surname'))
# print(a.surname)
# print(Test.name)
# setattr(Test, 'name', 'Петр')
# print(Test.name)
# # # print(a.name)
# setattr(a, 'surname', 'Сергей')
# a.set_name("Петя")
# print(a.name)
# # print(b.name)
# a.name = 10
# print(a.name)
# print(a.__dict__)
# print(getattr(a, 'name'))
# delattr(a, 'name')
# print(a.__dict__)
# print(getattr(a, 'name'))
# # print(getattr(a, 'name'))
# delattr(Test, 'name')
# print(getattr(a, 'name'))
# print(getattr(b, 'name'))


# Модуль os.path
# import os
# # print(os.path.abspath('..'))
# # print(os.path.dirname('./test/test1'))
# print(os.path.exists('test/test1'))
# # print(os.path.getatime('Lesson9.py'))
# # print(os.path.getmtime('Lesson9.py'))
# # print(os.path.getctime('Lesson9.py'))
# # print(os.path.getsize('Lesson9.py'))
# print(os.path.isfile('test'))
# print(os.path.isdir('test'))
# print(os.path.isabs('C://Windows'))

# print("ttt" * 8.6)
# class MyStr(str):
#     def __mul__(self, other):
#         if type(other) == type(float()):
#             return super().__mul__(int(other))
#         return super().__mul__(other)
#
# ttt = MyStr("ttt")
# ttt.dfgdg = 5
#
# # print(type(8.6) == type(float()))
# print(ttt * 8.6)
# print(ttt.dfgdg)
