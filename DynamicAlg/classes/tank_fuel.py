# Czołg jedzie z punktu A do punktu B. Spalanie czołgu to
# dokładnie jeden litr paliwa na jeden kilometr trasy. W baku miesci sie dokładnie L litrów paliwa. Trasa z A
# do B to prosta, na której znajduja sie stacje benzynowe (na pozycjach bedacych liczbami naturalnymi; A
# jest na pozycji 0). Prosze podac algorytmy dla nastepujacych przypadków:

# (1) Wyznaczamy stacje na których tankujemy tak, zeby łaczna liczba tankowan była minimalna.

# (2) Wyznaczamy stacje tak, zeby koszt przejazdu był minimalny (w tym wypadku kazda stacja ma dodatkowo
# cene za litr paliwa). Na kazdej stacji mozemy tankowac dowolna ilosc paliwa.

# (3) j.w., ale jesli na stacji tankujemy, to musimy zatankowac do pełna.
# algorytm dynamiczny. F(i, fuel) - minimalny koszt dotarcia do stacji 'i', majac w zapasie 'fuel' litrow paliwa
# F(0, 0) = 0
# F(0, fuel) = float('inf') (odrzucamy takie rozwiazania), gdzie fuel > 0
# F(i, k) = min( F(i - 1, k + D[i - 1][i], min( F(i - 1, z) + (L - z) * C[i - 1] ), po 0 <= z <= L, D[i - 1][i] == L - k  )


# Podpunkt (1) --------------------------------------

def next_station_search(S, left, right, val):
    while left <= right:
        mid = (left + right) // 2
        if val < S[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return right

def min_refuels(stations, L, destination, fuel):

    n = len(stations)

    firstStation = next_station_search(stations, 0, n - 1, fuel)
    lastStation = next_station_search(stations, 0, n-1, destination)

    if stations[0] > fuel: return -1
    if fuel >= destination: return 0

    counter = 0
    position = firstStation

    while position<lastStation:
        counter += 1
        nextStop = next_station_search(stations, position + 1, lastStation, stations[position] + L)

        if nextStop == position:
            return -1
        position = nextStop

    return counter if destination - stations[lastStation] <= L else -1

# Podpunkt (2) --------------------------------------->TODO




