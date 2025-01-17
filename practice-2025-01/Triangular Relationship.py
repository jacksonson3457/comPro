N, K = map(int, input().split())

list = []

for i in range(3 * N + 1):
    if i % K == 0:
        list.append(i)


