H, W = map(int, input().split())

grid = [list(input()) for _ in range(H)]

def compress(grid):
    new_grid = [row[:] for row in grid]
    #横のチェック
    for i in range(H-1,-1,-1):
        c = 0
        for j in range(W):
            if grid[i][j] != '.':
                c += 1
        if c == 0:
            del new_grid[i]
    new_h = len(new_grid)
    new_w = len(new_grid[0])
    #縦
    for j in range(new_w-1,-1,-1):
        c = 0
        for i in range(new_h):
            if new_grid[i][j] != '.':
                c += 1
        if c == 0:
            for i in range(new_h-1,-1,-1):
                del new_grid[i][j]
    
    return new_grid

res = compress(grid)

for row in res:
    res1 = ''.join(row)
    print(res1)