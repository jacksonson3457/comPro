N = int(input())
Array = list(map(int, input().split()))
count = 0
isEnd = False

while isEnd == False:
    for i in range(N):
        if Array[i] % 2 != 0:
            isEnd = True
            break
        else:
            Array[i] //= 2
            if i == N-1:
                count += 1

print(count)