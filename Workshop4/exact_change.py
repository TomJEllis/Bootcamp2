def exact_change(user_total):
    if type(user_total) != int or user_total < 0 :
        return None
    num_pennies, num_nickels, num_dimes, num_quarters = 0, 0, 0, 0
    if user_total >= 25:
        num_quarters = user_total // 25
        user_total = user_total % 25
    if user_total > 10:
        num_dimes = user_total // 10
        user_total = user_total % 10
    if user_total > 5:
        num_nickels = user_total // 5
        user_total = user_total % 5
    num_pennies = user_total
    
    return (num_pennies, num_nickels, num_dimes, num_quarters)

def print_change(user_total):
    num_pennies, num_nickels, num_dimes, num_quarters = exact_change(user_total)

    if num_pennies == 1:
        print(f"{num_pennies} penny")
    elif num_pennies > 1:
        print(f"{num_pennies} pennies")
    if num_nickels == 1:
        print(f"{num_nickels} nickel")
    elif num_nickels > 1:
        print(f"{num_nickels} nickels")
    if num_dimes == 1:
        print(f"{num_dimes} dime")
    elif num_dimes > 1:
        print(f"{num_dimes} dimes")
    if num_quarters == 1:
        print(f"{num_quarters} quarter")
    elif num_quarters > 1:
        print(f"{num_quarters} quarters")
    if not num_pennies and not num_nickels and not num_dimes and not num_quarters:
        print("no change")
        

if __name__ == '__main__': 
    input_val = int(input()) 
    print_change(input_val)