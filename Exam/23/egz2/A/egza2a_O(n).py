from kiwisolver import strength
from numpy.ma.core import greater

from egz2atesty import runtests

def dominance(P):
    max_x = max(P, key=lambda p: p[0])[0]  # znajdź maksymalne x
    max_y = max(P, key=lambda p: p[1])[1]  # znajdź maksymalne y

    greaterX = [0] * (max_x + 1)  # tablica do przechowywania liczby punktów o większym x
    greaterY = [0] * (max_y + 1)  # tablica do przechowywania liczby punktów o większym y
    equalX = [0] * (max_x + 1)  # tablica do przechowywania liczby punktów o równym x

    for x,y in P:
        greaterX[x] += 1
        greaterY[y] += 1
        equalX[x] += 1

    for x in range(1, max_x + 1): # oblicz liczbę punktów o większym x
        greaterX[x] += greaterX[x - 1]
    for y in range(max_y-1, -1, -1): # oblicz liczbę punktów o większym y
        greaterY[y] += greaterY[y + 1]

    max_strength = []
    for x,y in P:
        strength = greaterX[x] - greaterY[y] + equalX[x] + 1
        max_strength.append(strength)
    return max(max_strength)  # zwróć maksymalną dominację

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
