##############################
class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.val = value

###############################
class BinarySearchTree:
    def __init__(self):
        self.root = None

def print_tree(node): 
    if node == None:
        return
    print_tree(node.left)
    print_tree(node.right) 
    print(node.val)


#################################################
# Task 1: get_nodes_in_range function 
#################################################  
def get_nodes_in_range(node,min,max):
    left_vals = []
    right_vals = []
    if node.left:
        left_vals = get_nodes_in_range(node.left,min,max)
    if node.right:
        right_vals = get_nodes_in_range(node.right,min,max)
    if node.val >= min and node.val <= max:
        return set([node.val] + list(left_vals) + list(right_vals))
    else:
        return set([] + list(left_vals) + list(right_vals))
    
    
def get_closest_vals(node,n):
   
   vals = []
   
   if node is None:
       return None
   
   vals += get_closest_vals(node.left,n) if get_closest_vals(node.left,n) is not None else []
   vals += [(abs(node.val - n),node.val)]
   vals += get_closest_vals(node.right,n)if get_closest_vals(node.right,n) is not None else []

   return vals

def get_closest_val(tree,n):
    vals =  get_closest_vals(tree.root,n)
    smallest = vals[0]

    for val in vals:
        if val[0] < smallest[0]:
            smallest = val
    return smallest[1]


            
         


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
 
    print(get_nodes_in_range(BST.root, 6, 20))
    print(type(get_nodes_in_range(BST.root, 6, 20)))

    print("Looking for node closest to 4")
    print("Value:",get_closest_val(BST, 21))