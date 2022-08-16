###### FIZZBUZZ ######

# Intro
print('Welcome to FizzBuzz!\n')

# Enter the number for the FizzBuzz program to review
num = int(input('Enter a number: '))

# loops through the num while looking for factors that include 3 and 5
for x in range(num + 1):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)    