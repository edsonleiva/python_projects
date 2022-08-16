###### PIZZA ORDER ######

#the bill is initiated at 0
bill = 0

#intro
print('Welcome to Xtreme Pizza!')

#request pizza information from the user
size = input('What size of Xtreme Pizza would you like? S, M, or L ').upper()
pepperoni = input('Would you like pepperoni? Y or N ').upper()
cheese = input('Would you like extra cheese? Y or N ').upper()


#adjust the bill according to the size of the pizza
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25

#adjust prize for pepperoni
if pepperoni == 'Y' and size == 'S':
    bill += 2
elif pepperoni == 'Y' and (size == 'M' or size == 'L'):
    bill += 3
else:
    pass

#adjust price for extra cheese
if cheese == 'Y':
    bill += 1

#print the total bill out
print(f'Your final bill is: ${bill}')