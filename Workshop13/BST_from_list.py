class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.val = value

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,node):
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



def print_tree(node): 
    if node == None:
        return
    print_tree(node.left)
    print_tree(node.right) 
    print(node.val)


if __name__ == "__main__":
    input_list = [5,6,7,1,2,3]
    BST = BinarySearchTree()
    for item in input_list:
        BST.insert(Node(item))
    print_tree(BST.root)