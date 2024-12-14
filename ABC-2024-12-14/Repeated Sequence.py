N, S = map(int, input().split())
A = list(map(int, input().split()))

for i in N:
    if i == 0 or  i ==N-1:
        if S % A[i] == 0 or S % A[i]*2 == 0:
            print('Yes')

    count = 0
    for j in range(i+1, N+1):
        count += A[j]
        if S % count == 0:
            print('Yes')

print('No')

