import math
T = int(input())
N = [0]*T
for k in range(T):
    N[k] = int(input())
for k in range(T):
    print(sum(int(i) for i in str(math.factorial(N[k]))))
