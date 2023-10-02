import math
import operator
from functools import reduce


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


X = int(input())
Y = 2 * X - 1
num_prime_factors = math.floor(math.log(Y, 3))
primes = rwh_primes2(200)[:30]
prime_power_dict_temp = {5 ** i: [5] * i for i in range(6)}
for key in list(prime_power_dict_temp.keys()):
    prime_power_dict_temp[7 * key] = [7] + prime_power_dict_temp[key]
    prime_power_dict_temp[7 ** 2 * key] = [7] * 2 + prime_power_dict_temp[key]
    prime_power_dict_temp[7 ** 3 * key] = [7] * 3 + prime_power_dict_temp[key]
    prime_power_dict_temp[9 * 7 * key] = [9] + [7] + prime_power_dict_temp[key]
    prime_power_dict_temp[9 * 7 ** 2 * key] = [9] + [7] * 2 + prime_power_dict_temp[key]
    prime_power_dict_temp[9 * 7 ** 3 * key] = [9] + [7] * 3 + prime_power_dict_temp[key]
    prime_power_dict_temp[9 ** 2 * 7 * key] = [9] * 2 + [7] + prime_power_dict_temp[key]
    prime_power_dict_temp[9 ** 2 * 7 ** 2 * key] = [9] * 2 + [7] * 2 + prime_power_dict_temp[key]
    prime_power_dict_temp[9 ** 2 * 7 ** 3 * key] = [9] * 2 + [7] * 3 + prime_power_dict_temp[key]
    prime_power_dict_temp[9 ** 3 * 7 * key] = [9] * 3 + [7] + prime_power_dict_temp[key]
    prime_power_dict_temp[9 ** 3 * 7 ** 2 * key] = [9] * 3 + [7] * 2 + prime_power_dict_temp[key]
    prime_power_dict_temp[9 ** 3 * 7 ** 3 * key] = [9] * 3 + [7] * 3 + prime_power_dict_temp[key]
    prime_power_dict_temp[9 * key] = [9] + prime_power_dict_temp[key]
    prime_power_dict_temp[9 ** 2 * key] = [9] * 2 + prime_power_dict_temp[key]
    prime_power_dict_temp[9 ** 3 * key] = [9] * 3 + prime_power_dict_temp[key]
    prime_power_dict_temp[9 ** 4 * key] = [9] * 4 + prime_power_dict_temp[key]
    prime_power_dict_temp[9 ** 5 * key] = [9] * 5 + prime_power_dict_temp[key]
    prime_power_dict_temp[9 ** 6 * key] = [9] * 6 + prime_power_dict_temp[key]
# Accommodate higher powers of 2 as potential candidates
for key in list(prime_power_dict_temp.keys()):
    for odd in range(11, 20, 2):
        prime_power_dict_temp[odd * key] = [odd] + prime_power_dict_temp[key]
max_num_prime_factors = math.ceil(math.log(Y, 3))
prime_power_dict = {}
for key in prime_power_dict_temp:
    if 3 * Y < key:
        continue
    count_3 = math.ceil(math.log(max(Y / key, 1), 3))
    new_key = key * 3 ** count_3
    if new_key in prime_power_dict:
        prime_power_dict[new_key].append(prime_power_dict_temp[key] + [3] * count_3)
    else:
        prime_power_dict[new_key] = [prime_power_dict_temp[key] + [3] * count_3]
potential_answers = []
for key in prime_power_dict:
    prime_power_permutations = prime_power_dict[key]
    potential_answers.append(min([reduce(operator.mul, [primes[j] ** ((prime_power_permutations[k][j] - 1) // 2) for j in range(len(prime_power_permutations[k]))]) for k in range(len(prime_power_permutations))]))
print(min(potential_answers))
