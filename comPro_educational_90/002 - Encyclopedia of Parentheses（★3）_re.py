N = int(input())

s = []
def makePair():
    for mask in range(1 << N):
        for i in range(N):
            if (mask >> (N-1-i) & 1 == 0):
                s.append('(')
            else:
                s.append(')')
        s = ''.join(s)