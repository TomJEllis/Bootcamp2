ice_cream_prices = {
   "Chocolate": [5.00, 7.00],
   "Vanilla" : [4.00, 6.00]
}

sizes = {
   "small" : 0,
   "large" : 1
}



opt = 0
while opt != 4:
   print("\n**** OPTIONS: ****")
   print("1: Add Ice Cream Flavour")
   print("2: Update price of Ice Cream")
   print("3: Get Price")
   print("4: Exit")
   opt = int(input("Which option: "))

   match opt:
      case 1:
         print("\n*** Add Ice Cream Flavour ***")
         new_flavour = input("Enter new flavour: ")
         if new_flavour in ice_cream_prices.keys():
            print("Error, flavour already exists, use menu option 2 to update price")
         else:
            new_small_price = float(input("Enter price for small: "))
            new_large_price = float(input("Enter price for large: "))
            ice_cream_prices[new_flavour] = [new_small_price, new_large_price]
            print(f"Added: {new_flavour} Small: ${ice_cream_prices[new_flavour][0]:.2f} Large: ${ice_cream_prices[new_flavour][1]:.2f}")
      case 2:
         print("\n*** Update Price of Ice Cream ***")
         new_flavour = input("Enter flavour: ")
         if new_flavour not in ice_cream_prices.keys():
            print("Error, flavour does not exits, creating a new flavour instead")
         new_small_price = float(input("Enter price for small: "))
         new_large_price = float(input("Enter price for large: "))
         ice_cream_prices[new_flavour] = [new_small_price, new_large_price]
         print(f"Updated: {new_flavour} Small: ${ice_cream_prices[new_flavour][0]:.2f} Large: ${ice_cream_prices[new_flavour][1]:.2f}")
      
      case 3:
         print("\n*** Get Price of Ice Cream ***")
         user_flavour = input("What flavour of ice cream? ")
         user_size = input("What size? small or large? ")
         user_number = int(input("How many ice creams? "))
         if user_flavour not in ice_cream_prices:
            print("Invalid flavour")
         elif user_size not in ["small", "large"]:
            print("Invalid size")
         elif user_number < 0:
            print("Invalid number of ice creams")
         else:
            total_cost = ice_cream_prices[user_flavour][sizes[user_size]] * user_number
            print(f"Total Cost: {user_number} {user_size} {user_flavour} is ${total_cost:.2f}")
      case 4:
         print("Exiting now")
   

