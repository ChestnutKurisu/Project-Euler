T = int(input())
N = [0] * T
d = [0] * T
for k in range(T):
    N[k], d[k] = map(int, input().split())
for k in range(T):
    if d[k] ** 2 >= 2 * N[k]:
        print(0)
        continue
    palin_sum_list = set()
    for a in range(1, int((2 * N[k] - d[k] ** 2) ** 0.5 - d[k]) // 2 + 1):
        n = 1
        while True: 
            t = a ** 2 * (n + 1) + a * d[k] * n * (n + 1) + d[k] ** 2 * n * (n + 1) * (2 * n + 1) // 6
            if t >= N[k]:
                break
            st = str(t)
            if st == st[::-1]:
                palin_sum_list.add(t)
            n += 1
    print(sum(palin_sum_list))
