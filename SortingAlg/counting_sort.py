def counting_sort(arr):
    n=len(arr)

    # maximum element of an array
    maxx = max(arr)
    counts = [0]*(n+1)

    # for every num in arr
    for x in arr:
        counts[x]+=1

    i=0
    for c in range(maxx+1):
        while counts[c]>0:
            arr[i]=c
            i+=1
            counts[c]-=1
    return arr

print(counting_sort([1,5,12,13,7,3,3,8,2,5,8,9,0]))
