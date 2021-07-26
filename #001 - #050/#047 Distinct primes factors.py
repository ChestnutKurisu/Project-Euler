import random


def modular_exp(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y % 2 == 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def miller_rabin_test(d, n):
    a = 2 + random.randint(1, n - 4)
    x = modular_exp(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False


def isPrime(n, k):
    if n <= 1 or n == 4:
        return False
    if n == 2 or n == 3:
        return True
    d = n - 1
    while d % 2 == 0:
        d //= 2
    for i in range(k):
        if not miller_rabin_test(d, n):
            return False
    return True


N, K = map(int, input().split())
primes = []
for i in range(1, N + 1):
    if isPrime(i, 3):
        primes.append(i)
ndpm = [0] * (N + K)
for p in primes:
    for k in range(1, (N + K - 1) // p + 1):
        ndpm[k * p] += 1
for n in [j for j in range(N + 1) if ndpm[j] == K]:
    if [ndpm[j] for j in range(n + 1, n + K)] == [K] * (K - 1):
        print(n)
