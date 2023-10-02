T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
for k in range(T):
    while not N[k] & 1:
        N[k] //= 2
    if N[k] == 1:
        print(2)
        continue
    max_i = 0
    i = 3
    while i <= int(N[k] ** 0.5):
        if N[k] % i == 0:
            N[k] //= i
            max_i = i
            i -= 2
        i += 2
    print(N[k] if N[k] >= 3 else max_i)
