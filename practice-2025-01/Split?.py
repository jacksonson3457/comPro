S = input()
N = len(S)
s = '$' + S


def is_split(s):
    #False: 全部倒れている True: 1つ以上立っている
    pins = [False] * 7
    pins[0] = (s[7] == '1')
    pins[1] = (s[4] == '1')
    pins[2] = (s[8] == '1') or (s[2] == '1')
    pins[3] = (s[5] == '1') or (s[1] == '1')
    pins[4] = (s[9] == '1') or (s[3] == '1')
    pins[5] = (s[6] == '1')
    pins[6] = (s[10] == '1')
    

    for i in range(7):
        for j in range(i):
            if pins[i] and pins[j]:
                for k in range(j+1,i):
                    if pins[k] == False:
                        return 'Yes'
    return 'No'

if s[1] == '1':
    print('No')
else:
    print(is_split(s))