from collections import Counter

N = int(input())
words = list(map(int, input().split()))

# カウント
counter = Counter(words)
res = 0
for key in counter:
    if key == counter[key]: continue
    if counter[key] < key: res += counter[key]
    else: res += counter[key] - key

print(res)
