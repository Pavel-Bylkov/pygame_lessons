"""Создать класс танка.
Продумать все необходимые аттрибуты и методы.
После этого создать несколько экземпляров класса с разными характеристиками
"""
from time import sleep
from math import cos, sin, radians

tanks = []
PAUSE = 3
# кешируем вычисления для ускорения
cache_sin = {}
cache_cos = {}

class Tank:
    def __init__(self, name, armor, power, range, speed, lives, x, y, angle, map_index):
        super().__init__()
        self.name = name            # Имя танка
        self.armor = armor          # броня
        self.power = power          # мощность снарядов
        self.range = range          # дальность стрельбы
        self.speed = speed          # скорость движения
        self.lives = lives          # живучесть
        self.x = x                  # координата Х
        self.y = y                  # координата У
        self.direction = angle      # угол - направление
        self.cache_cos = {}
        self.cache_sin = {}
        self.map_index = map_index
        self.print_info()

    def print_info(self):
        print(f"{self.name} готов к бою!")
        print(f"Характеристики:")
        print(f" - Текущие координаты ({self.x}, {self.y}), направление {self.direction}")
        print(f" - Броня {self.armor}")
        print(f" - Живучесть {self.lives}")
        print(f" - Дальность стрельбы {self.range}")
        print(f" - Максимальный урон {self.power}")
        print(f" - Скорость {self.speed}")
        print()

    def getHit(self, x, y, power):
        if self.x == x and self.y == y:
            damage = power
            if self.armor > 0:
                damage -= self.armor
                self.armor -= power // 10
                if self.armor < 0:
                    self.armor = 0
                if damage < 0:
                    damage = 0
            self.lives -= damage
            if self.lives <= 0:
                self.lives = 0
                print(f"{self.name} подбит!")
                tanks.remove(self)
            else:
                print(f"Докладывает {self.name} попадание!")
                self.state_info()
        else:
            print(f"Докладывает {self.name} атака прошла мимо!")
        print()

    def state_info(self):
        print(f"Состояние: ")
        print(f" - Текущие координаты ({self.x}, {self.y}), направление {self.direction}")
        print(f" - Броня {self.armor}")
        print(f" - Живучесть {self.lives}")

    def rotate(self, angle):
        if self.direction + angle > 180:
            self.direction = (self.direction + angle) % 180 - 180
        elif self.direction + angle < -179:
            self.direction = self.direction + angle + 360
        else:
            self.direction += angle

    def move_forward(self):
        print(f"Докладывает {self.name} полный вперед!")
        self.x += self.get_delta_x()
        self.y += self.get_delta_y()
        self.state_info()
        print()

    def move_back(self):
        print(f"Докладывает {self.name} полный назад!")
        self.x -= self.get_delta_x()
        self.y -= self.get_delta_y()
        self.state_info()
        print()

    def get_delta_x(self):
        # кешируем вычисления для ускорения
        if self.direction not in cache_cos:
            cache_cos[self.direction] = cos(radians(self.direction))
        if self.direction not in self.cache_cos:
            self.cache_cos[self.direction] = int(self.speed * cache_cos[self.direction])
        return self.cache_cos[self.direction]

    def get_delta_y(self):
        # кешируем вычисления для ускорения
        if self.direction not in cache_sin:
            cache_sin[self.direction] = sin(radians(self.direction))
        if self.direction not in self.cache_sin:
            self.cache_sin[self.direction] = -int(self.speed * cache_sin[self.direction])
        return self.cache_sin[self.direction]

    def attack(self):
        if self.direction not in cache_cos:
            cache_cos[self.direction] = cos(radians(self.direction))
        if self.direction not in cache_sin:
            cache_sin[self.direction] = sin(radians(self.direction))
        pos_kill = (self.x + int(self.range * cache_cos[self.direction]),
                    self.y - int(self.range * cache_sin[self.direction]))
        print(f"Атакует {self.name} цель {pos_kill} потенциальный урон {self.power}")
        print()
        return pos_kill[0], pos_kill[1], self.power


arg_tank1 = {
    "name": "Tank 1",
    "armor": 20,
    "power": 50,
    "range": 10,
    "speed": 2,
    "lives": 100,
    "x": -7, "y": -8,
    "angle": 0,
    "map_index": "1"
}

arg_tank2 = {
    "name": "Tank 2",
    "armor": 30,
    "power": 40,
    "range": 10,
    "speed": 2,
    "lives": 100,
    "x": 6, "y": 7,
    "angle": 180,
    "map_index": "2"
}

#             Y                               -90
#             |                                ^
#    (-5, 5)  |   (5, 5)                       |
#             |                                |
# X ----------+----------     180 <------ направление ------> 0
#             |                                |
#    (-5, -5) |   (5, -5)                      |
#             |                                v
#                                              90

tank1 = Tank(**arg_tank1)
tank2 = Tank(**arg_tank2)
sleep(PAUSE)

tanks.append(tank1)
tanks.append(tank2)

