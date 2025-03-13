def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def siftDown(lst,i,upper):
    while (True):
        l,r = i*2+1, i*2+2 # refering to the parent children node and heap in the tree
        if max(l,r) < upper: # it means we have two children
            if lst[i] >= max(lst[l], lst[r]): break
            elif lst[l]>lst[r]: # which child is greater? righ one or left one
                swap(lst, i, l)
                i = l # we are moving a pointer to the parent node
            else:
                swap(lst, i, r)
                i=r
        elif  l < upper: # left child
            if lst[l] > lst[i]: # if child is bigger than a parent
                swap(lst, i, l)
                i=l
            else: break
        elif r < upper:
            if lst[r]>lst[i]:
                swap(lst,i,r)
                i=r
            else:break
        else:break



def heapsort(l):
    n=len(l)
    for j in range(n-2//2, -1, -1):
        siftDown(l,j,n)

    for end in range(n-1, 0, -1):
        swap(l, 0, end) #swaping last biggest with smallest
        siftDown(l, 0, end)

lst = [5,16,814,20,10,1,2,3,16,5]
heapsort(lst)
print(lst)