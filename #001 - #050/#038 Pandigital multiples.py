N, K = map(int, input().split())
pan = [str(i) for i in range(1, K + 1)]
for n in range(2, N):
    p = ''
    i = 1
    while len(p) < K:
        p += str(n * i)
        i += 1
    if sorted(p) == pan:
        print(n)
