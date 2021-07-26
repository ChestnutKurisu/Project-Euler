import random
from functools import reduce
import operator


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


def primeCount(n, p):
    d = 0
    while n % p == 0:
        d += 1
        n /= p
    return d


T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
N_max = max(N)
i = 1
maxd = -1
tn = []
divs = []
primes = []
for j in range(2000):
    if isPrime(j, 4):
        primes.append(j)
while maxd <= N_max:
    n = i * (i + 1) // 2
    primeFactors = [primeCount(n, p) for p in primes if n % p == 0 and p <= n]
    divisors = reduce(operator.mul, [(j + 1) for j in primeFactors], 1)
    if divisors > maxd:
        maxd = divisors
        tn.append(n)
        divs.append(divisors)
    i += 1
for k in range(T):
    for j in range(len(tn)):
        if divs[j] > N[k]:
            print(tn[j])
            break
