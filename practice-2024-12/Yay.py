from collections import defaultdict

S = input()
char_count = defaultdict(int)

for char in S:
    char_count[char] += 1

serachChar = ''
for a in char_count:
    if char_count[a] == 1:
        serachChar = a

print(S.index(serachChar) + 1)
