from collections import deque
S = input()
N = len(S)


def string_shift_max(S,N):
    def dic_check(S,T):
        if S <= T:
            return T
        else:
            return S
    
    result = S
    s_list = deque(S)
    for i in range(N):
        c = s_list.pop()
        s_list.appendleft(c)
        result = dic_check(result, "".join(s_list))
    return result

def string_shift_min(S,N):
    def dic_check(S,T):
        if S >= T:
            return T
        else:
            return S
    
    result = S
    s_list = deque(S)
    for i in range(N):
        c = s_list.pop()
        s_list.appendleft(c)
        result = dic_check(result, "".join(s_list))
    return result

print(string_shift_min(S,N))
print(string_shift_max(S,N))