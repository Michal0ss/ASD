from zad4testy import runtests
from queue import PriorityQueue


def spacetravel(n, E, S, a, b):
    graph = [[] for _ in range(n)]
    for u, v, t in E:
        graph[u].append((v, t))
        graph[v].append((u, t))

    #tworze krawedzie tam gdzie wystepuja teleportacje i dodaje im wage 0
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            u, v = S[i], S[j]
            graph[u].append((v, 0))
            graph[v].append((u, 0))


    #  DIJKSTRA
    distances = [float('inf')] * n
    distances[a] = 0
    pq = PriorityQueue()
    pq.put((0, a))

    while not pq.empty():
        current_dist, u = pq.get()

        if u == b: # cel zostal znaleziony
            return current_dist


        if current_dist > distances[u]:
            continue

        for v, weight in graph[u]:
            if distances[v] > distances[u] + weight:
                distances[v] = distances[u] + weight
                pq.put((distances[v], v))

    return

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
