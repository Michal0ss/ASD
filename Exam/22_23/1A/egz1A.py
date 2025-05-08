from egz1Atesty import runtests

from queue import PriorityQueue

def dijkstra(G, start, cost_multiplier=1, ransom=0):
    """ Standardowy Dijkstra z możliwością zmiany wag (po napaści). """
    n = len(G)
    distance = [float("inf")] * n
    distance[start] = 0

    Q = PriorityQueue()
    Q.put((0, start))

    while not Q.empty():
        dist, v = Q.get()

        if dist > distance[v]:
            continue

        for u, w in G[v]:
            new_cost = dist + cost_multiplier * w + ransom
            if new_cost < distance[u]:
                distance[u] = new_cost
                Q.put((new_cost, u))

    return distance

def gold(G, V, s, t, r):
    n = len(G)

    # 1️⃣ Koszt bez napaści
    dist_no_rob = dijkstra(G, s)
    best_cost = dist_no_rob[t]  # Najlepszy koszt bez napaści

    # 2️⃣ Sprawdzamy napaść na każdy zamek
    for robbed_castle in range(n):
        if robbed_castle == s or robbed_castle == t:
            continue  # Nie napadamy na startowy ani końcowy zamek

        # Dojście do zamku bez napaści
        to_castle = dist_no_rob[robbed_castle]

        if to_castle == float("inf"):
            continue  # Nie da się dojść

        # Po napaści: koszt = 2*w + r
        dist_after_rob = dijkstra(G, robbed_castle, cost_multiplier=2, ransom=r)

        to_end = dist_after_rob[t]

        if to_end == float("inf"):
            continue  # Nie da się dojść do końca po napaści

        total_cost = to_castle + to_end - V[robbed_castle]  # Odejmujemy złoto

        # Jeśli zysk → koszt będzie mniejszy (nawet ujemny!)
        if total_cost < best_cost:
            best_cost = total_cost

    return best_cost


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
