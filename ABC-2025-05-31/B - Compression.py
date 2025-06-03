N = int(input())
A = list(map(int, input().split()))

set_A = sorted(set(A))

print(len(set_A))
print(*set_A)