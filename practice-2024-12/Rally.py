def min_squared_sum(N, coordinates):
    mean = sum(coordinates) // N
    candidates = [mean, mean + 1]

    results = []
    for P in candidates:
        total = sum(abs(x - P) ** 2 for x in coordinates)
        results.append(total)

    return min(results)


N = int(input())
coordinates = list(map(int, input().split()))
print(min_squared_sum(N,coordinates))
