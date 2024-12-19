from itertools import permutations

def remake(input_shape: list, H: int, W: int) -> list:
    """
    入力図形を列単位のリストに再編成する
    """
    remake_list = [[''] * H for _ in range(W)]  # W列×H行の二次元リストを初期化
    for i in range(H):
        for j in range(W):
            remake_list[j][i] = input_shape[i][j]  # 行列を転置するように変換
    return remake_list

def match(input_shape: list, target_shape: list) -> bool:
    """
    並べ方を試し、ターゲット図形と一致するか確認する
    """
    for perm in permutations(input_shape):  # 列の順列を試す
        if list(perm) == target_shape:  # 順列をリストに変換して比較
            return True
    return False

# 入力部分
H, W = map(int, input().split())
input_shape = [input().strip() for _ in range(H)]  # 入力図形
target_shape = [input().strip() for _ in range(H)]  # ターゲット図形

# 再編成と一致確認
if match(remake(input_shape, H, W), remake(target_shape, H, W)):
    print('Yes')
else:
    print('No')
