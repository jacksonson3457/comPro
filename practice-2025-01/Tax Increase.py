A, B = map(int,input().split())
result = 0
for i in range(1,10000):
    if i * 8 // 100 == A and i * 10 // 100 == B:
        result = i
        break

if result == 0:
    print(-1)
else:
    print(result)