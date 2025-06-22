from math import inf
from egz1btesty import runtests


def planets(D, C, T, E):
    n = len(D)

    costs = [[inf] * (E+1) for _ in range(n)]
    costs[0][0] = 0

    for i in range(n-1):
        for j in range(1,E+1):
            costs[i][j] = min (costs[i][j], costs[i][j-1] + C[i])
        if T[i][0]>i:
            costs[T[i][0]][0] = min(costs[T[i][0]][0], costs[i][0] + T[i][1])
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=True)