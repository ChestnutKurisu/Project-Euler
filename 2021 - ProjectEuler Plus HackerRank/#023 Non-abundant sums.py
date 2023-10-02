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


def primeCount(n, p):
    d = 0
    while n % p == 0:
        d += 1
        n /= p
    return d


def isAbundant(n):
    s = 1
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            s *= (1 - p ** (primeCount(n, p) + 1)) / (1 - p)
        if s > 2 * n:
            return True
    return False


T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
N_max = max(N)
abundant = [0] * min(N_max + 1, 28124)
abundants = []
primes = []
for j in range(N_max // 2 + 1):
    if isPrime(j, 3):
        primes.append(j)
for i in range(1, min(N_max + 1, 28124)):
    if isAbundant(i):
        abundant[i] = 1
        abundants.append(i)
for k in range(T):
    if N[k] > 28123:
        print('YES')
        continue
    flag = False
    for j in abundants:
        if j > N[k] // 2:
            break
        if abundant[N[k] - j]:
            print('YES')
            flag = True
            break
    if not flag:
        print('NO')

# s = 0
# for i in range(28124):
#     flag = False
#     for j in abundants:
#         if j > i // 2:
#             break
#         if abundant[i - j]:
#             flag = True
#             break
#     if not flag:
#         s += i
# print(s)
