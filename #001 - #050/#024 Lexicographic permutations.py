import math

T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input()) - 1
for k in range(T):
    w = [c for c in 'abcdefghijklm']
    s = ''
    for i in range(len(w) - 1, 0, -1):
        c = w[(N[k] // math.factorial(i)) % len(w)]
        w.remove(c)
        s += c
    s += w[0]
    print(s)
