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


# projecteuler.net version
# N = [i for i in range(3, 10000, 2) if not isPrime(i, 4)]
# T = len(N)

T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
N_max = max(N)
primes = []
for i in range(3, N_max):
    if isPrime(i, 4):
        primes.append(i)
for k in range(T):
    ncomb = 0
    for p in primes:
        if p > N[k]:
            break
        if (((N[k] - p) // 2) ** 0.5).is_integer():
            ncomb += 1
    # if ncomb == 0:
    #     print(N[k])
    print(ncomb)
