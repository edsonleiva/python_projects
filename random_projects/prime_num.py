def is_prime(num):
    #checks to see if the number is divisible by any number up to itself
    for x in range(2,num):
        if num % x == 0:
            return False

    return True

#ask the user for a number to check
check_num = int(input('Enter a Number: '))
#call the function
output = is_prime(check_num)

print(f'Is {check_num} a prime number? \n{output}')