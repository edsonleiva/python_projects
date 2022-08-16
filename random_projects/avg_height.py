###### Average Height ######

# Enter everyone's height. Seperated by a space!
group_heights = input('Please enter the heights of the group: ').split()

# a placeholder for the sum of everyone's height combined
total_height = 0

# converts the string form of the group height into an int form
for x in range(0, len(group_heights)):
    group_heights[x] = int(group_heights[x])

# this loop combines everyones height to get the total height
for x in range(0, len(group_heights)):
    total_height += group_heights[x]

# averages the height of the group by dividing the groups total height the length of the group
avg_height = round(total_height/len(group_heights))

# print the average height of the group
print(f'The average height of the group is: {avg_height}')