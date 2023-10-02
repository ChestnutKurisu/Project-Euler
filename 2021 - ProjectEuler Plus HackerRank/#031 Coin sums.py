T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
N_max = max(N)
coins = [1] * (N_max + 1)
den = [1, 2, 5, 10, 20, 50, 100, 200]
# coins counts the number ways to make N with denominations at most d
for d in den:
    if d == 1:
        continue
    for i in range(d, N_max + 1):
        coins[i] += coins[i - d]
for k in range(T):
    print(coins[N[k]] % (10 ** 9 + 7))
