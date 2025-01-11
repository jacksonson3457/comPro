N = int(input())
S = input()

def ab(N,S):
    for i in range(0, N-1):
        if S[i] == 'a' and S[i+1] == 'b':
            return 'Yes'
        elif S[i] == 'b' and S[i+1] == 'a':
            return 'Yes'
    return 'No'

print(ab(N,S))