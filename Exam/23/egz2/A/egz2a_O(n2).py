from egz2atesty import runtests

def dominance(P):
  # najpierw sortujemy tablcie po wartosciach x
  P.sort(key=lambda p: p[0])
  P.reverse()  # odwracamy kolejność, aby mieć największe x na początku


  max_dominance = 0  # tablica do przechowywania maksymalnej dominacji dla każdego punktu

  for i in range(len(P)):
    x, y = P[i]
    power = 0
    for j in range(i,len(P)):
      if P[j][1] >= y or P[j][0] == x:
        pass
      elif P[j][1] < y and P[j][0] < x:
        power += 1
      max_dominance = max(max_dominance, power)
  return max_dominance

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
