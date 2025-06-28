# tanagram czyli jesli dwa sslowa maja te same litery i mozemy z jednego zrobic durgie przesuwajac o
# pozycje dlugosci najwyzej t
from tanagramtest import runtests

def tanagram(x, y, t):
    n = len(x)
    if len(x) != len(y):
        return  False
    istaken = [False] * n
    for i in range(n):
        start_j = max(0, i-t)
        end_j = min(n, i+ t + 1)
        for j in range(start_j, end_j):
            if x[i] == y[j] and not istaken[j]:
                istaken[j] = True
                break
        else:
            return False
    return True

runtests(tanagram)