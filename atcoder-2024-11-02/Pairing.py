# 標準入力を処理し、必要な出力を行う
def count_even_divisions(numbers):
    hash_map = {}
    for num in numbers:
        if num in hash_map:
            hash_map[num] += 1
        else:
            hash_map[num] = 1

    count = 0
    for key in hash_map:
        # 2で割れる回数を数える
        while hash_map[key] > 1:
            hash_map[key] -= 2
            count += 1

    return count

# 入力を受け取る
numbers = list(map(int, input().split()))

# 結果を表示
print(count_even_divisions(numbers))
