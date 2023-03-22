def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)
    
def reverse_list(input_list, temp_list, output_list):
    if len(input_list) == 0:
        output_list += temp_list
    else: 
        reverse_list(input_list[:-1], temp_list + input_list[-1:], output_list)
    return output_list

def alt_reverse_list(input_list):
    if len(input_list) <= 1:
        return input_list
    else:
        return input_list[-1:] + alt_reverse_list(input_list[:-1])

def reverse_traversal(input_list):
    print(input_list.pop(-1))
    if len(input_list) > 0:
        reverse_traversal(input_list)
fib_calls = 0

def fib(n):
    global fib_calls
    fib_calls += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib(n-2) + fib(n-1))
    
def alt_fib(n,t0,t1):
    print(f"||n: {n}|| ||t0: {t0}|| ||t1: {t1}||")
    global fib_calls
    fib_calls += 1
    if n == 0:
        return t0
    if n == 1:
        return t1
    return alt_fib(n-1, t1, t0 + t1)
    
def multiply(a,b):
    if b == 1:
        return a
    else:
        return a + multiply(a,b-1)
    

    
def num_pattern(n, step = 1, stop = -1):
    print(n, end=" ")
    if stop == -1:
        stop = n
        num_pattern(n-step, step, stop)
    elif n > 0 and n < stop:
        num_pattern(n-step, step, stop)
    elif n <= 0:
        num_pattern(n+step, -step, stop)


def alt_num_pattern(n, step=1):
    if n <= 0:
        print(n, end=" ")
        return
    else:
        print(n, end= " ")
        alt_num_pattern(n-step, step)
        print(n, end=" ")


def return_num_pattern(n,step=1):
    if n < 0:
        return n
    else:
        return f"{n} {return_num_pattern(n-step, step)} {n}"
    
def one_line_return_num_pattern(n,step=1):
        return f"{n} {return_num_pattern(n-step, step)} {n}" if n >= 0 else n


def is_palindrome(input_string):
    if len(input_string) <= 1:
        return True
    else:
        return input_string[0] == input_string[-1] and is_palindrome(input_string[1:-1])

def reverse_string(in_str):
    if len(in_str) == 0:
        return in_str
    else:
        return in_str[-1] + reverse_string(in_str[:-1])
    
def alt_reverse_string(in_str):
    if len(in_str) <= 1:
        return in_str
    else:
        return f"{in_str[-1]}{reverse_string(in_str[1:-1])}{in_str[0]}"
        
    
def permutate(input_list, output_list):
    if len(input_list) == 0:
        print(output_list)
    else:
        for i in range(len(input_list)):
            permutate(input_list[:i] + input_list[i+1:], output_list + [input_list[i]])




    
    


if __name__ == "__main__":

    print(factorial(4))

    print(reverse_list([1,2,3,4,5],[],[]))

    reverse_traversal([1,2,3,4,5])

    print(f"Fib:{alt_fib(7,0,1)}")
    print(f"Number of calls: {fib_calls}")

    print(multiply(12,12))

    print(alt_reverse_list([1,2,3,4,5]))

    num_pattern(6)
    print()

    print(is_palindrome("madamimadam"))

    alt_num_pattern(6)
    print()

    alt_num_pattern(6,4)
    print()

    print(return_num_pattern(12, 3))

    in_str = "This is my String"
    result_str = reverse_string(in_str)
    print('Reverse of "' + in_str +  '" is "' + result_str + '".')
    result_str = alt_reverse_string(in_str)
    print('Reverse of "' + in_str +  '" is "' + result_str + '".')

    permutate([1,2,3],[])

    print(one_line_return_num_pattern(12,3))