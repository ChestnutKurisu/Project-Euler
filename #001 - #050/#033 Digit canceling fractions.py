import math
from itertools import *


def fill(masks, n):
    f = set()
    n = str(n)
    n = '0' * (N - K - len(n)) + n
    for m in masks:
        c = ''
        i = 0
        for d in m:
            if d == '.':
                c += n[i]
                i += 1
            else:
                c += d
        c = int(c)
        if c >= 10 ** (N - 1):
            f.add(c)
    return f


N, K = map(int, input().split())
# precomputed
# if (N, K) == (4, 1):
#     print(12999936, 28131911)
#     exit(0)
nsum = dsum = 0
frac = []
for num in range(1, 10 ** (N - K)):
    for den in range(num + 1, 10 ** (N - K)):
        for can in combinations_with_replacement('123456789', K):
            masks = {''.join(p) for p in permutations(''.join(can) + '.' * (N - K))}
            n_ori = fill(masks, num)
            d_ori = fill(masks, den)
            for n in n_ori:
                for d in d_ori:
                    if num * d == den * n:
                        frac.append((n, d))

frac = set(frac)
for n, d in frac:
    nsum += n
    dsum += d
print(nsum, dsum)
