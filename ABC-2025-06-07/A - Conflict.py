N = int(input())
T = input()
A = input()

def check():
    for i in range(N):
        if T[i] == 'o' and A[i] == 'o':
            return 'Yes'
    return 'No'

print(check())
