N = int(input())
A = list(map(int, input().split()))

data = {}

for i in range(2*N):
    p = A[i]
    if p not in data:
        data[p] = [i]
    else:
        data[p].append(i)

res = 0
for v in data:
    a,b = data[v]
    if abs(a-b) == 2:
        res += 1

print(res)
