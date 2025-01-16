from collections import Counter

N = int(input())
array = list(map(int, input().split()))
sorted_array = sorted(array, reverse=True)
counter_ = list(Counter(sorted_array).items())
cN = len(counter_)

for k in range(N):
    if k < cN:
        print(counter_[k][1])
    else:
        print(0)
    