
def binarySearch(A, value):
    #
    start = 0
    end   = len(A) - 1

    while start <= end:
        middle = ( start + end ) // 2

        if value > A[middle]: start += 1
        else: end -= 1

    #end while
    return start
#end procedure binarySearch


def LongestIncreasingSubsequence(A):
    #
    n = len(A)
    F = []

    for i in range(n):
        idx = binarySearch(F, A[i])

        if idx == len(F): F.append( A[i] )
        else: F[idx] = A[i]

    #end 'for' loop

    return len(F)
#end procedure LongestIncreasingSubsequence()