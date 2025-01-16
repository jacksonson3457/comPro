A, B = map(int, input().split())

q = [1,2,4]
def check(P):
    if P == 0:
        return [False, False, False]
    if P == 1:
        return [True, False, False]
    if P == 2:
        return [False, True, False]
    if P == 4:
        return [False, False, True]
    if P == 3:
        return [True, True, True]
    if P == 6:
        return [False, True, True]
    if P == 5:
        return [True, False, True]
    if P == 7:
        return [True, True, True]

res_a = check(A)
res_b = check(B)

c = 0
for i in range(3):
    if res_a[i] or res_b[i]:
        c += q[i]

print(c)