N = int(input())
M = [list(map(int, input().split())) for i in range(N)]
M_DP = [[0] * N for i in range(N)]
for i in range(N):
    M_DP[i][0] = M[i][0]
for j in range(1, N):
    M_DP[0][j] = M_DP[0][j - 1] + M[0][j]
    for i in range(1, N):
        M_DP[i][j] = min(M_DP[i - 1][j], M_DP[i][j - 1]) + M[i][j]
    for i in range(N - 2, -1, -1):
        M_DP[i][j] = min(M_DP[i][j], M_DP[i + 1][j] + M[i][j])
print(min([M_DP[i][N - 1] for i in range(N)]))
