#2. Write a python program which prompts the user for a name and a list of numbers (
#e.g. student and scores on tests) and saves this in a dictionary. 
#It will continue until a sentinel value is entered (e.g. 'q'). 
#Print out the dictionary. Then prompt the user for a name (key) and 
#print out the highest number in the value associated with that key. 

# Make sure to handle user entering a name that isn't in the dictionary.
name = ""
all_scores = {}

while name != "q":
   name = input("Enter a name (q to end): ")
   if name == "q":
      break
   scores = input("Enter test scores: ")
   scores = scores.split()

   all_scores[name] = scores

print(all_scores)

name = input("Enter a name to get highest score: ")
if name not in all_scores:
   print(f"Error {name} is not in the dictionary")
else:
   print(f"Highest score: {max(all_scores[name])}")