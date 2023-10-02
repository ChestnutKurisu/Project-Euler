import math

N = int(input())
M = []
for i in range(N):
    B, E = map(int, input().split())
    M.append((B, E, E * math.log(B)))
K = int(input())
M = sorted(M, key=lambda x: x[2])
print(*M[K - 1][:2])
