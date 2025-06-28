from math import inf
from queue import PriorityQueue
from jumpertesty import runtests

def convert(graph):
    n = len(graph)
    new_graph = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if graph[u][v]:
                new_graph[u].append([v, graph[u][v]])
                new_graph[v].append([u, graph[u][v]])

    return new_graph

def jumper(G,s,e):
    """
    dist[i][0] przechowuje najkrótszy koszt dotarcia do wierzchołka i kończąc ruchem normalnym.
    dist[i][1] przechowuje najkrótszy koszt dotarcia do wierzchołka i kończąc dwumilowym skokiem.
    """
    n = len(G)
    adjl=convert(G)
    dist = [[inf]*2 for _ in range(n)]
    dist[s][0] = 0
    pq = PriorityQueue()
    pq.put((0,s,0)) # distance, start, flag=0 czyli poprzedni ruch nie byl skokiem


    # teraz kluczowe jest rozbicie na przypadki
    # pierwszy przypadek gdy flaga = 1 czyli gdy poprzedni skok dwumilowy
    # else: wykonuje skok dwumilowy badz trzecia opcja wykonuje skok dwumilowy
    while not pq.empty():
        w, u, f = pq.get()
        if f == 1:
            for v,d in adjl[u]:
                new_cost = d + w
                if dist[v][0]>new_cost:
                    dist[v][0] = new_cost
                    pq.put((new_cost, v, 0))
        else:
            # normalny skok
            for v, d in adjl[u]:
                new_cost = d + w
                if dist[v][0] > new_cost:
                    dist[v][0] = new_cost
                    pq.put((new_cost, v, 0))

            # skok dwumilowy
            for v, d in adjl[u]:
                for x,wx in adjl[v]:
                    if u!=x:
                        jump_cost = max(d,wx)
                        new_cost = w + jump_cost
                        if dist[x][1] > new_cost:
                            dist[x][1] = new_cost
                            pq.put((new_cost, x, 1))
    return min(dist[e][0], dist[e][1])

runtests(jumper)