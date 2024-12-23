N, M = map(int, input().split())

#N個の頂点とM個の辺を受け取ってグラフを作成する

G = [[] for i in range(N)]

#頂点に辺を入れる
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

#編の数がN-1かどうか調べる
if M == N - 1:
    check1 = True
else:
    check1 = False

#全ての頂点からの繋がりが2以下かどうかを調べる
check2 = True
for i in range(N):
    if len(G[i]) > 2:
        check2 = False
        break

#幅優先探索をして全てが繋がっているかどうかを調べる
from collections import deque
reach = [False] * N
d = deque()

reach[0] = True
d.append(0)

while d:
    current = d.popleft()
    for v in G[current]:
        if not reach[v]:
            reach[v] = True
            d.append(v)

if sum(reach) == N:
    check3 = True
else:
    check3 = False

if check1 and check2 and check3:
    print('Yes')
else:
    print('No')