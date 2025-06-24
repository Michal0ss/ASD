def matrix_to_adj_list(matrix):
    n = len(matrix)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):   # żeby nie dublować krawędzi
            if matrix[i][j]:
                adj[i].append(j)
                adj[j].append(i)
    return adj
