import math

m = int(input())
s = 0
for d in range(1, m):
    for q in range(1, 10):
        for k in range(1, 10):
            r = q * (10 ** d - k)
            if r % (10 * k - 1) == 0:
                n = r // (10 * k - 1)
                # Removing extraneous solutions
                if k == 1 or int(math.log10(10 * n + q)) == d:
                    s += 10 * n + q
print(s % 10 ** 5)
