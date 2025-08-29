from heapq import heappop, heappush


def minRefuelStops(target, startFuel, stations):
    heap = []
    output = 0
    prev = 0
    fuel = startFuel

    for distance, gas in stations + [[target, 0]]:
        fuel -= (distance - prev)
        while heap and fuel < 0:
            # dopoki mozemy dodajemy paliwo i jedziemy jak najdaej
            fuel += -heappop(heap) # - bo heappop w pythonie sa minimalne a my chcemy maksymalna ilosc paliwa
            output += 1 # obliczamy ile razy tanktujemy
        if fuel < 0: return  -1

        heappush(heap, -gas)
        prev = distance
    return output