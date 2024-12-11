A, B = map(int, input().split())  # A=4, B=10
count = 0
X = 1

while X < B:
    X += A - 1  # A-1だけ増加
    count += 1
print(count)
