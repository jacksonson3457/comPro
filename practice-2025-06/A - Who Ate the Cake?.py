A, B = map(int, input().split())
candidate = [1,2,3]

res = -1

if A != B:
    candidate.remove(A)
    candidate.remove(B)
    res = candidate[0]

print(res)