def ex1_with_map():
    import os

    def screen_clear():
        if os.name == 'nt':
            os.system('cls')  # Windows
        elif os.name == 'posix':
            os.system("clear")  # Mac os

    def get_map():
        battle_map = [list(" " * 41) for i in range(21)]
        # Название осей
        battle_map[0][20] = "Y"
        battle_map[10][0] = "X"
        # Ось Х
        for i in range(2, 41):
            battle_map[10][i] = "-"
        # Ось Y
        for i in range(1, 21):
            battle_map[i][20] = "|"
        battle_map[10][20] = "+"
        return battle_map

    def print_map(x=None, y=None):
        battle_map = get_map()
        for i in range(len(tanks)):
            # Pos Tank
            if -20 < tanks[i].x < 20 and -10 < tanks[i].y < 10:
                ty = -tanks[i].y
                battle_map[ty + 10][tanks[i].x + 20] = tanks[i].map_index
        # Attack
        if x is not None and y is not None and -20 < x < 20 and -10 < y < 10:
            y = -y
            battle_map[y + 10][x + 20] = "*"
        for row in battle_map:
            print(*row, sep=" ")

    sleep(PAUSE)
    screen_clear()
    print_map()
    sleep(PAUSE)
    screen_clear()
    tank2.rotate(-45)
    tank2.move_forward()
    sleep(PAUSE)
    screen_clear()
    print_map()
    sleep(PAUSE)
    screen_clear()
    tank1.rotate(-45)
    tank1.move_forward()
    sleep(PAUSE)
    screen_clear()
    print_map()
    sleep(PAUSE)
    x, y, power = tank1.attack()
    sleep(PAUSE)
    screen_clear()
    print_map(x, y)
    sleep(PAUSE)
    screen_clear()
    tank2.getHit(x, y, power)
    sleep(PAUSE)
    screen_clear()
    print_map()
    sleep(PAUSE)
    screen_clear()
    tank1.move_forward()
    tank2.move_forward()
    sleep(PAUSE)
    screen_clear()
    print_map()
    sleep(PAUSE)
    screen_clear()
    tank1.move_forward()
    tank2.move_forward()
    sleep(PAUSE)
    screen_clear()
    print_map()
    sleep(PAUSE)
    x, y, power = tank2.attack()
    sleep(PAUSE)
    screen_clear()
    print_map(x, y)
    sleep(PAUSE)
    tank1.getHit(x, y, power)
    sleep(PAUSE)
    screen_clear()
    tank1.rotate(-45)
    tank1.move_forward()
    sleep(PAUSE)
    screen_clear()
    print_map()
    sleep(PAUSE)
    x, y, power = tank2.attack()
    sleep(PAUSE)
    screen_clear()
    print_map(x, y)
    sleep(PAUSE)
    tank1.getHit(x, y, power)
    sleep(PAUSE)
    screen_clear()
    tank1.rotate(45)
    sleep(PAUSE)
    screen_clear()
    print_map()
    sleep(PAUSE)
    x, y, power = tank2.attack()
    sleep(PAUSE)
    screen_clear()
    print_map(x, y)
    sleep(PAUSE)
    tank1.getHit(x, y, power)
    sleep(PAUSE)
    x, y, power = tank1.attack()
    sleep(PAUSE)
    screen_clear()
    print_map(x, y)
    sleep(PAUSE)
    tank2.getHit(x, y, power)
    sleep(PAUSE)
    screen_clear()
    print_map()
    sleep(PAUSE)
    x, y, power = tank2.attack()
    sleep(PAUSE)
    screen_clear()
    print_map(x, y)
    sleep(PAUSE)
    tank1.getHit(x, y, power)
    sleep(PAUSE)
    x, y, power = tank1.attack()
    sleep(PAUSE)
    screen_clear()
    print_map(x, y)
    sleep(PAUSE)
    tank2.getHit(x, y, power)
    sleep(PAUSE)
    screen_clear()
    print_map()
    sleep(PAUSE)
    x, y, power = tank2.attack()
    sleep(PAUSE)
    screen_clear()
    print_map(x, y)
    sleep(PAUSE)
    tank1.getHit(x, y, power)
    sleep(PAUSE)
    screen_clear()
    print_map()

def ex1():
    sleep(PAUSE)
    tank2.rotate(-45)
    tank2.move_forward()
    sleep(PAUSE)
    tank1.rotate(-45)
    tank1.move_forward()
    sleep(PAUSE)
    x, y, power = tank1.attack()
    sleep(PAUSE)
    tank2.getHit(x, y, power)
    sleep(PAUSE)
    tank1.move_forward()
    sleep(PAUSE)
    tank2.move_forward()
    sleep(PAUSE)
    tank1.move_forward()
    sleep(PAUSE)
    tank2.move_forward()
    sleep(PAUSE)
    x, y, power = tank2.attack()
    sleep(PAUSE)
    tank1.getHit(x, y, power)
    sleep(PAUSE)
    tank1.rotate(-45)
    tank1.move_forward()
    sleep(PAUSE)
    x, y, power = tank2.attack()
    sleep(PAUSE)
    tank1.getHit(x, y, power)
    sleep(PAUSE)
    tank1.rotate(45)
    sleep(PAUSE)
    x, y, power = tank2.attack()
    sleep(PAUSE)
    tank1.getHit(x, y, power)
    sleep(PAUSE)
    x, y, power = tank1.attack()
    sleep(PAUSE)
    tank2.getHit(x, y, power)
    sleep(PAUSE)
    x, y, power = tank2.attack()
    sleep(PAUSE)
    tank1.getHit(x, y, power)
    sleep(PAUSE)
    x, y, power = tank1.attack()
    sleep(PAUSE)
    tank2.getHit(x, y, power)
    sleep(PAUSE)
    x, y, power = tank2.attack()
    sleep(PAUSE)
    tank1.getHit(x, y, power)
    sleep(PAUSE)

# ex1()
ex1_with_map()