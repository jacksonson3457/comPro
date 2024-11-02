def returnNextCollectDay(d, q, r):
    if d % q == r:
        return d
    
    remainder = d % q
    if r - remainder > 0:
        return d + r - remainder
    else:
        return d + (q - (remainder - r))

typeList = []
N = int(input()) 
for i in range(N):
    # 整数を受け取る場合
    q, r = map(int, input().split())
    typeList.append(
        {"q": q,
         "r": r}
    )

Q = int(input())
for j in range(Q):
    t, d= map(int, input().split())
    print(returnNextCollectDay(d, typeList[t-1]["q"], typeList[t-1]["r"]))