import time

n = int(input("n="))

def dec_func(func):
    def wraper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Время выполнения - {(time.time() - start):.6f} сек")
        return result

    return wraper

@dec_func
def ex1(n):
    a = list(range(n+1))
    # a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1
    print(len(lst))

@dec_func
def ex2(n):
    if n < 2:
        print(0)
        return 0
    lst = [2]
    for i in range(3, n, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return len(lst)

@dec_func
def ex3(n):
    def is_prime(num):
        """Возвращает True если число простое"""
        if num < 2:
            return False
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for num in range(2, n+1):
        if (num > 10) and num % 10 in (2, 4, 5, 6, 8):
            continue
        if is_prime(num):
            count += 1

    print(count)

ex1(n)
print(ex2(n))
ex3(n)