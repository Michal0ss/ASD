'''
Michal Bialas ft.Szymon Pytel
Tablica G opisuje sasiadow dla wierzcholkow o numerze takim jak indeks
V to drzewa, a E to systemy korzeniowe
Z rosnaca jednostka czasu grzyby sie rozrastaja o swoich sasiadow, jesli oba trafia do jednego drzewa
w jednym momencie, wygrywa grzyb o mniejszym indeksie
Moim pomyslem jest zasymulowac rozrastanie sie wszystkich grzybow w tym samym czasie
na biezaco przypisujac wierzcholkom numer grzyba
Skoro po jednej jednostce czasu rosniemy o sasiadow kazdego wierzcholka, pasuje nam tutaj BFS
w ktorym na poczatku ustawiamy pozycje startowe grzybow oraz idac po sasiadach
zapisujemy indeks grzybowy
Co wiecej, rozwiazanie gwarantuje zlozonosc wzorcowa
'''
from egz3atesty import runtests
from collections import defaultdict
from collections import deque

def BFS(graph, T):
  visited = set()
  queue = deque()

  for i in range(len(T)):
    visited.add(T[i])
    queue.append((T[i], i))

  order = []
  while queue:
    (s, t) = queue.popleft()
    order.append((s, t))
    cur_t = t
    for neighbor in graph[s]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor, cur_t))
  return order


def mykoryza( G,T,d ):
  graph = defaultdict(list)
  for node in range(len(G)):
    graph[node] = G[node]
  print(graph)

  order = BFS(graph, T)
  ctr = 0
  for node, type in order:
    if type == d:
      ctr += 1
  return ctr


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )