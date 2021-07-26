T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
for k in range(T):
    n = N[k]
    n2 = n // 2
    print((n ** 2 + n2 * (4 * n ** 2 + 6 * n + 6) + 8 * n2 * (n2 + 1) * (2 * n2 + 1) // 3 - (8 * n + 6) * n2 * (
                n2 + 1)) % (10 ** 9 + 7))
