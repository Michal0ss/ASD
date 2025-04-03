import queue
from queue import Queue


def czy_dwudzielny(T):
    """mozemy do definicji grafu dwudzielnego dopasowac drzewo binarne
    i pokolrujemy je korzystajac z BFS"""

    n = len(T)
    p =queue.Queue()
    colors = [-1]*n
    p.put(0)
    colors[0] =1
    while not p.empty():
        q = p.get()
        for v in range(n):
            if T[v][q] and colors[v] == -1:
                p.put[v]
                colors[v]=3-colors[q]
            elif T[v][q] and colors[v] == colors[q]: # czy dwa wierzcholki maja ten sam kolor
                return False
    return True