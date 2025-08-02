N = int(input())
S = input()

MOD = 10**9 + 7
T = "atcoder"

dp = [ [0] * (len(T) + 1) for _ in range(N+1)]
dp[0][0] = 1

for i , ch in enumerate(S):
    for j in range(len(T) + 1):
        # 文字を選ばない
        dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD
        # 文字を選ぶ（一致時のみ j -> j+1）
        if j < len(T) and ch == T[j]:
            dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD

print(dp[N][len(T)] % MOD)