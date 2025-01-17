N = int(input())
A = list(map(int, input().split()))
l = []
for i in range(N-1):
    p = A[i] * A[i+1]
    l.append(p)

print(" ".join(map(str, l)))