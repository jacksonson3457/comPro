def isPreOrSuf(N, M, S, T):
    if S == T[:N] and S == T[-N:]:
        return 0
    
    if S == T[:N]:
        return 1
    
    if S == T[-N:]:
        return 2
    
    return 3


N, M = map(int, input().split())
S = input()
T = input()
print(isPreOrSuf(N, M, S, T))
