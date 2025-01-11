N, X = map(int, input().split())
friends = list(map(int, input().split()))
result = [False] * (10 ** 5)
result[X-1] = True
i = friends[X-1]-1

while True:
    if result[i] == False:
        result[i] = True
        i = friends[i]-1
    else:
        res = sum(result)
        break

print(res)