import math
from decimal import Decimal, getcontext

# def evaluate_convergent(continued_fraction):
#     num, den = 1, continued_fraction[-1]
#     for i in range(len(continued_fraction) - 2, -1, -1):
#         num, den = den, den * continued_fraction[i] + num
#     return den, num

# def find_continued_fraction(x, length):
#     continued_fraction = [math.floor(x)]
#     for i in range(length):
#         x = 1 / (x - continued_fraction[-1])
#         continued_fraction.append(math.floor(x))
#         if x.is_integer():
#             break
#     return continued_fraction

# https://en.wikipedia.org/wiki/Pell%27s_equation#Fundamental_solution_via_continued_fractions
# https://oeis.org/A033316

getcontext().prec = 500
N = int(input())
x_max, D_max = 0, 0
for D in range(2, N + 1):
    if math.sqrt(D).is_integer():
        continue
    x = 0
    r = Decimal(D).sqrt()
    # Using Pieter Geerkens answer at https://math.stackexchange.com/questions/1428002/determine-convergents-for-square-root
    # Continued fraction of r is [a_0; a_1, a_2, ...]
    # Sequence of convergents of r is c_0, c_1, ...
    h_prev, k_prev = 1, 0
    a_0 = math.floor(r)
    h_current, k_current = a_0, 1
    r = 1 / (r - Decimal(h_current))
    a_current = math.floor(r)
    while True:
        h_current, k_current, h_prev, k_prev = a_current * h_current + h_prev, a_current * k_current + k_prev, h_current, k_current
        if h_current ** 2 - D * k_current ** 2 == 1:
            x = h_current
            break
        r = 1 / (r - math.floor(r))
        a_current = math.floor(r)
    if x_max < x:
        x_max, D_max = x, D
print(D_max)
