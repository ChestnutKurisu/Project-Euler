# Pg. 27 of http://people.csail.mit.edu/mip/papers/farey/talk.pdf
A, D = map(int, input().split())
T = [q // A for q in range(D + 1)]
S = [q // (A + 1) for q in range(D + 1)]
for q in range(1, D + 1):
    for m in range(2, D // q + 1):
        T[m * q] -= T[q]
        S[m * q] -= S[q]
print(sum(T) - sum(S) - 1)
