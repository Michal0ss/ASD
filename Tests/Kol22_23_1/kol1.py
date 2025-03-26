"""

Algorytm w czesci glownej, w petli for, ktora wykona sie n - p + 1 razy ( poniewaz mamy znalezc sumy od z_0 do z_(n-p ) ), tworzy pomocnicza
tablice o dlugosci ( p - 1 ) i wykonuje na niej algorytm QuickSelect. Funkcja Quick Select zwraca wartosc, ktora znalazla by sie 
w pomocniczej tablicy po posortowaniu jej. Korzysta przy tym z funkcji Partition ( w tym przypadku dziala ona odwrotnie niz zazwyczaj tj. elementy
wieksze przerzuca na lewo, a elementy mniejsze na prawo od pivota). Jest tak, bo chcemy znalezc k-ty najwiekszy element po posortowaniu.
Wyniki poszczegolnych sum, dodaje do zmiennej sup, ktora zostaje na koncu zwrocona.

Zlozonosc QuickSelecta to O(p). Wywoluje go n razy, wiec zlozonosc ogolna to O(np)

"""


from kol1testy import runtests

"""Dana jest n-elementowa tablica liczb naturalnych T oraz dodatnie liczby naturalne k i p, gdzie
k ≤ p ≤ n. Niech zi będzie k-tą największą spośród elementów: T[i], T[i+1], ..., T[i+p-1]. Innymi
słowy, zi to k-ty największy element w T w przedziale indeksów od i do i + p − 1 włącznie.
Doprecyzowanie: Rozważmy tablicę [17,25,25,30]. W tej tablicy 1-wszy największy element
to 30, 2-gi największy element to 25, 3-ci największy element to także 25 (drugie wystąpienie), a
4-ty największy element to 17.
Proszę zaimplementować funkcję ksum(T, k, p), która dla tablicy T (o rozmiarze n elementów) i
dodatnich liczb naturalnych k i p (k ≤ p ≤ n) wylicza i zwraca wartość sumy:
z0 + z1 + z2 + . . . + zn−p
"""

def partition(T, left, right):
    i = left - 1
    #
    for j in range(left, right):
        #
        if T[j] > T[right]:
            i += 1
            T[j], T[i] = T[i], T[j]
        #
    #
    T[i+1], T[right] = T[right], T[i+1]

    return i + 1 
#end def ^^^


def select(A,k, left, right):
    if right >= left:
        pivot = partition(A, left, right)
        if k == pivot: return A[k]
        elif k < pivot: return select(A, k, left, pivot - 1)
        else: return select(A,k, pivot + 1, right)
    #
#end def


def ksum(T, k, p):
    n = len(T)
    sum = 0
    #
    for i in range( n - p + 1 ):
        A = T[ i : i + p ]
        value = select(A, k - 1, 0, len(A) - 1)
        sum += value
    #
    return sum
#end def ^^^


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=False)
