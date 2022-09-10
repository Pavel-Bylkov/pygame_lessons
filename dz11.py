"""Реализовать родительский класс Person, который в качестве
аргументов принимает имя, возраст и имеет методы вывода
этих значений, а также реализовать дочерний класс Student,
который наследуется от Person и имеет собственные аргументы
школа и класс. Также реализовать методы по выводу этих
значений и создать экземпляр класса
"""

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def print_name(self):
        print(f'имя: {self._name}')

    def print_age(self):
        print(f'возраст: {self._age}')


class Student(Person):
    def __init__(self, name, age, school, class_name):
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self._school = school
        self._class_name = class_name

    def print_school(self):
        print(f'школа: {self._school}')

    def print_class_name(self):
        print(f'класс: {self._class_name}')

# person = Person('Петя', 14)
#
# person.print_name()
# person.print_age()
#
# student = Student('Иван', 15, 10, '8Б')
# student.print_name()
# student.print_age()
# student.print_school()
# student.print_class_name()
# person.print_school()


"""Реализовать класс, наследуемый от класса list и переопределить
метод append, реализовав в нем не добавление элементов,
как по умолчанию, а удаление последнего элемента"""

class My_list(list):
     def append(self):
         # super().append()
         self.pop()

#
# b = My_list((1, 2, 5, 67, 23))
# print(b)
# b.append()
# print(b)