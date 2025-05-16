MOD = 10**9
N, K = map(int, input().split())
array = [1 for _ in range(N + 1)]
window_sum = sum(array[:K])

for i in range(K, N + 1):
    array[i] = window_sum % MOD
    window_sum = (window_sum + array[i] - array[i - K]) % MOD

print(array[N])
