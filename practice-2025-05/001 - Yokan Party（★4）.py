N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

#チェック関数
#長さX以上のピースで、K+1個作れるか？
def isOK(X):
    prev = 0
    count = 0
    for pos in A:
        if pos - prev >= X:
            count += 1
            prev = pos
    if L - prev >= X:
        count += 1
    return count >= K + 1



#二分探索してlogNで範囲を検索していく
def binary_search():
    left, right = 1, L+1
    while right - left > 1:
        mid = (left + right) // 2
        if isOK(mid):
            left = mid
        else:
            right = mid
    return left

print(binary_search())

    