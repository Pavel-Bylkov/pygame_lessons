"""Дана строка, состоящая из слов, разделенных пробелами.
Написать программу, находящую количество слов.
Решение должно быть в одну строку."""
def ex1():
    string = "    строка    состоящая  из   слов   разделенных пробелами  "
    print(f"\"{string}\" - состоит из {len(string.split())} слов")
# ex1()

"""Создайте словарь из строки 'programmer' следующим образом:
 в качестве ключей возьмите буквы строки, а значениями пусть 
 будут числа, соответствующие количеству вхождений данной буквы в строку."""
def ex2():
    string = 'programmer'
    result = {}
    for s in string:
        result[s] = string.count(s)
    print(result)

def ex2_2():
    word = "programmer"
    a = {keys: word.count(keys) for keys in word}
    print(a)
# ex2()
# ex2_2()
"""Написать программу, которая находит сумму всех простых чисел от 10 до 250."""
def ex3():
    def is_prime(num):
        """Возвращает True если число простое"""
        if num < 2:
            return False
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True

    result = 0
    num = 1
    i = 0
    print("Простые числа от 10 до 250:")
    while num < 250:
        if is_prime(num):
            result += num
            print(num, end="\t")
            i += 1
            if i % 10 == 0:
                print()
        num += 1

    print("\nСумма:", result)
ex3()