class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def inorder_traversal(node):
    if node is None:
        return
    inorder_traversal(node.left)
    print(node.data)
    inorder_traversal(node.right)

def preorder_traversal(node):
    if node is None:
        return
    print(node.data)
    preorder_traversal(node.left)
    preorder_traversal(node.right)

def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data)

# Notice that the difference between the orderings are just the arrangement of
# parent node, left child, and right child.