from math import inf
from queue import PriorityQueue

from egz3atesty import runtests


def matrix_to_adj_list_with_weights(G):
  n = len(G)
  # Zamiana macierzy na listę sąsiedztwa z wagami
  adj = [[] for _ in range(n)]
  for i in range(n):
    for j in range(i+1, n):
      if G[i][j] != -1:
        adj[i].append((j, G[i][j]))
        adj[j].append((i, G[i][j]))

  return adj, n

def goodknight(G, start, t):
  adj_g, n = matrix_to_adj_list_with_weights(G)

  # dist[v][c] = najkrótszy czas dotarcia do v mając c godzin bez snu
  dist = [[inf]*17 for _ in range(n)]
  dist[start][0] = 0
  pq = PriorityQueue()
  pq.put((0,start,0))  # (distance, node, no slep time)

  while not pq.empty():
    time, u, awake = pq.get()
    if u == t:
      return time
    if dist[u][awake] < time:
        continue

    for v, w in adj_g[u]:
      if awake + w <= 16:
        if time + w < dist[v][awake + w]: # relaxacja grafu
          dist[v][awake+w] = time + w
          pq.put((time+w, v, awake + w))
      else:
        # Koszt: obecny czas + 8h odpoczynku + czas podróży w
        next_time = time + 8 + w
        # Nowy czas czuwania po dotarciu do v to po prostu w, bo podróż zaczęła się "na świeżo"
        next_awake = w
        if next_time < dist[v][next_awake]:
          dist[v][next_awake] = next_time
          pq.put((next_time, v, next_awake))

  return min(dist[t])
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )
