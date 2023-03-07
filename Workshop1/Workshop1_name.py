first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

print(f"Your first name has {len(first_name)} characters")
print(f"Your last name has {len(last_name)} characters")
print(f"Your full name has {len(first_name) + len(last_name)} characters")
print(f"Your initials are: {first_name[0]}. {last_name[0]}.")