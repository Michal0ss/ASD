from collections import deque


def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:

        node, path = queue.popleft()

        if node == end:
            return path

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)

                queue.append((nei, path+[nei]))

    return None