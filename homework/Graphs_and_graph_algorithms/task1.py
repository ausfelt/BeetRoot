def dfs_scc(graph, v, visited, stack):
    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs_scc(graph, u, visited, stack)
    stack.append(v)


def scc(graph):
    n = len(graph)
    visited = [False] * n
    stack = []
    for v in range(n):
        if not visited[v]:
            dfs_scc(graph, v, visited, stack)

    transposed_graph = [[] for _ in range(n)]
    for v in range(n):
        for u in graph[v]:
            transposed_graph[u].append(v)

    visited = [False] * n
    scc_list = []
    while stack:
        v = stack.pop()
        if not visited[v]:
            scc = []
            dfs_scc(transposed_graph, v, visited, scc)
            scc_list.append(scc)

    return scc_list


# Example usage
graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: [5],
    5: [3]
}

strongly_connected_components = scc(graph)
print(strongly_connected_components)