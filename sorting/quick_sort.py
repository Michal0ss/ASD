# sorting with pivot point
def quick_sort(seq):
    n = len(seq)
    if n <= 1:
        return seq
    else:
        pivot = seq.pop()

    items_greater = []
    items_lower = []

    for item in seq:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

print(quick_sort([5,16,814,20,10,1,2,3,16,5]))