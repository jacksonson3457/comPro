A, B = map(int, input().split())
count = 1
X = 1

while X < B:
    X += A - 1
    count += 1
print(count)
