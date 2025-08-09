from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

def mod46(array: list):
    for i in range(N):
        array[i] = array[i] % 46
    return Counter(array)

count_A = mod46(A)
count_B = mod46(B)
count_C = mod46(C)

ans = 0
for elem_a, count_a in count_A.items():
    for elem_b, count_b in count_B.items():
        for elem_c, count_c in count_C.items():
            if (elem_a + elem_b + elem_c) % 46 == 0:
                ans += count_a * count_b * count_c

print(ans)