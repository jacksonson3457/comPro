N, L = map(int, input().split())
D = list(map(int, input().split()))

L = [0] * (L+1)
L[0] = 1
sum_now = 0
for i in range(N-1):
    sum_now += D[i]
    L[sum_now%L] += 1

count = 0
plus = L // 3
for j in range(L+1):
    if L[j] > 0 and L[(j+plus) % L] > 0 and L[(j+plus * 2) % L] > 0:
        #正三角形になる点の組み合わせを求める
        count += L[j] * L[(j+plus) % L] * L[(j+plus * 2) % L]

print(count)

