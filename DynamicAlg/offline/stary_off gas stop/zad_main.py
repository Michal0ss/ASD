from heapq import heappush, heappop

from zad8testy import runtests

def to_linear(t):
    n,m = len(t), len(t[0])

    def rek(i,j):
        gasoline_sum = t[i][j]
        t[i][j]=0 #aby sie rekurencja nie zapetlila konieczne

        if j - 1 > -1 and t[i][j-1]!= 0:
            gasoline_sum += rek(i, j-1)
        if j + 1 < m and t[i][j + 1] != 0:
            gasoline_sum += rek(i, j + 1)
        if i - 1 > -1 and t[i - 1][j] != 0:
            gasoline_sum += rek(i - 1, j)
        if i + 1 < n and t[i + 1][j] != 0:
            gasoline_sum += rek(i + 1, j)

        return gasoline_sum


    for j in range(m):
        if t[0][j] != 0:
            t[0][j] = rek(0, j)

    return t[0]

def plan(T):
    """klasyczny roblem minimalnej ilosci tankowan rozwiazuje to za pomoca greedy i heap"""
    A = to_linear(T)
    m  = len(A)

    pq= []
    fuel = A[0] - 1 # bo odejmuje odraz u za pierwszy przebyty kilometr
    i=1
    counter = 1


    while i<m-1:
        if A[i]!=0:
            heappush(pq, -A[i]) # wartość ujemna by był maxheap

        if fuel == 0:
            fuel += -heappop(pq)
            counter+=1

        i+=1
        fuel-=1

    return counter


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )