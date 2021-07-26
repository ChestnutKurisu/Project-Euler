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


def cycles(n):
    n = str(n)
    return [int(n[i:] + n[:i]) for i in range(len(n))]


N = int(input())
primes = [0] * 10 ** 6
for i in range(2, len(primes)):
    if isPrime(i, 3):
        primes[i] = 1
s = 0
for i in range(1, N):
    flag = 1
    for i in cycles(i):
        if not primes[i]:
            flag = 0
            break
    if flag:
        s += i  # 1
print(s)
