"""Это мой модуль"""
print("Import module", __name__)
def sqrt(a):
    '''Расчитывает квадратный корень'''
    print("my_sqrt")
    return a ** 0.5

def summa(a, b):
    return a + b

def sum_list(list):
    return sum(list)

def str(a):
    return 'hello'
#
number = 5
if __name__ == '__main__':
    print(__name__)
    print('Я основная программа')