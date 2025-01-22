from collections import Counter

N = int(input())
array = list(map(int, input().split()))
count = Counter(array)

V = N * (N-1) // 2
p = 0
for key in count:
    if count[key] > 1:
        p += count[key] * (count[key] - 1) // 2

res = V - p
print(res)