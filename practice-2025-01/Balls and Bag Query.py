Q = int(input())
dic = {}

def q1(x):
    if x in dic:
        dic[x] = dic[x] + 1
    else:
        dic[x] = 1

def q2(x):
    dic[x] = dic[x] - 1
    if dic[x] == 0:
        del dic[x]

def q3():
    v = len(dic)
    print(v)

for i in range(Q):
    # 入力の処理
    values = list(map(int, input().split()))

    # 入力された値が1つの場合
    if len(values) == 1:
        q, x = values[0], 0  # xには0を代入
    # 入力された値が2つの場合
    elif len(values) == 2:
        q, x = values
    if q == 1:
        q1(x)
    elif q == 2:
        q2(x)
    else:
        q3()