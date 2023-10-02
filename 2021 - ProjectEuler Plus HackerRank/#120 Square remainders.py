T = int(input())
A = [0] * T
e = [0] * T
for k in range(T):
    A[k], e[k] = map(int, input().split())
for k in range(T):
    if e[k] == 2:
        if A[k] == 1:
            print(0)
        else:
            M = (A[k] - 2) >> 1
            print((2 + M * (M + 1) * (8 * M + 13) // 3 + (A[k] * (A[k] - 1) if A[k] & 1 else 0)) % (10 ** 9 + 7))
    else:
        M = A[k]
        print(((M * (M + 1) * (M ** 2 + M - 3) + 2 * ((M + 1) // 2 if M & 1 else -M // 2)) // 4) % (10 ** 9 + 7))
