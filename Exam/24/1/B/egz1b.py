from math import inf
from egz1btesty import runtests

"""wystarczy nie patrzec na odcinanie poszczegolnych fragmentow bo wowczas zlozonosc bedzie tragiczna.
Zatem problem rozwiazujemy liczac tylko maksymalne sumy dla podproblemow jak to zazwyczaj w dp.
Tworzymy liste o dlugosci k+1 na n i zapisujemy sumy dla itego elementu tablicy t dp[i] = max(T[i], dp[i-1] + T[i])
wtedy sumy fragmentow ladnie nam sie wpisza w tablice dp. """
def kstrong( T, k):
    n = len(T)
    dp = [[0]*(k+1) for _ in range(n)]
    max_sofar = -inf
    for i,num in enumerate(T):
        for j in range(k+1):

            if num >= 0: # wowczas nie polepszy to naszej sumy wiec nie bierzemy tego pod uwage w szukaniu maksimum
                dp[i][j] = dp[i-1][j] + num
            else:
                if j==0:
                    dp[i][j] = max(0, dp[i-1][j] + num)
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j] + num) # max(poprzedni element z poprzednim k, poprzedni element z nowym k)
            max_sofar = max(max_sofar, dp[i][j])
    return max_sofar
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = False )
