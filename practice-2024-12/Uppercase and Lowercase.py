S = input()

low_count = 0
up_count = 0

N = len(S)

for i in range(N):
    if S[i].islower():
        low_count += 1
    else:
        up_count += 1

if up_count > low_count:
    print(S.upper())
else:
    print(S.lower())