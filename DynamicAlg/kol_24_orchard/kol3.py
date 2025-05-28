from kol3testy import runtests


def orchard(T, m):
    n = len(T)
    dp = [n+1] * m # dp[mod] = minimalna liczba wycięć, by suma pozostałych ≡ mod
    sum_all = sum(T)
    dp[sum_all%m]=0 # na poczatku nic nie wycinasz

    for i in range(n):
        new_dp = dp[:]
        for mod in range(m):
            if dp[mod]<n+1:
                new_mod = (mod - T[i]) % m
                if new_dp[new_mod] > dp[mod] + 1:
                    new_dp[new_mod] = dp[mod] + 1
        dp = new_dp
    return dp[0] if dp[0]<n+1 else -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
