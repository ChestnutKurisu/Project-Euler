import math
from decimal import *

getcontext().prec = 30

def bisection(a, b, f, e):
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    c = (a + b) / 2
    while abs(f(c)) >= 0:
        c_old = c
        if f(a) * f(c) < 0:
            b = c
            c = (a + c) / 2
        elif f(b) * f(c) < 0:
            a = c
            c = (c + b) / 2
        if abs(c - c_old) <= e:
            break
    return c


q = int(input())
for i in range(q):
    a, d, n, x = map(Decimal, input().split())
    if a * n - d * n * (n + 1) / Decimal(2) + x == Decimal(0):
        print(1)
        continue


    def f(r):
        if r == Decimal(1):
            return a * n - d * n * (n + 1) / 2 + x
        return a * (1 - r ** n) / (1 - r) - d * (1 - (n + 1) * r ** n + n * r ** (n + 1)) / (1 - r) ** 2 + x


    # if f(-1) == 0:
    #     print(-1)
    #     continue
    r = bisection(Decimal(0), Decimal(1.17), f, Decimal(10) ** Decimal(-13))
    print(r)
