N, M = map(int, input().split())

# 整数列を受け取る場合
numlist = list(map(int, input().split()))
cashe = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j: cashe[i][j] = numlist[i]%M
        else: 
            cashe[i][j] = (numlist[i] + numlist[j]) % M

