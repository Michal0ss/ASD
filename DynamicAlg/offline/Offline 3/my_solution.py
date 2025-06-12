from zad9testy import runtests

import heapq

def min_cost(O, C, T, L):
    # Dodaj A (0) i B (L)
    O.append(0)
    C.append(0)
    O.append(L)
    C.append(0)

    # Posortuj parkingi według odległości
    parkingi = sorted(zip(O, C))
    n = len(parkingi)

    dp = [[float('inf')] * 2 for _ in range(n)]
    dp[0][0] = 0  # Start w A, bez kosztu i bez wyjątku

    # Heap bez wyjątku: (koszt, indeks)
    heap_no_exc = [(0, 0)]
    # Heap z wyjątkiem: (koszt, indeks)
    heap_with_exc = []

    for i in range(1, n):
        pos_i, cost_i = parkingi[i]

        # Odsuwamy nieosiągalne zasięgi z obu kopców
        while heap_no_exc and parkingi[i][0] - parkingi[heap_no_exc[0][1]][0] > T:
            heapq.heappop(heap_no_exc)
        while heap_with_exc and parkingi[i][0] - parkingi[heap_with_exc[0][1]][0] > 2 * T:
            heapq.heappop(heap_with_exc)

        # Przejazd bez wyjątku (tylko jeśli <= T)
        if heap_no_exc:
            min_cost_no_exc = heap_no_exc[0][0] + cost_i
            dp[i][0] = min(dp[i][0], min_cost_no_exc)

        # Przejazd z użyciem wyjątku – możemy go użyć teraz
        if heap_no_exc:
            min_cost_with_exc = heap_no_exc[0][0] + cost_i
            dp[i][1] = min(dp[i][1], min_cost_with_exc)

        # Przejazd kontynuując wyjątek (czyli już go użyliśmy wcześniej)
        if heap_with_exc:
            min_cost_with_exc = heap_with_exc[0][0] + cost_i
            dp[i][1] = min(dp[i][1], min_cost_with_exc)

        # Dodaj aktualny parking do heapów
        heapq.heappush(heap_no_exc, (dp[i][0], i))
        heapq.heappush(heap_with_exc, (dp[i][1], i))

    return min(dp[-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost, all_tests=True)