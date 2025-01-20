X = int(input())

# N! = X を満たすN
pre = 1
for i in range(1,X+1):
    v = pre * i
    if v == X:
        print(i)
        break
    else:
        pre = v