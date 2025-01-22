s = input()
N = len(s)

i = 0
res = ''
while i < N:
    j = i + 1
    count = 1
    while j < N and s[i] == s[j]:
        j += 1
        count += 1
    res += f'{s[i]}{count}'
    i = j

print(res)
