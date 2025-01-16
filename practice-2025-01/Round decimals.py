from decimal import Decimal, getcontext, ROUND_HALF_UP

X = float(input())
d = Decimal(X)
res = d.quantize(Decimal('0'), rounding=ROUND_HALF_UP) 
print(res)