from kol2testy import runtests


class Node:
    def __init__(self, id):
        self.id = id
        self.parent = self
        self.rank = 0
    #
#end Class

def beautree(G):
    # tu prosze wpisac wlasna implementacje
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
