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


def sum_div(n):
    return int(
        reduce(operator.mul, [(1 - p ** (primeCount(n, p) + 1)) / (1 - p) for p in primes if p <= n and n % p == 0],
               1) - n)


T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
N_max = max(N)
primes = []
for j in range(5000):
    if isPrime(j, 3):
        primes.append(j)
sum_of_divisors = [0] * (N_max + 1)
amicable = []
for n in range(1, N_max + 1):
    sum_of_divisors[n] = sum_div(n)
    if (sum_of_divisors[n] < n == sum_of_divisors[sum_of_divisors[n]]) or (
            sum_of_divisors[n] > n == sum_div(sum_of_divisors[n])):
        amicable.append(n)
ami_sum = [sum(i for i in amicable if i <= j) for j in amicable]
for k in range(T):
    if amicable[0] > N[k]:
        print(0)
    elif amicable[-1] < N[k]:
        print(ami_sum[-1])
    else:
        for j in range(len(amicable)):
            if amicable[j] > N[k]:
                print(ami_sum[j - 1])
                break
