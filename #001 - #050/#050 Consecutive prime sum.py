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
    prime_sums = []
    prime_sum = 0
    for i in range(n + 1):
        if is_prime[i]:
            prime_list.append(i)
            prime_sum += i
            prime_sums.append(prime_sum)
    return is_prime, prime_list, prime_sums


isPrime, primes, primeSums = get_primes_eratosthenes_sieve(6 * 10 ** 6)
T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
for k in range(T):
    startSum = 0
    startInd = 0
    for psInd in range(1, len(primeSums)):
        if primeSums[psInd] > N[k]:
            startInd = psInd - 1
            break
    for i in range(startInd, -1, -1):
        startSum = primeSums[i]
        foundFlag = False
        for j in range(startInd - i + 2):
            if (startSum < 6 * 10 ** 6 and isPrime[startSum]) or is_prime_miller_rabin(startSum, 4):
                print(startSum, i + 1)
                foundFlag = True
                break
            startSum = startSum - primes[j] + primes[j + i + 1]
            if startSum > N[k]:
                break
        if foundFlag:
            break
