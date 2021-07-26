def isPalindrome(n):
    n = str(n)
    return n[:] == n[::-1]


T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
palin = []
for i in range(100, 1000):
    for j in range(i, 1000):
        n = i * j
        if isPalindrome(n) and n not in palin:
            palin.append(n)
palin = sorted(palin)
for k in range(T):
    for i in range(len(palin) - 1, -1, -1):
        if palin[i] < N[k]:
            print(palin[i])
            break
