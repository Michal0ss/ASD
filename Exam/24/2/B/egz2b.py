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

def dijkstra(graph, start, end):

def tory_amos( E, A, B ):
  ...
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = False )
