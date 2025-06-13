from kolutesty import runtests

def ice_cream(T):
    T.sort(reverse=True)
    total = 0
    for i in range(len(T)):
        eatable = max(0, T[i] - i)
        total += eatable
    return total

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )
