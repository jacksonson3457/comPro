X, Y = map(int, input().split())

count = 0

for i in range(1,7):
    for j in range(1,7):
        if i + j >= X or abs(i-j) >= Y:
            count += 1
v = count / 36
if v == 0.0:
    v = 0

print(v)