def heapify(A,n,i):
    """heap sort (sortowanie kopcowe)""" #TODO
    l=left(i)
    r=right(i)
    max_inf =i
    if l<=n and A[i]>A[max_inf]:
        max_inf=l
    if r<=n and A[i]>A[max_inf]
