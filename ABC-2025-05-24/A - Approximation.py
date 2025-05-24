A, B = map(int, input().split())

P = A / B
P2 = A // B
P3 = P - P2

if P3 <= 0.5:
    print(P2)
else:
    print(P2 + 1)