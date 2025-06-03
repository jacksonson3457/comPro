N, S = map(int, input().split())
A = list(map(int, input().split()))

def check():
    if A[0] >= S + 0.5:
        return False
    
    for i in range(1,N):
        now = A[i]
        last = A[i-1]
        if now - last >= S + 0.5:
            return False
    
    return True

if check():
    print('Yes')
else:
    print('No')