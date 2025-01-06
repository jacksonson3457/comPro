X = int(input())
result = 0

for i in range(1,10):
    for j in range(1,10):
        if i * j == X:
            continue
        else:
            result += i * j

print(result)