N = int(input())

X = int(N / 1.08 + 0.5)

if (int(X * 1.08) == N):
    print(X)
elif int((X + 1) * 1.08) == N:
    print(X+1)
else:
    print(':(')