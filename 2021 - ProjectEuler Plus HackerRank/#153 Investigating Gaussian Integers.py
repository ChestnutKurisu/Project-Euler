import math
from itertools import combinations_with_replacement

N = int(input())
S = 0
for k in range(1, N + 1):
    S += k * (N // k)
for re, im in combinations_with_replacement(range(1, int(N ** 0.5) + 1), 2):
    gcd = math.gcd(re, im)
    if gcd != 1:
        continue
    max_gcd = (N // (re ** 2 + im ** 2))
    S += (2 * re if re == im else 2 * (re + im)) * sum(
        g * (N // (g * (re ** 2 + im ** 2))) for g in range(1, max_gcd + 1))
print(S)

# Other solutions from projecteuler.net

"""Fast solution using a Farey sequence generator by OldCigarette"""
"""https://projecteuler.net/action=redirect;post_id=96681"""
# import math
#
# def sum_over_range(n, m):
#     return (m * (m + 1) - n * (n + 1)) // 2
#
#
# def summation_sigma_1(n):
#     if n < len(summation_sigma_1.memo):
#         return summation_sigma_1.memo[n]
#     s = 0
#     max_d = int(math.sqrt(n)) if n > 0 else 1
#     next_n_d = n
#     for d in range(1, max_d):
#         n_d = next_n_d  # n // d
#         next_n_d = n // (d + 1)
#         s += d * (n_d + sum_over_range(next_n_d, n_d))
#     s += (n // max_d) * max_d
#     if n // max_d != max_d:
#         s += max_d * sum_over_range(n // (max_d + 1), n // max_d)
#     return s
#
#
# summation_sigma_1.memo = []
# summation_sigma_1.memo = [summation_sigma_1(n) for n in range(0, 50000)]
#
#
# def co_prime_generator_Farey(n):
#     # Generates all relatively prime pairs <= n
#     # Adapted from https://en.wikipedia.org/wiki/Farey_sequence
#     a, b, c, d = 0, 1, 1, n
#     while c <= n:
#         k = (n + b) // d
#         a, b, c, d = c, d, k * c - a, k * d - b
#         yield a, b
#
#
# N = int(input())
# S = summation_sigma_1(N)
# S += sum(2 * (re if re == im else re + im) * summation_sigma_1(N // (re * re + im * im)) for re, im in
#          co_prime_generator_Farey(int(math.sqrt(N))))
# print(S)

"""Very fast, O(N^3/4) solution by Min_25"""
"""https://projecteuler.net/action=redirect;post_id=237634"""
# from math import sqrt
#
# def isqrt(n, dblcutoff=1<<52):
#   if n < dblcutoff:
#     return int(sqrt(n))
#   x = int(sqrt(n * (1 + 1e-14)))
#   while True:
#     y = (x + n // x) >> 1
#     if y >= x:
#       return x
#     x = y
#
# def icbrt(n):
#   if n <= 0:
#     return 0
#
#   x = int(n ** (1. / 3.) * (1 + 1e-12))
#   while True:
#     y = (2 * x + n // (x * x)) // 3
#     if y >= x:
#       return x
#     x = y
#
# def prob153(N=10**8):
#   """
#   10 **  9: 1797231035470229962, 0.586 sec.
#   10 ** 10: 179726445633260218662, 2.140 sec.
#   10 ** 11: 17972750272542089793485, 9.971 sec.
#   10 ** 12: 1797278370292056629263518, 47.969 sec.
#   10 ** 13: 179727942749349269842849984, 256.118 sec.
#   """
#   def S(n):
#     v = isqrt(n)
#     ret = 0
#     for i in range(v, 0, -1):
#       t = n // i
#       ret += t * (2 * i + t + 1)
#     ret -= v * v * (v + 1)
#     return ret >> 1
#
#   def C(n):
#     v = isqrt(n)
#     w = isqrt(n // 2)
#     ret = 0
#     for i in range(v, w, -1):
#       t = isqrt(n - i * i)
#       ret += t * (2 * i + t + 1)
#     ret += w * w * (w + 1)
#     return ret >> 1
#
#   def sum_imaginary_numbers(N):
#     def T(n):
#       return n * (n + 1) // 2
#
#     def calc_coprime(n):
#       ret = smalls[n] if n < w else larges[N // n]
#       u = icbrt(n)
#       prev = T(isqrt(n))
#       for i in range(1, u + 1):
#         curr = T(isqrt(n // (i + 1)))
#         ret -= (prev - curr) * smalls[i]
#         prev = curr
#       for i in range(2, isqrt(n // (u + 1)) + 1):
#         d = n // (i * i)
#         ret -= i * (smalls[d] if d < w else larges[N // d])
#       return ret
#
#     v = isqrt(N)
#     w = N // v
#
#     larges = [0] + [C(N // i) for i in range(1, v + 1)]
#     smalls = [0] + [C(i) for i in range(1, w)]
#
#     for i in range(1, w):
#       smalls[i] = calc_coprime(i)
#
#     for i in range(v, 0, -1):
#       larges[i] = calc_coprime(N // i)
#
#     for i in range(1, v):
#       larges[i] -= larges[i + 1]
#     larges[v] -= smalls[w - 1]
#     for i in range(w - 2, 0, -1):
#       smalls[i+1] -= smalls[i]
#
#     ret = 0
#     for i in range(1, w):
#       if smalls[i] > 0:
#         ret += smalls[i] * S(N // i)
#     for i in range(1, v + 1):
#       ret += larges[i] * S(i)
#     return 2 * ret
#
#   ans = sum_imaginary_numbers(N) + S(N)
#   return ans
#
# print(prob153(int(input())))