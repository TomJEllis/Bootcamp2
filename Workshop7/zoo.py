import random

class Zoo:
   def __init__(self):
      self.animals = []
      for i in range(5):
         x = random.randint(0,9)
         y = random.randint(0,9)
         animal = Lion(x, y)
         self.animals.append(animal)

   def print_zoo(self):
      for y in range(9,-1,-1):
         for x in range(9):
            char = " "
            for animal in self.animals:
               if animal.x == x and animal.y == y:
                  char = "x"
            print(char, end="")
         print()

class Animal:
   def __init__(self, x, y):
      self.x = x
      self.y = y

   def __str__(self):
      return f"x: {self.x} y: {self.y}"

class Lion(Animal):
   pass

class Giraffe(Animal):
   pass

my_zoo  = Zoo()
my_zoo.print_zoo()