N = int(input())
list_s = []

for i in range(N):
    S = input()
    list_s.append(S)

X, Y = map(str, input().split())
X = int(X)

if list_s[X-1] == Y:
    print('Yes')
else:
    print('No')