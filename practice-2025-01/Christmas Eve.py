N, K = map(int, input().split())
trees = list()
for _ in range(N):
    trees.append(int(input()))

sorted_trees = sorted(trees)

min_h = float('inf')

for i in range(K-1,N):
    h = sorted_trees[i] - sorted_trees[i-(K-1)]
    if h < min_h:
        min_h = h

print(min_h)

