n, m = (int(x) for x in input().split())

count = 0
while n != 0 and m != 0:
    n, m = min(n, m), max(n, m)
    count += (m // n)
    m %= n
print(count)