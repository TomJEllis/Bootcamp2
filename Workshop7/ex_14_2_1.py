import globals

class TransportMode:
    def __init__(self, name, speed):
        globals.increment_call_count()
        self.name = name
        self.speed = speed

    def info(self):
        print(f'{self.name} can go {self.speed} mph.')

class MotorVehicle(TransportMode):
    def __init__(self, name, speed, mpg):
        # TransportMode.__init__(self, name, speed)
        super().__init__(name, speed)
        self.mpg = mpg
        self.fuel_gal = 0 

    def add_fuel(self, amount):
        self.fuel_gal += amount

    def drive(self, distance):
        required_fuel = distance / self.mpg
        if self.fuel_gal < required_fuel:
            print('Not enough gas.')
        else:
            self.fuel_gal -= required_fuel
            print(f'{self.fuel_gal:f} gallons remaining.')

class MotorCycle(MotorVehicle):
    def __init__(self, name, speed, mpg):
        # MotorVehicle.__init__(self, name, speed, mpg)
        super().__init__(name, speed, mpg)

    def wheelie(self):
        print('That is too dangerous.')



if __name__ == '__main__':
    ###################################
    # DON'T change this line
    globals.initialise_call_count()
    ###################################

    scooter = MotorCycle('Vespa', 55, 40)
    dirtbike = MotorCycle('KX450F', 80, 25)

    scooter.info()
    dirtbike.info()
    choice = input('Select scooter (s) or dirtbike (d): ')
    bike = scooter if (choice == 's') else dirtbike

    menu = '\nSelect add fuel(f), go(g), wheelie(w), quit(q): '
    command = input(menu)
    while command != 'q':
        if command == 'f':
            fuel = int(input('Enter amount: '))
            bike.add_fuel(fuel)
        elif command == 'g':
            distance = int(input('Enter distance: '))
            bike.drive(distance)
        elif command == 'w':
            bike.wheelie()
        elif command == 'q':
            break
        else:
            print('Invalid command.')

        command = input(menu)

    print(f'Number calls to TransportMode constructor {globals.get_call_count()}')