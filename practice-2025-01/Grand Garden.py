def check():
    N = int(input())
    array = list(map(int, input().split()))
    i = 0
    res = 0
    while i < N:
        if sum(array) == 0: return res
        if array[i] == 0:
            i += 1
            continue

        j = i
        while j < N and array[j] != 0:
            j += 1
        for p in range(i,j):
            array[p] -= 1
        #水やり
        res += 1
        
    
print(check())

