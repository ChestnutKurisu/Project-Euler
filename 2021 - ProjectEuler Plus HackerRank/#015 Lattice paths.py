import math

T = int(input())
N = [0] * T
M = [0] * T
for k in range(T):
    N[k], M[k] = map(int, input().split(' '))
for k in range(T):
    print((math.factorial(M[k] + N[k]) // (math.factorial(M[k]) * math.factorial(N[k]))) % (10 ** 9 + 7))
