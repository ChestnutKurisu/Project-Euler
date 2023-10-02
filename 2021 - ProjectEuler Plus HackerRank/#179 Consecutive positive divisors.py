t = int(input())
k = [int(input()) for i in range(t)]
k_max = max(k)
divisor_count = [0] * (k_max + 1)
for n in range(1, k_max + 1):
    for q in range(1, k_max // n + 1):
        divisor_count[q * n] += 1
cumulative_match_count = [0] * (k_max + 1)
c = 0
for n in range(1, k_max):
    if divisor_count[n] == divisor_count[n + 1]:
        c += 1
    cumulative_match_count[n] = c
for i in range(t):
    print(cumulative_match_count[k[i] - 1])
