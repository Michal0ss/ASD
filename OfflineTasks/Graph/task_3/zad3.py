from zad3testy import runtests
from collections import deque

""""""

def longer( G, s, t ):
    def bfs_shortest_path(graph, s, t, exclude_edge=None):
        n = len(G)
        visited = [False] * n  # Śledzenie odwiedzonych wierzchołków
        parent = [-1] * n      # Tablica rodziców do odtwarzania ścieżki
        queue = deque([s])     # Kolejka FIFO dla BFS
        visited[s] = True      # Zaznacz start jako odwiedzony

        while queue:
            node = queue.popleft()

            if node == t:
                break

            for nei in G[node]:

                if exclude_edge and ((node == exclude_edge[0] and nei == exclude_edge[1]) or
                                     (node == exclude_edge[1] and nei == exclude_edge[0])):
                    continue


                if not visited[nei]:
                    visited[nei] = True
                    parent[nei] = node
                    queue.append(nei)

        path = []
        current = t
        while current != -1:
            path.append(current)
            current = parent[current]
        path.reverse()

        if path and path[0] == s:
            return path
        return []


    original_path = bfs_shortest_path(G, s, t)

    if not original_path:
        return None

    original_length = len(original_path) -1

    for i in range(original_length):
        u,v = original_path[i], original_path[i+1]

        new_path = bfs_shortest_path(G, s, t, exclude_edge=(u,v))

        if not new_path or len(new_path) - 1>original_length:
            if u<v:
                return u,v
            return v,u
    return None
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
