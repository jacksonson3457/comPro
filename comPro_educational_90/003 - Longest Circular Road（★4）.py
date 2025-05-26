from collections import deque

def bfs(start):
    dist = [-1] * N
    dist[start] = 0
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        for next_node in G[now]:
            if dist[next_node] == -1:
                dist[next_node] = dist[now] + 1
                q.append(next_node)
    
    # 最も遠い点とその距離を返す
    max_dist = max(dist)
    farthest_node = dist.index(max_dist)
    return farthest_node, max_dist

N = int(input())

# 頂点数NのグラフGを定義
G = [[] for _ in range(N)]

for _ in range(N-1):
    #グラフ作成
    A, B = map(int, input().split())

    #頂点番号を0始まりにする
    A -= 1
    B -= 1

    #グラフに辺を追加
    G[A].append(B)
    G[B].append(A)

#2回BFSして直径を調べる
node_a, _ = bfs(0)
_, diameter = bfs(node_a)

#最後にスタート地点に橋をかけるので+1
print(diameter+1)

