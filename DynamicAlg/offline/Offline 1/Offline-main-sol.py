from zad7testy import runtests

#wypelniamy tablice F wartosciami [-inf, -inf] tam, gdzie jest sciana #,
#czyli nie mozna tam wejsc

def FillNull(L,F,n):

    for i in range(n):
        for j in range(n):

            if L[j][j] == '#':
                F[i][j] = [-float('inf'), -float('inf')]
    return F

def Traversal(L):
    n= len(L)

    F = [ [[0,0] for _ in range(n)] for _ in range(n)]
    F = FillNull(L,F,n)

    for row in range(1,n):
        F[row][0][0] += F[row-1][0][0] +1
        F[row][0][1] = -float('inf')

    for column in range(1,n):
        F[0][column][0] += F[0][column-1][0] + 1
        F[0][column][1] += F[0][column - 1][1] + 1

    for x in range(1,n):

        if L[0][x] == '.':
            F[0][x][0] = max( F[0][x-1][0], F[0][x-1][1]) + 1

        for y in range(1,n):

            leftMaxVal = max(F[y][x-1][0], F[y][x-1][1])
            upMaxVal = F[y-1][x][0]

            if L[y][x] == '.':
                F[y][x][0] = max(leftMaxVal, upMaxVal) + 1

        if L[n-1][x] == '.':
            F[n-1][x][1] = max(F[y][x-1][0], F[y][x-1][1]) + 1

        for z in reversed(range(n-1)):
            leftMaxVal = max(F[z][x-1][0], F[z][x-1][1])
            downMaxVal = F[z+1][x][1]

            if  L[z][x] == '.':
                F[z][x][1] = max(leftMaxVal, downMaxVal) + 1

    return F[n-1][n-1][0] if F[n - 1][n - 1] != [ -float('inf'), -float('inf') ] else -1



def maze( L ):

    return Traversal( L )

runtests( maze, all_tests = True )