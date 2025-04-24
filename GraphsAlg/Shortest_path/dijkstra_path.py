import heapq

def dijkstra(graph, start, end):
    heap = [(0, start, [])]
    visited = set()

    while heap:
        cost, node, path = heapq.heappop(heap)

        if node == end:
            return path + [node], cost

        if node not in visited:
            visited.add(node)
            for nei, weight in graph[node]:
                heapq.heappush(heap, (cost+weight, nei, path+[node]))

    return None