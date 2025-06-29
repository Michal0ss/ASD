
# Wyliczam koszty przejscia przed i po rabowaniu
# Następnie przechodząc po kolejnych wierzchołkach wybieram który obrabuję
# Obliczam koszt całkowitego przejscia i zwracam minimum
#
# Złożoność: O(V^2logV)

from egz1Atesty import runtests
from queue import PriorityQueue


def dijkstra(graph:list, s:int) -> list:
    """bez listy odiwedzonych wierzcholkow bo mozemy pare razy odwiedzi ten sam"""
    n = len(graph)
    q = PriorityQueue()
    dist = [float("inf") for _ in range(n)]
    dist[s] = 0
    q.put((0, s))

    while not q.empty():
        distance, u = q.get()
        for v, time in graph[u]:
            if dist[v] > dist[u] + time:
                dist[v] = dist[u] + time
                q.put((dist[v], v))
    return dist

def gold(G, V, s, t, r):
    n = len(G)
    cost_before = dijkstra(G, s)
    min_cost = cost_before[t]

    for v in range(n):
        for w in range(len(G[v])):
            new_modified_v = (G[v][w][0], (2*G[v][w][1]) + r)
            G[v][w] = new_modified_v

    cost_after_robbery = dijkstra(G, t) # od t bo chce koszty do konca a nie od pocatku do danego zamku


    for u in range(n):
        cost_for_robbery_trace = cost_before[u] - V[u] + cost_after_robbery[u]
        min_cost = min(min_cost, cost_for_robbery_trace)
    return min_cost
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=True)