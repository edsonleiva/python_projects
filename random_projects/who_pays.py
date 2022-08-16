###### WHO WILL PAY THE BILL ######

import random

#request for the names of the people who want to participate
participants = input('Enter the names of the participants seperated by a space: ')

# seperate names onto a list
names = participants.split(' ')

# picks a random person from the list
random_person = random.randint(0, (len(names)-1))

# print out the name of the person that will pay the bill
print(f'{names[random_person]} is paying for the meal today!')

