# Mamy przyczepę o nośności k.
# Ładunki o wagach: w1, w2, ..., wn (w_i - waga i-tego ładunku)
# w_i należy do {1, 2, 4, 8, ...} (potęgi 2) i należy do { 1, ..., n }

# Proszę podać algorytm zachłanny, który wybiera ładunki tak aby przyczepa była możliwe najbardziej zapełniona.
# I jak najmniej ładunków.

def greedy_trailer(w, k):
    w.sort(reverse=True)  # Sort weights in descending order
    result = []

    for weights in w:
        while weights<=k:
            result.append(weights)
            k -= weights

    return result
