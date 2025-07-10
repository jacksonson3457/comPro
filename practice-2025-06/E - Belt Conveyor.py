#gridの受け取り
H, W = map(int, input().split())
grid = [input() for _ in range(H)]
visited = [[False] * W for _ in range(H)]

def u(i,j):
    if i == 0:
        return -1
    return i-1,j

def d(i,j):
    if i == H-1:
        return -1
    return i+1,j

def l(i,j):
    if j == 0:
        return -1
    return i,j-1

def r(i,j):
    if j == W-1:
        return -1
    return i,j+1

def doWhile():
    pos_i, pos_j = 0, 0 
    visited[pos_i][pos_j] = True
    while True:
        conduct = grid[pos_i][pos_j]
        #上
        if conduct == 'U':
            res = u(pos_i,pos_j)
            if res == -1:
                return pos_i, pos_j
            pos_i += res[0]
            pos_j += res[1]
            if visited[pos_i][pos_j]:
                return -1
            visited[pos_i][pos_j] = True
        #下
        if conduct == 'D':
            res = d(pos_i,pos_j)
            if res == -1:
                return pos_i, pos_j
            pos_i += res[0]
            pos_j += res[1]
            if visited[pos_i][pos_j]:
                return -1
            visited[pos_i][pos_j] = True
        #左
        if conduct == 'L':
            res = l(pos_i,pos_j)
            if res == -1:
                return pos_i, pos_j
            pos_i += res[0]
            pos_j += res[1]
            if visited[pos_i][pos_j]:
                return -1
            visited[pos_i][pos_j] = True
        #右
        if conduct == 'R':
            res = r(pos_i,pos_j)
            if res == -1:
                return pos_i, pos_j
            pos_i += res[0]
            pos_j += res[1]
            if visited[pos_i][pos_j]:
                return -1
            visited[pos_i][pos_j] = True

print(doWhile())