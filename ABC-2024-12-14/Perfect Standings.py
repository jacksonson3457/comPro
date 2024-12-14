from itertools import combinations

inputs = list(map(int, input().split()))
words = ['A','B','C','D','E']
points = {'A': inputs[0],
          'B': inputs[1],
          'C': inputs[2],
          'D': inputs[3],
          'E': inputs[4]}
result = {}

for r in range(1, 6):
    for key in combinations(points, r):
        value = 0
        for p in key:
            value += points[p]
        result[''.join(key)] = value

result_sorted = sorted(result.items(), key=lambda x: (-x[1], x[0]))

for participant in result_sorted:
    print(participant[0])


