# class Person:
#     numbers = 0
#
#     def __init__(self, name='Вася'):
#         self.name = name
#         Person.numbers += 1
#         # self.numbers += 1
#
#     @classmethod
#     def clear_numbers(cls):
#         cls.numbers = 0
#
#
# a = Person()
# b = Person()
# c = Person()
#
# print(Person.numbers)
# print(a.numbers)
# print(b.numbers)
# print(c.numbers)
# Person.clear_numbers()
# print(Person.numbers)
# print(a.numbers)
# print(b.numbers)
# print(c.numbers)

# class Person:
#     def __init__(self, name='name'):
#         self._name = name
#
# a = Person()
# print(a.__dict__)
# a._name = 'Вася'
# print(a.__dict__)
# print(a._name)

# class Person:
#     def __init__(self, name='name'):
#         self.__name = name
#
# a = Person()
# # print(a.__name)
# print(a.__dict__)
#
# print(a._Person__name)

from functools import singledispatch

# class Person:
#     @singledispatch
#     def get_value(value):
#         print(f'По умолчанию {value}')
# #
#     @get_value.register(int)
#     def _(value):
#         print(f'int: {value}')
#
#     @get_value.register(str)
#     def _(value):
#         print(f'str: {value}')
#
#     @get_value.register(tuple)
#     def _(value):
#         print(f'tuple: {value}')

#     def get_value(self, value):
#         if type(value) == type(int()):
#             self._1(value)
#         elif type(value) == type(str()):
#             self._2(value)
#         elif type(value) == type(tuple()):
#             self._3(value)
#         else:
#             print(f'По умолчанию {value}')
#
#     def _1(self, value):
#         print(f'int: {value}')
#
#     def _2(self, value):
#         print(f'str: {value}')
#
#     def _3(self, value):
#         print(f'tuple: {value}')
# #
# a = Person()
# a.get_value(5)
# a.get_value('hello')
# a.get_value([1, 2, 3, 4])
# a.get_value((1, 2, 3, 4))

# class Test:
#     def __getattr__(self, attr):
#         print('Вызван несуществующий атрибут')
#
# a = Test()
# print(a)
# a.b

# class Base:
#     def __init__(self, *args):
#         for name, value in zip(self._fields, args):
#             setattr(self, name, value)
#
# class Test(Base):
#     _fields = ['name', 'test', 'value']
#
# a = Test(1, 2, 3)
# print(a.__dict__)
# print(a.name)
# a.name = 'Вася'
# print(a.name)

#     def __init__(self, value) -> None:
#         self.value = value
#
#     def __len__(self):
#         return self.value.count("l") #len(self.value)
#
# a = Base('hello')
# print(len(a))

# class Test:
#     def __init__(self, value) -> None:
#         self.value = value
#
#     def __len__(self):
#         return 12
#
# a = Test('hello')
# print(len(a))


# class Test:
#     def __init__(self, value):
#         self.value = value
#
#     def __len__(self):
#         return 5 ** 2
#
# a = Test('hello')
# print(len(a))


# class TestDict(dict):
#     def __setitem__(self, key, value):
#         print('__setitem__')
#         return super().__setitem__(key, [value] * 2)
#
#     def __getitem__(self, key):
#         print('__getitem__')
#         return super().__getitem__(key)

# a = TestDict(one=1, two=2)
# print(f'TestDict {a}')
# a['two'] = 3
# print(f'TestDict {a}')
# print(a['one'])

class Base:
    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor

    def attack(self, other):
        other.health -= self.power
        if other.health <= 0:
            other.health = 0

class Tank(Base):
    def attack(self, other):
        print(f"Tank {self.name} attack {other.name}")
        super().attack(other)
        print(f"{other.name} health is {other.health}")

class Soldat(Base):
    def attack(self, other):
        print(f"Soldat {self.name} attack {other.name}")
        super().attack(other)
        print(f"{other.name} health is {other.health}")

t = [Tank("T1", 100, 50, 20),
    Tank("T2", 900, 60, 30),
     Soldat("S1", 10, 10, 5)]

for i in range(len(t)):
    for j in range(len(t)):
        if i != j:
            t[i].attack(t[j])
