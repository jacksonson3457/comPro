from collections import Counter
array = list(map(int, input().split()))
cards = Counter(array)
isOk = False

if len(cards) <= 2:
    for v in cards:
        for w in cards:
            if v == w: continue
            if (cards[v] == 2 and cards[w] == 2) or (cards[v] == 3 and cards[w] == 1) or (cards[v] == 1 and cards[w] == 3):
                isOk = True

if isOk:
    print('Yes')
else:
    print('No')