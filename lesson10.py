# class Person:
#     def __init__(self, name):
#         self.name = name
#
# person1 = Person('Иван')
# print(person1.name)
# person1.name = 'Петя'
# print(person1.name)
#
#
# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         print('Вернули значение атрибута')
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         print('Изменили значение атрибута')
#         self._name = value
#
#     @name.deleter
#     def name(self):
#         print('Удалили атрибут')
#         del self._name
#
# person1 = Person('Иван')
# # # print(person1.get_name())
# # # person1.set_name('Петя')
# # # print(person1.get_name())
# # # print(person1._name)
# # print(person1.name)
# # del person1._name
# print(person1.name)
# person1.name = 'Петя'
# print(person1.name)
# del person1.name
# print(person1.name)

class TextField:
    def __init__(self, text=""):
        self.counter = 0
        self.value = text

    def __get__(self, instance, owner):
        self.counter += 1
        print('__get__', self.counter)
        return self.value

    def __set__(self, instance, value):
        print('__set__')
        self.value = value

class Person:
    text = TextField("test")
    lastname = TextField()
    def __init__(self, name, lastname):
        self.name = TextField(name)
        self.lastname = lastname

person1 = Person("Вася", "Петров")
print(person1.name)
person1.text = "test2"
print(person1.text)
print(person1.lastname)
person1.lastname = 'Иван'
print(person1.lastname)
# print(person1.name)
# person2 = Person()
# print(person2.name)
#
# class Person:
#     def __init__(self, name='Иван'):
#         self.name = name
#         self.age = 10
#
#     def get_name(self):
#         return self.name
#
#     @staticmethod
#     def get_pow(x, y):
#         return x ** y
#
#     def foo(self):
#         self.age = Person.get_pow(self.age, 2)
# #
# # person1 = Person(name='Петя')
# # print(person1.name)
# # print(person1.get_pow(2, 3))
# print(Person.get_pow(2, 3))

# class Person:
#     __slots__ = ['name', 'age', 'lastname']
#     def __init__(self, name='Петя', age=15):
#         self.name = name
#         self.age = age
#
# person1 = Person()
# person1.foo = 40
# # person1.lastname = 'Иванов'
# # print(person1.lastname)
# # print(dir(Person))
# # print(dir(person1))
# person2 = Person()
# person2.name = 'Иван'
# print(person2.name)
# print(person2.age)
# person2.lastname = 'Иванов'
# print(person2.lastname)
#
# class Base:
#     def __init__(self, type, health):
#         self.type = type
#         self.health = health
#
#     def attack(self):
#         print('Метод атаки')
#         self.health -= 5
#
# class Wizard(Base):
#     def add_health(self):
#         self.health += 3
# #
# class Archer(Base):
#     def __init__(self, type, health, armor=10):
#         super().__init__(type, health)
#         self.armor = armor
#
#     def attack(self):
#         print('Метод атаки')
#         self.health -= self.armor - 5
#
#
# wizard = Wizard('Маг', 80)
# archer = Archer('Лучник', 100, 6)
# print('Лучник атакует')
# wizard.attack()
# print(f'Жизни мага {wizard.health}')
# wizard.add_health()
# print(f'Жизни мага {wizard.health}')
# print('Маг атакует')
# archer.attack()
# print(f'Жизни лучника {archer.health}')

# import calendar
#
# cal = calendar.month(2022, 1, 2, 1)
# print(cal)
# print(type(cal))

# cal = calendar.calendar(2020, 2, 1, 6, 3)
# print(cal)

# print(calendar.isleap(int(input('Введите год: '))))
# print(calendar.leapdays(2000, 2022))
# print(calendar.weekday(2022, 2, 24))
# print(calendar.weekheader(3))
# print(calendar.monthrange(2022, 12))
# print(calendar.monthcalendar(2022, 12))

# cal = calendar.TextCalendar()
# # print(cal.formatmonth(2022, 2))
# cal.prmonth(2022, 2)
# # print(type(cal))