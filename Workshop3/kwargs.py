def func(**kwargs):
   key = input("Enter a key: ")
   if key in kwargs:
      print(kwargs[key])
   else:
      print("No such group")


if __name__ == "__main__":
   func(group1='julie', group2='geela', group3='axel', group4='azadeh')