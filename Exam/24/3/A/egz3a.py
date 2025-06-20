from math import inf

from egz3atesty import runtests
from collections import deque

def bfs(adj_g, T, n):
  V = len(adj_g)
  visited_time = [inf] * V
  tree_owner = [-1] * V

  q = deque()

  for i in range(len(T)):
    u = T[i]
    q.append(u)

  while q:
    curr = q.popleft()
    t= visited_time[curr] + 1
    for x in adj_g[curr]:
      if visited_time[x] > t:
        visited[x] = True
        q.append(x)
  ...

def mykoryza( G,T,d ):
  ...

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = False )
