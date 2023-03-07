cart_items = ["orange", "mango", "banana", "apple", "salmon"]
item_name = "apple"

for i in range(len(cart_items)):
   if cart_items[i] == item_name:
      remove_index = i

cart_items.pop(remove_index)

print(cart_items)