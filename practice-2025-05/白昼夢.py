S = input()

s_reversed = S[::-1]

words = ["dream", "dreamer", "erase", "eraser"]
# 後ろから見ていく

while len(s_reversed) > 0:
    if s_reversed[:5] == words[0][::-1] or s_reversed[:5] == words[2][::-1]:
        s_reversed = s_reversed[5::]
    elif s_reversed[:7] == words[1][::-1]:
        s_reversed = s_reversed[7::]
    elif s_reversed[:6] == words[3][::-1]:
        s_reversed = s_reversed[6::]
    else:
        print("NO")
        break

    if len(s_reversed) == 0:
        print("YES")
        break

