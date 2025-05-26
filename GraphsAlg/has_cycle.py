def has_cycle(G):
    n = len(G)
    visited = [False] * n

    def dfs(u, parent):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:
                # Znaleźliśmy cykl!
                return True
        return False

    for u in range(n):
        if not visited[u]:
            if dfs(u, -1):
                return True

    return False
