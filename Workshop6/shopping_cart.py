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
    
    # add_item()
    # Adds an item to cart_items list. Has a parameter of type ItemToPurchase. Does not return anything.
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)
    
    # remove_item()
    # Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
    # If item name cannot be found, output this message: Item not found in cart. Nothing removed.
    def remove_item(self, item_name):
        if item_name in self.cart_items:
            self.cart_items.remove(item_name)
        else:
            print("Item not found in cart. Nothing removed.")
    
    # modify_item()
    # Modifies an item's quantity. Has a parameter of type ItemToPurchase. Does not return anything.
    # If item can be found (by name) in cart, modify item in cart.
    # If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
    def modify_item(self, item_to_purchase):
        print("Modifying item")
        
    # get_num_items_in_cart() (2 pts)
    # Returns quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        return len(self.cart_items)
        
    # get_cost_of_cart() (2 pts)
    # Determines and returns the total cost of items in cart. Has no parameters.
    def get_cost_of_cart(self):
        cost = 0
        for item in self.cart_items:
            cost += item.get_total()
        return cost
        
    # print_total()
    # Outputs total of objects in cart.
    # If cart is empty, output this message: SHOPPING CART IS EMPTY
    def print_total(self):
        if self.get_num_items_in_cart() > 0:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart}")
            print()
            for item in self.cart_items:
                item.print_item_cost()
            print()
            print(f"Total: ${self.get_cost_of_cart}")
        else:
            print("SHOPPING CART IS EMPTY")
        
    # print_descriptions()
    # Outputs each item's description.
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
    
def execute_menu(optons, cart):
    print("Executing!")
    


if __name__ == "__main__":
    print("Enter customer's name:")
    name = input()
    print("Enter today's date:")
    date = input()
    print()
    print(f"Customer name: {name}")
    print(f"Today's date: {date}")
    
    shopping_cart = ShoppingCart(name,date)
    
    option = ""
    while option != "q": 
        print_menu()
        print("\nChoose an option:")
        option = input()
        if option in ["a","r","c","i","o"]:
            execute_menu(option, shopping_cart)
      
    
#     (6) In the main section of the code, call print_menu() and prompt 
#     for the user's choice of menu options. Each option is represented by a single character.
# If an invalid character is entered, continue to prompt for a valid choice. 
# When a valid option is entered, execute the option by calling execute_menu().
# Then, print the menu and prompt for a new option. 
# Continue until the user enters 'q'. Hint: Implement Quit before implementing other options. (1 pt)

    
