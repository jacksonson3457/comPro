S = input()

def calc(t):
    if len(t) < 3:
        return 0
    if t[0] != "t" or t[len(t)-1] != "t":
        return 0
            
    count = t.count("t")
    res = (count - 2) / (len(t) - 2)
    return res
            

def c(S):
    ans = 0
    N = len(S)
    if len(S) < 3: 
        print("0.000000000000")
        return
    for i in range(N):
        for j in range(i+1, N+1):
            t = S[i:j]
            res = calc(t)

            if ans < res:
                ans = res
    print(f"{ans:.12f}")

c(S)


    