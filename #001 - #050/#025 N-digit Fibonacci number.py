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
first = [0] * (N_max + 1)
i = 1
n = 1
while True:
    f = fib(n)
    if int(math.log10(f) + 1) == i:
        first[i] = n
        i += 1
        n += 3
    n += 1
    if i > N_max:
        break
for k in range(T):
    print(first[N[k]])
