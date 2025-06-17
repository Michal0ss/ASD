from egz2atesty import runtests
from math import inf

def wired(T):
    N = len(T)
    if N == 0:
        return 0
    dp = [[0] * N for _ in range(N)]

    for i in range(2, N+1, 2):
        # i - długość rozważanego podproblemu (musi być parzysta)
        for j in range(N-i+1):
            # j - początek przedziału
            k = j + i - 1
            # k - koniec przedziału
            raw_sum= 1 + abs(T[j] - T[k]) + dp[j+1][k-1]
            min_cost = raw_sum

            for m in range(j+1, k-1, 2):
                cost_diagonal = dp[j][m] + dp[m+1][k]
                if cost_diagonal < min_cost:
                    min_cost = cost_diagonal
            dp[j][k] = min_cost
    return dp[0][N-1]
#def wired(T):
#    """
#    Oblicza minimalny koszt połączenia wejść zgodnie z zadanymi zasadami.
#    Używa programowania dynamicznego.
#
#    Głownym problem zadania jest zauwazanie ze dlugosci tych kabli do polaczenia musza byc parzyste
#    czyli zaczynamy sprawdzac od dlg 2, 4 itd.
#
#    Złożoność czasowa: O(n^3), gdzie 2n to liczba wejść.
#    Złożoność pamięciowa: O(n^2).
#    """
#    N = len(T)
#    if N == 0:
#        return 0
#
#    # dp[i][j] = minimalny koszt sparowania wejść w przedziale [i, j]
#    dp = [[0] * N for _ in range(N)]
#
#    # l - długość rozważanego podproblemu (musi być parzysta)
#    for l in range(2, N + 1, 2):
#        # i - początek przedziału
#        for i in range(N - l + 1):
#            j = i + l - 1
#            cost_outer_pair = (1 + abs(T[i] - T[j])) + dp[i + 1][j - 1]
#            min_cost_for_ij = cost_outer_pair
#
#            # Opcja 2: Problem [i,j] jest rozbity na dwa mniejsze [i,k] i [k+1,j]
#            # Długość [i,k] musi być parzysta, więc k-i+1 jest parzyste.
#            # k przeskakuje co 2.
#            for k in range(i + 1, j - 1, 2):
#                cost_split = dp[i][k] + dp[k + 1][j]
#                if cost_split < min_cost_for_ij:
#                    min_cost_for_ij = cost_split
#
#            dp[i][j] = min_cost_for_ij
#
#    return dp[0][N - 1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wired, all_tests = True )
