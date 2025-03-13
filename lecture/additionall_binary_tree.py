# revision of binary trees for self develop

class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    """traversal recursive algorythm"""
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root,"") # we start with an empty str but preorder_print will
                                                             # print our binary tree
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root,"")
        elif traversal_type == "postorder":
            return self.inorder_print(tree.root,"")

    def preorder_print(self, start, traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right,traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """left -> root -> right"""
        if start:
            traversal = self.inorder_print((start.left), traversal) # going in the left direction until we come to the end
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print((start.right), traversal) # if there is no turning left we turn right
        return traversal

    def postorder_print(self, start, traversal):
        """left -> right -> root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal
#   1
#  / \
# 2   3
#and so on

#setup tree:
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)


print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
