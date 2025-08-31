import math

N = int(input())
A = []

sum_r = 0
sum_c = 0
for _ in range(N):
    R, C = map(int, input().split())
    sum_r += R
    sum_c += C
    A.append([R, C])

ave_r = sum_r // N
ave_c = sum_c // N

#誰が一番aveから遠いのかを知りたい
max_dis = 0
who = 0
for i in range(N):
    R, C = A[i][0], A[i][1] 
    dis = abs(R - ave_r) + abs(C - ave_c)
    if dis > max_dis:
        max_dis = dis
        who = i

def main(who, max_dis):
    R, C = A[who][0], A[who][1] 
    dis = abs(R - ave_r) ** 2 + abs(C - ave_c) ** 2
    #三平方で出した距離の整数値を取っておけば勝手に最短移動回数になってくれないかなあという希望的観測
    root_dis = int(math.sqrt(dis))
    return root_dis

print(main(who, max_dis))