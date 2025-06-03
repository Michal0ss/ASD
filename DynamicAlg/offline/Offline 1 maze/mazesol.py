from zad7testy import runtests
from math import inf


def maze(L):
    N = len(L)
    col0 = [-inf] * N  # the last column
    col1 = [-inf] * N  # the column that's currently being processed

    col1[0] = -1
    for x in range(N):
        col0, col1 = col1, col0

        # scan downwards
        last = -inf
        for y in range(N):
            if L[y][x] == '.':
                last = max(last, col0[y]) + 1
            else:
                last = -inf
            col1[y] = last

        # scan upwards
        last = -inf
        for y in range(N)[::-1]:
            if L[y][x] == '.':
                last = max(last, col0[y]) + 1
            else:
                last = -inf
            col1[y] = max(col1[y], last)
    return max(col1[-1], -1)

runtests(maze, all_tests=False)


