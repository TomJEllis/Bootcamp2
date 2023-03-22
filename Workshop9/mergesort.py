# Modify the following code so that it accepts a word from the user and
# then uses merge sort to 'scramble' it i.e. reorder the letters in the 
# word so that they are in descending order


def merge(word, i, j, k):
    merged_size = k - i + 1   #  Size of merged partition
    merged_word = []        #  Temporary list for merged word
    for l in range(merged_size):
        merged_word.append(0)
        
    merge_pos = 0      #  Position to insert merged number
    
    left_pos = i       #  Initialize left partition position
    right_pos = j + 1  #  Initialize right partition position
    
    #  Add smallest element from left or right partition to merged word
    while left_pos <= j and right_pos <= k:
        if word[left_pos] < word[right_pos]:
            merged_word[merge_pos] = word[left_pos]
            left_post = left_pos + 1
        else:
            merged_word[merge_pos] = word[right_pos]
            right_pos = right_pos + 1
        merge_pos = merge_pos + 1
    

    #  If left partition is not empty, add remaining elements to merged word
    while left_pos <= j:
        merged_word[merge_pos] = word[left_pos]
        left_pos = left_pos + 1
        merge_pos = merge_pos + 1

    #  If right partition is not empty, add remaining elements to merged word
    while right_pos <= k:
        merged_word[merge_pos] = word[right_pos]
        right_pos = right_pos + 1
        merge_pos = merge_pos + 1

    #  Copy merge number back to word
    merge_pos = 0
    while merge_pos < merged_size:
        word[i + merge_pos] = merged_word[merge_pos]
        merge_pos = merge_pos + 1


def merge_sort(word, i, k):
   j = 0
   
   if i < k:
       j = (i + k) // 2
       merge_sort(word,i,j)
       merge_sort(word,j+1,k)
       
       merge(word, i, j, k)
  
if __name__ == '__main__':           
    user_string = [letter for letter in input()]
    merge_sort(user_string, 0, len(user_string) -1)
    print(f"merge scrambled: {user_string}")
