import math


def base_digit_sum(n, b):
    s = 0
    while n != 0:
        s += n % b
        n //= b
    return s


B = int(input())
interesting = []
for i in range(2, int(B * 100 * math.log(10, B))):
    for j in range(max(2, int(math.log(B, i))), int(100 * math.log(10, i) + 1)):
        if base_digit_sum(i ** j, B) == i:
            interesting.append(i ** j)
print(' '.join(str(i) for i in sorted(interesting)))
