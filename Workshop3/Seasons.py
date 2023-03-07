input_strings = input().split()
input_month = input_strings[0]
input_day = int(input_strings[1])


# seasons = {
#    "March" : [1,19,"Winter",20,31,"Spring"],
#    "April" : [1,30,"Spring"],
#    "May" : [1,31,"Spring"],
#    "June" : [1,20,"Spring",21,30,"Summer"],
#    "July" : [1,31,"Summer"],
#    "August" : [1,31,"Summer"],
#    "September" : [1,21,"Summer",22,30,"Autumn"],
#    "October" : [1,31,"Autumn"],
#    "November" : [1,30,"Autumn"],
#    "December" : [1,20,"Autumn",21,31,"Winter"],
#    "January" : [1,31,"Winter"],
#    "February" : [1,28,"Winter"] 
# }

# if input_day >= seasons[input_month][0] and input_day <= seasons[input_month][1]:
#    print(seasons[input_month][2])
# elif len(seasons[input_month]) > 3 and input_day >= seasons[input_month][3] and input_day <= seasons[input_month][4]:
#    print(seasons[input_month][5])
# else:
#    print("Invalid")

seasons = {
   "March" : [(1,19,"Winter"),(20,31,"Spring")],
   "April" : [(1,30,"Spring")],
   "May" : [(1,31,"Spring")],
   "June" : [(1,20,"Spring"),(21,30,"Summer")],
   "July" : [(1,31,"Summer")],
   "August" : [(1,31,"Summer")],
   "September" : [(1,21,"Summer"),(22,30,"Autumn")],
   "October" : [(1,31,"Autumn")],
   "November" : [(1,30,"Autumn")],
   "December" : [(1,20,"Autumn"),(21,31,"Winter")],
   "January" : [(1,31,"Winter")],
   "February" : [(1,28,"Winter")] 
}
if input_month not in seasons:
   print("Invalid")
   exit()
string = "Invalid"
for val in seasons[input_month]:
   if input_day >= val[0] and input_day <= val[1]:
      string = val[2]
      break
print(string)