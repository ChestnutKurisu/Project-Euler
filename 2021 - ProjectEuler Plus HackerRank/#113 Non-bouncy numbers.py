T = int(input())
k = [int(input()) for i in range(T)]
k_max = max(k)
# increasing_non_bouncy (inb) and decreasing_non_bouncy (dnb)
inb = [{i: 1 for i in range(1, 10)}]
dnb = [{i: 1 for i in range(9, -1, -1)}]
not_bouncy_count = [0, 9]
for j in range(2, k_max + 1):
    inb.append({i: sum(inb[-1][l] for l in range(i, 10)) for i in range(1, 10)})
    dnb.append({i: sum(dnb[-1][l] for l in range(i, -1, -1)) for i in range(9, -1, -1)})
    dnb[-2][0] = 0
    # Subtract 9 to remove repeats
    not_bouncy_count.append(not_bouncy_count[-1] + sum(inb[-1][l] for l in range(1, 10)) + sum(
        dnb[-1][l] for l in range(9, 0, -1)) - 9)
for i in range(T):
    print(not_bouncy_count[k[i]] % (10 ** 9 + 7))
