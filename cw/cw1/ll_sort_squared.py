import math


class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def min_detached(head):
    """usuwa element o najmnieszej wartosci"""
    v=None
    if head.next == None:
        return None
    min_val = -math.inf
    while head.next.val!=None:
        if head.next.val<min_val:
            min_val=head.next.val
            v=head
    pet = v
    v.next=v.next.next
    return pet

def insert(head,v):
    """wstawia element do ll"""
    while head.next is not None:
        if head.next.val >v.val:
            v.next=head.next
            head.next=v
            return
        head=head.next
    v.next=None
    head.next=v

def sort(head):
    w=Node(0,None) # nowa lista
    while head.next is not None:
        v=min_detached(head) # usuwamy element o namniejszej wartosc
        insert(w,v) # do nowej list dodajemy kolejno te najmneijsze elementy
    return w

