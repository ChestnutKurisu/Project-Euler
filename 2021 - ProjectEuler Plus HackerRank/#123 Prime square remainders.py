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
B = [(i, int(input())) for i in range(T)]
primes = get_primes_eratosthenes_sieve(3 * 10 ** 6)
r = [(2, 2)] + [(n, (primes[n - 1] * n * 2) % primes[n - 1] ** 2) for n in range(3, len(primes), 2)]
sorted_B = sorted(B, key=lambda x: x[1])
A = [0] * T
c = 0
k = 0
while k < len(r) and c != T:
    if r[k][1] > sorted_B[c][1]:
        A[sorted_B[c][0]] = r[k][0]
        c += 1
        k -= 1
    k += 1
for k in range(T):
    print(A[k])
