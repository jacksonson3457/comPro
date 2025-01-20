from collections import deque
Q = int(input())
# [head, tail]
snakes = deque()

offset = 0
def q1(l):
    if len(snakes) == 0:
        snakes.append([0, l])
    else:
        last = snakes[len(snakes)-1]
        snakes.append([last[1], last[1] + l])

def q2():
    global offset
    first = snakes.popleft()
    offset += first[1] - first[0]  # オフセットを更新

def q3(k):
    print(snakes[k-1][0] - offset)



for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        q1(query[1])
    elif query[0] == 2:
        q2()
    elif query[0] == 3:
        q3(query[1])
