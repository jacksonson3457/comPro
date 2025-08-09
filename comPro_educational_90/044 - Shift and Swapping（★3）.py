from collections import deque

N, Q = map(int, input().split())
A = deque(map(int, input().split()))

def q1(x,y):
    A[x], A[y] = A[y], A[x]

def q2():
    A.rotate(1)

def q3(x):
    print(A[x])

for i in range(Q):
    T, x, y = map(int, input().split())

    if T == 1:
        q1(x-1,y-1)
    elif T == 2:
        q2()
    else:
        q3(x-1)