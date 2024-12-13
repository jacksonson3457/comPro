def canEat(maxValue, array):
    counter = 0
    current = 0
    for v in array:
        
        current += v
        counter += 1

        # 食べた後に制約を確認する
        if current > maxValue:
            break
    return counter

N, X, Y = map(int, input().split())
sweaty = sorted(map(int, input().split()), reverse=True)
salty = sorted(map(int, input().split()), reverse=True)
print(min(canEat(X, sweaty), canEat(Y, salty)))
