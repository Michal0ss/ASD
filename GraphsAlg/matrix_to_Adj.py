def convert(graph):
    n = len(graph)
    new_graph = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if graph[u][v]:
                new_graph[u].append([v, graph[u][v]])
                new_graph[v].append([u, graph[u][v]])

    return new_graph


def matrix_to_adj_list(matrix):
    n = len(matrix)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):   # żeby nie dublować krawędzi
            if matrix[i][j]:
                adj[i].append(j)
                adj[j].append(i)
    return adj
