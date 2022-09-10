n, m = (int(x) for x in input().split())

def move_horse(x, y, n, m):
    if x == n and y == m:
        return 1
    if x > n or y > m:
        return 0
    return move_horse(x+1, y+2, n, m) + move_horse(x+2, y+1, n, m)

print(move_horse(1, 1, n, m))