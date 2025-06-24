
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

def change_g_after_robbery(G, r):
    """zwraca graf zmodyfikowanych krawedzi po rabunku"""
    n = len(G)
    new_graph = [[] for _ in range(n)]
    for u in range(n):
        for v,w in G[u]:
            new_graph[u].append((v, 2 * w + r))
    return new_graph


def gold(G, V, s, t, r):
    n = len(G)
    koszty_przed = dijkstra(G, s)
    min_koszt = koszty_przed[t]  # koszt bez rabunku

    for castle in range(n):
        if castle == s or castle == t:
            continue
        G_after = change_g_after_robbery(G, r)
        koszty_po = dijkstra(G_after, castle)
        # Jeżeli nie można się dostać do t po rabunku, pomiń
        if koszty_przed[castle] == float("inf") or koszty_po[t] == float("inf"):
            continue
        koszt_rabunku = koszty_przed[castle] + koszty_po[t] - V[castle]
        min_koszt = min(min_koszt, koszt_rabunku)
    return min_koszt


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=True)