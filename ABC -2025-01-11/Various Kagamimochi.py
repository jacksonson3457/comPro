from collections import Counter
from itertools import accumulate
import bisect

N = int(input())
motis = list(map(int,input().split()))
motis_counter = Counter(motis)
sorted_keys = sorted(motis_counter.keys())
freq = [motis_counter[key] for key in sorted_keys]
cumulative_freq = list(accumulate(freq))

result = 0
for i,v in enumerate(sorted_keys):
    limit = v // 2
    limit_index = bisect.bisect_right(sorted_keys, limit) - 1
    if limit_index >= 0:
        result += cumulative_freq[limit_index] * motis_counter[v]

print(result)