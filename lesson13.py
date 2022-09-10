# a = [1, 2, 3, 4, 5]
# for elem in a:
#     print(elem)
# a_iter = a.__iter__()
# print(a_iter)
# print(type(a_iter))
# print(a_iter.__next__())
# print(a_iter.__next__())
# print(a_iter.__next__())
# print(a_iter.__next__())
# print(a_iter.__next__())
# print(next(a_iter, "stop"))

# str1 = 'Python'
# # str1_iter = str1.__iter__()
# # print(type(str1_iter))
# str1_iter = iter(str1)
# # print(type(str1_iter))
# print(next(str1_iter))
# print(next(str1_iter))
# print(next(str1_iter))

# iter_str = iter('Python')
# while True:
#     # try:
#     #     i = next(iter_str)
#     #     print(i)
#     # except StopIteration:
#     #     break
#     i = next(iter_str, "stop")
#     if i != "stop":
#         print(i)

#
# class StrIter:
#     def __init__(self, value):
#         self.value = value
#         self.i = 0
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         if self.i < len(self.value):
#             char = self.value[self.i]
#             self.i += 1
#             return char
#         else:
#             raise StopIteration
#
# #
# #
# #
# a = StrIter('Python')
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(next(a))
# print(a.__next__())
# print(a.__next__())
# try:
#     print(a.__next__())
# except StopIteration:
#     print('Элементов больше нет')
#
# for s in a:
#     print(s)

# class Test:
#     def __init__(self, number=0):
#         self.number = number
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n <= self.number:
#             result = self.n ** 2
#             self.n += 1
#             return result
#         else:
#             raise StopIteration
# #
# a = Test(10)
# i = iter(a)
#
# while True:
#     result = next(a, "stop")
#     if result != "stop":
#         print(result)
#     else:
#         break
#
# a = iter(int, 1)
# while True:
#     print(next(a))
list_person = ['Иван', 'Сергей', 'Федор', 'Василий', 'Михаил']
person_iter = iter(list_person)
print(next(person_iter))
while True:
    try:
        if input('Переключить. y/n ').lower() == 'y':
            print(next(person_iter))
            try:
                num = int(input("введите число"))
            except ValueError:
                print("ошибка")
            chars = input("введите число")
            checker = set(chars).intersection(list("abcdef"))
            if not checker:
                num = int(chars)
            else:
                print("ошибка")
        else:
            break
    except StopIteration:
        print('Сотрудников больше нет')
        break
# import copy
# class Test:
#     def __init__(self, n = 0):
#         self.num = n
#
#     def __iter__(self):
#         self.num = 0
#         return copy.copy(self)
#
#     def __next__(self):
#         if self.num < 100:
#             num = self.num
#             self.num += 1
#             return num
#         else:
#             raise StopIteration
# #
# obj = Test()
# print(next(obj))
# print(next(obj))
# print(next(obj))
#
# for i in obj:
#     for j in obj:
#         print(i + j)

class Test:
    def __init__(self, name='Иван'):
        self.name = name

    def __call__(self, *args, **kwargs):
        return f'Ваше имя {self.name} {args=} {kwargs=}'

    def info(self, *args, **kwargs):
        return f'Ваше имя {self.name} {args=} {kwargs=}'

def foo(func, *args, **kwargs):
    print(func(*args, **kwargs))

a = Test()
print(a(1, 2, 3, 4, [3, 3, 3], par1=33, par2=44))
foo(a, 1, 2, 3, 4, [3, 3, 3], par1=33, par2=44)
print(a.info(1, 2, 3, 4, [3, 3, 3], par1=33, par2=44))
foo(a.info, 1, 2, 3, 4, [3, 3, 3], par1=33, par2=44)