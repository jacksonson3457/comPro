import re

N, K = map(int, input().split())
S = input()

n = len(S)
target = "O" * K
result = 0
i =0

#部分文字列をスライドさせる
while i < n - K + 1:
    substring = S[i:i + K]
    if substring == target:
        result += 1
        i += K
    else:
        i += 1

print(result)