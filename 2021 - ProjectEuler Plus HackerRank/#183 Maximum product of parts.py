import math
from fractions import Fraction
from itertools import accumulate

q = int(input())
n = [0] * q
for i in range(q):
    n[i] = int(input())
n_max = max(n)
D = [0] * (n_max + 1)
for N in range(5, n_max + 1):
    k = int(round(N * math.e ** -1))
    k = Fraction(N, k).denominator
    while k % 2 == 0:
        k /= 2
    while k % 5 == 0:
        k /= 5
    D[N] = N if k != 1 else -N
accumulate_D = list(accumulate(D))
for i in range(q):
    print(accumulate_D[n[i]])
