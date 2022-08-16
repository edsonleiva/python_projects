###### ROCK, PAPER, SCISSORS ######
import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# places the strings above in a list for easy access
choices = [rock,paper,scissors]

# ask for user input
player_choice = int(input('Choose 0 for Rock, 1 for Paper, and 2 for Scissors: '))

# randomizes what the computer will pick
cpu_choice = random.randint(0,2)

# display what was chosen
print('You chose:')
print(choices[player_choice]+'\n')
print('CPU chose:')
print(choices[cpu_choice]+'\n')

# the different winning scenarios
if player_choice == cpu_choice:
    print('It is a draw!')
elif player_choice == 0 and cpu_choice == 1:
    print('CPU Wins!')
elif player_choice == 0 and cpu_choice == 2:
    print('Player Wins!')
elif player_choice == 1 and cpu_choice == 0:
    print('Player Wins!')
elif player_choice == 1 and cpu_choice == 2:
    print('CPU Wins!')
elif player_choice == 2 and cpu_choice == 0:
    print('CPU Wins!')
elif player_choice == 2 and cpu_choice == 1:
    print('Player Wins!')
