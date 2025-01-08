S = list(input())
T = list(input())

N = len(S)
can = 'No'

for i in range(0,N-1):
    S[i], S[i+1] = S[i+1], S[i]
    if S == T:
        can = 'Yes'
    S[i], S[i+1] = S[i+1], S[i]
    
print(can)