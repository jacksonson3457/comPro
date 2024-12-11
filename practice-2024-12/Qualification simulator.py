def isQualify(confirmed, participant, maxConfirm, maxAbroadConfirm, abroadConfirmed):
    if confirmed < maxConfirm:
        if participant == 'a':
            return 'Yes'
        elif participant == 'b':
            if abroadConfirmed < maxAbroadConfirm:
                return 'Yes'
            else:
                return 'No'
    else:
        return 'No'




N,A,B = map(int, input().split())
participants = input().strip()

confirmed = 0
abroadConfirmed = 0
maxConfirm = A + B
for x in participants:
    if x == 'a':
        if isQualify(confirmed, x, maxConfirm, B, abroadConfirmed) == 'Yes':
            confirmed += 1
            print('Yes')
        else:
            print('No')
    elif x == 'b':
        if isQualify(confirmed, x, maxConfirm, B, abroadConfirmed) == 'Yes':
            confirmed += 1
            abroadConfirmed += 1
            print('Yes')
        else:
            print('No')
    else:
        print('No')