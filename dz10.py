"""Реализовать класс Child, имеющего атрибуты имя, фамилия,
класс в котором он учится. При создании класса вы можете
использовать getter, setter или же dunder методы get, set.
"""

class TextField:
    def __init__(self, text=""):
        self._value = text

    def __get__(self, instance, owner):
        print("get")
        return self._value

    def __set__(self, instance, value):
        print("set")
        self._value = value


class Child:
    name = TextField()
    surname = TextField()
    class_name = TextField()

    def __init__(self, name, surname, class_name):
        self.name = name
        self.surname = surname
        self.class_name = class_name


# child = Child('Иван', 'Иванов', '8Б')
# child2 = Child('Сергей', 'Петров', '8Б')
# print(child.name)
# print(child2.name)
# child.name = "Петя"
# print(child.name)
# print(child2.name)

"""Создать базовый класс и два дочерних класса с типами персонажа. 
Классы должны иметь атрибуты имя, кол-во жизней, броня. 
Реализовать метод атаки, в котором персонажи атакуют друг друга 
пока жизни какого то из них, не будут равны или меньше нуля. 
"""

class Base:
    def __init__(self, type, name, health, damage, armor=5):
        self.type = type
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def attack(self, other):
        print(f"{self.type} {self.name} атакует {other.type} на {self.damage}")
        damage = self.damage - other.armor
        if damage < 0:
            damage = 0
        other.health -= damage
        if other.health <= 0:
            print(f"{other.type} {other.name} погиб!")
        else:
            print(f"{other.type} {other.name} ранен, осталось {other.health} здоровья!")


class Human(Base):
    def __init__(self, name, health, damage):
        super().__init__("Human", name, health, damage)


class Wizard(Base):
    def __init__(self, name, health, damage):
        super().__init__("Wizard", name, health, damage)


wizard = Wizard('Ludvig', 15, 4)
human = Human('Arnold', 20, 12)
human.attack(wizard)
wizard.attack(human)
wizard.attack(human)
human.attack(wizard)
human.attack(wizard)

