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


T = int(input())
N = [int(input()) for i in range(T)]
primes = rwh_primes2(5 * 10 ** 7)
for k in range(T):
    semi_primes = 0
    primes_temp = primes
    while len(primes_temp) != 0:
        p = primes_temp[0]
        for j in range(len(primes_temp) - 1, -1, -1):
            if p * primes_temp[j] < N[k]:
                primes_temp = primes_temp[:j + 1]
                break
            if j == 0:
                primes_temp = []
        semi_primes += len(primes_temp)
        primes_temp = primes_temp[1:]
    print(semi_primes)
