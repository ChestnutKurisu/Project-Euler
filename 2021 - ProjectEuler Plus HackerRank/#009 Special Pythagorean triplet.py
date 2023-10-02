T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
for k in range(T):
    max_prod = -1
    for a in range(1, N[k] // 2):
        b = (N[k] * (2 * a - N[k])) / (2 * (a - N[k]))
        prod = a * b * (a ** 2 + b ** 2) ** 0.5
        if b == int(b) and prod > max_prod:
            max_prod = int(prod)
    print(max_prod)
