# Zeller's algorithm
def isSunday(y, m, d):
    y = y - 1 if m <= 2 else y
    m = m if m >= 3 else m + 12
    return (d + (13 * (m + 1)) // 5 + y + y // 4 - y // 100 + y // 400) % 7 == 1


T = int(input())
Sundays = [0] * T
for k in range(T):
    Y1, M1, D1 = map(int, input().strip().split())
    Y2, M2, D2 = map(int, input().strip().split())
    if Y1 == Y2 and (M1 > M2 or (M1 == M2 and D1 > D2)):
        M1, M2 = M2, M1
        D1, D2 = D2, D1
    if D1 != 1:
        D1 = 1
        if M1 < 12:
            M1 += 1
        else:
            M1 = 1
            Y1 += 1
    while True:
        if Y1 > Y2 or (Y1 == Y2 and M1 > M2):
            break
        Sundays[k] += 1 if isSunday(Y1, M1, D1) else 0
        if M1 < 12:
            M1 += 1
        else:
            M1 = 1
            Y1 += 1
for k in range(T):
    print(Sundays[k])
