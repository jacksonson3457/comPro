A, B, C, X, Y = map(int, input().split())

res = float('INF')

max_need = max(X,Y)

for AB in range(max_need+1):
    need_a = X - AB
    need_b = Y - AB
    if need_a < 0: need_a = 0
    if need_b < 0: need_b = 0

    price = A * need_a + B * need_b + C * AB * 2
    res = min(res, price)

print(res)