N = int(input())
print(max([sum([int(i) for i in str(j)]) for j in [a ** b for a in range(1, N) for b in range(1, N)]]))