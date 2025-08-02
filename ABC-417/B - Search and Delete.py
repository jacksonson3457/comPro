N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(M):
    b = B[i]
    if b in A:
        A.remove(b)

print(" ".join(map(str, A)))