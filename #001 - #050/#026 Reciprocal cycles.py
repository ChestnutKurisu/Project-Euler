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


def ord(n, p):
    for i in range(1, p):
        if pow(n, i, p) == 1:
            return i


T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
N_max = max(N)
primes = []
for j in range(N_max + 1):
    if isPrime(j, 3) and j != 2 and j != 5:
        primes.append(j)
primes.extend([p ** 2 for p in primes if p ** 2 <= N_max + 1])
primes.extend([p ** 3 for p in primes if p ** 3 <= N_max + 1])
primes = sorted(primes)
smallest = []
l = 1
for i in primes:
    k = ord(10, i)
    if k >= l:
        l = k + 1
        smallest.append(i)
for k in range(T):
    for d in reversed(smallest):
        if d < N[k]:
            print(d)
            break
