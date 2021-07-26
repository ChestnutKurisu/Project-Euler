import math
from decimal import *

getcontext().prec = 30


def fib(n):
    return int(round(Decimal(1) / Decimal(5).sqrt() * (((Decimal(1) + Decimal(5).sqrt()) / Decimal(2)) ** Decimal(n) - (
            (Decimal(1) - Decimal(5).sqrt()) / Decimal(2)) ** Decimal(n))))


T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
N_max = max(N)
f = []
i = 3
while True:
    f_i = fib(i)
    if f_i <= N_max:
        f.append(f_i)
    else:
        break
    i += 3
for k in range(T):
    s = 0
    for i in range(len(f)):
        if f[i] > N[k]:
            break
        s += f[i]
    print(s)
