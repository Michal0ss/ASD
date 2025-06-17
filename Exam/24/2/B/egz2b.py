from copyreg import dispatch_table
from math import inf
from queue import PriorityQueue

from egz2btesty import runtests

# 5 Jednostek czasu za wjechanie i wyjechanie linia indyjska
# 10 jednostek czasu za wjechanie i wyjechanie linia przylądkowa
# 20 jednostek czasu za zmiane rozstawy szyn

# odstepy miedzy stacjami nie max 10km
def edge_to_adj(edges):
  N= max([x for x,y,w,type in edges] + [y for x,y,w,type in edges]) + 1
  adj_list =  [[] for _ in range(N)]
  for x,y,w,type in edges:
    adj_list[x].append(y, w, type)  # dodaj krawedz x->y
    adj_list[y].append(x, w, type)  # dodaj krawedz y->x
  return adj_list, N


def dijkstra(G, start, end):
    """
    graph: adjacency list, where graph[u] = list of (v, weight, type) tuples
    start: starting node index
    end: ending node index
    Returns: shortest distance from start to end
    """
    n = len(G)
    di = [inf] * n
    dp = [inf] * n

    pq = PriorityQueue()
    pq.put((0, start, None))  # (distance, node, type)
    di[start] = 0# najlepsze tymczasowe koszty dla indyjskiej linii
    dp[start] = 0# najlepsze tymczasowe koszty dla przylądkowej linii


    while not pq.empty():
        u_weight, u, type = pq.get()
        if u == end: break
        if u_weight > di[u] and u_weight > dp[u]:
            continue

        for v,w,new_type in G[u]:
          if type == None:
            if new_type == 'I':
                di[v] = w
            else:
                dp[v] = w
          elif type == new_type:
            if type == 'I':
              c=di[u] + w + 5
              if di[v]>c:
                di[v] = c
                pq.put((c, v, type))
            else:
              c=dp[u] + w + 10
              if dp[v]>c:
                dp[v] = c
                pq.put((c, v, type))
          else:
            if new_type == 'P':
              c=dp[u] + w + 20
              if di[v]>c:
                di[v] = c
                pq.put((c, v, new_type))
            else:
              c=di[u] + w + 20
              if dp[v]>c:
                dp[v] = c
                pq.put((c, v, new_type))






    return di[end]

def tory_amos( E, A, B ):
  ...
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = False )
