import math

T = int(input())
N = [0] * T
L = [0] * T
for k in range(T):
    N[k], L[k] = map(int, input().split())
fact = {i: math.factorial(i) for i in range(10)}
loop_length = {1: 1, 2: 1, 145: 1, 169: 3, 363601: 3, 1454: 3, 871: 2, 45361: 2, 872: 2, 45362: 2, 40585: 1}
N_max = max(N)
chain_length = {i: [] for i in range(61)}
chain_length_list = [0] * (10 ** 6 + 1)
for n in loop_length:
    chain_length_list[n] = loop_length[n]
for n in range(N_max + 1):
    if chain_length_list[n] != 0:
        chain_length[chain_length_list[n]].append(n)
        continue
    m = sum(fact[int(i)] for i in str(n))
    nit = 1
    while m != n:
        if m < len(chain_length_list) and chain_length_list[m] != 0:
            nit += chain_length_list[m]
            break
        else:
            nit += 1
            m = sum(fact[int(i)] for i in str(m))
    chain_length[nit].append(n)
    chain_length_list[n] = nit
for k in range(T):
    l = [str(n) for n in chain_length[L[k]] if n <= N[k]]
    if len(l) == 0:
        print(-1)
    else:
        print(' '.join(l))
