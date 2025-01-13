N = int(input())

def c(N):
    for i in range(26):
        for j in range(15):
            if i * 4 + j * 7 == N:
                return 'Yes'
    return 'No'

print(c(N))