import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input('How many letters would you like in your password: '))
num_numbers = int(input('How many numbers would you like in your password: '))
num_symbols = int(input('How many symbols would you like in your password: '))

#password is created based on the input for letters, numbers and symbols wanted in the password
password = []
for x in range(num_letters):
    password.append(random.choice(letters))

for y in range(num_numbers):
    password.append(random.choice(numbers))

for z in range(num_symbols):
    password.append(random.choice(symbols))

#shuffles the password to randomize the chars
random.shuffle(password)

#takes the list and makes it into a string
new_password = ''.join(password)

print(f'Your new password is: {new_password}')