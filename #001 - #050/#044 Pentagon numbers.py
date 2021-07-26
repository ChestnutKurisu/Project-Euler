N, K = map(int, input().split())
for n in range(K + 1, N):
    if (-36 * K ** 2 + 12 * K * (6 * n - 1) + 1 >= 0 and (
            ((-36 * K ** 2 + 12 * K * (6 * n - 1) + 1) ** 0.5 + 1) / 6).is_integer()) or (
            ((36 * K ** 2 + K * (12 - 72 * n) + 72 * n ** 2 - 24 * n + 1) ** 0.5 + 1) / 6).is_integer():
        print((n * (3 * n - 1)) >> 1)

# projecteuler.net version
# N = 10 ** 4
# D = float('inf')
# for k in range(1, N):
#     for j in range(k + 1, N):
#         if (((36 * j ** 2 - 12 * j + (1 - 6 * k) ** 2) ** 0.5 + 1) / 6).is_integer() and (
#                 ((36 * j ** 2 - 12 * j - 36 * k ** 2 + 12 * k + 1) ** 0.5 + 1) / 6).is_integer():
#             d = (j * (3 * j - 1) - k * (3 * k - 1)) >> 1
#             if D > d:
#                 D = d
# print(D)
