"""Напишите программу на Python, чтобы проверить,
существует ли данный ключ в словаре."""
def ex1():
    import time
    my_dict = {x: k for k, x in enumerate(list("abcdefghk"), 1)}
    print(my_dict)
    key = input("введите ключ: ")

    if my_dict.get(key) is None:
        print(f"{key} нет в словаре")
    else:
        q = my_dict[key]
        print(f"{key} есть в словаре")

    STEPS = 10_000_000

    count = 0
    start = time.time()
    for _ in range(STEPS):
        if my_dict.get(key) is None:
            count -= 1
        else:
            q = my_dict[key]
            count += 1
    print("if my_dict.get(key) is None", time.time() - start, "sec")

    count = 0
    start = time.time()
    for _ in range(STEPS):
        if key in my_dict:
            q = my_dict[key]
            count += 1
        else:
            count -= 1
    print("if key in my_dict", time.time() - start, "sec")

    count = 0
    start = time.time()
    for _ in range(STEPS):
        try:
            q = my_dict[key]
            count += 1
        except KeyError:
            count -= 1
    print("try", time.time() - start, "sec")

# ex1()

"""Напишите программу на Python для суммирования
 всех элементов в словаре.

"""

def ex2():
    my_dict = {'a': 13, 'b': 3, 'c': 7, 'd': 8}
    print(f"словарь {my_dict}")
    numbers_sum = 0
    for i in my_dict:
        numbers_sum += my_dict[i]
    print(f"сумма всех значений словаря = {numbers_sum}")
    print(F'сумма всех значений словаря = {sum(my_dict.values())}')

# ex2()

"""Напишите программу на Python, чтобы проверить, 
пустой список или нет."""

def ex3():
    my_list = [1, 9, 87, 4, 35]
    print(my_list)

    if len(my_list):
        print("список не пустой")
    else:
        print("список пустой")

    if my_list:
        print("список не пустой")
    else:
        print("список пустой")

ex3()