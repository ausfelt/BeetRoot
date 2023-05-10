from collections import deque

def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example usage
graph = [
    [0, 1, 4, 2, 0, 0],
    [0, 0, 2, 3, 7, 0],
    [0, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0]
]

all_pairs_shortest_path = floyd_warshall(graph)
print(all_pairs_shortest_path)