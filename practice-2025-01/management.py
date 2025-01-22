N = int(input())
array = list(map(int, input().split()))

subordinates = [0] * N

for i in range(N-1):
    v = array[i] -1
    subordinates[v] += 1

for i in range(N):
    print(subordinates[i])