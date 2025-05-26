from queue import PriorityQueue
from kol2testy import runtests


# Michal Bialas
# algorytm polega na tym ze korzystajac z zmodyfikowanego algorytmu dijkstry znajdujemy po kolei od naszego start_city najkrotsze sciezki 
# do poszczegolnych resortow (przechodzac przez tablice resorts w funkcji lets_roll). 
# "Zmodyfikowanego alg dijkstry" mam na mysli ze od klasycznej implementacji rozni sie on tym ze dodajemy 
# resorts_banned ktore sa lista resosrtow ktore juz odwiedzilismy a jak wiemy gdy odiwedzimy juz dany resort to nie mozemy przez niego ponownie przejsc, 
# automatycznie szukajac dalej najkrotszej sciezki wykluczajac odwiedzony resort (line: 33).
# Korzystalem rowniez z funkcji edges_to_adj poniewaz ulatwia mi ona skorzystanie  z algorytmu z adjency list a nie edges list (czysto dla wygody)
# oczywiscie w petli w glownej funkcji sumujemy kazdy wynik ktory zwraca nam dijkstra dla poszczegolnych najkrotszych sciezek nie musimy tam zmieniac sumy
# poniewaz dijkstra zwraca juz podwojony wynik uwzgledniajac jednoczesnie powroty z tresci 
#
# zlozonosc ciezko mi okreslic ale pewnie duza bo blokuje sie na ktoryms tescie algorytm

def dijkstra(G, s, e, resorts_banned):
    n = len(G)
    distance = [float("inf")] * n
    distance[s] = 0

    PQ = PriorityQueue()
    PQ.put((0, s))

    while not PQ.empty():
        cur_distance, v = PQ.get()

        if cur_distance > distance[v]:
            continue
        
        for v_son, weight in G[v]:
            dist = cur_distance + weight

            if dist < distance[v_son] and v_son not in resorts_banned:
                distance[v_son] = dist
                PQ.put((dist, v_son))

    return distance[e]*2


def edges_to_adjency(graph):
    n=0
    for u,v,w in graph:
        n=max(n,u,v)
    adj = [[] for _ in range(n+1)]
    for u,v,w in graph:
        adj[u].append((v,w)) 
        adj[v].append((u,w)) # poniewaz graf nieskierowany 
    return adj


def lets_roll(start_city, flights, resorts):
    G=edges_to_adjency(flights) # zamieniona na adj list postac grafu
    banned = [] # odwiedzone resort
    suma=0
    for element in resorts:
        suma+= dijkstra(G, start_city, element, banned)
        banned.append(element)
    return suma

runtests(lets_roll, all_tests = True)
