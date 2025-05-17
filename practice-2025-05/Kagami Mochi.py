N = int(input())
array = []

for i in range(N):
    num = int(input())
    if num in array:
        continue
    else:
        array.append(num)

print(len(array))