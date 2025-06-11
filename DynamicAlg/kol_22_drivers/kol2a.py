from math import inf

from kol2atesty import runtests

def drivers(P, B):
    n = len(P)  # ilosc punktów
    points = sorted([(P[i][0], P[i][1], i) for i in range(n)]) # points[i] = (pozycja,czy_przesiadkowy,idx)
    points.append((B, False, -1))
    n += 1

    dp = [[[inf] * 2 for _ in range(3)] for _ in range(
        n)]  # dp[i][change][marian] - najmniejszy koszt dojechania od miejsca i z change (ilosc pktow kontrolnych od ostatniej przesiadki) i z marianem/jackiem 1/0
    changes = [[[[],[]] for _ in range(3)] for _ in
               range(n)]  # changes[i][change][marian] - tablica punktow przesiadkowych w ktorym przesiadami się
    # wiemy ze zeby dojechac z miasta ostatniego (Czyli B) do miasta B to koszt to 0
    for change in range(3):
        for marian in range(2):
            dp[n - 1][change][marian] = 0
    for i in range(n - 2, -1, -1):
        pos, pkt_przesiadkowy, idx = points[i]
        for change in range(3):
            for marian in range(2):
                if pkt_przesiadkowy:
                    if change < 2:
                        bez_przesiadki = dp[i + 1][change + 1][marian]
                        if dp[i][change][marian] > bez_przesiadki:
                            dp[i][change][marian] = bez_przesiadki
                            changes[i][change][marian] = changes[i + 1][change + 1][marian]

                    z_przesiadka = dp[i + 1][0][1 - marian]
                    if dp[i][change][marian] > z_przesiadka:
                        dp[i][change][marian] = z_przesiadka
                        changes[i][change][marian] = [idx] + changes[i + 1][0][1 - marian]
                else:  # pkt kontrolny
                    if marian == 1:
                        dp[i][change][marian] = min(dp[i][change][marian], dp[i + 1][change][marian] + 1)
                    else:
                        dp[i][change][marian] = min(dp[i][change][marian], dp[i + 1][change][marian])
                    changes[i][change][marian] = changes[i+1][change][marian]

    return changes[0][0][0]


# Uruchomienie testów
runtests(drivers, all_tests=True)
