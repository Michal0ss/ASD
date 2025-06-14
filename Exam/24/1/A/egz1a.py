from queue import PriorityQueue

from egz1atesty import runtests



def edge_to_adj(edges):
  # zeby znalezc ilosc wierzcholkow, potrzebujemy znalezc maksymalny indeks wierzcholka
  N = max([a for a,b, _  in edges]  + [b for a,b, _ in edges]) + 1
  adj_l = [[] for _ in range(N)]

  for u,v,w in edges:
    adj_l[u].append((v,w)) # dodaj krawedz u->v
    adj_l[v].append((u,w)) # dodaj krawedz v->u (graf nieskierowany)
  return adj_l, N

#def change_weight(B,i_B, w_next):
#  p=B[i_B][1]
#  q=B[i_B][2]
#  new_weight = (w_next * p )// q
#  return new_weight

def get_B_idx(B):
  vertecies = []
  for i,p,q in B:
    vertecies.append(i)
  return vertecies

def dijkstra(B, G, start, end):
  bike_idx = get_B_idx(B)
  n = len(G)
  dist = [float('inf')] * n
  dist[start] = 0
  pq = PriorityQueue()
  pq.put((0, start))  # (distance, node)

  while not pq.empty():
    d, u = pq.get()
    if dist[u]  < d:
      continue
    for v, w in G[u]:
      scaled_w = w
      if u in bike_idx:
        p,q= B[u][1], B[u][2]
        scaled_w = (w * p) // q  # zmieniamy wagę zgodnie z rowerem
      if dist[v] > d + scaled_w:
        dist[v] = d + scaled_w
        pq.put((dist[v], v))
  return dist, dist[end]


def armstrong( B, G, s, t):
  #B - lista rowerow z p i q ktore sa przelicznikami wagi w*p/q
  n_G, N = edge_to_adj(G)
  root1, end=dijkstra(n_G, s, t)



  return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = False )
