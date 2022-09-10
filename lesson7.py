# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(5))

# def factorial(5):
#     if 5 == 1:
#         return 5
#     else:
#         return 5 * factorial(5 - 1)

# def factorial(4):
#     if 4 == 1:
#         return 4
#     else:
#         return 4 * factorial(4 - 1)

# ...

# def factorial(1):
#     if 1 == 1:
#         return 1
#     else:
#         return 1 * factorial(1 - 1)

# n = int(input())
# def fib(n):
#     if n == 2:
#         return 1
#     if n == 1:
#         return 0
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# print(fib(n))


# FILE_NAME = 'text.txt'
# with open(FILE_NAME, 'w') as file:
#     print('hello')
# import os.path
# import sys
#
# FILE_NAME = 'schedule.txt'
#
#
# def read_file():
#     with open(FILE_NAME, 'r') as file:
#         schedule = file.read()
#     if schedule:
#         return eval(schedule)
#     else:
#         return {}
#
#
# def write_file(data):
#     with open(FILE_NAME, 'w') as file:
#         file.write(str(data))
#
#
# def print_schedule(data):
#     for day, deals in data.items():
#         print(day)
#         for hour, deal in deals.items():
#             print(hour, deal, sep=' - ')
#         print()
#
# def add_update(data):
#     day = input('Введите день: ')
#     hour = input('Введите время в формате ч:мм: ')
#     deal = input('Введите дело: ')
#     if day in data:
#         data[day].update({hour: deal})
#     else:
#         data[day] = {hour: deal}
#     write_file(data)
#     # return data
#
# # def edit_int(number):
# #     number = 1
# #
# # num = 5
# # edit_int(num)
# # print(num)
#
# def main():
#     if not os.path.isfile(FILE_NAME):
#         file = open(FILE_NAME, 'w')
#         file.close()
#     schedule = read_file()
#     run = True
#     while run:
#         choice = input('1-Вывести расписание.\n2-Изменить расписание\n0 - Выход\n')
#         if choice == '1':
#             print_schedule(schedule)
#         elif choice == '2':
#             add_update(schedule)
#         elif choice == '0':
#             print('Завершение программы...')
#             run = False
#             # sys.exit()
#         else:
#             print('Данного пункта нет')
#
#
# if __name__ == '__main__':
#     main()

# eval(выражение, globals=,locals=)

# x = 1
#
# print(eval('x==1'))
# print(eval('x+1'))
# print(eval('x==2'))
# a = "['a', 1, 'b', 2]"
# print(type(a))
# a = eval(a)
# print(type(a))


import os


# print(os.path.exists("base.txt"))

# print(os.name)

# print(os.environ)

# print(os.getlogin())

# print(os.getpid())

# print(os.uname())

# print(os.access('text.txt', os.F_OK))
# print(os.access('text.txt', os.R_OK))
# print(os.access('text.txt', os.W_OK))
# print(os.access('text.txt', os.X_OK))

# os.chdir('../')

# os.chmod()

# print(os.getcwd())

# print(os.listdir())

# os.makedirs('test/test1')
# os.mkdir('text')
# os.remove('text.txt')

# os.rmdir('text')

# print(os.system("cls"))