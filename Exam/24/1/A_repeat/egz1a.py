from math import inf, floor
from multiprocessing.resource_tracker import unregister
from queue import PriorityQueue

from egz1atesty import runtests



def edge_to_adj(edges):
  # zeby znalezc ilosc wierzcholkow, potrzebujemy znalezc maksymalny indeks wierzcholka
  N = max([a for a,b, _  in edges]  + [b for a,b, _ in edges]) + 1
  adj_l = [[] for _ in range(N)]

  for u,v,w in edges:
    adj_l[u].append((v,w)) # dodaj krawedz u->v
    adj_l[v].append((u,w)) # dodaj krawedz v->u (graf nieskierowany)
  return adj_l

#def change_weight(B,i_B, w_next):
#  p=B[i_B][1]
#  q=B[i_B][2]
#  new_weight = (w_next * p )// q
#  return new_weight

def dijkstra(G, start, end):
  n= len(G)
  dist = [inf] * n
  dist[start] = 0

  pq = PriorityQueue()
  pq.put((0,start))

  while not pq.empty():
    wu,u = pq.get()
    if u == end:
      break
    for v,w in G[u]:
      #relaksacja
      if dist[v] > wu+w:
        dist[v] = wu+w
        pq.put((dist[v], v))

  return dist

def armstrong( B, G, s, t):
  nG = edge_to_adj(G)
  n=len(nG)
  bikes=[1]*n
  for v,p,q in B:
    if bikes[v] > p/q:
      bikes[v] = p/q

  distance = dijkstra(nG, s, t)
  min_dist = distance[t]
  distance_reversed = dijkstra(nG, t, s)

  for i in range(n):
    cost = distance[i] + (distance_reversed[i]*bikes[i])
    if cost < min_dist:
      min_dist = cost
  return floor(min_dist) if min_dist != inf else inf



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
