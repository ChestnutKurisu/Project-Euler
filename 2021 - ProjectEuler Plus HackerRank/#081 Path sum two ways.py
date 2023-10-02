N = int(input())
M = [list(map(int, input().split())) for i in range(N)]
M_DP = [[0] * N for i in range(N)]
M_DP[0][0] = M[0][0]
for i in range(1, N):
    M_DP[0][i] = M_DP[0][i - 1] + M[0][i]
    M_DP[i][0] = M_DP[i - 1][0] + M[i][0]
for i in range(1, N):
    for j in range(1, N):
        M_DP[i][j] = M[i][j] + min(M_DP[i][j - 1], M_DP[i - 1][j])
print(M_DP[N - 1][N - 1])
