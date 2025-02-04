import collections
S = list(input())
c = collections.Counter(S)
#most_commonは初出順なんだ
print(c.most_common()[0][0])