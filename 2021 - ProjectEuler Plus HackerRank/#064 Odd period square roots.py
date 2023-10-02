# Theorem 2.3: http://web.math.princeton.edu/mathlab/jr02fall/Periodicity/mariusjp.pdf
def find_period(D):
    bk = ak = a0 = int(D ** 0.5)
    ck = D - ak ** 2
    k = 0
    while ak != 2 * a0:
        ak = (a0 + bk) // ck
        bk = ak * ck - bk
        ck = (D - bk ** 2) // ck
        k += 1
    return k


N = int(input())
odd_count = 0
period = {m: 0 for m in range(1, N + 1)}
for m in range(1, int(N ** 0.5) + 1):
    period[m ** 2] = -2
for m in range(1, N + 1):
    if period[m] == -2:
        continue
    period[m] = find_period(m)
print(len([m for m in period.keys() if period[m] & 1]))
