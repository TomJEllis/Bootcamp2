names = input("Enter some names: ").split()

i = 1
for name in names:
    print(f"{i}. {name}")
    i += 1