### calculates the days, weeks, and months
### you have left til the age 90

#get the user's age
age = int(input('What is your age? '))

#claculates the lifetime left til 90
years_left = 90 - age
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left *12

print(f'You have {days_left} days, {weeks_left} weeks, and {months_left} months left.')