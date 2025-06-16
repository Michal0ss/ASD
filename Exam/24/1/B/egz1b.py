from math import inf

from egz1btesty import runtests


def kstrong( T, k):
  n = len(T)
  bestof = [[None] * (k + 1) for _ in range(n)]

  def p(i,j):
    if bestof[i][j] == None:
      bestof[i][j] = max(
        T[i], # bierzemy aktualna (zaczynamy ciag)
        p(i-1, j-1) if i > 0 and j> 0 else -inf, # pomijamy liczbe
        T[i] + p(i-1, j) if i > 0 else -inf # bierzemy liczbe i dodajemy do ciagu
      )
      return bestof[i][j]
  return max(p(i,k) for i in range(n))



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = False )
