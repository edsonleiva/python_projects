###### Even Number Check ######

#ask the user for the number they want checked
num = int(input('What number would you like to check? '))

#checks to see if number is even or odd
if num % 2 == 0:
    print('This is an even number.')
else:
    print('This is an odd number.')