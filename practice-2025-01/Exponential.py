X = int(input())

half_x = X // 2

candidate = [1]

for i in range(half_x):
    for j in range(2,11):
        if i ** j <= X:
            candidate.append(i ** j)

res = max(candidate)
print(res)