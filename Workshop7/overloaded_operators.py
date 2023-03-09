import os

class OnlineOrder:
   def __init__(self, product, customer_name, price):
      self.product = product
      self.customer_name = customer_name
      self.price = price
   
   def __gt__(self, threshold):
      if self.price > threshold:
         return True
      else:
         return False
      
   def __str__(self):
      return f"{self.product} was purchased by {self.customer_name} for ${self.price:.2f}"
   
def create_file():
   file_path = os.path.split(__file__)
   with open( file_path[0]+ "/orders.csv", "w") as output:
      output.write("Banana, Tom, 54.6\n")
      output.write("Taco, Sandra, 2.0\n")
      output.write("Taco, Anndy, 99.0\n")

def read_file():
   file_path = os.path.split(__file__)
   with open(file_path[0] + "/orders.csv", "r") as input:
      orders = input.readlines()
      return_data = []
      for order in orders:
         data = order.strip().split(",")
         online_order = OnlineOrder(data[0],data[1],float(data[2]))
         return_data.append(online_order)
      return return_data

if __name__ == "__main__":
   create_file()
   orders = read_file()
   free_delivery_threshold = 50.0

   for order in orders:
      if order > free_delivery_threshold:
         print(f"{order} and is eligible for free delivery")
      else:
         print(f"{order} and is not eligible for free delivery")