def A002487(n):
    if n < 2:
        return n
    if n & 1:
        b = (n - 1) // 2
        if b not in a:
            a[b] = A002487(b)
        if b + 1 not in a:
            a[b + 1] = A002487(b + 1)
        return a[b] + a[b + 1]
    else:
        b = n // 2
        if b not in a:
            a[b] = A002487(b)
        return a[b]


a = {2 ** i: 1 for i in range(90)}
print(A002487(int(input()) + 1))
