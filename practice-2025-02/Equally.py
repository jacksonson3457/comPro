A,B,C = map(int, input().split())

def main():
    if A == B and B == C:
        return 'Yes'
    if A + B == C or B + C == A or A + C == B:
        return 'Yes'
    
    return 'No'

print(main())