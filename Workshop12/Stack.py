from LinkedList import LinkedList, Node

class Stack:
   def __init__(self):
      self.list = LinkedList()

   def push(self, data):
      self.list.prepend(Node(data))

   def pop(self):
      if self.list.head == None:
         return None
      popped = self.list.head.data
      self.list.remove_after(None)
      return popped
   
   def peek(self):
      if self.list.head is not None:
         return self.list.head.data
      
   def __bool__(self):
      if self.list.head is not None:
         return True
      else:
         return False
