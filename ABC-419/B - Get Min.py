Q = int(input())
A = []

for _ in range(Q):
    B = list(map(int, input().split()))
    type = B[0]

    if type == 1:
        target = B[1]
        A.append(target)
    else:
        A.sort(reverse=True)
        res = A.pop()
        print(res)
        