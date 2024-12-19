N = int(input())
Player = []
minAge = 10 ** 9
index = 0

for i in range(N):
    S, A = input().split()
    A = int(A)
    if A < minAge:
        minAge = A
        index = i
    Player.append((S, A))

for i in range(index, index + N):
    j = i % N
    print(Player[j][0])

