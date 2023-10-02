from functools import reduce
import operator

T = int(input())
N = [''] * T
K = [0] * T
for k in range(T):
    a, K[k] = map(int, input().split())
    N[k] = str(input())
for k in range(T):
    M = list(int(i) for i in N[k])
    print(max([reduce(operator.mul, M[i:i + K[k]], 1) for i in range(len(M) - K[k])]))
