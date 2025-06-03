N, M = map(int, input().split())
wall_list = [0] * N
diff = [0] * (N + 1)

for i in range(M):
    L, R = map(int, input().split())
    #差分配列を更新
    #L-1を+1
    diff[L-1] += 1
    #Rを-1
    diff[R] -= 1

current = 0
#差分配列を使って累積和を取っていき正しい状態にする
for i in range(N):
    current += diff[i]
    wall_list[i] = current

result = min(wall_list)
print(result)

