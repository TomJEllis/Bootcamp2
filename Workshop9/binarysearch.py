recursions = 0
comparisons = 0

def binary_search(nums, target, lower, upper):
    global comparisons
    global recursions
    recursions += 1
    mid = (lower + upper) // 2
    
    comparisons += 1
    if target == nums[mid]:
        return mid
        
    if lower == upper:
        return -1
    
    comparisons += 1
    if target > nums[mid]:
        return binary_search(nums, target, mid + 1, upper)
    
    comparisons += 1
    if target < nums[mid]:
        return binary_search(nums, target, lower, mid -1)
    
    
        
    return -1
    

if __name__ == '__main__':
    # Input a list of nums from the first line of input
    nums = [10,15,20,25,30,35,40,45]
    
    # Input a target value
    target = 50

    # Start off with default values: full range of list indices
    index = binary_search(nums, target, 0, len(nums) - 1)

    # Output the index where target was found in nums, and the
    # number of recursions and comparisons performed
    print(f'index: {index}, recursions: {recursions}, comparisons: {comparisons}')
