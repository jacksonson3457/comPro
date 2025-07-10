M = int(input())
D = list(map(int, input().split()))

middle = (sum(D) + 1) // 2 

def check():
    sum_day = 0
    for i in range(M):
        if sum_day + D[i] >= middle:
            # middleの日はi+1月にある
            day = middle - sum_day
            return i + 1, day
        sum_day += D[i]

a, b = check()
print(f'{a} {b}')
        
