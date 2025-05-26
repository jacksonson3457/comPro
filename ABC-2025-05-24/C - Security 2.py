S = input()
len_S = len(S)

#1番左の文字
left_num = int(S[0])
# 現在の1番左の1桁
prev = 0

count = 0

for i in range(len_S-1):
    #Aボタンを押す
    count += 1

    #次に入れたい文字
    next_num = int(S[i+1])

    #iが最後の文字
    if i == len_S:
        count += int(S[i])
    
    #次に入れたい文字がleft_numより小さいか
    if next_num <= left_num:
        #target
        t = left_num - next_num
        if t < prev:
            prev = t
            #Bをt回おす
            count += t
            #Aをおして0を追加
            count += 1
        else:
            v = 10 + t - 



