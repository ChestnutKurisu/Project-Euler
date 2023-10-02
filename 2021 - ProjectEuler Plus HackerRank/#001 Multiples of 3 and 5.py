import math

T = int(input())
for i in range(T):
    N = int(input()) - 1
    print(int(3 * math.floor(N / 3) * (math.floor(N / 3) + 1) + 5 * math.floor(N / 5) * (
            math.floor(N / 5) + 1) - 15 * math.floor(N / 15) * (math.floor(N / 15) + 1)) >> 1)
