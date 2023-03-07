#########################################
# Task 1: Complete this function 
# change_str_multi(in_string:str, change_char:str, replace_char:str) -> str:
# ################################ 
def change_str_multi(in_string, change_char, replace_char):
    words = in_string.split(" ")
    new_words = []
    for word in words:
        new_words.append(word.replace(change_char,replace_char))
    return " ".join(new_words)
    

#########################################
# Task 2: Complete this function  
# change_str_single(in_string:str, change_char:str, replace_char:str) -> str:
#########################################
def change_str_single(in_string, change_char, replace_char):
    # words = in_string.split()
    # new_words = []
    # for word in words:
    #     new_words.append(word.replace(change_char,replace_char,1))
    # return " ".join(new_words)
    
    return " ".join([word.replace(change_char,replace_char,1) for word in in_string.split(" ")])
    
    

#########################################
# Task 3: Complete this function  
# change_str(in_string:str, change_num:int, change_char:str, replace_char:str) -> str:
#########################################
def change_str(in_string, change_num, change_char, replace_char):
   #  words = in_string.split(" ")
   #  new_words = []
   #  for word in words:
   #    word_parts = word.split(change_char)
   #    new_words.append("i".join(word_parts[0:change_num]) + (replace_char if word != "" and change_char in word else "") + "i".join(word_parts[change_num:]))
   #  return " ".join(new_words)

   return " ".join(["i".join(word.split(change_char)[0:change_num]) + (replace_char if word != "" and change_char in word else "")  + "i".join(word.split(change_char)[change_num:]) for word in in_string.split(" ")])
    
#######################################################################
# NOTE: 
# The code below is provided for you during development and testing
# Your code will be tested with unit tests that DO NOT use the code below 
####################################################################### 
if __name__ == '__main__':
    orig_string = 'distilling instilling         fulfilling bootcamp'
     
    multi_string = change_str_multi(orig_string, 'i', '*')
    print(f'Multi: {multi_string}')
    
    single_string = change_str_single(orig_string, 'i', '*')
    print(f'Single: {single_string}')
    
    num_string = change_str(orig_string, 2, 'i', '*')
    print(f'Nth: {num_string}')