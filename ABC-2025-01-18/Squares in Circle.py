def count_contained_squares(R):
    count = 0
    # グリッド上を走査
    for x in range(-R, R):
        for y in range(-R, R):
            # 各正方形の4つの頂点を確認
            if (
                (x**2 + y**2 <= R**2) and
                ((x+1)**2 + y**2 <= R**2) and
                (x**2 + (y+1)**2 <= R**2) and
                ((x+1)**2 + (y+1)**2 <= R**2)
            ):
                count += 1
    return count

# 半径 R の入力
R = int(input("半径 R を入力してください: "))
print(f"円に完全に内包される正方形の数: {count_contained_squares(R)}")
