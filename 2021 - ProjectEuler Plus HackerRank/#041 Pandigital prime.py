import random
from itertools import permutations


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


T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
pandigital_primes = []
for n in range(1, 10):
    for p in permutations(''.join(str(i) for i in range(1, n + 1))):
        m = int(''.join(p))
        if isPrime(m, 4):
            pandigital_primes.append(m)
pandigital_primes = list(reversed(sorted(pandigital_primes)))
for k in range(T):
    for p in pandigital_primes:
        if p <= N[k]:
            print(p)
            break
    else:
        print(-1)
