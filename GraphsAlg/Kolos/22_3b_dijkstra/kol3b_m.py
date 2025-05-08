from kol3btesty import runtests
from queue import PriorityQueue


def airports(G, A, s, t):
    n = len(G)
    distance = [float('inf')] * (n + 1)  # n+1 dla wierzchołka "niebo"
    processed = [False] * (n + 1)

    queue = PriorityQueue()
    queue.put((0, s))
    distance[s] = 0

    while not queue.empty():
        current_cost, u = queue.get()

        if u == t:
            return current_cost

        if processed[u]:
            continue
        processed[u] = True

        # Przetwarzanie normalnych krawędzi grafu (tylko jeśli u jest normalnym lotniskiem)
        if u < n:
            for (v, cost) in G[u]:
                if not processed[v] and distance[v] > current_cost + cost:
                    distance[v] = current_cost + cost
                    queue.put((distance[v], v))

            # Możliwość startu szybowcem do "nieba", jesli cena z distance[n] jest wieksza
            # kosztu lotu samolotem to lecimy
            if not processed[n] and distance[n] > current_cost + A[u]:
                distance[n] = current_cost + A[u]
                queue.put((distance[n], n))

        # Jeśli jesteśmy w "niebie", możemy wylądować na dowolnym lotnisku
        else:
            for v in range(n):
                if not processed[v] and distance[v] > current_cost + A[v]:
                    distance[v] = current_cost + A[v]
                    queue.put((distance[v], v))

    return distance[t] #end procedure airports()


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )