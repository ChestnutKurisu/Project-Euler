import math

f = [math.factorial(i) for i in range(10)]
N = int(input())
print(sum(i for i in range(10, N) if sum(f[int(j)] for j in str(i)) % i == 0))
