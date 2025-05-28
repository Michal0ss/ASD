from zad6testy import runtests


def parking(X, Y):
    n = len(X)
    m = len(Y)

    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    for i in range(m+1):
        dp[0][i] = 0

    for x in range(1,n+1):
        for y in range(1,m+1):
            cost = abs(X[x-1]-Y[y-1])
            dp[x][y]  = min(dp[x][y-1], dp[x-1][y-1] + cost)

    return dp[n][m]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=False)
