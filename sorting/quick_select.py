# The algorithm is similar to QuickSort. The difference is, instead of recurring for both sides (after finding pivot),
# it recurs only for the part that contains the k-th smallest element. The logic is simple,
# if index of the partitioned element is more than k, then we recur for the left part.
# If index is the same as k, we have found the k-th smallest element and we return.
# If index is less than k, then we recur for the right part.
# This reduces the expected complexity from O(n log n) to O(n), with a worst-case of O(n^2).

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low, high):
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):

        if arr[j] >= pivot:  # >= bo szukamy większych!
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, high)

    return i + 1

def kthSmallest(arr, l, r, k):

    # if k is smaller than number of
    # elements in array
    if (k > 0 and k <= r - l + 1):

        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        index = partition(arr, l, r)

        # if position is same as k
        if (index - l == k - 1):
            return arr[index]

        # If position is more, recur
        # for left subarray
        if (index - l > k - 1):
            return kthSmallest(arr, l, index - 1, k)

        # Else recur for right subarray
        return kthSmallest(arr, index + 1, r, k - index + l - 1)

def kthHigher(arr, low, high, k):

    if k>0 and k<=high-low+1:

        index = partition(arr, low, high)

        #amount of elements before index
        count=index-low+1

        if count == k:
            return arr[index]

        if count > k:
            return kthHigher(arr, low, index-1,k)

        else:
            return kthHigher(arr, index+1, high, k-count)

    return None

arr=[17,25,25,30]
print(kthHigher(arr,0,len(arr)-1,1))
