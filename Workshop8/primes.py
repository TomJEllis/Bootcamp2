
def find_next_prime(curr_prime):
    next_prime = curr_prime + 1
    while any(next_prime % divisor == 0 for divisor in range(2,next_prime)):
              next_prime += 1
    return next_prime


def solution(n):
    primeString = ""
    nextPrime = 2

    while len(primeString) < n+5:
        primeString += str(nextPrime)
        nextPrime = find_next_prime(nextPrime)
    return primeString[n:n+5]

print(solution(0))

