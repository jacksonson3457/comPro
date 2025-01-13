bingo = [list(map(int, input().split())) for _ in range(3)]
N = int(input())

def is_bingo(bingo):
    if sum(bingo[0]) == 0 or sum(bingo[1]) == 0 or sum(bingo[2]) == 0 \
    or bingo[0][0] + bingo[1][0] + bingo[2][0] == 0 \
    or bingo[0][1] + bingo[1][1] + bingo[2][1] == 0 \
    or bingo[0][2] + bingo[1][2] + bingo[2][2] == 0 \
    or bingo[0][0] + bingo[1][1] + bingo[2][2] == 0 \
    or bingo[0][2] + bingo[1][1] + bingo[2][0] == 0:
        return 'Yes'
    else: return 'No'

for _ in range(N):
    b = int(input())

    for i in range(3):
        for j in range(3):
            if bingo[i][j] == b:
                bingo[i][j] = 0

print(is_bingo(bingo))