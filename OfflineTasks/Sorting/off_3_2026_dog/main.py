# tablica T o dlg n oraz q zapytan. Dla kazdego zapytania 1<= qi <= n nalezy odp jaka jest qi-ta najwieksza liczba w tablicy T



import sys
def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]

def siftDown(lst,i,upper):
    while (True):
        l = i*2+1
        r = i*2+2
        if max(l,r) < upper:
            if lst[i] >= max(lst[l], lst[r]): break
            elif lst[l]>lst[r]:
                swap(lst, i, l)
                i = l
            else:
                swap(lst, i, r)
                i=r

        elif  l < upper:
            if lst[l] > lst[i]:
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
        swap(l, 0, end)
        siftDown(l, 0, end)


def pies():
    input = sys.stdin.readline

    n = int(input())
    T = [0] * n

    for i in range(n):
        T[i] = int(input())

    t=heapsort(T)

    q = int(input())

    out = []
    for _ in range(q):
        k = int(input())
        out.append(str(t[-k]))

    sys.stdout.write("\n".join(out))

pies()