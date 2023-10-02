def collatz_fill(n):
    if n < 5 * 10 ** 6 and chain_size[n] != 0:
        return chain_size[n]
    if n & 1:
        comp = 1 + (
            chain_size[3 * n + 1] if 3 * n + 1 < 5 * 10 ** 6 and chain_size[3 * n + 1] != 0 else collatz_fill(
                3 * n + 1))
    else:
        comp = 1 + (
            chain_size[n >> 1] if n >> 1 < 5 * 10 ** 6 and chain_size[n >> 1] != 0 else collatz_fill(n >> 1))
    if n < 5 * 10 ** 6:
        chain_size[n] = comp
    return comp


T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
N_max = max(N)
chain_size = [0] * (5 * 10 ** 6 + 1)
chain_size[1] = 1
start_num = [1]
max_chain_size = 1
for i in range(2, N_max + 1):
    size = collatz_fill(i)
    if size >= max_chain_size:
        start_num.append(i)
        max_chain_size = size
for k in range(T):
    print([i for i in start_num if i <= N[k]][-1])
