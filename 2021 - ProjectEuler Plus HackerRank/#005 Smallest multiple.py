import math
from functools import reduce
import operator

T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
for k in range(T):
    p = list(range(1, N[k] + 1))
    print(reduce(operator.mul, p, 1) // reduce(math.gcd, [reduce(operator.mul, p, 1)//i for i in p]))
