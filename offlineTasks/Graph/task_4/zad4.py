from zad4testy import runtests
import heapq


def spacetravel( n, E, S, a, b ):

    graph = {i: [] for i in range(n)}
    for u,v,t in E:
        graph[u].append((v,t))
        graph[v].append((u,t)) # bo graf nieskierowany

    #dodajemy krawedzie przy osobliwosciach (teleportacja) z waga 0
    for u in S:
        for v in S:
            if u != v:
                graph[u].append((v,0))

    def dijkstra(start):
        distances = {node: float('inf') for node in range(n)}
        distances[start]=0
        heap=[(0, start)] #kolejka priorytetowa (czas, planeta)

        while heap:
            current_dist, u = heapq.heappop(heap)
            if current_dist > distances[u]:
                continue
            for v, weight in graph[u]:
                if distances[v]>distances[u] + weight:
                    distances[v] = distances[u] + weight
                    heapq.heappush(heap, (distances[v], v))
        return distances

    distances_a = dijkstra(a)
    result = distances_a[b]

    return result if result != float('inf') else None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
