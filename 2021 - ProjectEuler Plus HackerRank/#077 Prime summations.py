import random


def is_prime_miller_rabin(n, k):
    def miller_rabin_test(d, m):
        a = 2 + random.randint(1, m - 4)

        def modular_exp(x, y, p):
            res = 1
            x = x % p
            while y > 0:
                if y % 2 == 1:
                    res = (res * x) % p
                y = y >> 1
                x = (x * x) % p
            return res

        x = modular_exp(a, d, m)
        if x == 1 or x == m - 1:
            return True
        while d != m - 1:
            x = (x * x) % m
            d *= 2
            if x == 1:
                return False
            if x == m - 1:
                return True
        return False

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
# projecteuler.net version
# T = 10 ** 4
# N = list(range(1, 10 ** 4 + 1))
N_max = max(N)
sum_ways = [0] * (N_max + 1)
primes = []
for i in range(2, N_max + 1):
    if is_prime_miller_rabin(i, 3):
        primes.append(i)
for p in primes:
    sum_ways[p] += 1
    for i in range(p, N_max + 1):
        sum_ways[i] += sum_ways[i - p]
for k in range(T):
    # if sum_ways[N[k]] > 5000:
    #     print(N[k])
    #     break
    print(sum_ways[N[k]])
