N, K = map(int, input().split())
cube_count = {}
sorted_cubes = {}
for n in range(1, N):
    sorted_cube = ''.join(sorted(str(n ** 3)))
    if sorted_cube in cube_count:
        cube_count[sorted_cube] += 1
        sorted_cubes[sorted_cube].append(n ** 3)
    else:
        cube_count[sorted_cube] = 1
        sorted_cubes[sorted_cube] = [n ** 3]
for sorted_cube in [sc for sc in cube_count if cube_count[sc] == K]:
    print(sorted_cubes[sorted_cube][0])
