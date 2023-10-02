import math

T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
N_max = max(N)
# Euclid's method, generating primitive pythagorean triples
p_sols = [0] * (N_max + 1)
for m in range(1, int((N_max // 2) ** 0.5)):
    for n in range(1, m):
        if math.gcd(m, n) != 1 or (m + n) % 2 == 0:
            continue
        for k in range(1, N_max // (2 * m * (m + n)) + 1):
            p_sols[2 * m * (m + n) * k] += 1
p_max = [0] * (N_max + 1)
m = 0
m_p = 0
for p in range(N_max + 1):
    if m < p_sols[p]:
        m = p_sols[p]
        m_p = p
    p_max[p] = m_p
for k in range(T):
    print(p_max[N[k]])
