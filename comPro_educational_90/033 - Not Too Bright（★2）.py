H, W = map(int, input().split())

def splitBy2(x):
    return (x + 1) // 2

if H == 1 or W == 1:
    print(H * W)
else:
    print(splitBy2(H) * splitBy2(W))