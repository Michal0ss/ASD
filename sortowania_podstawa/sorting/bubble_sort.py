def bubble_sort(arr):
    """ algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order"""
    n=len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[41,9,2,10,15,2,28,1,2,3,1]
print(bubble_sort(arr))