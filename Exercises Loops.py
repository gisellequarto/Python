## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor
divider = 2


for number in check_prime:
    while divider < (number / 2):
        if number % divider == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(number, divider, number))
            break
        divider += 1
    
    if divider > (number / 2):
        divider = 2
        print('{} IS a prime number'.format(number))
    