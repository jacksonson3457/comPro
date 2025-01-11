N = int(input())

def check(N):
    if N // 10 == 0:
        return 'Yes'
    
    c = N % 10
    N = N // 10
    while 0 < N:
        next_c = N % 10
        if c >= next_c:
            return 'No'
        N = N // 10
        c = next_c
    return 'Yes'

print(check(N))