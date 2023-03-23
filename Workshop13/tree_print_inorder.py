class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.val = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            curr_node = self.root
            while curr_node is not None:
                if node.val < curr_node.val:
                    if curr_node.left is None:
                        curr_node.left = node
                        curr_node = None
                    else:
                        curr_node = curr_node.left
                        
                else:
                    if curr_node.right is None:
                        curr_node.right = node
                        curr_node = None
                    else:
                        curr_node = curr_node.right

    def print_inorder(self,node):

        if not node:
            return       
        self.print_inorder(node.left)
        print(node.val)
        self.print_inorder(node.right)

if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(9)

    tree.print_inorder(tree.root)