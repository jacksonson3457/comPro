N, M = map(int, input().split())

condition = [list(map(int,input().split())) for _ in range(M)]

def check(str_i, condition):
    for s, c in condition:
        if str_i[s-1] != str(c):
            return False
    return True

res = -1
for i in range(10 ** N):
    str_i = str(i)
    if len(str_i) != N: continue
    if check(str_i, condition):
        res = int(str_i)
        break

print(res)

    