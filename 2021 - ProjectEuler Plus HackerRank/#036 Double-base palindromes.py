def base(n, b):
    if n == 0:
        return '0'
    c = ''
    while n != 0:
        c += str(n % b)
        n //= b
    return c[::-1]


N, K = map(int, input().split())
s = 0
for i in range(1, N):
    si = str(i)
    si_b = base(i, K)
    if si == si[::-1] and si_b == si_b[::-1]:
        s += i
print(s)
