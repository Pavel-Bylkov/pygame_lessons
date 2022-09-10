"""Создать генератор чисел от 1 до 250 и перебрать его через цикл.
"""
def ex1():
    def gen_nbr():
        count = 1
        while count <= 250:
            yield count
            count += 1

    for i in gen_nbr():
        print(i, end="\t")
        if i % 25 == 0:
            print()
    print()

    gen2 = (n for n in range(1, 251))
    for i in gen2:
        print(i, end="\t")
        if i % 25 == 0:
            print()
    print()

    gen3 = [n for n in range(1, 251)]
    for i in gen3:
        print(i, end="\t")
        if i % 25 == 0:
            print()
    print()

# ex1()

"""Создать генератор всех четных чисел от 1 до 200, все числа, 
которые кратны 5 разделить на 3.
"""
def ex2():
    def gen_nbr():
        count = 2
        while count <= 200:
            if count % 5 == 0:
                yield round(count / 3, 2)
            else:
                yield count
            count += 2

    for i in gen_nbr():
        print(i, end="\t")
        if i % 10 == 0:
            print()
    print()

    gen2 = (round(cnt / 3, 2) if cnt % 5 == 0 else cnt for cnt in range(2, 201, 2))
    for i in gen2:
        print(i, end="\t")
        if i % 10 == 0:
            print()
    print()

ex2()