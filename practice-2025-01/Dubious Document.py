from collections import Counter

n = int(input())
words = [input().strip() for _ in range(n)]
nums = [Counter(s) for s in words]

res = []
for char in range(26):
    c =chr(char + ord('a'))
    min_count = min(counter.get(c, 0) for counter in nums)
    res.append(c * min_count)

print("".join(res))