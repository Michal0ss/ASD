# Zadanie 2. (spadające klocki) Każdy klocek to przedział postaci [a,b]. Dany jest ciąg klocków [a1,b1],
# [a2,b2], ..., [an,bn]. Klocki spadają na oś liczbową w kolejności podanej w ciągu. Proszę zaproponować
# algorytm, który oblicza ile klocków należy usunąć z listy tak, zeby każdy kolejny spadajacy klocek mieścił
# się w całości na klocku, który spadł tuż przed nim.

# f(i) = maksymalna wysokość wieży "spójnej" (moje oznaczenie) skonstruowanej używając klocków do indeksu i
# n - max f = wynik

# f(i) = max { (f[0, i - 1] jeżeli przedział a_i zawiera się w przedziale a_i-1) + 1 }

# O(n^2) - dla każdego klocka sprawdzam wszystkie poprzednie, czy się mieszczą
def bricks(a):
    n = len(a)
    a.sort(key=lambda x: x[0])  # Sort by the starting point of the intervals

    dp = [1] * n  # Initialize dp array where dp[i] is the max height ending with brick i

    for i in range(1, n):
        for j in range(i):
            if a[j][0] <= a[i][0] and a[j][1] >= a[i][1]:  # Return the number of bricks to remove to achieve the maximum tower height
                dp[i] = max(dp[i], dp[j] + 1) # ile moge na itym indeksie umiescic klockow

    return n - max(dp)