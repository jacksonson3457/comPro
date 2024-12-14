N, C1, C2 = map(str, input().split())
N = int(N)
S = input()
result = ''

for i in range(N):
    if S[i] != C1:
        result += (C2)
    else:
        result += (S[i])

print(result)