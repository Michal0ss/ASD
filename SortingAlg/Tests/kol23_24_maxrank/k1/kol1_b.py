# Dana jest n-elementowa tablica liczb naturalnych T. Dla każdego indeksu i < n, rangą elementu
# na pozycji i określamy liczbę elementów, które w tablicy występują przed elementem i-tym, a ich
# wartość jest mniejsza od T [i].
# Proszę zaimplementować funkcję maxrank(T), która dla tablicy T o rozmiarze n elementów zwróci
# maksymalną rangę pośród wszystkich elementów tablicy.

from kol1testy import runtests

def swap(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]

def partition(T,p,r):
    pivot = T[r]
    i=p-1
    for j in range(p,r):
        if T[j]<pivot:
            i+=1
            swap(T,i,j)

    swap(T,i+1, r)
    return i+1
def quick_sort(arr, low, high):
    if low<high:
        pi = partition(arr,low,high)

        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

def maxrank(arr):
    n = len(arr)

    for i in range(n):
        arr[i] = (arr[i], i)

    quick_sort(arr, 0, n-1)

    max_rank = 0
    i = n-1

    while i>max_rank:
        idx = arr[i][1]

        #jesli mamy te same cyfry  na roznych indeksach np [7,7,7]
        while i>0 and arr[i-1][0] == arr[i][0]:
            i-=1
            if arr[i][1]>idx:
                idx=arr[i][1]

        # ranga= oryginalny index - ile mniejszych elementow znajduje sie za liczba o indeksie i
        rank=idx-(n-i-1)

        # aktualizacja maksymalnej rangi
        if rank>max_rank:
            max_rank=rank
        i-=1
    return max_rank



# Testy
runtests(maxrank, all_tests=True)
