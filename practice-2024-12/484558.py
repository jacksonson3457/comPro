N = int(input())
hexN = hex(N)
strN = str(hexN)
result = strN[2:].upper()
if len(result) < 2:
    result = '0' + result

print(result)