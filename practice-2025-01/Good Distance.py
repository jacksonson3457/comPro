import math
N, D = map(int, input().split())

array = [list(map(int, input().split())) for i in range(N)]

res = 0
for i in range(N):
    for j in range(i+1,N):
        c = 0
        for k in range(D):
            a = array[i][k]
            b = array[j][k]
            c += (abs(b-a)) ** 2
        if round(math.sqrt(c)) == math.sqrt(c):
            res += 1

print(res)
            
