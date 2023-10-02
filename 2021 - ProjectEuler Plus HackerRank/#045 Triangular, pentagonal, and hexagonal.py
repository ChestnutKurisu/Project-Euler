N, a, b = map(int, input().split())
if a == 3 and b == 5:
    for n in range(1, int(((24 * N + 1) ** 0.5 + 1) / 6)):
        if (((12 * n ** 2 - 4 * n + 1) ** 0.5 - 1) / 2).is_integer():
            print(n * (3 * n - 1) >> 1)
if a == 5 and b == 6:
    for n in range(1, int(((8 * N + 1) ** 0.5 + 1) / 4)):
        if (((48 * n ** 2 - 24 * n + 1) ** 0.5 + 1) / 6).is_integer():
            print(n * (2 * n - 1))

# projecteuler.net version
# Use a, b = 5, 6 since every hexagonal number is also triangular
