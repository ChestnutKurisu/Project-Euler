# Generates x and y for Bezout's identity: ax + by = gcd(a,b)
def extended_euclidean_algorithm(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean_algorithm(b % a, a)
        return gcd, y - (b // a) * x, x


T = int(input())
a = [0] * T
b = [0] * T
N = [0] * T
for k in range(T):
    a[k], b[k], N[k] = map(int, input().split())
# https://math.stackexchange.com/questions/578975/computational-complexity-of-finding-adjacent-terms-in-farey-sequence
for k in range(T):
    # ab_0 - ba_0 = gcd(a,b) = 1
    # Solutions are: a_0 = a_0 + na[k], b_0 = b_0 + nb[k]
    gcd, b_0, a_0 = extended_euclidean_algorithm(a[k], -b[k])
    max_n = (N[k] - b_0) // b[k]
    print(a_0 + max_n * a[k], b_0 + max_n * b[k])
