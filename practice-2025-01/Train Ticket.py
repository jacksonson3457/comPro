S = input()

def add(P,Q):
    return P+Q
def sub(P,Q):
    return P-Q
 
def check(S):
    A = int(S[0])
    B = int(S[1])
    C = int(S[2])
    D = int(S[3])
    for i in range(2):
        c = 0
        res = ''
        if i == 0:
            c = add(A,B)
            res += f'{A}+{B}'
        else:
            c = sub(A,B)
            res += f'{A}-{B}'
        for j in range(2):
            res1 = res
            if j == 0:
                c1 = add(c,C)
                res1 += f'+{C}'
            else:
                c1 = sub(c,C)
                res1 += f'-{C}'
            for k in range(2):
                res2 = res1
                if k == 0:
                    c2 = add(c1,D)
                    res2 += f'+{D}'
                else:
                    c2 = sub(c1,D)
                    res2 += f'-{D}'
                
                if c2 == 7:
                    return res2+'=7'
                    
print(check(S))