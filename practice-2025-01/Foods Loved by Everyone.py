N, M = map(int, input().split())

backet = {}

for _ in range(N):
    values = list(map(int, input().split()))
    K = values[0]
    for k in range(1,1 + K):
        food = values[k]
        if food in backet:
            backet[food] += 1
        else:
            backet[food] = 1

res = sum(backet[key] == N for key in backet)
print(res)