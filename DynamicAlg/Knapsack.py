def knapsack(W, P, B):
    n = len(W)
    # F[i][b] = maksymalna wartość, jaką można uzyskać rozważając pierwsze i+1 przedmiotów i mając pojemność dokładnie b
    F = [[0 for _ in range(B + 1)] for i in range(n)]

    # Inicjalizacja pierwszego wiersza
    for b in range(W[0], B + 1):
        F[0][b] = P[0]

    # Wypełnianie tablicy dynamicznej
    for b in range(B + 1):
        for i in range(1, n):
            F[i][b] = F[i - 1][b]
            if b - W[i] >= 0:
                F[i][b] = max(F[i][b], F[i - 1][b - W[i]] + P[i])

    return F[n - 1][B]
