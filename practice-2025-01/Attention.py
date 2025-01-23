N = int(input())
S = input()

#向いている方向のリストをとりあえず作る
E = [0] * N
W = [0] * N

for i in range(N):
    if S[i] == 'E':
        E[i] = 1
    else:
        W[i] = 1

#この配列をもとに累積和を作る
for i in range(1,N):
    E[i] += E[i-1]
    W[i] += W[i-1]

ans = float('inf')
for i in range(N):
    sm = 0
    if i > 0:
        sm += W[i-1]
    sm += E[N-1] - E[i]
    ans = min(ans, sm)
print(ans)