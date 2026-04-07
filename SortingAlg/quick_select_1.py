def partition(T, left, right):
    pivot = T[right]
    i = left

    for j in range(left, right):
        if T[j] <= pivot:
            T[i], T[j] = T[j], T[i]
            i += 1

    T[i], T[right] = T[right], T[i]
    return i


def quickselect(T, left, right, k):
    if left == right:
        return T[left]

    pivot_index = partition(T, left, right)

    if k == pivot_index:
        return T[k]
    elif k < pivot_index:
        return quickselect(T, left, pivot_index - 1, k)
    else:
        return quickselect(T, pivot_index + 1, right, k)