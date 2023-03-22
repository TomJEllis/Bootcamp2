from Stack import Stack

def eval_rpn(in_string):
   number_stack = Stack()
   for number in in_string.split()[::-1]:
      number_stack.push(number)

   num1 = None
   num2 = None
   operator = None
   expression = ""

   while number_stack.list.head != None and number_stack.list.head.next != None:
      num1 = number_stack.pop()
      num2 = number_stack.pop()
      operator = number_stack.pop()
      expression = f"{num1} {operator} {num2}"
      result = eval(expression)
      number_stack.push(result)
   
   return number_stack.pop()

def infix_to_postfix(in_string: str):
   out_string = ""
   stack = Stack()

   for char in in_string:
      if char not in ["(", ")", "+", "-", "*", "/"]:
         out_string += char
      elif char == "(":
         stack.push(char)
      elif char == ")":
         popped = stack.pop()
         while popped != "(":
            out_string += popped
            popped = stack.pop()
      elif char in ["+", "-", "*", "/"]:
         if not stack or stack.peek() == "(":
            stack.push(char)
         else:
            out_string += stack.pop


   """

   For i in inxexp:
    If i is alphabet or digit:
        Append it to the postfix expression
    Else if i is '(':
        Push '(' in the stack
    Else if i is ')':
        Pop the element from the stack and append it postfix expression until we get ')' on top of      the stack.
        Pop '(' from the stack and don't add it in postfix expression.
    Else if i is in '*/+-‘:
        If stack is empty or top of the stack is '(':
            Push the operator in the stack.
        Else:
            Pop the elements from the stack and continue this until the operator on the top of the stack has same or less residence then the i.
    Else:
        Push i in stack.
   in_string: (3 + 4) * 5
   out_string: 3 4 5 + *

   in_string: 3 + (4 * 5)
   out_string 4 5 * 3 +

   in_string 1 + ((2 + 3) + 4)
   out_string 2 3 + 4 + 1 +
   

   
   """


   return out_string



input_string = "4 5 * 3 +"
print(eval_rpn(input_string))

input_string = "1 + ((2 + 3) + 4)"
print(infix_to_postfix(input_string))

