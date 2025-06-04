# Między punktem A a pkt B jedzie traktor. Spala on 1 l / 1 km.
# L - pojemność baku traktora.
# P_i - koszt na itej stacji

# Traktor jedzie po prostej, na której znajdują się stacje benzynowe - są to liczby naturlane.
# S1, S2, S3....

# Chcemy wyznaczyć rozwiązania do problemów:

# 1) Wybrać stacje tak, by liczba tankowań była minimalna.
# 2) Wyznaczamy stacje tak by koszt przejazdu był minimalny. Mamy podane ceny paliwa i pozycje stacji.
# Zakładamy tutaj, że można tankować dowolną ilość paliwa.
# 3) Jak wyżej, ale jeśli tankujemy na stacji to musimy zatankować do pełna.

# Ad.
# 1) Tankujemy do pełna (zawsze).
# Zakładam, że tankowałem wcześniej, a potem, że później.
# Pokazuję, że da się to rozwiązanie poprawić, więc lepiej jest zawsze tankować wcześniej.
# Załóżmy, że potrafimy dojechać zarówno do P1 i P2 na aktualnym stanie baku.
# Załóżmy, że tankuję w P1, jadę do P2: liczba paliwa = L-p1+p2
# Jeśli zatankujemy w P2, to w punkcie L2 (dalszym) mam paliwa L zamiast L-p1+p2 i tankowań też jest i, co
# jest optymalniejszym rozwiązaniem.

# O(n)

