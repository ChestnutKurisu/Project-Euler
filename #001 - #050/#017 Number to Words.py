T = int(input())
N = [0] * T
for k in range(T):
    N[k] = int(input())
words = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine',
         10: 'Ten',
         11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
         18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
         70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}


def tenths(n):
    if n == 0:
        return ''
    if 1 <= n <= 19:
        return words[n]
    return words[(n // 10) * 10] + ' ' + words[n % 10]


for k in range(T):
    if N[k] == 0:
        print('Zero')
        exit(0)
    if N[k] == 10 ** 12:
        print('One Trillion')
        exit(0)
    u = N[k] % 10 ** 3
    th = N[k] // 10 ** 3
    m = th // 10 ** 3
    b = m // 10 ** 3
    th = th % 10 ** 3
    m = m % 10 ** 3
    w = ''
    if b > 0:
        if b >= 100:
            w += ' ' + words[b // 100] + ' ' + 'Hundred'
        if b % 100 > 0:
            w += ' ' + tenths(b % 100)
        w = w.strip()
        w += ' Billion'
    if m > 0:
        if m >= 100:
            w += ' ' + words[m // 100] + ' ' + 'Hundred'
        if m % 100 > 0:
            w += ' ' + tenths(m % 100)
        w = w.strip()
        w += ' Million'
    if th > 0:
        if th >= 100:
            w += ' ' + words[th // 100] + ' ' + 'Hundred'
        if th % 100 > 0:
            w += ' ' + tenths(th % 100)
        w = w.strip()
        w += ' Thousand'
    if u > 0:
        if u >= 100:
            w += ' ' + words[u // 100] + ' ' + 'Hundred'
        if u % 100 > 0:
            w += ' ' + tenths(u % 100)
        w = w.strip()
    print(w)
