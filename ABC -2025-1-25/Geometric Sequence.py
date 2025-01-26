def is_geometric_sequence(array):
    N = len(array)
    
    # 初項と2項から公比を求める
    first = array[0]
    second = array[1]
    ratio = second // first  # 整数の商を計算
    
    # 等比数列の判定
    for i in range(1, N):
        # 前項が公比と一致するかを確認
        if array[i] * first != array[i - 1] * second:
            return "No"
    return "Yes"

# 入力部分
N = int(input())
array = list(map(int, input().split()))
print(is_geometric_sequence(array))