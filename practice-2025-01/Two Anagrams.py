s = input()
t = input()

def check(s, t):
    min_s = sorted(s)
    max_t = sorted(t, reverse=True)

    if min_s < max_t:
        return 'Yes'
    else:
        return 'No'

print(check(s,t))
