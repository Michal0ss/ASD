from kol2testy import runtests

class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0
    #


"""kluczem w zrozumienia zadania jest to, ze poza naszym drzewem rozpinajacym 
ktore znajdujemy za pomoca algorytmu kruskala kazda krawedz jest 
albo wieksza od kazdej w drzewie albo mniejsza od kazdej krawedzi drzewa
rozpinajacego T """

"""funckja rekurencyjnie szuka rodzica (potrzebne do algorytmu kruskala)"""
def Find(x):
    if x.parent != x:
        x.parent = Find( x.parent )
    #
    return x.parent

"""funkcja korzystajac z find (szukanie rodzica) laczy dwa zbiory """
def Union(X, Y): # X - root, Y - root 
    if X.rank > Y.rank:
        Y.parent = X

    elif X.rank < Y.rank:
        X.parent = Y

    else:
        X.parent = Y 
        Y.rank += 1


def Kruskal(G, Edges, i):
    n = len(G)  # liczba wierzchołków
    minSpanningTree = []  # tu przechowujemy krawędzie MST
    Vertices = [Node(v) for v in range(n)]  # struktura Union-Find
    sumOfMST = 0  # suma wag drzewa

    for edge in Edges[i:]:  # iterujemy od i-tej krawędzi                                                                               \
        a, b, weight = edge
        rootA, rootB = Find(Vertices[a]), Find(Vertices[b])

        if rootA != rootB:  # jeśli nie tworzy cyklu
            Union(rootA, rootB)  # łącz zbiory
            minSpanningTree.append(edge)  # dodaj do drzewa
            sumOfMST += weight  # zwiększ sumę wag

        if len( minSpanningTree ) == n - 1:
            minEdgeValue = minSpanningTree[0][2]
            maxEdgeValue = minSpanningTree[ n - 2 ][2]
            return minEdgeValue, maxEdgeValue, minSpanningTree, sumOfMST
    #end for
    return None, None, None, None
#end procedure Kruskal()

"""zapisuje krawedzie w liscie edges i zwraca tablice tuple (a,b,waga)"""
def getEdgesList(G):
    #
    edges = []

    for vertex in range( len(G) ):
        for (neighbour, weight) in G[vertex]:
            if vertex < neighbour:
                edges.append( (vertex, neighbour, weight) )
    #end 'for' loops

    return edges
#end procedure getEdgesList()

"""sprawdzamy czy krawedzie poza mst spelniaja warunki """
def checkEdges(Edges, minSpanningTree, minEdgeValue, maxEdgeValue):
    #
    for edge in Edges:
        if edge not in minSpanningTree:
            a, b, weight = edge 
            if minEdgeValue <= weight <= maxEdgeValue:
                return False 
    #
    return True 
#end procedure checkEdges() 


def beautree(G):
    #
    Edges = getEdgesList(G)
    Edges.sort( key = lambda x: x[2] )
    minSum = float('inf')

    for i in range( len(Edges) ):
        #
        minEdgeValue, maxEdgeValue, minSpanningTree, sumOfMST = Kruskal(G, Edges, i)

        if sumOfMST != None and checkEdges( Edges, minSpanningTree, minEdgeValue, maxEdgeValue ):
            minSum = min( minSum, sumOfMST )
        #
    #end 'for' loop
    
    if minSum != float('inf'): return minSum
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )


