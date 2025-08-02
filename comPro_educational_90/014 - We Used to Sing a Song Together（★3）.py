N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sorted_a = sorted(A)
sorted_b = sorted(B)
res = 0

for i in range(N):
    value = abs(sorted_a[i] - sorted_b[i])
    res += value

print(res)
    