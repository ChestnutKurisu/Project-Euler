import math


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
    return prime_list


def euler_totient(n, primes):
    prod = n
    for p in primes:
        if p > n:
            break
        if n % p == 0:
            prod -= prod // p
    return prod


N = int(input())
r_min = 10
n_min = 0
primes = get_primes_eratosthenes_sieve(N)
if N >= 10 ** 4:
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            n = primes[i] * primes[j]
            if n >= N:
                break
            phi_n = (primes[i] - 1) * (primes[j] - 1)
            if ''.join(sorted(str(phi_n))) != ''.join(sorted(str(n))):
                continue
            r = n / phi_n
            if r < r_min:
                r_min = r
                n_min = n
else:
    for n in range(2, N):
        phi_n = euler_totient(n, primes)
        if phi_n <= 10 ** int(math.log10(n)):
            continue
        if ''.join(sorted(str(phi_n))) != ''.join(sorted(str(n))):
            continue
        r = n / phi_n
        if r < r_min:
            r_min = r
            n_min = n
print(n_min)
