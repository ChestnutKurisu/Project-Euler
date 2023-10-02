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


N = int(input())
side_length = 1
primeCount = 0
while True:
    for k in [side_length ** 2 + (side_length + 1) * i for i in range(1, 5)]:
        if is_prime_miller_rabin(k, 3):
            primeCount += 1
    if primeCount / (5 + (side_length - 1) * 2) * 100 < N:
        print(side_length + 2)
        break
    side_length += 2
