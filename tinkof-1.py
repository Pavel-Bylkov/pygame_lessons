A, B, n = (int(x) for x in input().split())

# .... B ... X ... A
if B == A and n == 0:
    print("YES")
elif B > A or n == 0:
    print("NO")
else:
    X = (A - B) // 2 + B
    if X - B == A - X and (X - B) // n > 0:
        print("YES")
    else:
        print("NO")