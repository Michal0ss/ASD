from queue import PriorityQueue

def dijkstra(adjacency_list, start, end):
    previous = {v: None for v in adjacency_list}
    visited = {v: False for v in adjacency_list}
    distances = {v: float("inf") for v in adjacency_list}
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

        for neighbor, weight in adjacency_list[current_node]:
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


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

path, cost = dijkstra(graph, 'A', 'D')
print("Najkrótsza ścieżka:", path)
print("Koszt:", cost)
