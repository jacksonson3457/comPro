N, M = map(int, input().split())

# 超点数NのグラフGを定義
G = [[] for i in range(N)]

for i in range(M):
    u,v = map(int, input().split())

    #頂点番号を0始まりにする
    u -= 1
    v -= 1

    #グラフに辺を追加
    G[u].append(v)
    G[v].append(u)

for i in range(N):
    print(len(G[i]))