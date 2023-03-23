class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.val = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

def print_tree(node): 
    if node == None:
        return

def is_valid(node):
    if node.left is None and node.right is None:
        return True
    if node.left and node.right:
        return is_valid(node.left) and node.left.val <= node.val and node.right.val >= node.val and is_valid(node.right)
    if node.left:
        return is_valid(node.left) and node.left.val <= node.val
    if node.right:
        return node.right.val >= node.val and is_valid(node.right)
    

if __name__ == '__main__':
    BST = BinarySearchTree()
    BST.root = Node(10)
    BST.root.left = Node(5)
    BST.root.right = Node(15)
    BST.root.left.left = Node(2)
    BST.root.left.right = Node(8)
    BST.root.right.left = Node(12)
    BST.root.right.right = Node(20)
    BST.root.right.right.right = Node(25)

    not_BST = BinarySearchTree()
    not_BST.root = Node(10)
    not_BST.root.left = Node(11)
    not_BST.root.right = Node(15)
    not_BST.root.left.left = Node(2)
    not_BST.root.left.right = Node(8)
    not_BST.root.right.left = Node(12)
    not_BST.root.right.right = Node(20)
    not_BST.root.right.right.right = Node(25)

    print(is_valid(BST.root))
    print()
    print(is_valid(not_BST.root))