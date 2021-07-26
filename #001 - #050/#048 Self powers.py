N = int(input())
print(sum(pow(n, n, 10 ** 10) for n in range(1, N + 1)) % 10 ** 10)
