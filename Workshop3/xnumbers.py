user_list = []

num = int(input())
for i in range(num):
   user_list.append(int(input()))

for num in user_list:
   if num < 0:
      print("Negative! exiting!")
      break
   print(num, end="\n" if num == user_list[-1] else ",")
