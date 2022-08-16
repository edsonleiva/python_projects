###### TREASURE MAP #######

#creating the rows to print as a visual
row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']

#nests the rows into another list to create a 3x3
treasure_map = [row1,row2,row3]

# print out the rows to show the grid
print(f'{row1}\n{row2}\n{row3}')

# ask the user to pick a position
position = input('Where would you like to put your treasure? ')

# splits the two digits and adjusts for list
column = int(position[0]) - 1
row = int(position[1]) - 1

# change the index of whatever you pick to 'x' marks the spot
treasure_map[column][row] = 'X'

# reprint the new treasure map with the hidden treasure 
print(f'{row1}\n{row2}\n{row3}')