class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0

def Find(x):
    if x.parent != x:
        x.parent = Find(x.parent)
    return x.parent

def Union(x, y):
    if x.rank > y.rank:
        y.parent = x
    elif x.rank < y.rank:
        x.parent = y
    else:
        y.parent = x
        x.rank += 1

def Kruskal(Edges, num_vertices, start=0):
    MST = []
    total_weight = 0

    Vertices = [Node(v) for v in range(num_vertices)]

    for i in range(start, len(Edges)):
        u, v, w = Edges[i]

        rootU = Find(Vertices[u])
        rootV = Find(Vertices[v])

        if rootU != rootV:
            Union(rootU, rootV)
            MST.append((u, v, w))
            total_weight += w

        if len(MST) == num_vertices - 1:
            break

    if len(MST) == num_vertices - 1:
        return MST, total_weight
    else:
        return None, None

def adjacency_to_edges(graph):
    edges = []
    visited = set()

    for u in range(len(graph)):
        for v, weight in graph[u]:
            if (v, u) not in visited:
                edges.append((u, v, weight))
                visited.add((u, v))
    return edges

