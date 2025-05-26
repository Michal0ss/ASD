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


def merge_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    mid = n//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_arr = []
    i=j=0

    #merge
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i+=1
        else:
            sorted_arr.append(right[j])
            j+=1

    #scal pozostala reszte
    while i<len(left):
        sorted_arr.append(left[i])
        i+=1

    while j<len(right):
        sorted_arr.append(right[j])
        j+=1
    return sorted_arr


def strong_string(T):
    """Uzywamy sortowanie merge sort o zlozonosci NlogN aby przy pomocy kolejnosci leksykograficznej
    posortowac nasz liste a nastepnie normalizujemy nasze wyrazy przy pomocy funkci min() sprawdzajac
    co ma mniejsza wartosc leksykograficzna np wyraz kot czy tok odwracajac go za pomoca slicingu [::-1], wowczas
    zostanie nam posortowana lista o powtarzajacych sie wyrazach np: [kot, kot, kot, pies, pies]

    Na koniec liczymy moc kazdego wyrazu jedna petla na od 1 do n zatem koncowa zlozonosc to NlogN
    poniewaz w przypadku calego programu O(n) + O(nlogn) + O(n) = O(nlogn)"""

    n=len(T)

    norml=[ min(s,s[::-1]) for s in T] # normalizuje cala tablice
    sorted_normalize = merge_sort(norml) #nastepnie za pomoca scalania ja sortuje

    max_counter=1
    current = 0

    for i in range(1,n):
        if sorted_normalize[i-1]==sorted_normalize[i]:
            current+=1
        else:
            max_counter = max(max_counter,current)
            current=1
    max_counter=max(max_counter,current)

    return max_counter



runtests( strong_string, all_tests=True )
