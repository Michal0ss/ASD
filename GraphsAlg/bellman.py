#O(V * E) czas
#O(V) pamiec
'''
Opis:
Służy do znajdowania najkrótszych ścieżek z jednego wierzchołka do wszystkich pozostałych w grafie skierowanym.
Działa także, gdy w grafie są krawędzie o ujemnych wagach. Z UJEMNYMI

Zastosowanie:
Gdy istnieją ujemne wagi krawędzi i chcemy wykryć cykle o ujemnej wadze.
'''

def bellman_ford(edges, n, s):
    """
    edges - lista krawędzi w postaci (u, v, w) czyli z u do v o wadze w
    n - liczba wierzchołków (numerowane od 0 do n-1)
    s - wierzchołek startowy

    Zwraca: listę najkrótszych odległości od s do każdego wierzchołka
             lub None jeśli wykryto cykl ujemny
    """

    # 1. Inicjalizacja: ustawiamy wszystkie odległości na nieskończoność,
    # oprócz wierzchołka startowego (odległość = 0)
    dist = [float('inf')] * n
    dist[s] = 0

    # 2. Relaksujemy wszystkie krawędzie n-1 razy
    for i in range(n - 1):
        updated = False  # flaga do optymalizacji – sprawdzamy, czy coś się zmieniło
        for u, v, w in edges:
            # Jeśli znamy dystans do u i możemy poprawić dystans do v
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        # Jeśli w danej iteracji nic się nie zmieniło – można przerwać wcześniej
        if not updated:
            break

    # 3. Sprawdzamy istnienie cyklu o ujemnej wadze
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            # Wykryto cykl o ujemnej wadze
            return None

    # 4. Zwracamy wynik: najkrótsze dystanse z s do każdego wierzchołka
    return dist


def bellman_ford_edges(edges, V, start):
    dist = [float('inf')] * V
    dist[start] = 0

    for _ in range(V - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Wykrywanie cyklu ujemnego
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            print("Cykl o ujemnej wadze")
            return None

    return dist

# Przykład
edges = [(0, 1, 4), (0, 2, 5), (1, 2, -3), (2, 3, 4)]
print(bellman_ford_edges(edges, 4, 0))

def bellman_ford_adj_list(graph, V, start):
    dist = [float('inf')] * V
    dist[start] = 0

    for _ in range(V - 1):
        for u in range(V):
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    for u in range(V):
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                print("Cykl o ujemnej wadze")
                return None

    return dist

# Przykład
graph = {
    0: [(1, 4), (2, 5)],
    1: [(2, -3)],
    2: [(3, 4)],
    3: []
}
print(bellman_ford_adj_list(graph, 4, 0))

def bellman_ford_matrix(matrix, V, start):
    dist = [float('inf')] * V
    dist[start] = 0

    for _ in range(V - 1):
        for u in range(V):
            for v in range(V):
                w = matrix[u][v]
                if w != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    for u in range(V):
        for v in range(V):
            w = matrix[u][v]
            if w != float('inf') and dist[u] + w < dist[v]:
                print("Cykl o ujemnej wadze")
                return None

    return dist

# Przykład
INF = float('inf')
matrix = [
    [0, 4, 5, INF],
    [INF, 0, -3, INF],
    [INF, INF, 0, 4],
    [INF, INF, INF, 0]
]
print(bellman_ford_matrix(matrix, 4, 0))