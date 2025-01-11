N, M = map(int, input().split())

stores = list()
for _ in range(N):
    A, B = map(int, input().split())
    stores.append((A, B))

#この構造のままAの昇順に配列をソートする
sorted_stores = sorted(stores, key=lambda x: x[0])

count = M
res = 0
# pop(0) を使わず、単純なループで処理
for A, B in sorted_stores:
    if count <= 0:
        break
    if count - B < 0:
        res += A * count
        count = 0
    else:
        res += A * B
        count -= B

print(res)