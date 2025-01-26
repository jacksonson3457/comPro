R = int(input())

#まずはX,Y軸上
res = 4 * (R-1) + 1

p = 0
max_j = R-1
#X^2 + Y^2 <= R^2 であるX,Yは円内にある
#1*1の正方形が入るかどうかなので+0.5して正方形の角に寄せる
for i in range(1,R):
    # max_j から始めて条件を満たす j を探す
    while max_j > 0 and (i + 0.5) ** 2 + (max_j + 0.5) ** 2 > R ** 2:
            max_j -= 1  # 条件を満たさない場合 j を減少させる
    # 条件を満たす j の数を加算
    p += max_j

res += 4 * p
print(res)
