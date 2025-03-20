"""partition Lemuto"""
from sorting.quick_sort import quick_sort


def partition(A,p,r):
    x=A[r]
    i = p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[j],A[i]=A[i], A[j] # swap

    # Move pivot after smaller elements and
    # return its position
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quickSort(arr, low, high):
    """Wywolanie korzystajace z rekurencji ogonowej"""
    if low < high:
        # pi is the partition return index of pivot
        pi = partition(arr, low, high)

        # Recursion calls for smaller elements
        # and greater or equals elements
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def quicksort2(A,p,r):
    """rozwiazanie bez rekurencji ogonowej"""
    while p<r:
        q=partition(A,p,r)
        quicksort2(A,p,q-1)
        p=q+1


def quicksort3(A,p,r):
    """mniej porownan"""
    while p<r:
        q=partition(A,p,r)
        if q-p>r-q:
            quicksort3(A,q+1,r)
            r=q-1

        else:
            quicksort3(A,p,q-1)
            p=q+1

arr=[1,51,12,12,3,32,1,24,5,7]
n=len(arr)
quickSort(arr, 0, n-1)
print(arr)


