X, Y = map(int, input().split())

def fib():
    a, b = X, Y
    for _ in range(9):
        a, b = b, a + b

        #ここでrev変換
        # a = int(str(a)[::-1])
        b = int(str(b)[::-1])

    return a

print(fib())
