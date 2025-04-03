class Node:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None
        self.parent = None

def tree_delete(elem):
    if elem.left is None and elem.right is None:
        if elem.value == elem.parent.value:
            elem.parent.left=None
        else:
            elem.parent.right=None
        elem.parent=None

    if elem.left is None and elem.right is not None:
        if elem.value < elem.parent.value:
            elem.parent.left = elem.right
        else:
            elem.parent.right = elem.right