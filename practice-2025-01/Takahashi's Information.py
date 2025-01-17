grid = [list(map(int, input().split())) for _ in range(3)]

def check(A,B):
    for i in range(3):
        for j in range(3):
            if grid[i][j] != A[i] + B[j]:
                return False
    return True


def check2():
    for i in range(101):
        for j in range(101):
            for k in range(101):
                A = [i, j, k]
                b1 = grid[0][0] - A[0]
                b2 = grid[0][1] - A[0]
                b3 = grid[0][2] - A[0]
                B = [b1, b2, b3]
                if check(A,B):
                    return 'Yes'
    return 'No'

print(check2())

