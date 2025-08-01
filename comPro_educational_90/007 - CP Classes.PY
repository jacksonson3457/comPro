N = int(input())
A = list(map(int, input().split()))
Q = int(input())

sortedA = sorted(A)

def c():
    for _ in range(Q):
        B = int(input())
        #二分探索
        left, right = 0, N

        while left < right:
            mid = (left + right) // 2
            if sortedA[mid] < B:
                left = mid + 1
            else:
                right = mid

        candidates = []
        if left < N:
            candidates.append(abs(sortedA[left] - B))
        if left > 0:
            candidates.append(abs(sortedA[left - 1] - B))

        print(min(candidates))

c()