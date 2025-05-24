N, M = map(int, input().split())

grid_N = [input() for _ in range(N)]
grid_M = [input() for _ in range(M)]

def isSame(i,j):
    for mi in range(M):
        for mj in range(M):
            if grid_N[i + mi][j + mj] != grid_M[mi][mj]:
                return False
    return True

def main():
    for i in range(N-M+1):
        for j in range(N-M+1):
            #1マス目が一致していたらそこからTなのかどうかを判定する
            if grid_N[i][j] == grid_M[0][0]:
                if isSame(i,j):
                    return f"{i+1} {j+1}"
                else:
                    continue
            
print(main())
