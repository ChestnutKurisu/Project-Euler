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
digitOrderIndependentPrimes = {}
for i in range(1000, 10 ** 6):
    if isPrime(i, 3):
        arranged_i = ''.join(sorted(str(i)))
        if arranged_i in digitOrderIndependentPrimes:
            digitOrderIndependentPrimes[arranged_i].append(i)
        else:
            digitOrderIndependentPrimes[arranged_i] = [i]
primes = [p for p in digitOrderIndependentPrimes if len(digitOrderIndependentPrimes[p]) >= K]
primeAGPs = []
for p in primes:
    perms = digitOrderIndependentPrimes[p]
    if K == 3:
        for i in range(len(perms) - 2):
            if perms[i] >= N:
                break
            for j in range(i + 1, len(perms) - 1):
                p_k = 2 * perms[j] - perms[i]
                if p_k in perms:
                    primeAGPs.append(int(str(perms[i]) + str(perms[j]) + str(p_k)))
    if K == 4:
        for i in range(len(perms) - 3):
            if perms[i] >= N:
                break
            for j in range(i + 1, len(perms) - 2):
                d = perms[j] - perms[i]
                p_k = perms[j] + d
                p_l = p_k + d
                if p_k in perms and p_l in perms:
                    primeAGPs.append(int(str(perms[i]) + str(perms[j]) + str(p_k) + str(p_l)))
for agp in sorted(primeAGPs):
    print(agp)
