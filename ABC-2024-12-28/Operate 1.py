from collections import Counter

def check1(S, T):
    diff_count = 0
    cS = Counter(S)
    cT = Counter(T)
    if len(S) + 1 != len(T): return False

    for v in cT:
        if diff_count > 1: return False
        if v not in cS:
            diff_count += cT[v]
        elif cS[v] <= cT[v]:
            diff_count += cT[v] - cS[v]
        else:
            #cSの方に同じ文字が多くある場合何を挿入しても一致しない
            return False

    return diff_count == 1

def check2(S,T):
    #削除できるかどうか
    diff_count = 0
    cS = Counter(S)
    cT = Counter(T)
    #まずlenが1個多くないとダメ
    if len(S) - 1 != len(T): return False

    for v in cS:
        if diff_count > 1: return False
        if v not in cT:
            diff_count += cS[v]
        elif cS[v] >= cT[v]:
            diff_count += cS[v] - cT[v]
        else:
            #cTの方が多い場合cSから何を削除しても一致しない
            return False

    return diff_count == 1

def check3(S, T):
    # ある1文字を除いて他がすべて一致しているか
    diff_count = 0
    cS = Counter(S)
    cT = Counter(T)

    if len(S) != len(T): return False

    for v in cT:
        if v not in cS:
            diff_count += cT[v]
        elif cT[v] != cS[v]:
            diff_count += abs(cT[v] - cS[v])

    return diff_count == 1

            
        


K = int(input())
S = input()
T = input()
c1 = check1(S,T)
c2 = check2(S,T)
c3 = check3(S,T)


if c1 or c2 or c3 or S == T:
    print('Yes')
else:
    print('No')