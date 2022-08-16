###### Leap Year ######

#asking for what year the user wants to check
year = int(input('What year would you like to check? '))

#checks to see if it is a leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap year.')
        else:
            print('Not leap year.')
    else:
        print('Leap year.')
else:
    print('Not leap year.')