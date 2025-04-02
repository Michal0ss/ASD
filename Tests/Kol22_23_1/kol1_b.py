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


"""korzystajac z quick selecta jestesmy w stanie latwo okreslic ktory wyraz jest k-tym najwiekszym poniewaz
po wykonaniu partition """

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        if arr[j] >= pivot:  # >= bo szukamy większych!
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)

    return i + 1

def kthHigher(arr, low, high, k):

    if high>=low:

        index = partition(arr, low, high)

        if index == k:
            return arr[index]

        if index > k:
            return kthHigher(arr, low, index-1,k)

        else:
            return kthHigher(arr, index+1, high,k)

    return None

def ksum(t,k,p):
    sum=0
    n=len(t)
    for i in range(n-p+1):
        sum+= kthHigher(t[i:i+p],0,len(t[i:i+p])-1,k-1)

    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True)
