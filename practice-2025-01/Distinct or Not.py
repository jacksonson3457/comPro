from collections import Counter

N = int(input())
list = list(map(int, input().split()))

def c():
    count = Counter(list)
    for key in count:
        if count[key] > 1:
            return 'NO'
    return 'YES'

print(c())