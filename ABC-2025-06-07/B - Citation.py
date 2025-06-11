N = int(input())
A = list(map(int, input().split()))

res = 0
for i in range(1,N+1):
    count = 0
    for j in range(N):
        if A[j] >= i:
            count += 1
    if i <= count:
        res = i

print(res)


