N, M = map(int, input().split())
B = [list(map(int, input().split())) for i in range(N)]

#1列ずつ見ていって全部+7だったらいいよ
def c():
    for i in range(1,M):
        if B[0][i] != B[0][i-1] + 1:
            return 'No'
        
    for i in range(M):
        for j in range(1,N):
            if B[j][i] != B[j-1][i] + 7:
                return 'No'
    return ('Yes')

print(c())