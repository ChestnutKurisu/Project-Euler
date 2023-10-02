def euler_totient_list(n):
    """
      Function to find SPF (Smallest Prime Factor) for all numbers < N
      Time complexity = O(n log(log(n)))
      See also: https://github.com/leduckhai/Awesome-Competitive-Programming/blob/main/Mathematics/Sieve_SPF.ipynb,
      https://www.geeksforgeeks.org/prime-factorization-using-sieve-olog-n-multiple-queries/
    """

    from math import ceil, sqrt

    def Sieve_SPF(N):
        # Stores the smallest prime factor for every number
        # Mark the smallest prime factor for every odd number to be itself and every even number to be 2
        SPF_list = [0, 1] + [i if i & 1 else 2 for i in range(2, N + 1)]
        # Follow a Sieve of Eratosthenes like algorithm to fill SPF_list
        for p in range(3, ceil(sqrt(N + 1)), 2):
            # Check if i is prime
            if SPF_list[p] == p:
                # Mark SPFs for all numbers divisible by i
                for i in range(p * p, N + 1, p):
                    # Mark SPFs[i] if not previously marked
                    if SPF_list[i] == i:
                        SPF_list[i] = p
        return SPF_list

    '''
      Function to return prime factorization by dividing by SPF at every step
      Time complexity = O(log(n))
    '''

    def PrimeFactorization_SPF(x, SPF_list):
        # Set of all prime factors of x
        PF_list = set()
        while x != 1:
            PF_list.add(SPF_list[x])
            x = x // SPF_list[x]
        return PF_list

    SPF_list = Sieve_SPF(n)
    phi_list = [0]
    for n in range(1, n + 1):
        PF_list = PrimeFactorization_SPF(n, SPF_list)
        phi = n
        for p in PF_list:
            phi -= phi // p
        phi_list.append(phi)
    return phi_list


T = int(input())
N = [int(input()) for i in range(T)]
N_max = max(N)
card_F = [0] * (N_max + 1)
card_F[0] = 1
totient_list = euler_totient_list(N_max)
for i in range(1, N_max + 1):
    card_F[i] = card_F[i - 1] + totient_list[i]
for k in range(T):
    print(card_F[N[k]] - 2)
