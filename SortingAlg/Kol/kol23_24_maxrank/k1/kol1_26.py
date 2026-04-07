def maxrank(t):
    n = len(t)
    ranks = [0 for _ in range(n)]
    enum = [(val, idx) for idx, val in enumerate(t)]
    def merge_sort(arr):

        if len(arr)>1:
            mid = len(arr) // 2

            L=arr[:mid]
            R=arr[mid:]

            # Recursively sort both halves
            merge_sort(L)
            merge_sort(R)
            i=j=k=0

            # Merge elements back into arr[] in sorted order
            while i<len(L) and j<len(R):
                if L[i] < R[j]: # Compare elements from both halves
                    arr[k]=L[i] # place smaller elem in the main arr
                    i+=1
                else:
                    arr[k]=R[j]
                    j+=1
                k+=1

            # Copy any remaining elements from L[]
            while i<len(L):
                arr[k]=L[i]
                i+=1
                k+=1

            # Copy any remaining elements from R[]
            while j<len(R):
                arr[k]=R[j]
                j+=1
                k+=1
        return arr
