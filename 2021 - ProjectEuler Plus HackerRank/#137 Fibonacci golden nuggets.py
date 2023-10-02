def matrix_mul(A, B):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % m, (A[0][0] * B[1][0] + A[0][1] * B[1][1]) % m],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % m, (A[1][0] * B[1][0] + A[1][1] * B[1][1]) % m]]


def matrix_power(A, k):
    if k == 0:
        return [[1, 0], [0, 1]]
    X = matrix_power(A, k // 2)
    X = matrix_mul(X, X)
    if k & 1:
        X = matrix_mul(X, A)
    return X


m = 10 ** 9 + 7
T = int(input())
N = [int(input()) for i in range(T)]
for N in N:
    A = matrix_power([[1, 1], [1, 0]], 2 * N + 1)
    print((A[0][1] * A[1][1]) % m)
