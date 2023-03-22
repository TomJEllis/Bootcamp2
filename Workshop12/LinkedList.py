class Node:
   def __init__(self,data):
      self.data = data
      self.next = None

class LinkedList:
   def __init__(self):
      self.head = None
      self.tail = None
   
   def prepend(self, node):
      if self.head == None:
         self.head = node
         self.tail = node
      else:
         node.next = self.head
         self.head = node

   def remove_after(self, curr_node):
      if curr_node == None and self.head != None:
         succ_node = self.head.next
         self.head = succ_node
         if succ_node == None:
            self.tail = None
      elif curr_node.next != None:
         succ_node = curr_node.next.next
         curr_node.next = succ_node
         if succ_node == None:
            self.tail = curr_node
         
