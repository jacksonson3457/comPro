from itertools import permutations

def minimumDishes(N, X, Y, sweaty, salty):
    #甘さとしょっぱさをひとまとまりにする
    dishes = list(zip(sweaty, salty))
    minCount = N

    for order in permutations(dishes):
        sweetness, saltyness = 0, 0
        count = 0
        for a, b in order:
            sweetness += a
            saltyness += b
            count += 1

            if sweetness > X or saltyness > Y:
                break
        minCount = min(minCount, count)
    
    return minCount


    
    


N, X, Y = map(int, input().split())
sweaty = sorted(map(int, input().split()), reverse=True)
salty = sorted(map(int, input().split()), reverse=True)
print(minimumDishes(N, X, Y, sweaty, salty))
