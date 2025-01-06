from collections import deque

H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

start = goal = None
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            start = (i, j)
        if grid[i][j] == 'G':
            goal = (i,j)

def bfs(start,goal):
    # 上下左右の移動ベクトル
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([start])
    visited = [[False] * W for _ in range(H)]
    visited[start[0]][start[1]] = True
    distance = [[-1] * W for _ in range(H)]
    distance[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            return distance[x][y]
        #現在地から移動する
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            #隣が枠外か障害物の場合はそれ以上調べない
            if 0 <= nx < H and 0 <= ny < W and not grid[nx][ny] == '#':
                if visited[nx][ny] == True: continue
                #そうでない場合は新しくqueueに追加して、distance,visitedを更新する
                distance[nx][ny] = distance[x][y] + 1
                visited[nx][ny] = True
                queue.append((nx,ny))
    return -1

result = bfs(start,goal)
print(result)
#縦移動と横移動を交互にしないといけない