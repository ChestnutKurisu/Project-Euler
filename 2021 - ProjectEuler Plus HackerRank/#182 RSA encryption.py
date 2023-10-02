import operator
from functools import reduce
from math import gcd
import random


# Compute modular inverse of a (mod b) via extended_euclidean_algorithm(a, b)[1] % b
def extended_euclidean_algorithm(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean_algorithm(b % a, a)
        return gcd, y - (b // a) * x, x


# Pg. 22 of http://www.personal.psu.edu/rcv4/CENT.pdf
def chinese_remainder_theorem(linear_congruences):
    # Solves the system of linear congruences x = c_i (mod m_i)
    M = reduce(operator.mul, [m_i for c_i, m_i in linear_congruences])
    result = 0
    for c_i, m_i in linear_congruences:
        M_i = M // m_i
        GCD, x, y = extended_euclidean_algorithm(m_i, M_i)
        result += c_i * y * M_i
    return M, result % M


# Faster modular inverses of a (mod b) than extended_euclidean_algorithm; requires gcd(a, b) = 1
def mul_inv(a, b):
    if b == 1:
        return 1
    b_0 = b
    x_0, x_1 = 0, 1
    while a > 1:
        x_0, x_1 = x_1 - (a // b) * x_0, x_0
        a, b = b, a % b
    if x_1 < 0:
        x_1 += b_0
    return x_1


def miller_rabin(n, allow_probable=False):
    """Deterministic Miller-Rabin algorithm for primes ~< 3.32e24. Uses numerical analysis results to return whether or
    not the passed number is prime. If the passed number is above the upper limit, and allow_probable is True, then a
    return value of True indicates that n is probably prime. This test does not allow False negatives; a return value
    of False is ALWAYS composite.
    Parameters: n (int) - The integer to be tested. Since we usually care if a number is prime, n < 2 returns False
    instead of raising a ValueError; allow_probable: bool, default False, Whether or not to test n above the upper bound
    of the deterministic test.
    Raises: ValueError
    Reference: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test"""
    if n == 2:
        return True
    if not n % 2 or n < 2:
        return False
    if n > 5 and n % 10 not in (1, 3, 7, 9):
        return False
    if n > 3317044064679887385961981 and not allow_probable:
        raise ValueError(
            "Warning: upper bound of deterministic test is exceeded. "
            "Pass allow_probable=True to allow probabilistic test. "
            "A return value of True indicates a probable prime."
        )
    bounds = [2047, 1373653, 25326001, 3215031751, 2152302898747, 3474749660383, 341550071728321, 1,
              3825123056546413051, 1, 1, 318665857834031151167461, 3317044064679887385961981]
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    plist = primes[:]
    for idx, _p in enumerate(bounds, 1):
        if n < _p:
            plist = primes[:idx]
            break
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for prime in plist:
        pr = False
        for r in range(s):
            m = pow(prime, d * 2 ** r, n)
            if (r == 0 and m == 1) or ((m + 1) % n == 0):
                pr = True
                break
        if pr:
            continue
        return False
    return True


# https://github.com/zhangbo2008/python_algorithm2/blob/c53669703b957a079f100c12711f86f5fc2f9389/algorithms/factorization/pollard_rho.py
def pollard_rho_prime_factorization(x):
    def f(x):
        return x * x + 1

    def rho(n, x1=2, x2=2):
        if n % 2 == 0:
            return 2
        i = 0
        while True:
            x1 = f(x1) % n
            x2 = f(f(x2)) % n
            divisor = gcd(abs(x1 - x2), n)
            i += 1
            if divisor != 1:
                break
            if i > 500:
                x1 = random.randint(1, 10)
                x2 = random.randint(1, 10)
                i = 0
        return divisor

    def pollard_rho_rec(x, factors):
        if x == 1:
            return

        if miller_rabin(x):
            factors.append(x)
            return

        divisor = rho(x, random.randint(1, 10), random.randint(1, 10))
        pollard_rho_rec(divisor, factors)
        pollard_rho_rec(x // divisor, factors)

    if x == 1 or x == 0:
        return [x]
    factors = []
    pollard_rho_rec(x, factors)
    return factors


def decimal_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n != 0:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


p, q = map(int, input().split())
n = p * q
phi = (p - 1) * (q - 1)
carmichael_lambda = phi // gcd(p - 1, q - 1)
lambda_prime_factors = sorted(set(pollard_rho_prime_factorization(carmichael_lambda)).difference({2, 3}))
mod = phi % 24
h = 0
if mod == 12:
    h = 6
elif mod == 16:
    h = 4
elif mod == 0:
    h = 12
else:
    h = 2
# Using inclusion-exclusion principle for summing (hk - 1) over k = 1, ..., floor(phi/h), hk - 1 = 0, 1 (mod p)
# where p cycles over the factors of lambda
# See https://projecteuler.net/action=quote;post_id=372624
L = phi // h
S = L * (h // 2 * L + h // 2 - 1)
# Storing solutions to hk - 1 = 0 (mod p) and hk - 1 = 1 (mod p)
pf_solutions_dict = dict()
for p in lambda_prime_factors:
    inverse_h_mod_p = mul_inv(h, p)
    pf_solutions_dict[p] = [inverse_h_mod_p, 2 * inverse_h_mod_p]
for k in range(1, 3 ** len(lambda_prime_factors)):
    k_3 = decimal_to_base(k, 3)[::-1]
    system_of_congruences = []
    for i in range(len(k_3)):
        if k_3[i] != 0:
            p = lambda_prime_factors[i]
            system_of_congruences.append((pf_solutions_dict[p][k_3[i] - 1], p))
    # Solution for e = r (mod M) => e = Mq + r
    M, r = chinese_remainder_theorem(system_of_congruences)
    i = len(k_3) - k_3.count(0)
    N = L // M
    S += (-1) ** (i & 1) * (h // 2 * M * (N - 1) * N + h * N * r - N)
print(S % (10 ** 9 + 7))
