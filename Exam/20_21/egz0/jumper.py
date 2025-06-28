from GraphsAlg.bellman import matrix
from jumpertesty import runtests
from queue import PriorityQueue

import heapq


def jumper(G, s, w):
    """
    Znajduje długość najkrótszej ścieżki w grafie G z wierzchołka s do w,
    z wykorzystaniem mechanizmu "dwumilowych butów".

    Args:
        G (list[list[int]]): Graf reprezentowany jako macierz sąsiedztwa.
        s (int): Wierzchołek startowy.
        w (int): Wierzchołek końcowy.

    Returns:
        int or None: Długość najkrótszej ścieżki lub None, jeśli jest nieosiągalna.
    """
    n = len(G)

    # 1. Tablica odległości: dist[wierzchołek][flaga]
    # flaga = 0: dotarliśmy normalnym krokiem
    # flaga = 1: dotarliśmy dwumilowym skokiem
    distances = [[float('inf')] * 2 for _ in range(n)]

    # 2. Kolejka priorytetowa: (koszt, wierzchołek, flaga)
    pq = [(0, s, 0)]

    # 3. Warunek początkowy
    distances[s][0] = 0

    while pq:
        dist, u, flag = heapq.heappop(pq)

        # Jeśli znaleźliśmy już krótszą ścieżkę do tego stanu, pomijamy
        if dist > distances[u][flag]:
            continue

        # --- Rozważanie ruchów z wierzchołka u ---

        # A. Jeśli do u dotarliśmy normalnym krokiem (flag == 0),
        #    możemy teraz iść normalnie LUB skoczyć.
        if flag == 0:
            # A.1. Wykonujemy normalny krok (u -> v)
            for v in range(n):
                if G[u][v] > 0:  # Jeśli istnieje krawędź
                    new_dist = dist + G[u][v]
                    # Cel: v, dotarliśmy normalnym krokiem (flaga=0)
                    if new_dist < distances[v][0]:
                        distances[v][0] = new_dist
                        heapq.heappush(pq, (new_dist, v, 0))

            # A.2. Wykonujemy dwumilowy skok (u -> x -> v)
            for x in range(n):
                if G[u][x] > 0:  # Pierwsza część skoku
                    for v in range(n):
                        if G[x][v] > 0 and v != u:  # Druga część skoku
                            jump_cost = max(G[u][x], G[x][v])
                            new_dist = dist + jump_cost
                            # Cel: v, dotarliśmy skokiem (flaga=1)
                            if new_dist < distances[v][1]:
                                distances[v][1] = new_dist
                                heapq.heappush(pq, (new_dist, v, 1))

        # B. Jeśli do u dotarliśmy skokiem (flag == 1),
        #    teraz MUSIMY iść normalnie.
        if flag == 1:
            # B.1. Wykonujemy normalny krok (u -> v)
            for v in range(n):
                if G[u][v] > 0:
                    new_dist = dist + G[u][v]
                    # Cel: v, dotarliśmy normalnym krokiem (flaga=0)
                    if new_dist < distances[v][0]:
                        distances[v][0] = new_dist
                        heapq.heappush(pq, (new_dist, v, 0))

    # Wynik to minimum z dotarcia do celu 'w' na oba sposoby
    result = min(distances[w][0], distances[w][1])

    return result if result != float('inf') else None


runtests(jumper)