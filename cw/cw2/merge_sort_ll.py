import pickle

from merge_sorted_lists import l_merge

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

#weird way to solve merge sorting in linked lists
def ll_cut(l):
    """v to wskaznik, i wycinamy z ciagu podciag ktory jest rosnacym podciagiem (seria naturalna)"""

    result = Node(None)
    tail=result
    while l.next is not None:
        if result.next is None or tail.next.val<=l.next.val:
            v = l.next
            l.next = l.next.next
            if tail.next is None:
                tail.next =v
            else:
                tail.next.next=v
            tail=tail.next
            v.next=None
        else:
            return result

def merge_sort_ll(l):
    """szukamy za pomoca ll_cut najdluzszego rosnacego podciagu (seri naturalnej) i nastepnie
    np (1 , 5) (2) (0 , 9) i nastepnie scalamy je tak zeby byly w koljenosci rosnacej i robimy tak az
    wystapi tyylko jedno scalenie i nie bedzie czego odciac (gdy wartownik wskazuje na None)"""

    while True:

        cut_counter = 0
        temp = Node(None)
        tail = temp

        while l.next is not None:
            s1 = ll_cut(l)
            cut_counter+=1

            if l.next is None:
                tail.next = s1.next
                l.next = temp.next
                break

            s2 = ll_cut(l)
            cut_counter+=1
            s=l_merge(s1,s2) # scalam dwie pociete listy w jedna juz czesciowo posortowane
            tail.next=s.next

            while tail.next is not None:
                tail=tail.next

            if l.next is None:
                l.next = temp.next
                break
        if cut_counter<=2:
            return l