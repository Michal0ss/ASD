from math import inf
from egz2btesty import runtests

def parking(X,Y):
  n,m=len(X), len(Y)
  dp = [[float('inf') for _ in range(m)] for _ in range(n)]
  dp[0][0] = abs(X[0]-Y[0])
  for i in range(1,n):
    dp[i][i] = abs(X[i]-Y[i]) + dp[i-1][i-1]
  for j in range(1, m-n+1): # n-m+1 bo parking moze byc maksymanie o taka wartosc oddalony
    dp[0][j] = abs(X[0] - Y[j])
  for i in range(1,n):
    mini = float('inf')
    if m>n:
      mini = min(dp[i-1][i-1], dp[i-1][i])
    for j in range(1,m-n+i+1):
      dp[i][j] = abs(X[i]-Y[j])+mini
      mini = min(mini, dp[i-1][j])
      # porownuje z poprzednim biurem zeby znalezc najblizsze parkinigi dla sasiadujacych biur
  return min(dp[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
