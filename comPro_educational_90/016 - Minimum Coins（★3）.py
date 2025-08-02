N = int(input())
A,B,C = map(int, input().split())
#適当にでかい値
ans = 10 ** 9

L = 9999
for i in range(L):
    for j in range(L-i):
        rest = N - A*i - B*j
        if rest < 0:
            break
        k = rest // C
        if A*i + B*j + C*k == N:
            ans = min(ans, i+j+k)

print(ans)