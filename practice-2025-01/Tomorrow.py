M, D = map(int, input().split())
y,m,d = map(int, input().split())

if d+1 > D:
    d = 1
    m += 1
else:
    d += 1

if m > M:
    y += 1
    m = 1

print(f'{y} {m} {d}')