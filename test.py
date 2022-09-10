list1 = [1, 2, 3, 4, 5, 6]
prod = 1
summ = 0
for i in list1:
    if i % 2 == 0:
        summ += i
    else:
        prod *= i
print(summ, prod)
