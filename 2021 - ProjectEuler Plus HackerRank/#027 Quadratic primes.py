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


primes = [0] * 100000
for j in range(2, len(primes)):
    if isPrime(j, 3):
        primes[j] = 1
N = int(input())
m = 0
(A, B) = (0, 0)
for a in range(-2 * int(N ** 0.5), 2 * int(N ** 0.5) + 1):
    for b in range(-N, N + 1):
        s = 0
        for n in range(0, N):
            if primes[n ** 2 + a * n + b]:
                s += 1
            else:
                break
        if s > m:
            m = s
            A = a
            B = b
print(A, B)
