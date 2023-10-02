from fractions import Fraction

N = int(input())
continued_fraction = [2]
for k in range(1, 10001):
    continued_fraction.extend([1, 2 * k, 1])
continued_fraction = list(reversed(continued_fraction[:N]))
num = continued_fraction[0]
den = 1
for i in range(1, N):
    num, den = num * continued_fraction[i] + den, num
sequence_of_convergents = Fraction(num, den)
print(sum(int(d) for d in str(sequence_of_convergents.numerator)))
