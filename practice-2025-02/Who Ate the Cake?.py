A,B = map(int, input().split())

def main():
    if A == B:
        return -1
    if A + B == 3:
        return 3
    if A + B == 4:
        return 2
    if A + B == 5:
        return 1

print(main())