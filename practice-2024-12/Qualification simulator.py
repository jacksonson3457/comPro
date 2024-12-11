def isQualify(confirmed, participant, maxConfirm, maxAbroadConfirm, abroadConfirmed):
    if confirmed < maxConfirm:
        if participant == 'a':
            return 'Yes'
        if participant == 'b' and abroadConfirmed < maxAbroadConfirm:
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
    result = isQualify(confirmed, x, maxConfirm, B, abroadConfirmed)
    print(result)
    if result == 'Yes':
        confirmed += 1
        if x == 'b':
            abroadConfirmed += 1