from queue import PriorityQueue

def dijkstra(adj_matrix, start, end):
    num_nodes = len(adj_matrix)
    previous = [None] * num_nodes
    visited = [False] * num_nodes
    distances = [float('inf')] * num_nodes
    distances[start] = 0

    queue = PriorityQueue()
    queue.put((0, start))

    while not queue.empty():
        current_distance, current_node = queue.get()

        if visited[current_node]:
            continue
        visited[current_node] = True

        if current_node == end:
            break  # Znaleźliśmy najkrótszą ścieżkę do celu

        for neighbor in range(num_nodes):
            weight = adj_matrix[current_node][neighbor]
            # W macierzy sąsiedztwa brak krawędzi oznaczamy np. 0 lub float('inf')
            if weight == 0 or weight == float('inf'):
                continue
            if visited[neighbor]:
                continue
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                queue.put((new_distance, neighbor))

    # Odtwarzanie najkrótszej ścieżki
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    return path, distances[end]


# Przykładowa macierz sąsiedztwa (0 oznacza brak krawędzi)
#       A   B   C   D
adj_matrix = [
    [0, 1, 4, 0],  # A
    [0, 0, 2, 5],  # B
    [0, 0, 0, 1],  # C
    [0, 0, 0, 0]   # D
]

path, cost = dijkstra(adj_matrix, 0, 3)  # 0='A', 3='D'
print("Najkrótsza ścieżka:", path)
print("Koszt:", cost)