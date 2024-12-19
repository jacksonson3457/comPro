N, Q = map(int, input().split())
Q_array = list(map(int, input().split()))

teeth = [True] * N
for i in range(Q):
    teeth[Q_array[i] - 1] = not teeth[Q_array[i] - 1]

true_count = sum(teeth)
print(true_count)