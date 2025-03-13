def heapify(A,n,i):
    """heap sort (sortowanie kopcowe)"""
    l=2*i+1  #left(i)
    r=2*i+2       #right(i)
    max_inf =i
    if l<=n and A[i]>A[max_inf]:
        max_inf=l
    if r<=n and A[i]>A[max_inf]:
        max_inf = r
    if max_inf != i:
        A[i], A[max_inf] = A[max_inf], A[i]  # Swap
        heapify(A,n,max_inf)

def build_heap(arr):
    n=len(arr)
    for i in range(parent(n-1),-1,-1):
        heapify(arr,n,i)

def heap_sort(arr):
    n=len(arr)
    build_heap(arr)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)