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

# zachlanny

# O(n)



#Zawsze jedź jak najdalej się da na jednym baku.
#Jeśli już nie możesz jechać dalej, to tankuj na ostatniej dostępnej stacji, do której dojechałeś.
def refuel(stations, L, destination):
    stations += [0, destination]  # Add starting point and destination
    refuels = []  # Initialize refuels count
    current_fuel = L  # Start with a full tank
    n = len(stations)
    position = 0  # Start at the first station

    while position<n-1:

        next_position = position

        while next_position < n-1 and stations[next_position + 1] - stations[position] <= current_fuel:
            next_position += 1
        if next_position == position:
            # If we can't move forward, we are stuck
            return -1
        if next_position < n-1:
            refuels.append(stations[next_position])

        position = next_position
    return refuels
