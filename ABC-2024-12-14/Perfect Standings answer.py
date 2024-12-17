point = list(map(int, input().split()))

#bitを使うことで1が立っているかいないかで回答者を決めることができる
standings = []
for bit in range(1, 32):
    solved_point = 0
    name = ""
    #Pythonではビット演算子 &, << を使うとIntは自動的にbitになる
    for digit in range(5):
        if bit & 1 << digit:
            solved_point += point[digit]
            name += "ABCDE"[digit]
    standings.append((solved_point, name))

#最後に並べ替え
for _, name in sorted(standings, key=lambda x: (-x[0], x[1])):
    print(name)


