from itertools import accumulate, chain


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


def euler_totient(n, primes):
    prod = n
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            prod -= prod // p
    return prod


T = int(input())
a, b = zip(*[map(int, input().split()) for i in range(T)])
# https://oeis.org/A002110 - list of primorial numbers
primes = rwh_primes2(300)
primorials = list(accumulate(primes, lambda x, y: x * y))
# https://oeis.org/A060735
A060735 = (list(chain.from_iterable([[primorials[i] * j for j in range(1, primes[i + 1])] for i in range(len(primorials) - 1)])) + [primorials[-1]])[::-1]
ratios = [euler_totient(d, primes) / (d - 1) for d in A060735]
for k in range(T):
    print(A060735[binary_search_count_less_than(ratios, a[k] / b[k]) - 1])
