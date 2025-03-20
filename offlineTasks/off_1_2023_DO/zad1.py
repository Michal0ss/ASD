
"""
Cesarzowa Bajtocji zgubiła w napisie s swój ulubiony palindrom. Cesarzowa nikomu nie mówiła jaki
jest jej ulubiony palindrom i wiadomo jedynie, że jest bardzo długi oraz składa się z nieparzystej
liczby liter alfabetu łacińskiego. Postanowiono odnaleźć zaginiony palindrom cesarzowej.
W tym celu należy zaimplementować funkcję:

def ceasar( s )
która na wejściu otrzymuje słowo s (składające się wyłącznie z małych liter alfabetu łacińskiego)
i zwraca długość najdłuższego spójnego podsłowa, które jest palindromem i którego długość
jest nieparzysta. Użyty algorytm powinien być możliwie jak najszybszy.
Proszę uzasadnić jego
poprawność i oszacować złożoność obliczeniową.

Przykład. Dla słowa:
akontnoknonabcddcba wynikiem jest 7 (kontnok; proszę zwrócić uwagę, że abcddcba jest dłuższym palindromem, ale jest
długości parzystej więc na pewno nie jest zagubionym palindromem cesarzowej).
"""
from zad1testy import runtests


#def palindrome(sliced:str)-> bool:
#    return sliced == sliced[::-1]
#
#def ceasar( s:str ):
#    n=len(s)
#    max_sliced=3
#    if n < 4:
#        if palindrome(s[:-1]) or palindrome(s[1:]):
#            return 3
#    else:
#        for k in range(n-3):
#            for i in range(2+k,n,4):
#                if palindrome(s[:i]):
#                    max_sliced=max(max_sliced,len(s[:i]))
#    return max_sliced

def ceasar(s: str) -> int:
    """
    Znajduje długość najdłuższego spójnego podsłowa, które jest palindromem o nieparzystej długości.
    """
    n = len(s)
    max_length = 1  # Najkrótszy możliwy nieparzysty palindrom to 1

    for center in range(n):
        # Sprawdzamy palindromy o nieparzystej długości center to jedna cyfra ktora okresla srodek palindromu
        left, right = center, center
        while left >= 0 and right < n and s[left] == s[right]:
            if (right - left + 1) % 2 == 1:  # Długość nieparzysta
                max_length = max(max_length, right - left + 1)
            #zmniejszam od lewje i zwiekszam z prawej o 1 -> przesuniecie o 1 w prawo
            #w taki sposob sprawdzam kazda cyfre po lewej stronie srodka i po prawej
            left -= 1
            right += 1

    return max_length


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )

