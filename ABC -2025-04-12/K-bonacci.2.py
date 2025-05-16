from collections import deque

def main():
    N, K = map(int, input().split())
    q = deque()

    for i in range(K):
        q.append(1)
    total = K
    if N < K:
        return 1

    for i in range(K,N):
        q.append(total % (10 ** 9))
        total += total
        total -= q.popleft()

    return (total % (10 ** 9))

print(main())