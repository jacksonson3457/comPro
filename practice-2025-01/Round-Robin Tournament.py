N = int(input())
result = []
for i in range(N):
    count = 0
    s = input()

    for j in range(len(s)):
        if s[j] == '-': continue
        if s[j] == 'o': count += 1
        if s[j] == 'x': continue
    result.append((i, count))

sorted_result = sorted(result, key=lambda x: x[1], reverse=True)
result = [x[0]+1 for x in sorted_result]
print(*result)
