N = int(input())
array = list(map(int, input().split()))

res = 0
i = 0
while i < N:
    j = i+1
    count = 0
    while j < N and array[i] >= array[j]:
        i = j
        j += 1
        count += 1
    res = max(res, count)
    i = j
print(res)