N = int(input())
array = [0]
two = []
for i in range(N):
    a = int(input())
    array.append(a)

def c():
    #2のボタンから遡っていく
    cur = array[1]
    for i in range(1, 10 ** 5 + 1):
        if N < i: return -1
        if cur == 2:
            return i
        else:
            cur = array[cur]
    return -1

print(c())
