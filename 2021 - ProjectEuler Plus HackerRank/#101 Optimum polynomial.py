def evaluate_polynomial(x, B):
    B_x = (x * B[-1]) % (10 ** 9 + 7)
    for i in range(2, len(B)):
        B_x = (x * (B[-i] + B_x)) % (10 ** 9 + 7)
    return B[0] + B_x


N = int(input())
A = list(map(lambda x: int(x) % (10 ** 9 + 7), input().split()))
Y = [evaluate_polynomial(n, A) % (10 ** 9 + 7) for n in range(1, N + 1)]
FITS = []
binomial = [1]
for n in range(1, N + 1):
    FITS.append((-1) ** (1 + n & 1) * sum((-1) ** (k & 1) * binomial[k] * Y[k] for k in range(n)) % (10 ** 9 + 7))
    binomial = [1] + [(binomial[i] + binomial[(i + 1) % n]) % (10 ** 9 + 7) for i in range(n)]
print(*FITS)
