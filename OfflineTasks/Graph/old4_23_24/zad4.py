#from zad4testy import runtests
from collections import deque

def BFS(G, x, y):
    n = len(G)
    Q=deque()
    visited = [False for v in range(n)]
    visited[x]=True
    Q.append(x)
    while len(Q)>0 and not visited[y]:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                Q.append(v)
    return visited[y]


def Flight(L, x, y, t):
    n = 0
    for u, v, h in L:
        n = max(n, u, v)
    n = n + 1
    G = [[] for _ in range(n)]
    L = sorted(L, key=lambda edge: edge[2])
    i, j, E = 0, 0, len(L)
    while j < E:
        while j < E and L[j][2] - L[i][2] <= 2 * t:
            G[L[j][0]].append(L[j][1])
            G[L[j][1]].append(L[j][0])
            j += 1
        if G[x] != [] and G[y] != [] and BFS(G, x, y):
            return True
        while j < E and L[j][2] - L[i][2] > 2 * t:
            G[L[i][0]].remove(L[i][1])
            G[L[i][1]].remove(L[i][0])
            i += 1
    return False

# # zmien all_tests na True zeby uDruchomic wszystkie testy
#runtests( Flight, all_tests = True )