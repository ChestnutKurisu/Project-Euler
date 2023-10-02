primes = [2, 3, 5, 7, 9, 11, 13, 17, 19, 23]
N, K = map(int, input().split())
for x in range(1, N + 1):
    h = 1
    for d in str(x):
        h *= primes[int(d)]
    same_digit_count = 1
    for k in range(2, K + 1):
        if len(str(k * x)) > len(str(x)):
            break
        hk = 1
        for d in str(k * x):
            hk *= primes[int(d)]
        if hk == h:
            same_digit_count += 1
        else:
            break
    if same_digit_count == K:
        print(' '.join([str(k * x) for k in range(1, K + 1)]))
