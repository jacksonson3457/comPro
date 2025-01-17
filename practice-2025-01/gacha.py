N = int(input())

backet = set()

for _ in range(N):
    s = input()
    if s in backet:
        continue
    else:
        backet.add(s)

print(len(backet))
