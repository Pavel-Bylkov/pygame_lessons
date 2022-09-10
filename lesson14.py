# def gen_test(file):
#     for i in open(file):
#         yield i
#
# gen_test = (i for i in open('file.txt'))
# print(gen_test)

# a = range(5)
# print(type(a))
# a = list(a)
# print(a)

# def inf_seq():
#     num = 0
#     while True:
#         yield num
#         num += 1
#         if num == 5:
#             break
#
# t1 = []
# for i in inf_seq():
#     t1.append(i)
# print(t1)
#
# t1 = [i for i in inf_seq()]
# print(t1)
# #
# a = inf_seq()
# a.__iter__()
# a.__next__()
# print(type(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

#
# def gen_test():
#     for i in range(10):
#         if i % 2 == 0:
#             yield i
# #
# list1 = [x for x in gen_test()]
# print(list1)
# a = gen_test()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# def test():
#     str1 = 'hello'
#     yield str1
#
#     str2 = 'world'
#     yield str2
#     # test()

# a = test()
# print(next(a))
# print(next(a))
# print(next(a))

# a = [str(i ** 2) if i > 5 else 0 for i in range(1, 10) if i % 2 != 0]
# print(a)
# a = [letter for letter in input().upper().split()]
# print(a)

# print(len([char for char in input().split()]))
# import sys
# b = (int(input()) for _ in range(5))
# print(sys.getsizeof(b))
# for n in b:
#     print(n ** 2)
# a = [i ** 2 for i in range(1000000)]

# print(sys.getsizeof(a))



# a = [i for i in range(10)]
# b = (i for i in range(10))
#
# print(a)
# print(b)

# a = [1, -2, -3, 4, 5, -6]
# b = (i ** 2 if i < 0 else i * 2 for i in a if i % 2 == 0)
# for i in b:
#     print(i)

# a = [1, -2, -3, 4, 5, -6]
# b = [i ** 2 if i < 0 else i * 2 for i in a if i % 2 == 0]
# print(b)

# a = [i for i in input().split()]
# b = (i for i in a)
# while True:
#     if input('Далее? '):
#         print(next(b))