H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

#sum_w,sum_hを先に作っておく
def make_sums():
    sum_w = []
    for i in range(H):
        sum_w.append(sum(A[i]))

    sum_h = []
    for i in range(W):
        sum_vertical = 0
        for j in range(H):
            sum_vertical += A[j][i]
        sum_h.append(sum_vertical)
    
    return sum_w, sum_h

def makeArray():
    sum_w, sum_h = make_sums()
    resA = A
    for i in range(H):
        for j in range(W):
            #resA[i][j]に横一列＋縦一列-A[i][j]を入れていけばいい
            resA[i][j] = sum_w[i] + sum_h[j] - A[i][j]
    
    return resA

result = makeArray()
for row in result:
    print(*row)
