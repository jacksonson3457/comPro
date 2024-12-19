N = int(input())
A = list(map(int, input().split()))

numberSet = set(A)
numberList = list(numberSet)
numberList.sort()
print(numberList[-2])