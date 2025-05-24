N, Q = map(int, input().split())

#複数の鳩がいる巣の数をカウントしておく
count = 0
#鳩の巣
home = [1] * N
#鳩のいる位置を記録しておく　初期値は i : i-1
pigeon = {i: i - 1 for i in range(1, N + 1)}

def q1(P,H):
    global count
    #飛び立つので-1する
    if home[pigeon[P]] == 2:
        count -= 1
    home[pigeon[P]] -= 1
    #鳩の送り先
    if home[H-1] == 1:
        count += 1
    home[H-1] += 1
    #鳩のいる位置を変更する
    pigeon[P] = H-1

def q2():
    print(count)


for i in range(Q):
    # 入力の処理
    values = list(map(int, input().split()))

    # 入力された値が1つの場合
    if len(values) == 1:
        #q2を実行
        q2()
    else:
        P,H = values[1], values[2]
        q1(P,H)