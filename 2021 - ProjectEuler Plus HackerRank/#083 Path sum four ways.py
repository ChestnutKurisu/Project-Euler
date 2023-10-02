import heapq


# https://github.com/TheAlgorithms/Python/blob/master/graphs/dijkstra.py
def dijkstra(graph, start, end):
    heap = [(0, start)]
    visited = set()
    while heap:
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        if u == end:
            return cost
        for v, c in graph[u]:
            if v in visited:
                continue
            heapq.heappush(heap, (cost + c, v))
    return -1


N = int(input())
M = [list(map(int, input().split())) for i in range(N)]
G = {str(i) + '_' + str(j): [] for i in range(N) for j in range(N)}
for i in range(N):
    for j in range(N):
        key = str(i) + '_' + str(j)
        if i <= N - 2:
            G[key].append((str(i + 1) + '_' + str(j), M[i + 1][j]))
        if i >= 1:
            G[key].append((str(i - 1) + '_' + str(j), M[i - 1][j]))
        if j <= N - 2:
            G[key].append((str(i) + '_' + str(j + 1), M[i][j + 1]))
        if j >= 1:
            G[key].append((str(i) + '_' + str(j - 1), M[i][j - 1]))
print(M[0][0] + dijkstra(G, '0_0', str(N - 1) + '_' + str(N - 1)))
