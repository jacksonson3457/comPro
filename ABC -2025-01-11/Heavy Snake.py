N, D = map(int,input().split())
snakes = list()

for i in range(N):
    T, L = map(int,input().split())
    snakes.append([T,L])

result = []
for i in range(1,D+1):
    cur = []
    for snake in snakes:
        snake[1] += 1
        cur.append(snake[0] * snake[1])
    max_hev = max(cur)
    result.append(max_hev)

for v in result:
    print(v)

