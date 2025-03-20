

from zad2testy import runtests
"""
Opis algorytmu:
Algorytm wykorzystuje strukture kopca max, stad dodatkowe funkcje pomocnicze: heapify, buildheap.
Dzialanie algorytmu polega na zbudowaniu kopca z podanej tablicy z danymi, a nastepnie 
dodawanie do zmiennej sum_snow najwiekszych elementow tablicy tj. korzenia kopca T[0], dopoki
jest snieg (dopoki nie stopnial tj. S[0] - pom > 0 ). 
Korzystam z kopca max, gdyz nie ma potrzeby sortowac calej tablicy, bo snieg topnieje.

Tak przedstawiony algorytm dziala, gdyz to, czy zaczniemy brac snieg od wejsc, czy od elementu najwiekszego
nie ma znaczenia - suma zebranego sniegu bedzie taka sama, bo ten topnieje. Najlepiej opisac to na przykladzie:
S = [15,16,3,59,24,16]. Widac, ze najlepiej zaczac od prawej strony i wziac 16,24,59 itd ; suma sniegu to bedzie
16 + 23 + 57 = 96 itd..., ale te sama sume dostaniemy, gdy wezmiemy 59 + 23 + 14 = 96 , gdyz snieg stopnial 
w kazdym przypadku o 3. Widzimy wiec, ze nie ma znaczenia efektywny wybor sniegu z wejsc, 
czy branie go od wartosci najwiekszych w "posortowanej" tablicy.

Zlozonosc O(nlogn)
"""

"""System chłodzenia serwerów na pewnej uczelni wymaga stałych dostaw śniegu. 
Grupa zmotywowanych profesorów odnalazła w wysokich górach wąwóz, z którego można przywieźć śnieg. Wąwóz jest
podzielony na n obszarów i ma wjazdy z zachodu i wschodu. Na każdym obszarze wąwozu znajduje
się pewna ilość śniegu, opisana w tablicy S. W szczególności S[0] to liczba metrów sześciennych
śniegu bezpośrednio przy zachodnim wjeździe, S[1] to liczba metrów sześciennych śniegu na kolejnym obszarze, 
a S[n−1] to liczba metrów sześciennych śniegu przy wjeździe wschodnim (wiadomo,
że zawartość tablicy S to liczby naturalne). Profesorowie dysponują maszyną, która danego dnia
może zebrać śnieg ze wskazanego obszaru, wjeżdżając odpowiednio z zachodu lub wschodu. Niestety,
są trzy komplikacje
1. Po drodze do danego obszaru maszyna topi cały śnieg na tych obszarach, po których przejeżdża 
(o ile nie został wcześniej zebrany). Na przykład jadąc z zachodu do obszaru 2 zeruje
wartości S[0] oraz S[1] (bo po nich przejeżdża) oraz S[2] (bo ten śnieg zbiera).
2. Każdego dnia maszyna może zebrać śnieg tylko z jednego, dowolnie wybranego obszaru, wjeżdzając albo z zachodu albo ze wschodu.
3. Ze względu na wysoką temperaturę, po każdym dniu na każdym obszarze topi się dokładnie
jeden metr sześcienny śniegu.
Zadanie polega na zaimplementowaniu funkcji:
def snow( S )
która zwraca ile metrów sześciennych maksmalnie można zebrać z wąwozu (zebrany śnieg jest
zabezpieczany i już się nie topi).
"""


#
def left(i): return 2*i + 1 # left child
def right(i): return 2*i + 2 # right child
def parent(i): return ( i - 1 ) // 2 # parent
#

def heapify(A, i, n):
    #
    l = left(i)
    r = right(i)
    max_ind = i
    #
    if l < n and A[ l ] > A[ max_ind ]: max_ind = l # if left is in the arr and if left child is bigger than parent
    if r < n and A[ r ] > A[ max_ind ]: max_ind = r
    #
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, max_ind, n)
    #end if 

#end def heapify() ^^^


def buildheap(A):
    n = len(A)
    #
    for i in range( parent( n - 1 ), -1, -1):
        heapify(A, i, n)
#end def buildheap() ^^^


def snow( S ):
    #
    n = len(S)
    index = n - 1
    sum_snow = 0
    pom = 0
    #
    buildheap(S)
    #
    while S[ 0 ] - pom > 0 and index >= 0: # until the snow will meltdown and we wont get out of range
        S[0], S[index] = S[index], S[0] # replace first with the last one because we already built heap
        sum_snow += S[ index ] - pom
        heapify(S, 0, index) # we are using heapify func and then we decrase by 1 index so we wont use the biggest num
        pom += 1
        index -= 1
    #end while

    return sum_snow
#end def snow() ^^^

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )


