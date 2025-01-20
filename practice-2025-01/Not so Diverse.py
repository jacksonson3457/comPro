from collections import Counter, deque

# 入力を取得
N, K = map(int, input().split())
array = list(map(int, input().split()))

# 配列の要素をカウント
counter = Counter(array)
diverse = len(counter)

# カウントされた要素を出現回数でソートし、dequeに変換
sorted_counter = deque(sorted(counter.values()))

res = 0  # 削除した要素の数

# diverseがK以下になるまで処理
while diverse > K:
    min_d = sorted_counter.popleft()  # 先頭要素を削除（O(1)）
    res += min_d
    diverse -= 1

print(res)
