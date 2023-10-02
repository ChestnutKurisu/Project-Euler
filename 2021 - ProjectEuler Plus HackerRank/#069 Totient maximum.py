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


T = int(input())
N = [int(input()) for i in range(T)]
primes = get_primes_eratosthenes_sieve(10 ** 3)
prod_primes = []
prod = 1
for p in primes:
    if prod > 10 ** 18:
        break
    prod *= p
    prod_primes.append(prod)
for k in range(T):
    for i in range(len(prod_primes)):
        if prod_primes[i] >= N[k]:
            print(prod_primes[i - 1])
            break
