
from egzP8atesty import runtests
from math import inf
def reklamy ( T, S, o ):
    T.append((inf,inf))
    S.append(0)
    max_val=0
    for x in range(len(T)):
        for y in range(len(T)):
            if T[x][1] < T[y][0] or T[y][1] < T[x][0]:
                max_val =  max(max_val, S[x] + S[y])
    return max_val

runtests ( reklamy, all_tests=True )