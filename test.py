
def fix_string(input_string):
   output = ""
   changes = 0

   punctuation = False
   fix_next = True
   space = False

   for char in input_string:
      if fix_next:
         if char.islower():
            char = char.upper()
            changes += 1
         fix_next = False
      elif char in ("?",".","!"):
         punctuation = True
      elif punctuation and char == " ":
         fix_next = True
         punctuation = False
      else:
         punctuation = False


      output += char
   return(output,changes)


if __name__ == "__main__":
   input_string = "  why     did the RMIT programmer   quit their job? Because ?they didn't      get arrays!"
   print(fix_string(input_string))