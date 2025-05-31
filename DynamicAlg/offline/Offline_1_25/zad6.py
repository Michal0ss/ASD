from zad6testy import runtests

# Michal Bialas
"""Funkcja polega na znalezeniu minimalnej sumy kosztów parkowania samochodów.
Obliczam sume za pomoca tablicy dp o wymiarach (n+1) x (m+1), gdzie n to liczba samochodów.
Która w pierwszym wierszu  ma sama zera a w calej reszcie inf.
obliczjac koszt kolejnych róznic pomiedzy i-tym elementem z tablicy X a J-tym elementem z tablicy Y.
Zapisujemy ten koszt w tablicy i zmieniamy wartosci za pomca funkcji min aby znalezc minimalna sume kosztów.
porownujemy wartosc poprzednia z tego samego wiersza (nie zmieniamy nic w nastepnej kolumnie) z 
wartoscia z poprzedniego wiersza i kolumny, dodajac koszt parkowania.
W taki sposób rozwiązując mniejsze problemy i zapisując ich wyniki w tablicy dp, calosc algorytmu podaje nam w 
ostatniej komórce tablicy dp[n][m] minimalny koszt parkowania wszystkich samochodów.

"""

def parking(X, Y):
    n = len(X)
    m = len(Y)

    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    for j in range(m+1):
        dp[0][j] = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            cost = abs(X[i-1]-Y[j-1])
            dp[i][j]  = min(dp[i][j-1], dp[i-1][j-1] + cost)

    return dp[n][m]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=False)
