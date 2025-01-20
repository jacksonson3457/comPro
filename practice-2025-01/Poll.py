from collections import Counter

# 入力
N = int(input())
words = [input().strip() for _ in range(N)]

# カウント
counter = Counter(words)

# 最大値を取得
max_c = max(counter.values())

res = []
for key in counter:
    if counter[key] == max_c:
        res.append(key)

sorted_res = sorted(res)
for v in sorted_res:
    print(v)