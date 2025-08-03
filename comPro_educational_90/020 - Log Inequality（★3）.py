A,B,C = map(int, input().split())

def gcd2(x, y):
    while y:
        x, y = y, x % y
    return x

def gcd3(x, y, z):
    return gcd2(gcd2(x, y), z)

r = gcd3(A, B, C)
res1 = (A // r - 1)
res2 = (B // r - 1)
res3 = (C // r - 1)

print(res1 + res2 + res3)



