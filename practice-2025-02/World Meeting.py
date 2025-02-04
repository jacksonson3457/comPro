N = int(input())
d = [tuple(map(int, input().split())) for _ in range(N)]

max_count = 0
for i in range(25):
    count = 0
    for j in range(N):
        now = (i + d[j][1]) % 24
        if 9 <= now <= 17:
            count += d[j][0]
    max_count = max(max_count,count)
    
print(max_count)