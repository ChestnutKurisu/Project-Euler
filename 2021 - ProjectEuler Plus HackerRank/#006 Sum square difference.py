T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
for i in range(T):
    k = N[i]
    print(-k * (k + 1) * (2 * k + 1) // 6 + k ** 2 * (k + 1) ** 2 // 4)
