N = int(input())
A = list(map(int, input().split()))
odd = []
even = []

for i in range(N):
    if A[i] % 2 == 1:
        odd.append(A[i])
    else:
        even.append(A[i])

odd.sort(reverse=True)
even.sort(reverse=True)

mx = -1
if len(odd) >= 2:
    mx = max(mx, odd[0] + odd[1])
if len(even) >= 2:
    mx = max(mx, even[0] + even[1])

print(mx)