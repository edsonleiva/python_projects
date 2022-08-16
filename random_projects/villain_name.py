### villain name generator ###

#ask for their name
name = input('What is your name?\n')

#ask for a random item
item = input('Name a random item:\n')

# combine the first three letters of name and the last letters of the item to create villain name
print('Your villain name is ' + name[:3] + item[3:])
