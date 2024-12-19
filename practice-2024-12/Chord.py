S = input()

pairs = ['ACE','BDF','CEG','DFA','EGB','FAC','GBD']
isPair = False

for i in range(len(pairs)):
    if pairs[i] == S:
        isPair = True
        break

print('Yes' if isPair else 'No')