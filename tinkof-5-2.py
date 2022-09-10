n = int(input())  # высота горы
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]


def route_up(i, count=0):
    if i <= 0:
        return count
    for jump in range(a[i - 1], 0, -1):
        if i - jump + b[i - jump - 1] < i:
            i -= jump
            if i > 0:
                i += b[i - 1]
            result = route_up(i, count+1)
            if result >= 0:
                return result
    return -1

print(route_up(n))