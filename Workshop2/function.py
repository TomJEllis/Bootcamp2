#1. Write a function that is input a list and  returns a list which has some changes 
# but leaves the original list unchanged e.g. input a list of integers and an integer 
# and returns a list with the integer appended. 
# Print out the original and the new list at the end to show the original list is unchanged

def update_list(input_list, integer):
    new_list = input_list.copy()
    new_list.append(integer)
    return new_list

if __name__ == "__main__":
    my_list = [1,2,3,4,5]
    num = 9
    print(update_list(my_list, num))
    print(my_list)