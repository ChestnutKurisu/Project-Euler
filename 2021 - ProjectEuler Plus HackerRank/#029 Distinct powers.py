N = int(input())
s = 0
c = {1: N - 1}
twos = {b for b in range(2, N + 1)}  # 2 ** b
for j in range(2, 17):
    if 2 ** j > N:
        break
    d = {j * b for b in range(2, N + 1)}  # (2 ** j) ** b
    c[j] = len(d.difference(twos))
    twos = twos.union(d)
for a in range(2, N + 1):
    base = 0
    exp = 1
    for i in range(16, 1, -1):
        if round(a ** (1 / i)) ** i == a:
            exp = i
            break
    s += c[exp]
print(s)
