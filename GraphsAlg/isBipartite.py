from queue import Queue


def is_bipartite(G: 'graph represented using adjacency lists'):
    n = len(G)
    queue = Queue()
    colors = [0] * n  # 0 means no color (we will use 2 colors as we want to check if it's bipartite)

    # Loop over all vertices (for inconsistent graphs)
    for i in range(n):
        if colors[i]: continue
        queue.put((i, 1))  # Start with color 1
        while not queue.empty():
            j, color = queue.get()
            colors[j] = color
            for k in G[j]:
                if not colors[k]:
                    queue.put((k, -1 * color))  # Reverse color to the other one
                # If a vertex already has a color, check if this color is a proper one
                elif colors[k] == color:  # If the same color, a graph isn't bipartite
                    return False
    return True