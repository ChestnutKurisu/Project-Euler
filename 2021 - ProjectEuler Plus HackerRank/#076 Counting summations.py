T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
N_max = max(N)
sum_ways = [1] * (N_max + 1)
for n in range(2, N_max + 1):
    for i in range(n, N_max + 1):
        sum_ways[i] += sum_ways[i - n]
for k in range(N_max + 1):
    sum_ways[k] -= 1
for k in range(T):
    print(sum_ways[N[k]] % (10 ** 9 + 7))
