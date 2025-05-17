N = int(input())

def check():
    prev_t, prev_x, prev_y = 0, 0, 0
    for i in range(N):
        t, x, y = map(int, input().split())
        dt   = t - prev_t
        dist = abs(x - prev_x) + abs(y - prev_y)

        # 時間不足 or 偶奇不一致でアウト
        if dist > dt or (dt - dist) % 2 != 0:
            return("No")

        prev_t, prev_x, prev_y = t, x, y
                
        
    return("Yes")

print(check())

