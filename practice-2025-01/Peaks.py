N, M = map(int, input().split())
H = list(map(int, input().split()))

G = [[] for _ in range(N)]

for M in range(M):
    u,v = map(int, input().split())
    u -= 1
    v -= 1

    G[u].append(v)
    G[v].append(u)

count = 0
for i in range(N):
    peak = G[i]
    h = H[i]
    if len(peak) == 0:
        count += 1
        continue

    x = 0
    for v in peak:
        if h <= H[v]:
            break
        x += 1
    if x == len(peak):
        count += 1

print(count)
