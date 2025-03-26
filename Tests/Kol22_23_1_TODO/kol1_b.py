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

# T = [7, 9, 1, 5, 8, 6, 2, 12]
# k = 4
# p = 5
#Okna:
#[7, 9, 1, 5, 8] → posortowane: [1, 5, 7, 8, 9] → 4-ty największy = 5
#
#[9, 1, 5, 8, 6] → [1, 5, 6, 8, 9] → 4-ty największy = 5
#
#[1, 5, 8, 6, 2] → [1, 2, 5, 6, 8] → 4-ty największy = 2
#
#[5, 8, 6, 2, 12] → [2, 5, 6, 8, 12] → 4-ty największy = 5
#5+5+2+5=17

def ksum():
    ...

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True)
