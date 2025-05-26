def insertion_sort(arr):
    n=len(arr)
    for i in range(1, n): # Start from the second element (index 1)
        key = arr[i] # Store the current element to be placed correctly
        j=i-1 # Initialize j as the index of the previous element

        # Move elements that are greater than "key" which is current stored value one position ahead
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]  # Shift the larger element to the right
            j-=1  # Move to the previous element
        arr[j+1]=key   # Insert "key" at the correct position

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array:", arr)
