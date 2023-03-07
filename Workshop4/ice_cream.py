import random

flavours = {"vanilla", "chocolate", "pecan", "strawberry"}

shoppers = {"Bob", "Sue", "Joe", "Tim", "Helen"}

purchases = {}

key = input()
while key != "q":
   shopper = random.choice(list(shoppers))
   flavour = random.choice(list(flavours))

   print(shopper)
   print(flavour)
   
   if shopper not in purchases:
      purchases[shopper] = set()

   purchases[shopper].add(flavour)

   print(purchases)
   key = input()

bought_flavours = set()

for s in purchases.values():
   bought_flavours.update(s)

print(bought_flavours)
print(flavours.difference(bought_flavours))
