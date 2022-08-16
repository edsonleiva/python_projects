###### HEADS OR TAILS ######

import random

flip = True

while flip:

    #random generator to get the 50/50 for a coin flip
    coin = random.randint(1,2)

    #could not find tails as a ASCII image so tails is replaced with sailor
    if coin == 1:
        print('''
        88                                         88  
        88                                         88  
        88                                         88  
        88,dPPYba,   ,adPPYba, ,adPPYYba,  ,adPPYb,88  
        88P'    "8a a8P_____88 ""     `Y8 a8"    `Y88  
        88       88 8PP""""""" ,adPPPPP88 8b       88  
        88       88 "8b,   ,aa 88,    ,88 "8a,   ,d88  
        88       88  `"Ybbd8"' `"8bbdP"Y8  `"8bbdP"Y8
        ''')
    else:
        print('''
                             88 88                         
                             "" 88                         
                                88                         
        ,adPPYba, ,adPPYYba, 88 88  ,adPPYba,  8b,dPPYba,  
        I8[    "" ""     `Y8 88 88 a8"     "8a 88P'   "Y8  
         `"Y8ba,  ,adPPPPP88 88 88 8b       d8 88          
        aa    ]8I 88,    ,88 88 88 "8a,   ,a8" 88          
        `"YbbdP"' `"8bbdP"Y8 88 88  `"YbbdP"'  88                                                             
        ''')

    play = input('Would you like to flip again? Y or N ').upper()

    #checks to see if user wants to continue flipping the coin
    if play == 'N':
        flip = False
