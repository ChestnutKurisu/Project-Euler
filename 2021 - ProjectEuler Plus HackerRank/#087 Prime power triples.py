import math


# # permutations with replacement from https://stackoverflow.com/questions/6284396/permutations-with-unique-values
# def permutations_with_replacement(elements, n):
#     return permutations_helper(elements, [0] * n, n - 1)
#
#
# def permutations_helper(elements, result_list, d):
#     if d < 0:
#         yield tuple(result_list)
#     else:
#         for i in elements:
#             result_list[d] = i
#             all_permutations = permutations_helper(elements, result_list, d - 1)
#             for g in all_permutations:
#                 yield g


def rwh_primes2(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = bytearray([True]) * (n // 3)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = bytearray([False]) * ((n // 6 - k * k // 6 - 1) // k + 1)
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = bytearray([False]) * (
                    (n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) // k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]


def binary_search_count_less_than_equal_to(arr, key):
    left = 0
    right = len(arr) - 1
    count = 0
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] <= key:
            count = mid + 1
            left = mid + 1
        else:
            right = mid - 1
    return count


T = int(input())
N = [int(input()) for k in range(T)]
N_max = max(N)
primes = rwh_primes2(int(math.sqrt(N_max)))
L = set()
for p1 in primes:
    for p2 in [p for p in primes if p ** 3 <= N_max]:
        for p3 in [p for p in primes if p ** 4 <= N_max]:
            m = p1 ** 2 + p2 ** 3 + p3 ** 4
            if m <= N_max:
                L.add(m)
L = sorted(list(L))
for k in range(T):
    print(binary_search_count_less_than_equal_to(L, N[k]))
