from egz3btesty import runtests

def uncool(P):
    n = len(P)
    for i in range(n):
        for j in range(i + 1, n):
            a1, b1 = P[i]
            a2, b2 = P[j]

            # Sprawdź czy są rozłączne
            if b1 < a2 or b2 < a1:
                continue  # są fajne

            # Sprawdź czy jeden zawiera się w drugim
            if (a1 <= a2 and b1 >= b2) or (a2 <= a1 and b2 >= b1):
                continue  # są fajne

            # Jeśli nie są rozłączne i żaden nie zawiera się w drugim -> niefajna para
            return (i, j)

    return None  # zgodnie z treścią, zawsze istnieje jakaś para niefajna

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(uncool, all_tests=True)
