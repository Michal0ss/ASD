from zad4testy import runtests
from queue import PriorityQueue

def dijkstra(G, s, e):
    n = len(G)
    distance = [float("inf")] * n
    distance[s] = 0

    PQ = PriorityQueue()
    PQ.put((0, s))

    while not PQ.empty():
        cur_distance, v = PQ.get()

        if cur_distance > distance[v]:
            continue

        for v_son, weight in G[v]:
            dist = cur_distance + weight

            if dist < distance[v_son]:
                distance[v_son] = dist
                PQ.put((dist, v_son))

    return distance[e]


def spacetravel(n, E, S, a, b):

    G = [[] for _ in range(n+1)]

    #zamiana z postaci (u,v,w) na adjency list
    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))

    for i in S:
        G[n].append((i,0))
        G[i].append((n,0))

    time = dijkstra(G,a,b)

    return time if time<float('inf') else None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
