from math import inf

from egz2btesty import runtests
from math import inf


def parking(X, Y):
    n = len(X)
    m = len(Y)
    dp = [[inf] * (m + 1) for _ in range(n + 1)]

    for j in range(m + 1):
        dp[0][j] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i][j - 1]
            dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + abs(X[i - 1] - Y[j - 1]))

    return dp[n][m]
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)