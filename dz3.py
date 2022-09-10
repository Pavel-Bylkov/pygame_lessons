"""Добавить в игру пятнашки условие проверки (Мы можем переставлять
 соседние с пустой ячейки. Через одну и по диагонали переставлять не можем)"""
def ex1():
    import random
    import os
    import time
    import pyfiglet
    from progress.bar import IncrementalBar

    title = pyfiglet.figlet_format("TAG GAME")
    print(title)
    print('Добро пожаловать в игру пятнашки')
    print('Правила: соберите все костяшки в порядке возрастания')
    input('Нажмите Enter для начала игры...')
    mylist = [10, 22, 35, 44, 60, 69, 78, 100]
    bar = IncrementalBar('Загрузка: ', max=len(mylist))
    for _ in mylist:
        bar.next()
        time.sleep(random.uniform(0, 0.3))
    bar.finish()
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system("clear")  # Mac os
    else:
        print('Консоль не очищена')
    number_list = []  # [i for i in range(1, 16)]
    for i in range(1, 16):
        number_list.append(i)
    number_list.append(" ")
    result_list = list(zip(*[iter(number_list)] * 4))
    for i in range(len(result_list)):
        result_list[i] = list(result_list[i])
    random.shuffle(number_list)
    area = list(zip(*[iter(number_list)] * 4))
    for i in range(len(area)):
        area[i] = list(area[i])
    col_width = max(len(str(num)) for row in area for num in row) + 2
    while result_list != area:
        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system("clear")  # Mac os
        else:
            print('Консоль не очищена')
        for row in area:
            print(''.join(str(num).ljust(col_width) for num in row))
        quit_game = input("Завершить игру? (y/n) ")
        if quit_game.lower() == "y":
            break
        row1 = int(input('Введите строку, откуда вы хотите переместить элемент: ')) - 1
        column1 = int(input('Введите столбец, откуда вы хотите переместить элемент: ')) - 1
        row2 = int(input('Введите строку, куда вы хотите переместить элемент: ')) - 1
        column2 = int(input('Введите столбец, куда вы хотите переместить элемент: ')) - 1
        if (row1 < 0 or row1 > 3 or row2 < 0 or row2 > 3 or
                column1 < 0 or column1 > 3 or column2 < 0 or column2 > 3):
            print("Нумерация строк и столбцов от 1 до 4")
        elif not ((abs(row2-row1) == 0 and abs(column2-column1) == 1)
                or (abs(row2-row1) == 1 and abs(column2 - column1) == 0)):
            print("Перемещение возможно только из соседних ячеек в одном столбце или строке")
        elif area[row2][column2] == ' ':
            area[row1][column1], area[row2][column2] = area[row2][column2], area[row1][column1]
        else:
            print('Ячейка занята')
            # continue  # - бессмысленно
        time.sleep(2)
    else:
        print('Поздравляю! Вы победили')
    print(pyfiglet.figlet_format("THE END"))
# ex1()

"""Напишите программу, на вход которой в первой строке подаётся натуральное
 число n – количество городов, в последующих n строках вводятся различные 
 города. Программа должна выводить 'No', если введенный город уже указан."""
def ex2():
    n = int(input("Введите кол-во городов: "))
    cityList = set()
    print(f'Введите {n} разных городов ')
    for _ in range(n):
        cityName = input("Какой город добавить? ")
        if cityName.lower() in cityList:
            print('NO')
        else:
            cityList.add(cityName.lower())
    print(*cityList)
# ex2()

"""Создать два списка, наполненных числами. Найдите все числа, которые входят
 как в первый, так и во второй список и выведите их в порядке возрастания. 
 Для решения используйте множества. Постарайтесь решить задачу в одну строку"""
def ex3():
    a = [1, 45, 36, 4, 5, 6, 9, 43]
    b = [1, 67, 4, 78, 2, 5, 12, 3]
    print("Список 1 -", a)
    print("Список 2 -", b)
    print(*sorted(set(a).intersection(b)))
ex3()