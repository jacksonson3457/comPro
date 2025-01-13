H, W = map(int, input().split())

pixel = [input() for _ in range(H)]

for i in range(0,2*H,2):
    pixel.insert(i+1, pixel[i])

for v in pixel:
    res = ''.join(v)
    print(res)
