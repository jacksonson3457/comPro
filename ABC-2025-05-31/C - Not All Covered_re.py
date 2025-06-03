N, M = map(int, input().split())
cover = [0] * N 
diff = [0] * (N + 1)

for i in range(M):
    L, R = map(int, input().split())
    #まずは差分配列
    diff[L-1] += 1
    diff[R] -= 1

all_sum = 0
for j in range(N):
    all_sum += diff[j]
    cover[j] = all_sum

print(min(cover))

