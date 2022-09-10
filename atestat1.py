"""Реализовать функцию, принимающую на вход список целых чисел и
возвращающую произведение всех чисел последовательности """

def ex1(nums):
    prod = 1
    for num in nums:
        prod *= num
    return prod

# print(ex1([1, 2, 3, 4, 5]))


"""Реализовать программу, которая принимает на вход числа a, b. 
Результатом работы должно быть среднее значение всех чисел 
от a до b включительно, которые делятся на 3"""

def ex2():
    a, b = int(input()), int(input())
    if a > b:
        a, b = b, a
    count = 0
    summ = 0
    for i in range(a, b + 1):
        if i % 3 == 0:
            summ += i
            count += 1
    if count:
        print("среднее -", summ / count)
    else:
        print("чисел кратных 3 в диапазоне нет")

ex2()


"""Реализовать класс, который наследуется от класса списка и 
переопределяет метод append. Вместо добавления элемента в список, 
требуется возводить в степень все элементы списка на 
переданное в append значение"""

def ex3():
    class MyList(list):
        def append(self, num):
            if isinstance(num, int):
                for i in range(self.__len__()):
                    self[i] **= num

    test = MyList((1, 2, 3, 4, 5))
    print(test)
    test.append(2)
    print(test)

# ex3()