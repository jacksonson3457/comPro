def isOK1(x,y):
    return (x + y) % 2 == 1
    
def isOK2(x,y,z):
    return x < z < y

S = input()

x1 = S.find('B')
y1 = S.rfind('B')

isOK = False

x2 = S.find('R')
y2 = S.rfind('R')
z2 = S.find('K')

if isOK1(x1,y1) and isOK2(x2,y2,z2):
    isOK = True

if isOK :
    print('Yes')
else:
    print('No')