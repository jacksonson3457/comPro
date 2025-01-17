S = input()
N = len(S)

s_list = []
for l in range(N):
    for r in range(l+1,N+1):
        if  S[l:r] not in s_list:
            s_list.append(S[l:r])
    
res = len(s_list)
print(res)
