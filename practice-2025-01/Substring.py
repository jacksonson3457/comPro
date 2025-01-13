S = input()
T = input()

def check (S,T):
    len_s = len(S)
    len_t = len(T)
    ans = len_t
    for i in range(0,len_s - len_t + 1):
        diff = 0
        for j in range(len_t):
            if S[i+j] != T[j]:
                diff += 1
        ans = min(ans, diff)
    return ans

print(check(S,T))