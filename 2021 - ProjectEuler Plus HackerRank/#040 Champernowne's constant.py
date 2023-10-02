import decimal
import operator
from functools import reduce
from decimal import Decimal


def champernowne(i):
    exp = 0
    for j in range(len(exp_digit_sum)):
        if i > exp_digit_sum[j]:
            exp = len(exp_digit_sum) - j
            i -= exp_digit_sum[j]
            break
    return int(str(10 ** (exp - 1) - 1 + int((Decimal(i) / Decimal(exp)).to_integral_exact(rounding=decimal.ROUND_CEILING)))[i % exp - 1])


exp_digit_sum = [10 ** (n + 1) * (n + 1) - 10 * (10 ** n - 1) // 9 - 1 for n in range(20, -1, -1)]
exp_digit_sum.append(0)
T = int(input())
P = [0] * T
for k in range(T):
    i = list(map(int, input().split()))
    P[k] = reduce(operator.mul, [champernowne(i[j]) for j in range(7)])
for k in range(T):
    print(P[k])