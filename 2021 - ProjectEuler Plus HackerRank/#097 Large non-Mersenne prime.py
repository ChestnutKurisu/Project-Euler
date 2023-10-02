T = int(input())
A = [0] * T
B = [0] * T
C = [0] * T
D = [0] * T
for k in range(T):
    A[k], B[k], C[k], D[k] = map(int, input().split())
last_12_digits_sum = 0
for k in range(T):
    last_12_digits_sum += (A[k] * pow(B[k], C[k], 10 ** 12) + D[k]) % 10 ** 12
last_12_digits_sum = str(last_12_digits_sum % 10 ** 12)
print('0' * (12 - len(last_12_digits_sum)) + last_12_digits_sum)
