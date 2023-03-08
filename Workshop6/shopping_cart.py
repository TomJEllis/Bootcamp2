class ItemToPurchase:
    def __init__(self, item_name = "none", item_price = 0, item_quantity = 0, item_description = "none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    
    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")
        
    def get_total(self):
        return self.item_price * self.item_quantity

class ShoppingCart:
    def __init__(self, customer_name = "none", current_date = "January 1, 2016", cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
    
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)
    
    def remove_item(self, item_name):
        remove_index = -1
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item_name:
                remove_index = i
        if remove_index >= 0:
            self.cart_items.pop(remove_index)
        else:
            print("Item not found in cart. Nothing removed.")
    
    def modify_item(self, item_to_purchase):
        index = -1
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item_to_purchase.item_name:
                index = i
        if index >= 0:
            self.cart_items[index].item_quantity = item_to_purchase.item_quantity
        else:
            print("Item not found in cart. Nothing modified.")
        

    def get_num_items_in_cart(self):
        output = 0
        for item in self.cart_items:
            output += item.item_quantity
        return output
        
    def get_cost_of_cart(self):
        cost = 0
        for item in self.cart_items:
            cost += item.get_total()
        return cost
        
    def print_total(self):
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            print()
            if self.get_num_items_in_cart() > 0: 
                for item in self.cart_items:
                    item.print_item_cost()
            else:
                print("SHOPPING CART IS EMPTY")
            print()
            print(f"Total: ${self.get_cost_of_cart()}")
        
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print()
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()

def print_menu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    
def execute_menu(option, cart):
    if option == "o":
        print("OUTPUT SHOPPING CART")
        cart.print_total()
    if option == "a":
        print("ADD ITEM TO CART")
        print("Enter the item name:")
        name = input()
        print("Enter the item description:")
        description = input()
        print("Enter the item price:")
        price = int(input())
        print("Enter the item quantity:")
        quantity = int(input())
        new_item = ItemToPurchase(name, price, quantity, description)
        cart.add_item(new_item)
    if option == "i":
        print("OUTPUT ITEMS' DESCRIPTIONS")
        cart.print_descriptions() 
    if option == "r":
        print("REMOVE ITEM FROM CART")
        print("Enter name of item to remove:")
        name = input()
        cart.remove_item(name)
    if option == "c":
        print("CHANGE ITEM QUANTITY")
        print("Enter the item name:")
        name = input()
        print("Enter the new quantity:")
        quantity = int(input())
        new_item = ItemToPurchase(name, item_quantity = quantity)
        cart.modify_item(new_item)
    print()
        

    


if __name__ == "__main__":
    print("Enter customer's name:")
    name = input()
    print("Enter today's date:")
    date = input()
    print()
    print(f"Customer name: {name}")
    print(f"Today's date: {date}")
    print()
    
    shopping_cart = ShoppingCart(name,date)
    
    option = ""
    while option != "q": 
        print_menu()
        print("\nChoose an option:")
        option = input()
        while option not in ["a","r","c","i","o","q"]:
            print("Choose an option:")
            option = input()
        if option in ["a","r","c","i","o"]:
            execute_menu(option, shopping_cart)