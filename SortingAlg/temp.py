#
def left(i): return 2*i + 1 # left child
def right(i): return 2*i + 2 # right child
def parent(i): return ( i - 1 ) // 2 # parent
#

def heapify(A, i, n):
    #
    l = left(i)
    r = right(i)
    max_ind = i
    #
    if l < n and A[ l ] > A[ max_ind ]: max_ind = l # if left is in the arr and if left child is bigger than parent
    if r < n and A[ r ] > A[ max_ind ]: max_ind = r
    #
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, max_ind, n)
    #end if
#end def heapify() ^^^
def buildheap(A):
    n = len(A)
    #
    for i in range( parent( n - 1 ), -1, -1):
        heapify(A, i, n)
#end def buildheap() ^^^
arr = [1,23,15,124,4,46,8,9,2,231,5,6,7]
buildheap(arr)
print(arr)