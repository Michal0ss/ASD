# Mamy sobie prostą i na tej prostej mamy punkty.
# x1, x2, x3, ...., xn   --> nie koniecznie są we współrzędnych całkowitych

# Podać algorytm znajdujący minimalną liczbę odcinków jednostkowych (długości 1) niezbędną do pokrycia punktów od
# x1 do xn.

# W kolejności algorytmu znajduję piewszy punkt, który nie jest pokryty przedziałem, zwiększam
# liczbę i stawiam w nim nowy odcinek i powtarzam (odcinki muszą być domknięte oczywiście).

# O(n) (O(nlogn) - gdy potrzebny sort)

# zachlanny
def line_fragments(points):
    points.sort()  # Sort the points in ascending order
    counter = 0
    n = len(points)
    i = 0

    while i<n:
        start = points[i]  # Start of the current segment
        counter += 1

        while i < n and points[i] <= start + 1:
            # points[i] <= start + 1 to piszemy aby pokryc wszystekie punkty
            i+=1

    return  counter