N = int(input())
dic = set()

for _ in range(N):
    s = int(input())
    if s in dic:
        dic.remove(s)
    else:
        dic.add(s)

print(len(dic))