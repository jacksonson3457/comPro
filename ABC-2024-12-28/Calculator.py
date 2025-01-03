S = input()
N = len(S)
counter = 0

i = 0
while i < N:
    if S[i] == '0' and i < N - 1:
        if S[i + 1] == '0':
            counter += 1
            i += 2  # 次のペアに進む
        else:
            counter += 1
            i += 1  # 次の文字に進む
    else:
        counter += 1
        i += 1  # 次の文字に進む

print(counter)
