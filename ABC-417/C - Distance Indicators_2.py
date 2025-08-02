from collections import Counter

N = int(input())
A = list(map(int, input().split()))
# j - Aj配列を作っておく
V = [0] * (N+1)
for j in range(N):
    V[j] = j - A[j]
#それをさらにカウントしておく
V_counter = Counter(V)

count = 0

for i in range(N):
    a = i + A[i]
    count += V_counter[a]

print(count)