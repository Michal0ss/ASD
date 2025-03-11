def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_idx = i # indicator
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]: # checking if next nums are smaller than our current num
                min_idx = j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
arr=[41,9,2,10,15,2,28,1,2,3,1]
print(selection_sort(arr))