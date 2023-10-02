def binomial(n, r):
    if not 0 <= r <= n:
        return 0
    b = 1
    m = min(r, n - r)
    for k in range(m):
        b *= n
        b //= k + 1
        n -= 1
    return b


N, K = map(int, input().split())
c = 0
for n in range(1, N + 1):
    r = 0
    while r <= n // 2:
        if binomial(n, r) > K:
            c += n - 2 * r + 1
            break
        r += 1
print(c)
