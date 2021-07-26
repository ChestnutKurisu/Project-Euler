import math

N = int(input())
pd = list(range(1, N + 1))
s = 0
pan = [0] * 10000
for a in range(1, 9999):
    for b in range(a, 9999 // a):
        d = int(math.log10(a)) + int(math.log10(b)) + int(math.log10(a * b)) + 3
        if d > N:
            break
        if d != N:
            continue
        if sorted([int(i) for i in str(a) + str(b) + str(a * b)]) == pd:
            if pan[a * b] == 0:
                pan[a * b] = 1
                s += a * b
print(s)
