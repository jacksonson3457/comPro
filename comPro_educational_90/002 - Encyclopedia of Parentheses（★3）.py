N = int(input())

def is_valid(s):
    balance = 0
    for ch in s:
        if ch == "(":
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False  # 閉じ過ぎ
    return balance == 0  # 最終的に開閉数が等しいか


def generate_valid_parentheses(N):
    if N % 2 == 1:
        return []
    valid = []
    for mask in range(1 << N):
        #マスクから括弧列を作る
        parens = []
        for i in range(N):
            if (mask >> i) & 1:
                parens.append("(")
            else:
                parens.append(")")
        s = "".join(reversed(parens))
        if is_valid(s):
            valid.append(s)
    return sorted(valid)

for p in generate_valid_parentheses(N):
    print(p)
        