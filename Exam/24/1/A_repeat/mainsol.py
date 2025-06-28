from egz1atesty import runtests

from queue import PriorityQueue
from math import inf

# Zamiana listy krawędzi na listę sąsiedztwa
def edge_to_adj(edges):
    N = max([a for a, b, _ in edges] + [b for a, b, _ in edges]) + 1
    adj_l = [[] for _ in range(N)]
    for u, v, w in edges:
        adj_l[u].append((v, w))
        adj_l[v].append((u, w))  # graf nieskierowany
    return adj_l, N

def dijkstra(graph, bike_speeds, start, end):
    q = PriorityQueue()
    q.put((0,-1,start)) # czas, indeks roweru, wierzchołek

    n= len(graph)
    best_choices = [[inf]*(n+1) for _ in range(n)] # mnoze razy n+1 bo ostatnie pozycje to brak roweru przyda sie pozniej
    best_choices[start][-1] = 0 # brak roweru = indeks -
    # best_choices[v][bike] – najmniejszy znany czas dotarcia do v, posiadając rower o numerze bike

    while not q.empty():
        time, bike, v = q.get()
        if best_choices[v][bike] < time:
            continue
        if v == end:
            return time

        if bike == -1 and bike_speeds[v]<1:
            if time < best_choices[v][v]:
                #Luiza bierze rower z wierzchołka v, to:
                #Rower znajduje się właśnie w v, więc to naturalne, że jego "numer"
                #(czyli unikalny identyfikator roweru) to właśnie v.
                best_choices[v][v] = time
                q.put((time, v, v))

        for u, weight in graph[v]:
            speed = bike_speeds[bike] # 1 jesli brak roweru w przeciwnym wypadku przelicznik
            time_to_u = time + (weight*speed) # przejechany czas + przeliczony czas z jazdy
            if time_to_u < best_choices[u][bike]:
                best_choices[u][bike] = time_to_u
                q.put((time_to_u, bike, u))



def armstrong(B, G, s, t):
    # zamień G na listę sąsiedztwa
    graph, n = edge_to_adj(G)

    # przygotuj tablicę z najlepszym przelicznikiem prędkości dla każdego wierzchołka
    bike_speeds = [1] * (n + 1)  # 1 = pieszo
    for i, p, q in B:
        bike_speeds[i] = min(bike_speeds[i], p / q)

    return int(dijkstra(graph, bike_speeds, s, t)) # zaokrąglamy w dół

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
