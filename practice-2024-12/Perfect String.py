def hasUpAndLow(S:str):
    if S.isupper() or S.islower():
        return False
    else:
        return True 

def isDifferent(S:str):
    N = len(S)
    for i in range(N):
        for j in range(i+1,N):
            if S[i] == S[j]:
                return False
    return True
    
S = input()

if hasUpAndLow(S) and isDifferent(S):
    print('Yes')
else:
    print('No')