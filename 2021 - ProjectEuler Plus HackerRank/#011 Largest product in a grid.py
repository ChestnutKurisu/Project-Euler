grid = []
for i in range(20):
    grid.append([int(temp) for temp in input().strip().split(' ')])
max_prod = -1
for i in range(20):
    for j in range(17):
        prod = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
        if max_prod < prod:
            max_prod = prod
        prod = grid[j][i] * grid[j + 1][i] * grid[j + 2][i] * grid[j + 3][i]
        if max_prod < prod:
            max_prod = prod
for i in range(17):
    for j in range(17):
        prod = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
        if max_prod < prod:
            max_prod = prod
        prod = grid[i][j + 3] * grid[i + 1][j + 2] * grid[i + 2][j + 1] * grid[i + 3][j]
        if max_prod < prod:
            max_prod = prod
print(max_prod)
