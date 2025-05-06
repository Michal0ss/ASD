from zadtesty import runtests

def relax(distance, a, b, weight):
    if distance[b] > distance[a] + weight:
        distance[b] = distance[a] + weight
        return True
    return False

def BellmanFord(G, source):
    n = len(G)
    distance = [float('inf')] * n
    distance[source] = 0

    for _ in range(n - 1):
        for a in range(n):
            for (b, weight) in G[a]:
                relax(distance, a, b, weight)

    # Nie szukamy ujemnych cykli, bo wszystkie wagi są dodatnie + noclegi

    return distance

def goodknight(G, s, t):
    n = len(G)
    INF = float('inf')

    # Graf rozszerzony: (zamek, czas bez noclegu)
    N = n * 17
    graf = [[] for _ in range(N)]

    for u in range(n):
        for bez_noclegu in range(17):
            a = u * 17 + bez_noclegu
            for v in range(n):
                w = G[u][v]
                if w == -1:
                    continue

                # opcja bez noclegu
                if bez_noclegu + w <= 16:
                    new_bez_noclegu = bez_noclegu + w
                    b = v * 17 + new_bez_noclegu
                    graf[a].append((b, w))

                else:
                    # nocleg konieczny, ale NIE w t!
                    if v == t:
                        continue
                    new_bez_noclegu = w
                    if new_bez_noclegu <= 16:
                        b = v * 17 + new_bez_noclegu
                        graf[a].append((b, w + 8))  # 8h nocleg
    #

    source = s * 17 + 0
    distance = BellmanFord(graf, source)

    # Najmniejszy czas do t
    best = INF
    for bez_noclegu in range(17):
        v = t * 17 + bez_noclegu
        best = min(best, distance[v])

    return best

runtests(goodknight, all_tests=False)
