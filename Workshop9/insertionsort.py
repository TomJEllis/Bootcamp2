num_swaps = 0
num_comparisons = 0

def read_nums():
    """Read numbers from input and return them in a list"""
    return [int(num) for num in input().split()]

def print_nums(nums):
    """Output numbers, separating each item by a spaces;
    no space or newline before the first number or after the last."""
    print(' '.join([str(n) for n in nums]), end='')

def swap(nums, n, m):
    global num_swaps
    num_swaps += 1
    """Exchange nums[n] and nums[m]"""
    nums[n], nums[m] = nums[m], nums[n]

def insertion_sort(numbers):
    global num_comparisons
    """Sort the list numbers using insertion sort"""
    for i in range(1, len(numbers)):
        j = i
        # Insert numbers[i] into sorted part
        # stopping once numbers[i] is in correct position
        while j > 0:    
            num_comparisons += 1
            if numbers[j] < numbers[j - 1]:
                swap(numbers, j, j - 1)
            j -= 1
        
        print_nums(numbers)
        print()

if __name__ == '__main__':
    # Step 1: Read numbers into a list
    numbers = [3, 2, 1, 5, 9, 8]

    # Step 2: Output the numbers list
    print_nums(numbers)
    print(end='\n\n')

    # Step 3: Sort the numbers list
    insertion_sort(numbers)
    print()
    # Step 4: TODO: Output the number of comparisons and swaps performed
    print(f"comparisons: {num_comparisons}")
    print(f"swaps: {num_swaps}")