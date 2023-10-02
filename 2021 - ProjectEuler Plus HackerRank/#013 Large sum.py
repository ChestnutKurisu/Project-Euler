N = int(input())
M = [0] * N
for i in range(N):
    M[i] = int(input())
print(str(sum(M))[:10])
