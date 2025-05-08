def adjacency_to_edges(graph):
    edges = []
    visited = set()

    for u in range(len(graph)):
        for v, weight in graph[u]:
            if (v, u) not in visited:
                edges.append((u, v, weight))
                visited.add((u, v))
    return edges
