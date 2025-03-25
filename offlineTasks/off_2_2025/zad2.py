from zad2testy import runtests

#Dana jest tablica T zawierająca liczby naturalne. Proszę napisać funkcję count inversions(T),
#która dla tablicy zwraca liczbę inwersji w tablicy.

"""
Funkcja count_inversions liczy inwersje czyli: 
Inwersja w tablicy to para indeksów (i, j), taka że i < j oraz A[i] > A[j].
Zatem wykonuje to za pomoca sortowania przez scalanie (merge sort) korzystajac z divide and conquer dzielimy rekurencyjne 
na coraz to mniejsze fragmety. Posortowany lewy i prawy fragment tablicy pozwala okreslic ile jest inwersji
ponieważ jesli dla np tablicy [2,4,1,5,3] podzielimy na pol i posrtujemy te polowy: [2,4] i [1,5,3] to ilosc inwersji 
bedzie rowna ilosci wykonanych sortowan czyli w tablicy r (prawej) [1] [5<->3] = [1] [3,5] scalamy i mamy [1,3,5] i poprawilismy
jedna inwersje czyli licznik 0: inwersja+=1 dla tablicy l jest juz posortowana wiec wykonujemy glowne scalanie
1: 2>1=inwersja+=1 
2: 2<3
3: 4>3=inwersja+=1
4: 4<5
tablica = [1,2,3,4,5]
inwersja = 3 

"""
def count_inversions(arr):

    if len(arr)<=1:
        return 0

    mid = len(arr)//2

    l=arr[:mid]
    r=arr[mid:]

    inversion_l = count_inversions(l)
    inversion_r = count_inversions(r)
    i=j=k=0

    inversion_merge=0

    while i<len(l) and j<len(r):
        if l[i]<=r[j]:
            arr[k]=l[i]
            i+=1
        else:
            arr[k]=r[j]
            j+=1
            inversion_merge+=len(l)-i # inversions
            #left[i] <= left[i+1] <= ...)
        k+=1

    while i<len(l):
        arr[k]=l[i]
        i+=1
        k+=1

    while j<len(r):
        arr[k]=r[j]
        j+=1
        k+=1


    return inversion_merge + inversion_l + inversion_r


# Odkomentuj by uruchomic duze testy
# runtests( strong_string, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
runtests( count_inversions, all_tests=True )
