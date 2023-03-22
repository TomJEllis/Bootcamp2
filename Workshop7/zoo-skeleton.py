import random
import time

class Animal:
    # (1) complete this constructor which is input
    # x and y position, a symbol for the Animal (from ['G', 'L', 'T']) and an int (its speed)
    # note: 'x', 'y', 'symbol' and 'speed' are the attribute names
    def __init__(self, x, y, symbol, speed): # complete this
        self.x = x
        self.y = y
        self.symbol = symbol
        self.speed = speed

    def move(self, width, height):
        for _ in range(self.speed):
            dx = random.choice([-1, 0, 1])
            dy = random.choice([-1, 0, 1])
            new_x = self.x + dx
            new_y = self.y + dy
            if 0 <= new_x < width and 0 <= new_y < height:
                self.x, self.y = new_x, new_y

class Herbivore(Animal):
    pass

class Carnivore(Animal):
    pass

class Tiger(Carnivore):
    def __init__(self, x, y):
        super().__init__(x, y, 'T', 2)

class Giraffe(Herbivore):
    def __init__(self, x, y):
        super().__init__(x, y, 'G', 1)

class Llama(Herbivore):
    def __init__(self, x, y):
        super().__init__(x, y, 'L', 3)

class Zoo:
    def __init__(self, width, height, num_herbivores=20, num_carnivores=1):
        self.width = width
        self.height = height
        self.animals = []
        self.add_random_herbivores(num_herbivores)
        self.add_random_carnivores(num_carnivores)

    def random_location(self):
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)

    def add_random_herbivores(self, num_herbivores):
        # (2) 
        # Complete this function:
        # create num_herbivores objects, randomly choosing between Giraffe or Llama
        # and use rand_location to get x, y location for each on the grid
        #
        # 
        for i in range(num_herbivores):
            location = self.random_location()
            self.add_animal(random.choice([Llama(location[0],location[1]),Giraffe(location[0],location[1])]))


    def add_random_carnivores(self, num_carnivores):
        # (3) 
        # Complete this function:
        # create num_herbivores, randomly choosing between Giraffe or Llama
        # and use rand_location to get position to place each one on the grd
        # 
        for i in range(num_carnivores):
            location = self.random_location()
            self.add_animal(Tiger(x = location[0], y=location[1]))

    def add_animal(self, animal):
        self.animals.append(animal)

    def environment_step(self):
        for animal in self.animals:
            animal.move(self.width, self.height)

        self.check_for_eating()

    def check_for_eating(self):
        positions = {}
        for animal in self.animals:
            if (animal.x, animal.y) not in positions:
                positions[(animal.x, animal.y)] = [animal]
            else:
                positions[(animal.x, animal.y)].append(animal)

        survivors = []
        for position, animals in positions.items():
            if len(animals) > 1:
                non_carnivores = [animal for animal in animals if not isinstance(animal, Carnivore)]
                carnivores = [animal for animal in animals if isinstance(animal, Carnivore)]
                if carnivores:
                    survivors.extend(carnivores)
                else:
                    survivors.extend(non_carnivores)
            else:
                survivors.extend(animals)

        self.animals = survivors

    def print_zoo(self):
        # (4)
        # complete this to print the grid (as shown in the video) with:
        # '.' for empty location
        # either 'G' or 'L' or 'T' if the location is occupied 
        for y in range(self.height)[::-1]:
            for x in range(self.width):
                empty = True
                for animal in self.animals:
                    if animal.x == x and animal.y == y:
                        print(animal.symbol, end=" ")
                        empty = False
                        break
                if empty:
                    print(".", end = " ")
            print()
    
    def simulation_complete(self):
        herbivores_remaining = any(isinstance(animal, Herbivore) for animal in self.animals)
        return not herbivores_remaining

try:
    width = int(input("Enter width of zoo: "))
    if width <= 0:
        raise ValueError("width")
    height = int(input("Enter height of zoo: "))
    if height <= 0:
        raise ValueError("height")
    num_herbivores = int(input("Enter number of herbivores: "))
    if num_herbivores <= 0:
        raise ValueError("number of herbivores")
    num_carnivores = int(input("Enter number of carnivores: "))
    if num_carnivores <= 0:
        raise ValueError("number of carnivores")
    zoo = Zoo(width, height, num_herbivores=num_herbivores, num_carnivores=num_carnivores)
    zoo.print_zoo()
    step_count = 0
    while not zoo.simulation_complete():
        step_count += 1
        print(f"\nAfter environment step {step_count}:")
        zoo.environment_step()
        time.sleep(0.1)
        zoo.print_zoo()


    print(f"\nSimulation complete after {step_count} steps.")

except ValueError as excpt:
    length = (len(str(excpt))+8)
    print("*" * length)
    print(f"Invalid {excpt}")
    print(f"{'Exiting'}")
    print("*" * length)
    