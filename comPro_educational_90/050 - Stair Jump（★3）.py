N, L = map(int, input().split())

#dp[i] = i段目まで何通りで登れるか
dp = [0] * (N+1)
dp[0] = 1
for i in range(1, N+1):
    if i < L:
        dp[i] = dp[i-1]
    else:
        dp[i] = dp[i-1] + dp[i-L]

print(dp[N] % (10 ** 9 + 7))