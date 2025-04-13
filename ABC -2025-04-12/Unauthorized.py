N = int(input())

# 初期値ログアウト
isLogin = False
error_count = 0

def main(v):
    global isLogin
    global error_count
    if v == 'login':
        isLogin = True
    elif v == 'logout':
        isLogin = False
    elif v == 'public':
        return
    elif v == 'private':
        if not isLogin:
            error_count += 1

for i in range(N):
    S = input()
    main(S)

print(error_count)
