from collections import defaultdict

N = int(input())
S = input()
res = 0

for i in range(N):
    S1 = S[:i]
    S2 = S[i:]

    dictionary = defaultdict(int)
    for v in S1:
        if dictionary[v] == 0:
            dictionary[v] = 1
    
    for v in S2:
        if dictionary[v] == 1:
            dictionary[v] = 2
    
    count = 0
    for v in dictionary:
        if dictionary[v] == 2:
            count += 1
    res = max(res, count)

print(res)