from kol3testy import runtests

def orchard(T, m):
    dp = [-1] * m
    dp[0] = 0
    for v in T:
        nu = dp[:]
        for i in range(m):
            if dp[i] < 0: continue
            j = (i+v) % m
            nu[j] = max(nu[j], dp[i] + 1)
            # jesli wezme element ktory %m=0 wowczas do pierwszego
            # elementu tablicy dodaje +1 zatem dp[0] to ilosc elementow podzielnych przez m
            # reszty dzielen zapisuje w indeksach odpowiadahcym reszcie i wykorzystuje
            # je do kolejnych iteracji aby moc stworzyc sume z nastepnym elementem ktorej modulo m == 0
            # wtedy dodaje +1 przez co za pomoca pierwszego ifa juz nie dodam tej reszty do dp[0] i zwiekszam licznik o 1

            # np: Iteracja 3: dodajemy 7
        # 0 + 7 = 0 → dp[0] = max(0, 0+1) = 1
        #
        # 2 + 7 = 2 → dp[2] = max(1, 1+1) = 2
        #
        # 4 + 7 = 11 % 7 = 4 → dp[4] = max(2, 2+1) = 3

        # 2, 4 to sa reszty z poprzednich iteracji, a 0 to reszta z obecnej iteracji
        
        dp = nu
    return len(T) - dp[0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests = True)
