N = int(input())
S = input()

i = 0
res = 0
while i < N:
    j = i + 1
    while j < N and S[i] == S[j]:
        j += 1
        
    res += 1
    i = j
    

print(res)
