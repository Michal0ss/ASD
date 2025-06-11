# Mamy dany zbiór zadan T = {t1, . . . , tn}. Kazde zadanie ti
# dodatkowo posiada: (a) termin wykonania d(ti) (liczba naturalna) oraz (b) zysk g(ti) za wykonanie w
# terminie (liczba naturalna).

# Wykonanie kazdego zadania trwa jednostke czasu. Jesli zadanie ti zostanie
# wykonane przed przekroczeniem swojego terminu d(ti), to dostajemy za nie nagrode g(ti) (pierwsze wybrane
# zadanie jest wykonywane w chwili 0, drugie wybrane zadanie w chwili 1, trzecie w chwili 2, itd.).
# Prosze podac algorytm, który znajduje podzbiór zadan, które mozna wykonac w terminie i który prowadzi
# do maksymalnego zysku. Prosze uzasadnic poprawnosc algorytmu.

def prize_for_task(t):

    t.sort(key=lambda x: x[1], reverse=True)  # Sort by profit in descending order
    size = 0

    for (deadline, profit) in t:
        size = max(size, deadline)

    slots = [False for _ in range(size + 1)]
    result = []

    for (d, p) in t:
        for place in reversed(range(d)):
            if not slots[place]:
                slots[place] = True
                result.append((place, p))
                break
    return result