import math


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


def primes_in_range(low, high, prime_sieve):
    prime_list = prime_sieve(int(math.sqrt(high)) + 1)
    segmented_sieve = bytearray([True]) * (high - low + 1)
    for p in prime_list:
        lower = low // p
        if lower <= 1:
            lower = p + p
        elif low % p != 0:
            lower = lower * p + p
        else:
            lower = lower * p
        for j in range(lower, high + 1, p):
            segmented_sieve[j - low] = False
    for k in range(low, high + 1):
        if segmented_sieve[k - low]:
            yield k


# def segmented_sieve_primes(n, simple_prime_sieve):
#     limit = int(math.floor(math.sqrt(n)) + 1)
#     prime_list = simple_prime_sieve(limit)
#     for p in prime_list:
#         yield p
#     low = limit
#     high = limit * 2
#     while low < n:
#         if high >= n:
#             high = n
#         mark = bytearray([True]) * limit
#         for i in range(len(prime_list)):
#             lower_limit = int(math.floor(low / prime_list[i]) * prime_list[i])
#             if lower_limit < low:
#                 lower_limit += prime_list[i]
#             for j in range(lower_limit, high, prime_list[i]):
#                 mark[j - low] = False
#         for i in range(low, high):
#             if mark[i - low]:
#                 yield i
#         low = low + limit
#         high = high + limit


# Faster modular inverses of a (mod b) than extended_euclidean_algorithm; requires gcd(a, b) = 1 (satisfied because p_2 > 5 and so gcd(100, p_2) = 1)
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


def binary_search_count_less_than_equal_to(arr, key):
    left = 0
    right = len(arr) - 1
    count = 0
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] <= key:
            count = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return count


def S(p_1, p_2):
    n = len(str(p_1))
    return ((p_1 * pow(p_2, 2 ** (n + 1) * 5 ** (n - 1) - 1, 10 ** n)) % (10 ** n)) * p_2


T = int(input())
L, R = [0] * T, [0] * T
for k in range(T):
    L[k], R[k] = map(int, input().split())
for k in range(T):
    primes = list(primes_in_range(L[k], R[k] + 1000, rwh_primes2))
    print(sum(S(primes[i], primes[i + 1]) for i in range(0, binary_search_count_less_than_equal_to(primes, R[k]))))
