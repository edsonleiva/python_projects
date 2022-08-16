###### TIP CALCULATOR ######

#intro to the program
print('Welcome to the tip calculator!')

#get the total bill from the user
total_bill = float(input('What was the total bill? '))

#ask what percentage they want to tip
percentage = (int(input('What percentage tip would you like to give? 10, 12, or 15?' )) / 100) + 1

#ask how many people are splitting the bill
num_ppl = int(input('How many people to split the bill? '))

#calculate the new bill and divide it by person
new_bill = round((total_bill * percentage) / num_ppl, 2)

#using format to display the 2 decimal places
print('Each person should pay: $' + '{:.2f}'.format(new_bill))