class Seat:
   def __init__(self):
      self.first_name = ''
      self.last_name = ''
      self.paid = 0.0

   def reserve(self, f_name, l_name, amt_paid):
      self.first_name = f_name
      self.last_name = l_name
      self.paid = amt_paid

   def make_empty(self):
      self.first_name = ''
      self.last_name = ''
      self.paid = 0.0

   def is_empty(self):
      return self.first_name == ''
   
   def __str__(self):
      return (f"{self.first_name} {self.last_name}, Paid: {self.paid:.2f}\n")
   
class SeatReservation:
   def __init__(self):
      self.num_seats = 5
      self.available_seats = []
      for i in range(self.num_seats):
         self.available_seats.append(Seat())

   def __str__(self):
      output = ""
      for i in range(len(self.available_seats)):
         output += f"{i}: "
         output += str(self.available_seats[i])
      return output
   
   def make_seats_empty(self):
      for s in self.available_seats:
         s.make_empty()

   def reserve_seat(self):
      seat_num = int(input('Enter seat num:\n'))
      if seat_num > 0 and seat_num < self.num_seats:
         if not self.available_seats[seat_num].is_empty():
            print('Seat not empty')
         else:
            fname = input('Enter first name:\n')
            lname = input('Enter last name:\n')
            paid = float(input('Enter amount paid:\n'))
            self.available_seats[seat_num].reserve(fname, lname, paid)
      else:
         print("Invalid seat num")
   
def seat_reservation_menu(seat_reservations):
   command = input('Enter command (p/r/q): ')
   while command != 'q':
      if command == 'p':  # Print seats
         print(seat_reservations)
      elif command == 'r':  # Reserve a seat
         seat_reservations.reserve_seat()
      else:
         print('Invalid command.')

      command = input('Enter command (p/r/q):\n')

if __name__ == "__main__":
   seat_reservation = SeatReservation()
   seat_reservation_menu(seat_reservation)