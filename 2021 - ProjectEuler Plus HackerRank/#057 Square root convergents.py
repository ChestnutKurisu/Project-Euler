N = int(input())
num = 3
den = 2
for i in range(1, N + 1):
    if len(str(num)) > len(str(den)):
        print(i)
    num, den = num + 2 * den, num + den
