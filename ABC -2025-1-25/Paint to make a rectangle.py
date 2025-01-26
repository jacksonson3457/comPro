H, W = map(int, input().split())

grid = [input() for i in range(H)]

def c():
    #まずは端を求める
    a = W
    b = 0
    c = H
    d = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                if j < a: a = j
                if b < j: b = j
                if i < c: c = i
                if d < i: d = i
    
    for i in range(c,d+1):
        for j in range(a,b+1):
            if grid[i][j] == '#' or grid[i][j] == '?':
                continue
            else:
                #白があったらもうダメよ
                return ('No')
    return 'Yes'

print(c())