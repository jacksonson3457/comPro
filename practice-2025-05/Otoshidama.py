N, Y = map(int, input().split())

def check():
    for i in range(N+1):
        for j in range(N+1):
            C = Y - i*10000 - j*5000
            k = C // 1000
            if C % 1000 == 0 and i + j + k == N and C >= 0:
                return (f"{i} {j} {k}")
    return "-1 -1 -1"

print(check())
