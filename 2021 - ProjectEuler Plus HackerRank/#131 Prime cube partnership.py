import math


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


# Implementing antonio's algorithm using Tonelli-Shanks algorithm and a cuban sieve
# from https://projecteuler.net/action=redirect;post_id=244732
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


def extended_euclidean_algorithm(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean_algorithm(b % a, a)
        return gcd, y - (b // a) * x, x


# Via Euler's criterion
def legendre(a, p):
    return pow(a, (p - 1) // 2, p)


def tonelli_shanks(n, p):
    if legendre(n, p) != 1:
        return False
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r


T = int(input())
L = [int(input()) for i in range(T)]
L_max = max(L)
primes = rwh_primes2(int(math.sqrt(L_max)))[1:]
cuban_sieve = [True] * int((math.sqrt(12 * L_max - 3) + 3) / 6)
for p in primes:
    minus_3_inverse_mod_p = -extended_euclidean_algorithm(-3, p)[1]
    if minus_3_inverse_mod_p < 0:
        minus_3_inverse_mod_p += p
    n = minus_3_inverse_mod_p
    r = tonelli_shanks(n, p)
    if not r:
        continue
    for i in [(r - 1) // 2 if r & 1 else ((r - 1) * (p + 1) // 2) % p,
              (p - r - 1) // 2 if (p - r) & 1 else ((p - r - 1) * (p + 1) // 2) % p]:
        while i < len(cuban_sieve):
            if 3 * i * (i + 1) + 1 > p:
                cuban_sieve[i] = False
            i += p
cuban_primes = [3 * i ** 2 + 3 * i + 1 for i in range(1, len(cuban_sieve)) if cuban_sieve[i]]
for k in range(T):
    print(binary_search_count_less_than(cuban_primes, L[k]))
