N = int(input())
array = list(map(int, input().split()))

A = 0
B = 0

for i in range(len(array)):
    maxNum = max(array)
    if i % 2 == 0:
        A += maxNum
    else:
        B += maxNum
    array.remove(maxNum)

print(A-B)