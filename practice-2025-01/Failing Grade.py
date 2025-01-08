N, P = map(int, input().split())
students = list(map(int, input().split()))

result = 0

for i in range(N):
    if students[i] < P:
        result += 1

print(result)