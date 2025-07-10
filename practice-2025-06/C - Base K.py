K = int(input())
A, B = map(str, input().split())

A_ten = 0
B_ten = 0

for i in range(0,len(A)):
    A_ten += int(A[len(A) - i - 1]) * K ** i

for j in range(0,len(B)):
    B_ten += int(B[len(B) - j - 1]) * K ** j

print(A_ten * B_ten)

