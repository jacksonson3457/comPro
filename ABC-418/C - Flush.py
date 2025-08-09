N, Q = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

# 先にカードの枚数を累積和
pref = [0]
for x in A:
    pref.append(pref[-1] + x)

maxA = A[-1]

def binary_search(arr, t):
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] <= t:
            l = m + 1
        else:
            r = m
    return l

def c(B):
    #1以下なら1で要求で勝ち
    if B <= 1:
        return 1
    #BがmaxAよりでかいなら勝てない
    if B > maxA:
        return -1
    t = B - 1
    idx = binary_search(A, t)
    # sum(min(Ai, t)) = sum(A[:idx]) + (N-idx) * t
    s = pref[idx] + (N - idx) * t
    return s + 1

for _ in range(Q):
    B = int(input())
    print(c(B))
