from itertools import permutations


def div(n):
    for i in range(N - 2):
        if int(n[i + 1:i + 4]) % primes[i] != 0:
            return False
    return True


N = int(input())
primes = [2, 3, 5, 7, 11, 13, 17]
print(sum(int(n) for n in [''.join(p) for p in permutations(''.join(str(i) for i in range(N + 1)))] if div(n)))