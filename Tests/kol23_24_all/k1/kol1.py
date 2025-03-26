

# Dana jest n-elementowa tablica liczb naturalnych T. Dla każdego indeksu i < n, rangą elementu
# na pozycji i określamy liczbę elementów, które w tablicy występują przed elementem i-tym, a ich
# wartość jest mniejsza od T [i].
# Proszę zaimplementować funkcję maxrank(T), która dla tablicy T o rozmiarze n elementów zwróci
# maksymalną rangę pośród wszystkich elementów tablicy.
from kol1testy import runtests



def maxrank(t):
    n = len(t)
    ranks = [0 for _ in range(n)]
    enum = [(val, idx) for idx, val in enumerate(t)]

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr  # Zwracamy posortowaną jednoelementową listę

        mid = len(arr) // 2
        l = arr[:mid]
        r = arr[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i][0] < r[j][0]:
                arr[k]=l[i]
                i += 1
            else:
                val, idx = r[j]
                ranks[idx] += i  # Liczba elementów z lewej mniejszych
                arr[k]=r[j]
                j += 1
            k+=1

        while i < len(l):
            arr[k]=l[i]
            i += 1
            k+=1

        while j < len(r):
            val, idx = r[j]
            ranks[idx] += i
            arr[k]=r[j]
            j += 1
            k+=1

        return arr

    merge_sort(enum) # wywoluje merge sorta dla tablicy tuple gdzie [(oryginalna liczba, oryginalny idx tablicy),...]

    return max(ranks)

# Testy
runtests(maxrank, all_tests=True)
