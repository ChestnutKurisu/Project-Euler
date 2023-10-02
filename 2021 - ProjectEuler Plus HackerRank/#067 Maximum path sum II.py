T = int(input())
M = []
for k in range(T):
    n = int(input())
    t = []
    p = []
    for i in range(n):
        t.append(list(map(int, input().split())))
    p = t[-1]
    for i in range(n - 2, -1, -1):
        s = []
        for j in range(i + 1):
            s.append(t[i][j] + max(p[j], p[j + 1]))
        p = s
    M.append(p[0])
for k in range(T):
    print(M[k])
