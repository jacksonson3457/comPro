N = int(input())
sum_a = [0] * (N+1)
sum_b = [0] * (N+1)


for i in range(N):
    C, P = map(int, input().split())
    sum_a[i+1] = sum_a[i]
    sum_b[i+1] = sum_b[i]

    if C == 1:
        sum_a[i+1] += P
    else:
        sum_b[i+1] += P

Q = int(input())
for _ in range(Q):
    L, R = map(int, input().split())
    a = sum_a[R] - sum_a[L-1]
    b = sum_b[R] - sum_b[L-1]
    print(f"{a} {b}")
    

