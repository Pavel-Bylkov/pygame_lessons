"""Создать программу, которая считывает от пользователя список
чисел и выводит эти числа через знак -

Пример: 1-2-3-4-5-6"""
def ex1():
    q = "Введите список чисел через пробел: "
    # nums = list(map(int, input(q).split()))
    # nums = [int(x) for x in input(q).split()]
    # print(*nums, sep="-")
    myNumList = input(q).split()
    result = '-'.join(myNumList)
    print(result)
# ex1()

"""Написать lambda функцию, которая принимает два числа и 
возвращает произведение этих чисел деленое на 2
"""
def ex2():
    foo = lambda x, y: x * y / 2
    print("2 * 3 / 2 =", foo(2, 3))

# ex2()


"""Наполнить два списка: один со строками, второй с числами. 
После этого создать из них и вывести список кортежей

Для выполнения данной задачи используйте zip() и input()"""
def ex3():
    q = "Введите список слов через пробел: "
    words = input(q).split()
    q = "Введите список чисел через пробел: "
    nums = list(map(int, input(q).split()))
    print(list(zip(words, nums)))
    print(dict(zip(words, nums)))

ex3()
