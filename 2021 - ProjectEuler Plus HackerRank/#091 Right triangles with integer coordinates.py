from math import gcd

# from itertools import combinations
# def is_right_angled(A, B, C):
#     sides = sorted([(B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2, (C[0] - B[0]) ** 2 + (C[1] - B[1]) ** 2,
#                     (A[0] - C[0]) ** 2 + (A[1] - C[1]) ** 2])
#     return sides[0] + sides[1] == sides[2]
#
#
# O = (0, 0)
# N=int(input())
# lattice_points = [(i, j) for i in range(N + 1) for j in range(N + 1)]
# lattice_points.remove(O)
# count = 0
# rat_list = []
# for P, Q in combinations(lattice_points, 2):
#     if is_right_angled(O, P, Q):
#         count += 1
#         rat_list.append([P, Q])
# print(rat_list)
# print(count)

# https://oeis.org/A155154
# https://projecteuler.net/action=quote;post_id=386170 (Correction: floor(((N - b) * gcd(a, b)) / a)
# Number of integer lattice solutions to ax + by = a^2 + b^2, 0 <= x < a, b < y <= n
N = int(input())
print(3 * N ** 2 + sum(
    sum(2 * min((a * gcd(a, b)) // b, ((N - b) * gcd(a, b)) // a) for a in range(1, N + 1)) for b in range(1, N + 1)))
