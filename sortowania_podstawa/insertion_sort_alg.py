
def insert_sort(arr):
    """ We start with second element of the array as first element in the array is assumed to be sorted.
        Compare second element with the first element and check if the second element is smaller then swap them.
        Move to the third element and compare it with the first two elements and put at its correct position
        Repeat until the entire array is sorted."""
    n=len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    return arr



