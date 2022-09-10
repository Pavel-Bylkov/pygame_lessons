"""Перебрать с помощью итератора список целых чисел [1, 3, 4, 5, 8].
"""
def ex1():
    my_list = [1, 3, 4, 5, 8]
    # 1 способ
    print("1 способ")
    list_iter = iter(my_list)
    count = 0
    while count < len(my_list):
        print(next(list_iter))
        count += 1
    print()
    # 2 способ
    print("2 способ")
    list_iter = iter(my_list)
    while True:
        try:
            print(next(list_iter))
        except StopIteration:
            break
    list_iter = iter(my_list)
    for i in list_iter:
        print(i)
    print()
    # 3 способ
    print("3 способ")
    list_iter = iter(my_list)
    while True:
        elem = next(list_iter, "end")
        if elem != "end":
            print(elem)
        else:
            break

# ex1()

"""Создать класс итератора, обязательным атрибутом которого, 
является список слов и  реализовать методы __iter__ и __next__, 
для перебора данного списка"""

def ex2():
    class my_iter:
        def __init__(self, word_list):
            self.word_list = word_list
            self.i = 0

        def __iter__(self):
            self.i = 0
            return self

        def __next__(self, default=None):
            if default and self.i == len(self.word_list):
                return default
            if self.i == len(self.word_list):
                raise StopIteration
            self.i += 1
            return self.word_list[self.i - 1]

    a = my_iter(['word1', 'word2', 'word3'])

    iter_a = iter(a)
    print(next(iter_a))
    print(next(iter_a))
    print(next(iter_a))

    print("Перебор через цикл for")
    for word in a:
        print(word)

    for word in a:
        print(word)


ex2()