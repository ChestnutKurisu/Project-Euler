from operator import itemgetter

N = int(input())
palindromes = {}
checked = [0] * (N + 1)
for n in range(1, N + 1):
    if checked[n]:
        continue
    m = n
    nit = 0
    n_sequence = {m}
    while str(m) != str(m)[::-1] and nit < 60:
        nit += 1
        m += int(str(m)[::-1])
        if m <= N:
            n_sequence.add(m)
    if nit == 60:
        continue
    for k in n_sequence:
        if k <= N:
            checked[k] = 1
    if m in palindromes:
        palindromes[m] = palindromes[m].union(n_sequence)
    else:
        palindromes[m] = n_sequence
for n in palindromes:
    palindromes[n] = len(palindromes[n])
max_p = max(palindromes.items(), key=itemgetter(1))[0]
print(max_p, palindromes[max_p])
