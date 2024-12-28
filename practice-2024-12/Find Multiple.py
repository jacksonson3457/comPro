A, B, C = map(int, input().split())

exsist = False
for i in range(A, B):
    if i % C == 0:
        print(i)
        exsist = True
        break

if exsist == False:
    print(-1)