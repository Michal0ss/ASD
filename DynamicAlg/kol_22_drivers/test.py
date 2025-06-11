# na podstawimport sys

def drivers(P, B):
    INF = float('inf')
    n = len(P)
    # Sort points by position, keep original index
    points = sorted([(P[i][0], P[i][1], i) for i in range(n)])
    points.append((B, False, -1))
    n += 1

    # dp[i][change][marian]: minimal control points Marian passes from i, with 'change' transfer points since last switch, and marian (1=Marian, 0=Jacek) driving
    dp = [[[INF, INF] for _ in range(3)] for _ in range(n)]
    # changes[i][change][marian]: list of transfer point indices where switches happened
    changes = [[[[] for _ in range(2)] for _ in range(3)] for _ in range(n)]

    # At destination, cost is 0
    for change in range(3):
        for marian in range(2):
            dp[n-1][change][marian] = 0

    for i in range(n-2, -1, -1):
        pos, is_transfer, idx = points[i]
        for change in range(3):
            for marian in range(2):
                if is_transfer:
                    # No switch
                    if change < 2:
                        cost = dp[i+1][change+1][marian]
                        if dp[i][change][marian] > cost:
                            dp[i][change][marian] = cost
                            changes[i][change][marian] = changes[i+1][change+1][marian]
                    # Switch
                    cost = dp[i+1][0][1-marian]
                    if dp[i][change][marian] > cost:
                        dp[i][change][marian] = cost
                        changes[i][change][marian] = [idx] + changes[i+1][0][1-marian]
                else:
                    # Control point
                    add = 1 if marian == 1 else 0
                    cost = dp[i+1][change][marian] + add
                    if dp[i][change][marian] > cost:
                        dp[i][change][marian] = cost
                        changes[i][change][marian] = changes[i+1][change][marian]

    return changes[0][0][0]