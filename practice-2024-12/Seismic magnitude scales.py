A, B = map(int, input().split())

sub = (A - B)
magnitude = 32 ** sub
if sub == 1:
    print(1)
else:
    print(magnitude)