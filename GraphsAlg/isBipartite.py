from collections import deque
from queue import Queue
from typing import List

"""first solution by using BFS and coloring(-1 and 1)"""
def isBipartite(graph: List[List[int]]) -> bool:
    odd = [0] * len(graph)

    def bfs(i):
        if odd[i]:
            return True

        q=deque([i])
        odd[i] = -1
        while q:
            i = q.popleft()
            for nei in graph[i]:
                if odd[i] and odd[i] == odd[nei]:
                    return False
                elif not odd[nei]:
                    q.append(nei)
                    odd[nei] = -1*odd[i]
        return True

    for i in range(len(graph)):
        if not bfs(i):
            return False
    return True

"""second solution for finding out is graph bipartite by using coloring(-1 and 1) and BFS"""
def is_bipartite(G: 'graph represented using adjacency lists'):
    n = len(G)
    queue = Queue()
    colors = [0] * n  # 0 means no color (we will use 2 colors as we want to check if it's bipartite)

    # Loop over all vertices (for inconsistent graphs)
    for i in range(n):
        if colors[i]: continue
        queue.put((i, 1))  # Start with color 1
        while not queue.empty():
            j, color = queue.get()
            colors[j] = color
            for k in G[j]:
                if not colors[k]:
                    queue.put((k, -1 * color))  # Reverse color to the other one
                # If a vertex already has a color, check if this color is a proper one
                elif colors[k] == color:  # If the same color, a graph isn't bipartite
                    return False
    return True