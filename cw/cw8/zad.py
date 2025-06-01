# Zadanie 1. (Black Forest) Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las
# składa się z n drzew rosnących na pozycjach 0,..., n-1. Dla każdego i € {0,...,n—1} znany jest zysk c_i, jaki
# można osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych
# drzew, ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu
# John znajdzie optymalny plan wycinki.

# f(i) = największy zysk ze ściętych drzew do pozycji i (nie koniecznie drzewo z pozycji i zostało ścięte)
# f(i) = max { f(i - 1), f(i - 2) + C[i] } - albo nie ścinamy drzewa, albo ścinamy

# przypadki graniczne:
# f(0) = C[0]
# f(1) = max {f(0), C[1]}

# wynik f(n - 1)

# Powinna wystarczyć tylko jedna tablica, gdzie nadpisujemy z każdym następnym.

# O(n)

