import math
from fractions import Fraction


def co_prime_generator_Farey(n):
    # Generates all relatively prime pairs <= n
    # Adapted from https://en.wikipedia.org/wiki/Farey_sequence
    a, b, c, d = 0, 1, 1, n
    while c <= n:
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        yield a, b


k = int(input())
rationals = [Fraction(a, b) for a, b in co_prime_generator_Farey(k) if not (a == 1 and b == 1)]
distinct_s_values = set()
for i in range(len(rationals)):
    for j in range(i, len(rationals)):
        # x and y are interchangeable
        x = rationals[i]
        y = rationals[j]
        # f_n(x, y, z) = (x + y + z)(x^n + y^n - z^n)
        # n != 0 since x + y + z != 0 and n = -2, -1, 1, 2 by Fermat's Last Theorem
        c_1 = x + y
        z = c_1
        if 0 < z.numerator < z.denominator <= k:
            distinct_s_values.add(x + y + z)
        c_2 = x ** 2 + y ** 2
        z = Fraction(round(math.sqrt(c_2.numerator)), round(math.sqrt(c_2.denominator)))
        if 0 < z.numerator < z.denominator <= k and z ** 2 == c_2:
            distinct_s_values.add(x + y + z)
        c_2 = z
        c_3 = (x * y) / c_1
        z = c_3
        if 0 < z.numerator < z.denominator <= k:
            distinct_s_values.add(x + y + z)
        c_4 = (x * y) / c_2
        z = c_4
        if 0 < z.numerator < z.denominator <= k and z ** 2 == (x ** 2 * y ** 2) / (x ** 2 + y ** 2):
            distinct_s_values.add(x + y + z)
t = sum(distinct_s_values)
print(t.numerator + t.denominator)
