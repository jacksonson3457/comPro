N = int(input())
seen = set()
ans = []

for i in range(N):
    S = input()
    if S in seen:
        continue
    seen.add(S)
    ans.append(str(i+1))

print("\n".join(ans))