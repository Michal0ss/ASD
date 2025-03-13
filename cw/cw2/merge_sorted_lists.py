class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def l_merge(l1,l2):
    """we are merging two sorted linked list into one sorted"""
    res = Node(None)
    tail=res
    while l1.next is not None and l2.next is not None:
        if l1.next.val < l2.next.val:
            tail.next= l1.next
            l1=l1.next

        else:
            tail.next = l2.next
            l2=l2.next
        tail = tail.next

        if l1.next is not None:
            tail.next = l1.next
        if l2.next is not None:
            tail.next = l2.next
    return res