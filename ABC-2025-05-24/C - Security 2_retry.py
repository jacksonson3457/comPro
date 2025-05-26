S = input()
N = len(S)

origin_left_num = int(S[0])
now_left_num = 0
count = 0

for i in range(N):

    #iが最後の文字→now_left_numをS[0]に合わせて終了
    if i == N-1:
        count += (10 + origin_left_num - now_left_num) % 10
        break
    
    #次に入れたい文字
    next_num = int(S[i+1])
    
    #now_left_numをtargetに合わせる
    target = (10 + origin_left_num - next_num) % 10
    #targetにnow_left_numを合わせるためにBを何回押すか？
    how_many_b = (10 + target - now_left_num) % 10
    count += how_many_b
    #how_many_b回押してnow_left_numはtargetになった
    now_left_num = target

# AはN回必要
count += N

print(count)
