import math


def sort_to_x_comparsion(arr):
    """funkcja sortuje liste wykonujac tylko mniej niz 3/2n porownan"""
    n=len(arr)
    minim = 0
    maxim = -math.inf

    for i in range(0,n, 2):
        a