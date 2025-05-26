N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

def isOK(X):
    #長さX以上のピースをK+1個作れるか？
    prev = 0
    count = 0
    for a in A:
        if a - prev >= X:
            prev = a
            count += 1
    if L - prev >= X:
        count += 1
    
    return count >= K+1

#二分探索
left, right = 0, L

while right - left > 1:
    mid = (left + right) // 2
    if isOK(mid):
        #この大きさでは切り分けられるのでもう少し大きく切り分けるほうがいい
        left = mid
    else:
        #この大きさでは切り分けられないのでもう少し小さく切り分けるほうが良い
        right = mid

print(left)