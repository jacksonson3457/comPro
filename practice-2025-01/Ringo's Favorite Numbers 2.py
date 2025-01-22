from collections import Counter

N = int(input())
array = list(map(int, input().split()))
mod_array = [num % 200 for num in array]
count = Counter(mod_array)
sorted_count = dict(sorted(count.items(), key=lambda x: x[0]))

res = 0
for i in sorted_count:
    if sorted_count[i] > 1: res += sorted_count[i] * (sorted_count[i]-1) // 2
    for j in sorted_count:
        if i == j: continue
        if i < j and j-i % 200 == 0:
            res += sorted_count[j] * sorted_count[i]

print(res)


