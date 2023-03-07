user_list = []

for i in range(5):
   user_list.append(int(input()))

for num in user_list:
   if num < 0:
      print("Negative! exiting!")
      break
   print(num, end="\n" if num == user_list[4] else ",")



