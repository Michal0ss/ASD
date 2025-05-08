from zadtesty import runtests
from queue import PriorityQueue

def dijkstra_goodknight(G, s, t):
    n = len(G)

    # distance[v][h] = najmniejszy czas dotarcia do v z h godzinami marszu bez snu
    distance = [ [float("inf")] * 9 for _ in range(n) ]  # bo max 8h

    distance[s][0] = 0
    Q = PriorityQueue()
    Q.put((0, s, 0))  # (koszt całkowity, wierzchołek, godziny bez snu)

    while not Q.empty():
        cost, v, hours = Q.get()

        if cost > distance[v][hours]:
            continue

        for u in range(n):
            weight = G[v][u]
            if weight == -1:
                continue  # brak krawędzi

            # OPCJA 1: Idziemy dalej bez noclegu
            if hours + weight <= 8:
                if cost + weight < distance[u][hours + weight]:
                    distance[u][hours + weight] = cost + weight
                    Q.put((cost + weight, u, hours + weight))

            # OPCJA 2: Nocujemy (o ile u != s i u != t)
            if u != s and u != t:
                if cost + weight + 8 < distance[u][0]:
                    distance[u][0] = cost + weight + 8
                    Q.put((cost + weight + 8, u, 0))

    return min(distance[t])  # minimalny koszt dojścia do t z dowolną liczbą godzin bez snu

def goodknight(G, s, t):
    return dijkstra_goodknight(G, s, t)



runtests(goodknight, all_tests=True)
