def calc_expected_value(P):
    return (P + 1) / 2

N, K = map(int, input().split())
dices = list(map(int, input().split()))
expected_value = [0] * N
for i in range(N):
    expected_value[i] = calc_expected_value(dices[i])

max_value = 0
for i in range(N-K+1):
    p = sum(expected_value[i:i+K]) 
    max_value = max(max_value, p)

print(max_value)
