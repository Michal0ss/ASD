def heapify(lst, n, i):
    upper = i
    l = 2*i + 1
    r = 2*i + 2

    if l<n and lst[l] > lst[upper]:
        upper = l

    if r<n and lst[r] > lst[upper]:
        upper = r

    if upper != i:
        lst[i], lst[upper] = lst[upper], lst[i]
        heapify(lst, n, upper)

def heapSort(lst):
    n = len(lst)

    for i in range(n//2 -1, -1, -1):
        heapify(lst, n, i)

    for i in range(n-1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, i, 0)



if __name__ == "__main__":
    arr = [9, 4, 3, 8, 10, 2, 5]

    heapSort(arr)
    print("Sorted array is", arr)