N, L, R = map(int, input().split())
array = list(map(int, input().split()))

result = []
for a in array:
    if a < L:
        result.append(L)
    elif L <= a and a <= R:
        result.append(a)
    else:
        result.append(R)

print(' '.join(map(str, result)))