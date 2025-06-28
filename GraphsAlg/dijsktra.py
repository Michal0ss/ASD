# Python implementation of Dijkstra's algorithm using queue.PriorityQueue.
# The function dijkstra takes a graph in adjacency list form and a start node.
# It returns the shortest distances from the start node to all other nodes.
from math import inf
from queue import PriorityQueue

def dijkstra(graph, start):
    """
    graph: adjacency list, where graph[u] = list of (v, weight) pairs
    start: starting node index
    Returns: list of shortest distances from start to every node
    """
    n = len(graph)
    dist = [inf] * n
    dist[start] = 0
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, start))  # (distance, node)

    while not pq.empty():
        d, u = pq.get()
        if visited[u]:
            continue
        visited[u] = True
        for v, w in graph[u]:
            if not visited[v] and dist[v] > d + w:
                dist[v] = d + w
                pq.put((dist[v], v))
    return dist

# Example usage:
# graph = [
#     [(1, 2), (2, 4)],  # edges from node 0 to 1 (weight 2), to 2 (weight 4)
#     [(2, 1)],          # edge from node 1 to 2 (weight 1)
#     []                 # node 2 has no outgoing edges
# ]
# print(dijkstra(graph, 0))  # Output: [0, 2, 3]