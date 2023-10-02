import math
import operator
from functools import reduce
from math import gcd, log
import random


def fast_miller_rabin(n, use_probabilistic=False, tolerance=30):
    """
    Tests whether a number is prime using a deterministic version of the Miller-
    Rabin primality test. Optionally tests whether the specified number is a
    prime probabilistically up to a given tolerance using the regular version of
    the Miller-Rabin test. If the number is greater than 10^36, then all witnesses
    in the range [2, 2*log(n)*log(log(n))] are tested. However, this is conjectural
    and only heuristic evidence exists for it. To certify that a number is actually
    prime, one needs to test all witnesses in the range [2, 2*log(n)^2]. However,
    this is generally quite slow.
    Arguments:
        n (:int) - the integer to be tested
        use_probabilistic (:bool) - flag to indicate whether to use the regular
                                   version of the Miller-Rabin primality test
        tolerance (:int) - number of trials to be used to test primality
    Returns:
        True if 'n' is prime (or probably prime) and False otherwise
    References:
        - Francky from the PE Forums
        - https://miller-rabin.appspot.com/
        - https://en.wikipedia.org/wiki/Miller-Rabin_primality_test
    """
    firstPrime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    # Determine bases for deterministic Miller-Rabin test
    if n >= 10 ** 36:
        log_n = math.log(n)
        if not use_probabilistic:
            w = range(2, 2 * int(log_n * log(log_n) / log(2)))
        else:
            w = range(tolerance)
    elif n >= 1543267864443420616877677640751301:
        w = firstPrime[:20]
    elif n >= 564132928021909221014087501701:
        w = firstPrime[:18]
    elif n >= 59276361075595573263446330101:
        w = firstPrime[:16]
    elif n >= 6003094289670105800312596501:
        w = firstPrime[:15]
    elif n >= 3317044064679887385961981:
        w = firstPrime[:14]
    elif n >= 318665857834031151167461:
        w = firstPrime[:13]
    elif n >= 3825123056546413051:
        w = firstPrime[:12]
    # [2, 3, 5, 7, 11, 13, 17, 19, 23]
    elif n >= 341550071728321:
        w = firstPrime[:9]
    # [2, 3, 5, 7, 11, 13, 17]
    elif n >= 3474749660383:
        w = firstPrime[:7]
    elif n >= 2152302898749:
        w = firstPrime[:6]
    # [2, 3, 5, 7, 11, 13]
    elif n >= 4759123141:
        w = firstPrime[:5]
    # [2, 3, 5, 7, 11]
    elif n >= 9006403:
        w = [2, 7, 61]
    elif n >= 489997:
        # Some Fermat stuff
        if n & 1 and n % 3 and n % 5 and n % 7 and n % 11 and n % 13 and n % 17 and n % 19 and n % 23 and n % 29 and n % 31 and n % 37 and n % 41 and n % 43 and n % 47 and n % 53 and n % 59 and n % 61 and n % 67 and n % 71 and n % 73 and n % 79 and n % 83 and n % 89 and n % 97 and n % 101:
            hn, nm1 = n >> 1, n - 1
            p = pow(2, hn, n)
            if p == 1 or p == nm1:
                p = pow(3, hn, n)
                if p == 1 or p == nm1:
                    p = pow(5, hn, n)
                    return p == 1 or p == nm1
        return False
    elif n >= 42799:
        return n & 1 and n % 3 and n % 5 and n % 7 and n % 11 and n % 13 and n % 17 and n % 19 and n % 23 and n % 29 and n % 31 and n % 37 and n % 41 and n % 43 and pow(2, n - 1, n) == 1 and pow(5, n - 1, n) == 1
    elif n >= 841:
        return n & 1 and n % 3 and n % 5 and n % 7 and n % 11 and n % 13 and n % 17 and n % 19 and n % 23 and n % 29 and n % 31 and n % 37 and n % 41 and n % 43 and n % 47 and n % 53 and n % 59 and n % 61 and n % 67 and n % 71 and n % 73 and n % 79 and n % 83 and n % 89 and n % 97 and n % 101 and n % 103 and pow(2, n - 1, n) == 1
    elif n >= 25:
        return n & 1 and n % 3 and n % 5 and n % 7 and n % 11 and n % 13 and n % 17 and n % 19 and n % 23
    elif n >= 4:
        return n & 1 and n % 3
    else:
        return n > 1
    if not (n & 1 and n % 3 and n % 5 and n % 7 and n % 11 and n % 13 and n % 17
            and n % 19 and n % 23 and n % 29 and n % 31 and n % 37 and n % 41 and n % 43
            and n % 47 and n % 53 and n % 59 and n % 61 and n % 67 and n % 71 and n % 73
            and n % 79 and n % 83 and n % 89):
        return False
    # Miller-Rabin
    s = 0
    d = n - 1
    while not d & 1:
        d >>= 1
        s += 1
    for k in w:
        # Pick a random witness if probabilistic
        if use_probabilistic:
            p = random.randint(2, n - 2)
        else:
            p = k
        x = pow(p, d, n)
        if x == 1:
            continue
        for _ in range(s):
            if x + 1 == n:
                break
            x = x * x % n
        else:
            return False
    return True


def pollard_rho_prime_factorization(x):
    # https://github.com/zhangbo2008/python_algorithm2/blob/c53669703b957a079f100c12711f86f5fc2f9389/algorithms/factorization/pollard_rho.py
    # https://github.com/MaitriVaghela/Advanced-Cryptography/blob/34d49d90a7a7013c7a2ad02dafb9a5bd964b8397/Pollard-RHO%20factoring.py
    # https://stackoverflow.com/questions/16424369/python-pollard-p-1-factorization
    def pollard_rho_brent(n, seed=2, f=lambda x: x ** 2 + 1):
        if n & 1 == 0:
            return 2
        if n % 5 == 0:
            return 5
        x, y, p = seed, seed, 1
        count, z = 1, 1
        k = 10
        while p == 1:
            x = f(x) % n
            y = f(f(y)) % n
            z = (z * (x - y)) % n
            count = count + 1
            if (count % k) != 0:
                p = gcd(z, n)
                if 1 < p and p < n:
                    break
                else:
                    z = 1
        return p

    def pollard_rho_rec(x, factors):
        if x == 1:
            return

        if fast_miller_rabin(x):
            factors.append(x)
            return

        divisor = pollard_rho_brent(x, random.randint(1, 1000))
        pollard_rho_rec(divisor, factors)
        pollard_rho_rec(x // divisor, factors)

    if x == 1 or x == 0:
        return [x]
    factors = []
    pollard_rho_rec(x, factors)
    return [(f, factors.count(f)) for f in set(factors)]


T = int(input())
N = [int(input()) for k in range(T)]
for k in range(T):
    factor_list = pollard_rho_prime_factorization(N[k])
    print((reduce(operator.mul, [2 * multiplicity + 1 for p, multiplicity in factor_list]) + 1) // 2)
