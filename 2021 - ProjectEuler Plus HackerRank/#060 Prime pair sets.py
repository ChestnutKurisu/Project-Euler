import random
from itertools import combinations


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


def get_primes_eratosthenes_sieve(n):
    is_prime = [1] * (n + 1)
    p = 2
    is_prime[0] = 0
    is_prime[1] = 0
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * 2, n + 1, p):
                is_prime[i] = 0
        p += 1
    prime_list = []
    for i in range(n + 1):
        if is_prime[i]:
            prime_list.append(i)
    return is_prime, prime_list


def check_prime(p):
    return (p <= 10 ** 6 and is_prime[p]) or is_prime_miller_rabin(p, 3)


N, K = map(int, input().split())
is_prime, prime_list = get_primes_eratosthenes_sieve(10 ** 6)
prime_list = [p for p in prime_list if p <= N]
primes = {p: set() for p in prime_list}
prime_set_sums = []
for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        p_1, p_2 = prime_list[i], prime_list[j]
        if check_prime(int(str(p_1) + str(p_2))) and check_prime(int(str(p_2) + str(p_1))):
            primes[p_1].add(p_2)
for p_1 in primes:
    for p_2 in primes[p_1]:
        for t in combinations(primes[p_1].intersection(primes[p_2]), K - 2):
            flag = True
            t = sorted(t)
            for i in range(len(t)):
                for j in range(i + 1, len(t)):
                    p_3, p_4 = t[i], t[j]
                    if p_4 not in primes[p_3]:
                        flag = False
                        break
            if flag:
                prime_set_sums.append(sum((p_1, p_2, *t)))
for s in sorted(prime_set_sums):
    print(s)
