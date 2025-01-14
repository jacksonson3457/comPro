import math

A, B, W = map(int, input().split())
W *= 1000
list = []
L = math.ceil(W / B)
R = W // A

if A * L <= W <= B * R:
    print(f'{L} {R}')
else:
    print('UNSATISFIABLE')