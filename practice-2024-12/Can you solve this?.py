N, M, C = map(int, input().split())
B = list(map(int, input().split()))
result = 0

for i in range(N):
    score = 0
    A = list(map(int, input().split()))
    for j in range(M):
        score += A[j] * B[j]
    if score + C > 0:
        result += 1

print(result)

