n = int(input())

if n >= 59:
    print("Yes")
else:
    if 2 ** n > n * n:
        print("Yes")
    else:
        print("No")