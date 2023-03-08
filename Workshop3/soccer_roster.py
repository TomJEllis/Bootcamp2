def print_menu():
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print("\nChoose an option:")

def output_roster():
    jersey_numbers = list(player_rating.keys())
    jersey_numbers.sort()
    print("ROSTER")
    for num in jersey_numbers:
        print(f"Jersey number: {num}, Rating: {player_rating[num]}")
        
def add_player():
    jersey_number = int(input(f"Enter a new player's jersey number:\n"))
    rating = int(input(f"Enter the player's rating:\n"))
    player_rating[jersey_number] = rating

def delete_player():
    jersey_number = int(input("Enter a jersey number:\n"))
    player_rating.pop(jersey_number)

def update_player():
    jersey_number = int(input("Enter a jersey number:\n"))
    rating = int(input("Enter a new rating for player:\n"))
    player_rating[jersey_number] = rating

def output_players_above_rating():
    min_rating = int(input("Enter a rating:\n"))
    print()
    print(f"ABOVE {min_rating}")
    jersey_numbers = list(player_rating.keys())
    jersey_numbers.sort()
    for num in jersey_numbers:
        if player_rating[num] > min_rating:
            print(f"Jersey number: {num}, Rating: {player_rating[num]}")

player_rating = {}
for i in range(5):
    jersey_number = int(input(f"Enter player {i+1}'s jersey number:\n"))
    rating = int(input(f"Enter player {i+1}'s rating:\n"))
    player_rating[jersey_number] = rating
    print()

output_roster()

menu_option = ""
while menu_option != "q":
    print()
    print_menu()
    menu_option = input()
    
    if menu_option == "o":
        output_roster()
    if menu_option == "a":
        add_player()
    if menu_option == "d":
        delete_player()
    if menu_option == "u":
        update_player()
    if menu_option == "r":
        output_players_above_rating()