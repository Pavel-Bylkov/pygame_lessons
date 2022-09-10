from collections import Counter
n = int(input())
A = Counter([int(x) for x in input().split()])

def direct_order(x0):
    result = [x0]
    for a in A.keys():
        for _ in range(A[a]):
            result.append(result[-1] ** 2 - a)
            if result[-1] < 0:
                return False
    return True

def reverse_order(x0):
    result = [x0]
    for a in list(A.keys())[::-1]:
        for _ in range(A[a]):
            result.append(result[-1] ** 2 - a)
            if result[-1] < 0:
                return False
    return True


x0 = 0
while True:
    x0 += 1
    if direct_order(x0) or reverse_order(x0):
        break
print(x0)

"""
Пете дали мультимножество A размера n, содержащее натуральные число. 
Теперь Петя хочет по этому мультимножеству сгенерировать последовательность 
x_{0}, x_{1}, x_{n}x .

Правило для генерации x_{i} следующее: Сначала Петя выбирает положительное x_{0}. 
Затем Петя должен взять все элементы A ровно по одному разу (заметьте, Петин 
порядок может отличаться от изначального порядка элементов в А). 
Назовем текущий элемент множества A как a. Если до этого Петя взял k элементов
 A, то x_{k+1}=x_{k}^{2}-a.

Петя расстроится, если какой-то элемент последовательности x_{i} станет меньше нуля. 
Найдите минимальный подходящий x_{0}, который может выбрать Петя, чтобы у него 
была возможность сконструировать последовательность и не расстроиться.

Например, если x_{0}=3x 
0
​
 =3﻿, и ﻿A=\{3,4\}A={3,4}﻿, то можно сгенерировать такую последовательность:

﻿a=4, x_{1}=9-4=5a=4,x 
1
​
 =9−4=5﻿
﻿a=3, x_{2}=25-3=22a=3,x 
2
​
 =25−3=22﻿
Итоговая последовательность ﻿33﻿, ﻿55﻿, ﻿2222﻿ не расстроит Петю. При этом ﻿ x_0 = 2x 
0
​
 =2﻿ уже не подойдет (можно самостоятельно проверить, почему), значит, число ﻿33﻿ является ответом.

Формат входных данных

В первой строке дается целое число ﻿n\left(1 \leqslant n \leqslant 10^{5}\right)n(1⩽n⩽10 
5
 )﻿ В следующей строке через пробел вводится ﻿nn﻿ целых чисел ﻿a_{1}, \ldots, a_{i}, \ldots, a_{n}a 
1
​
 ,…,a 
i
​
 ,…,a 
n
​
 ﻿ ﻿\left(1 \leqslant a_i \leqslant 10^{18}\right)(1⩽a 
i
​
 ⩽10 
18
 )﻿﻿-−﻿ мультимножество ﻿AA﻿.

Обратите внимание, что для ввода чисел вам понадобится 64-битный тип данных.

Формат выходных данных

Выведите одно число ﻿-−﻿ такой минимальный ﻿x_0x 
0
​
 ﻿, с которым Петя сможет проделать все необходимые операции и не расстроиться.

Примеры данных
Пример 1
2
3 4

3

Пример 2
5
1 1 1 1 1

2

Пример 3
3
2 1 100

3

"""