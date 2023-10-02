T = int(input())
M = []
for k in range(T):
    n = int(input())
    m = [(0, int(input()))]
    for i in range(1, n):
        p = list(map(int, input().split()))
        s = []
        for (x, y) in m:
            s.append((x, y + p[x]))
            s.append((x + 1, y + p[x + 1]))
        m = s
    M.append(max(m, key=lambda z: z[1])[1])
for k in range(T):
    print(M[k])
