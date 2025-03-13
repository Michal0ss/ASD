from pydoc import visiblename

from zad1testy import runtests

# Mówimy, że dwa napisy są sobie równoważne, jeśli albo są identyczne, albo byłyby identyczne,
# gdyby jeden z nich zapisać od tyłu. Na przykład napisy “kot” oraz “tok” są sobie równoważne,
# podobnie jak napisy “pies” i “pies”. Dana jest tablica T zawierająca n napisów o łącznej długości
# N (każdy napis zawiera co najmniej jeden znak, więc N ≥ n; każdy napis składa się wyłącznie z
# małych liter alfabetu łacińskiego). Siłą napisu T[i] jest liczba indeksów j takich, że napisy T[i]
# oraz T[j] są sobie równoważne. Napis T[i] jest najsilniejszy, jeśli żaden inny napis nie ma większej
# siły.

# Proszę zaimplementować funkcję g(T), która zwraca siłę najsilniejszego napisu z tablicy T. Na
# przykład dla wejścia:

# #     0       1       2       3       4       5       6
# T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]

# wywołanie g(T) powinno zwrócić 3. Algorytm powinien być możliwie jak najszybszy. Proszę podać
# złożoność czasową i pamięciową zaproponowanego algorytmu.

def reversed_str(s):
    return s[::-1]

def strong_string(T):
    """korzystajac z mniej leksykograficznej wersji napisu i z wykorzystaniem slownika str_power
        tworze porownania o zlozonosci O(n)"""

    n=len(T)
    str_power = {}

    for element in T:
        key = min(element, reversed_str(element))
        str_power[key] = str_power.get(key, 0) + 1  # we are retrieving  value from dictionary and adding 1
                                                    # syntax: .get(our key, value returned if key not found)
    return max(str_power.values()) # maximum power of a single str


#def huge_complexity(T):
#    """method with 0(n^2) complexity just for self education how not to build algorithms"""
#    n = len(T)
#    max_amount = -1  # Stores the max strength of a string
#
#    visited = [0 for _ in range(n)]  # Track visited elements
#
#    for i in range(n):
#        if visited[i] == 1:  # Skip already counted elements
#            continue
#
#        count = 1  # Start counting with the current element
#        visited[i] = 1  # Mark as visited
#
#        for j in range(i + 1, n):  # Check the rest of the list
#            if visited[j] == 0 and (T[i] == T[j] or reversed_str(T[i]) == T[j]):
#                count += 1
#                visited[j] = 1  # Mark matched element as visited
#
#        max_amount = max(max_amount, count)  # Update max strength
#
#    return max_amount


# Zakomentuj gdy uruchamiasz duze testy
runtests( strong_string, all_tests=False )
# Odkomentuj by uruchomic duze testy
# runtests( strong_string, all_tests=True )