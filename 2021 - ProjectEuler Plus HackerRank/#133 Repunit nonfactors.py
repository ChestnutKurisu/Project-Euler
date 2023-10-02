from functools import reduce
from itertools import accumulate
from math import sqrt, gcd
import random


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


def get_primes_eratosthenes_sieve(n):
    is_prime = [1] * (n + 1)
    p = 2
    is_prime[0] = 0
    is_prime[1] = 0
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * 2, n + 1, p):
                is_prime[i] = 0
        p += 1
    prime_list = []
    for i in range(n + 1):
        if is_prime[i]:
            prime_list.append(i)
    return is_prime


def rwh_primes2(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = bytearray([True]) * (n // 3)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = bytearray([False]) * ((n // 6 - k * k // 6 - 1) // k + 1)
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = bytearray([False]) * (
                    (n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) // k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]


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

        if (x <= 10 ** 6 and is_prime[x]) or miller_rabin(x):
            factors.append(x)
            return

        divisor = rho(x, random.randint(1, 10), random.randint(1, 10))
        pollard_rho_rec(divisor, factors)
        pollard_rho_rec(x // divisor, factors)

    if x == 1 or x == 0:
        return [x]
    factors = []
    pollard_rho_rec(x, factors)
    return [(f, factors.count(f)) for f in set(factors)]


def divisor_list(n):
    # https://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
    factors = pollard_rho_prime_factorization(n)
    num_factors = len(factors)
    f = [0] * num_factors
    while True:
        yield reduce(lambda x, y: x * y, [factors[x][0] ** f[x] for x in range(num_factors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= num_factors:
                return


def divisor_list_small(n):
    divisors = []
    for d in range(1, int(sqrt(n)) + 1):
        if n % d == 0:
            divisors.append(d)
            if d ** 2 != n:
                divisors.append(n // d)
    return sorted(divisors)


def A(n):
    # https://math.stackexchange.com/questions/472404/repunit-divisibility
    if n == 1:
        return 1
    # Assuming n = p, where p is prime
    phi = 6 * (n - 1)
    phi_divisors = sorted(divisor_list(phi) if n > 10 ** 6 else divisor_list_small(phi))
    for d in phi_divisors:
        if pow(10, d, 9 * n) == 1:
            return d


def is_divisor_of_10_to_n(m):
    while m % 2 == 0:
        m //= 2
    while m % 5 == 0:
        m //= 5
    return m == 1


def binary_search_count_less_than(arr, key):
    left = 0
    right = len(arr) - 1
    count = 0
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] < key:
            count = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return count


is_prime = get_primes_eratosthenes_sieve(10 ** 6)
T = int(input())
L = [int(input()) for k in range(T)]
L_max = max(L)
primes = rwh_primes2(L_max)
primes_sum = list(accumulate(primes))
factor_primes = [p for p in primes[3:] if is_divisor_of_10_to_n(A(p))]
# Lookup table for the last two test cases on HackerRank
# factor_primes = [0, 11, 17, 41, 73, 101, 137, 251, 257, 271, 353, 401, 449, 641, 751, 1201, 1409, 1601, 3541, 4001, 4801, 5051, 9091, 10753, 15361, 16001, 19841, 21001, 21401, 24001, 25601, 27961, 37501, 40961, 43201, 60101, 62501, 65537, 69857, 76001, 76801, 160001, 162251, 163841, 307201, 453377, 524801, 544001, 670001, 952001, 976193, 980801, 1146881, 1378001, 1514497, 1610501, 1634881, 1676321, 1920001, 2800001, 3072001, 5070721, 5767169, 5882353, 6144001, 6187457, 6576001, 6600001, 7019801, 8253953, 8257537, 9011201, 12600001, 16384001, 18453761, 18750001, 21408001, 26214401]
factor_primes_sum = list(accumulate(factor_primes))
for k in range(T):
    print(primes_sum[binary_search_count_less_than(primes, L[k]) - 1] - factor_primes_sum[
        binary_search_count_less_than(factor_primes, L[k]) - 1] if L[k] >= 3 else 0)
